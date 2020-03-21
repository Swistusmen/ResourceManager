import requests, bs4



class webScrapper:
    def __init__(self):
        self.resources='https://www.bankier.pl/surowce/notowania'
        self.currencys="https://kursy-walut.mybank.pl/"
        self.ether="https://coinmarketcap.com/currencies/ethereum/markets/"
        self.btc="https://coinmarketcap.com/currencies/bitcoin/markets/"
        self.lisk="https://coinmarketcap.com/currencies/lisk/markets/"
        self.lite="https://coinmarketcap.com/currencies/litecoin/markets/"
        self.lista=[]

    def getActualData(self):
        self.lista=self.getResources()
        self.lista+=self.getCurrency()
        self.lista+=self.getCrypto()

        self.uniteBTC()

        self.convertToProper()
        self.lista[7]*=self.lista[4]/100
        self.lista[8]*=self.lista[4]/100
        self.lista[9]*=self.lista[4]/100
        self.lista[10]*=self.lista[4]/100

        return self.lista

    def getHistoricalData(self):
        pass

    def uniteBTC(self):
        sum=""
        for i in self.lista[7]:
            if i==',':
                pass
            else:
                sum+=i
        self.lista[7]=sum



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

    def convertToProper(self):
        if len(self.lista)==0:
            raise Exception ("The list is empty!")

        c=0
        for element in self.lista:
            sum=""
            for i in element:
                if i.isdigit():
                    sum+=i
                if i==",":
                    sum+="."
            self.lista[c]=float(sum)
            c+=1

        return self.lista

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

def unitTest():
    o=webScrapper()
    mistakes=0

    if(o.currencys!="https://kursy-walut.mybank.pl/"):
        mistakes+=1

    if(o.ether!="https://coinmarketcap.com/currencies/ethereum/markets/"):
        mistakes+=1

    if(o.lisk!="https://coinmarketcap.com/currencies/lisk/markets/"):
        mistakes+=1

    if(o.lite!="https://coinmarketcap.com/currencies/litecoin/markets/"):
        mistakes+=1
    
    if(o.btc!="https://coinmarketcap.com/currencies/bitcoin/markets/"):
        mistakes+=1

    if(o.resources!='https://www.bankier.pl/surowce/notowania'):
        mistakes+=1

    lista=o.getResources()
    if(type(lista)!=list):
        mistakes+=1
    if(len(lista)!=4):
        mistakes+=1
    
    lista.clear()
    lista=o.getCurrency()
    if(type(lista)!=list):
        mistakes+=1
    if(len(lista)!=3):
        mistakes+=1

    
    lista.clear()
    lista=o.getCrypto()
    if(type(lista)!=list):
        mistakes+=1
    if(len(lista)!=4):
        mistakes+=1

    lista.clear()
    lista=o.getActualData()
    if(type(lista)!=list):
        mistakes+=1
    if(len(lista)!=11):
        mistakes+=1

    sum=0
    for i in lista:
        try:
            sum+=i
        except Exception as err:
            mistakes+=1

    if mistakes==0:
        print("unit test for webScraper has been passed")
        return 1
    else:
        print("Unit test for webScraper has been failed")
        print("mistakes: "+str(mistakes))
        return 0


unitTest()




