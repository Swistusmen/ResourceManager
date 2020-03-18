import requests, bs4



class webScrapper:
    def __init__(self):
        self.resources='https://www.bankier.pl/surowce/notowania'
        self.currencys="https://kursy-walut.mybank.pl/"
        self.ether="https://coinmarketcap.com/currencies/ethereum/markets/"
        self.btc="https://coinmarketcap.com/currencies/bitcoin/markets/"
        self.lisk="https://coinmarketcap.com/currencies/lisk/markets/"
        self.lite="https://coinmarketcap.com/currencies/litecoin/markets/"

    def getActualData(self):
        lista=self.getResources()
        lista+=self.getCurrency()
        lista+=self.getCrypto()
        return lista


    def getHistoricalData(self):
        pass

    def getResources(self):
        req=requests.get(self.resources)
        req.raise_for_status()
        mydelko=bs4.BeautifulSoup(req.text,features='html.parser')
        wartosc=mydelko.select('td ')

        lista=list()
        lista.append((wartosc[2].text))
        lista.append((wartosc[10].text))
        lista.append((wartosc[18].text))
        lista.append((wartosc[26].text))
        return lista

    def getCurrency(self):
        req=requests.get(self.currencys)
        req.raise_for_status()
        mydelko=bs4.BeautifulSoup(req.text,features='html.parser')
        wartosc=mydelko.select('.tab_kursy tr td')
        lista=[]
        lista.append(wartosc[2].text)
        lista.append(wartosc[7].text)
        lista.append(wartosc[12].text)
        return lista

    def getCrypto(self):
        lista=[]

        req=requests.get(self.btc)
        req.raise_for_status()
        mydelko=bs4.BeautifulSoup(req.text,features='html.parser')
        wartosc=mydelko.select(".cmc-details-panel-price__price")
        lista.append(wartosc[0].text[1:])

        req=requests.get(self.ether)
        req.raise_for_status()
        mydelko=bs4.BeautifulSoup(req.text,features='html.parser')
        wartosc=mydelko.select(".cmc-details-panel-price__price")
        lista.append(wartosc[0].text[1:])

        req=requests.get(self.lisk)
        req.raise_for_status()
        mydelko=bs4.BeautifulSoup(req.text,features='html.parser')
        wartosc=mydelko.select(".cmc-details-panel-price__price")
        lista.append(wartosc[0].text[1:])

        req=requests.get(self.lite)
        req.raise_for_status()
        mydelko=bs4.BeautifulSoup(req.text,features='html.parser')
        wartosc=mydelko.select(".cmc-details-panel-price__price")
        lista.append(wartosc[0].text[1:])

        return lista

        



o=webScrapper()
i=o.getActualData()
print(i)
#l=o.getActualData()
#for i in l:
#    print(i)



