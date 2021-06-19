from StockAnalyzer import StockAnalyzer
from tkinter import *

class GUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('StockAnalyzer')

        titleLabel = Label(self.root,text='Stock Analyzer',padx=10,pady=10)
        titleLabel.grid(row=0,column=0)
        
        entr = Entry(self.root,width=10)
        entr.grid(row=1,column=0)

        submitBtn = Button(self.root,text='Enter',height = 1,width=8,command=lambda:self.enter(entr.get()))
        submitBtn.grid(row=1,column=1)

        self.msgLabel = Label(self.root,padx=10,pady=12)
        self.msgLabel.grid(row=2,column=0)
        self.msgLabel['text'] = 'Enter Ticker Symbol'

        self.root.mainloop()

    def enter(self,tckr):
        # clear results


        sa = StockAnalyzer(tckr)

        if(sa[1]):
            self.msgLabel['text'] = 'Displaying Results'

            sa = sa[0]
            #Display information on GUI
            self.ticker = Label(self.root, text=f'Ticker: {sa.ticker}')
            self.ticker.grid(row=4,column=0)

            self.name = Label(self.root, text=f'Name: {sa.name}')
            self.name.grid(row=5,column=0)

            self.price = Label(self.root, text=f'Price: ${sa.price}')
            self.price.grid(row=6,column=0)

            self.mktCap = Label(self.root, text=f'Market Cap: ${sa.mktCapStr}')
            self.mktCap.grid(row=7,column=0)

            self.valuation = Label(self.root, text=f'Valuation: ${sa.valuationStr}')
            self.valuation.grid(row=8,column=0)

            self.shares = Label(self.root, text=f'Shares Outstanding: {sa.sharesStr}')
            self.shares.grid(row=9,column=0)

            self.netIncome = Label(self.root, text=f'Net Income: ${sa.netIncomeStr}')
            self.netIncome.grid(row=10,column=0)

            self.revenue = Label(self.root, text=f'Revenue: ${sa.revenueStr}')
            self.revenue.grid(row=11,column=0)

            self.eps = Label(self.root, text=f'EPS (Basic): {sa.eps}')
            self.eps.grid(row=12,column=0)

            self.peRatio = Label(self.root, text=f'P/E Ratio: {sa.peRatio}')
            self.peRatio.grid(row=13,column=0)

            self.idealPrice = Label(self.root, text=f'Ideal Price: ${sa.idealPrice}')
            self.idealPrice.grid(row=14,column=0)

        else:
            self.msgLabel['text'] = 'Invalid Ticker, Enter again'
            if 'self.name' in locals(): 
                self.ticker.destroy()
                self.name.destroy()
                self.price.destroy()
                self.mktCap.destroy()
                self.valuation.destroy()
                self.shares.destroy()
                self.netIncome.destroy()
                self.revenue.destroy()
                self.eps.destroy()
                self.peRatio.destroy()
                self.idealPrice.destroy()
            
        self.msgLabel.grid(row=2,column=0)

#Driver
GUI()