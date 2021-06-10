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

        msgLabel = Label(self.root,padx=10,pady=12)
        msgLabel.grid(row=2,column=0)
        msgLabel['text'] = 'Enter Ticker Symbol'

        self.root.mainloop()

    def enter(self,tckr):
        sa = StockAnalyzer(tckr)

        #Display information on GUI
        ticker = Label(self.root, text=f'Ticker: {sa.ticker}')
        ticker.grid(row=5,column=0)

        name = Label(self.root, text=f'Name: {sa.name}')
        name.grid(row=4,column=0)

        price = Label(self.root, text=f'Price: ${sa.price}')
        price.grid(row=5,column=0)

        mktCap = Label(self.root, text=f'Market Cap: ${sa.mktCapStr}')
        mktCap.grid(row=6,column=0)

        valuation = Label(self.root, text=f'Valuation: ${sa.valuationStr}')
        valuation.grid(row=7,column=0)

        shares = Label(self.root, text=f'Shares Outstanding: {sa.sharesStr}')
        shares.grid(row=8,column=0)

        netIncome = Label(self.root, text=f'Net Income: ${sa.netIncomeStr}')
        netIncome.grid(row=9,column=0)

        revenue = Label(self.root, text=f'Revenue: ${sa.revenueStr}')
        revenue.grid(row=10,column=0)

        eps = Label(self.root, text=f'EPS (Basic): {sa.eps}')
        eps.grid(row=11,column=0)

        peRatio = Label(self.root, text=f'P/E Ratio: {sa.peRatio}')
        peRatio.grid(row=12,column=0)

        idealPrice = Label(self.root, text=f'Ideal Price: ${sa.idealPrice}')
        idealPrice.grid(row=13,column=0)


GUI()