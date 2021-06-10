from bs4 import BeautifulSoup
import requests

class StockAnalyzer:
    def __init__(self,tckr) -> None:
        try:
            htmlText = requests.get('https://www.macroaxis.com/invest/ratio/'+tckr).text
            soup = BeautifulSoup(htmlText, 'lxml')

            # Ticker
            self.ticker = tckr

            # Name
            self.name = soup.find('a', class_='c-gray fadingTex').text

            # Price
            for s in soup.findAll('span'):
                if s.get('id') == 'symbolQuoteValueFlat':
                    self.price = float(s.text)                    

            info = soup.findAll('tr')
            for i in info:
                t = i.find('a', class_ = 'plainLink')

                # Market Capitalization
                if(t != None and "Market Capitalization" in t):
                    self.mktCapStr = i.findAll('td')[2].text

                # Valuation
                if(t != None and "Current Valuation" in t):
                    self.valuationStr = i.findAll('td')[2].text

                # Outstanding Shares
                elif(t != None and "Shares Outstanding" in t):
                    self.sharesStr = i.findAll('td')[2].text
                    num,letter = self.sharesStr.split()

                    if letter == 'B':
                        self.sharesFloat = int(num *  1000000000)
                    elif letter == 'M':
                        self.sharesFloat = int(num *  1000000)
                    else:
                        self.sharesFloat = int(num)
                       
                # Net Income
                elif(t != None and "Net Income" in t):
                    self.netIncomeStr = i.findAll('td')[2].text
                    self.netIncomeStr = self.netIncomeStr.replace('(','').replace(')','')

                    num,letter = self.netIncomeStr.split()

                    if letter == 'B':
                        self.netIncomeFloat = int(float(num) *  1000000000)

                # Revenue
                elif(t != None and "Revenue" in t):
                    self.revenueStr = i.findAll('td')[2].text

            #eps (basic)
            self.eps = self.netIncomeFloat/self.sharesFloat

            #P/E ration = stockPrice/eps
            self.peRatio = self.price/self.eps

            #ideal price = priceFloat/(peRatio/14)
            self.idealPrice = self.price/(self.peRatio/14)

            #self.printValues()
        except:
            print('Exception encountered initializing StockAnalyzer')
    

    def printValues(self):
        print(f'Ticker: {self.ticker}')
        print(f'Name: {self.name}')
        print(f'Price: ${self.price}')
        print(f'Market Cap: {self.mktCapStr}')
        print(f'Valuation: {self.valuationStr}')
        print(f'Shares Outstanding: {self.sharesStr}')
        print(f'Net Income: {self.netIncomeStr}')
        print(f'Revenue: {self.revenueStr}')
        print(f'Earnings Per Share (Basic): {self.eps}')
        print(f'P/E Ratio: {self.peRatio}')

        print(f'\nThe ideal stock price for {self.name} is around ${self.idealPrice}')
