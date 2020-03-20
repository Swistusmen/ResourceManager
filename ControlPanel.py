import calculations, userDB, manageRDB


class ControlPanel:
    def __init__(self,test=None):
        self.resources=manageRDB.rbd(test)
        self.wallet=userDB.userWallet(test)

        self.resourcesAmount=self.getAmountsFromWallet()
        self.exchangeRates=self.getCurrentValues()
        self.money=self.MoneyInWallet()

    def getCurrentValues(self):
        lista=self.resources.getCurrentData()
        return lista

    def getAmountsFromWallet(self):
        lista=self.wallet.CurrentRow()
        return lista

    def getPercentageDiff(self, measurement=1):
        if self.resources.wb.active.max_row-1>measurement:
            number=self.resources.wb.active.max_row-measurement
            return calculations.retThePercentage(self.exchangeRates,self.resources.getPointedData(number))
        else:
            lista=[0,0,0,0,0,0,0,0,0,0,0]
            return lista

    def getDiff(self, measurement=1):
        if self.resources.wb.active.max_row-1>measurement:
            number=int(self.resources.wb.active.max_row-measurement)
            return calculations.retTheDiffrence(self.exchangeRates,self.resources.getPointedData(number))
        else:
            lista=[0,0,0,0,0,0,0,0,0,0,0]
            return lista


    def MoneyInWallet(self):
        lista1=self.getCurrentValues()
        lista2=self.getAmountsFromWallet()
        buf=lista2[0]
        lista2.remove(buf)
        lista3=[buf]
        lista3+=calculations.getRealValues(lista1,lista2)
        return lista3

    def PayIn(self, amount):
        if((type(amount)!=int)and(type(amount)!=float)):
            raise Exception ("Wrong data type")
        if(amount<=0):
            raise Exception ("Wrong operation")
        self.wallet.PayInOut(amount)
        self.actualize()
        
    def PauOut(self, amount):
        if((type(amount)!=int)and(type(amount)!=float)):
            raise Exception ("Wrong data type")
        if(amount>=0):
            raise Exception ("Wrong operation")
        self.wallet.PayInOut(amount)
        self.actualize()

    def BuyResource(self, resource, forPLN):
        if (not (resource in ["Oil","Gold","Copper","Silver","USD","EUR","CHF","Bitcoin","Etherum","Lisk","Litecoin"])):
            raise Exception ("Wrong resource")
        if((type(forPLN)!=int)and(type(forPLN)!=float)):
            raise Exception ("Wrong type of data")
        if(forPLN<0):
            raise Exception ("Wrong amount of money")
        moneyIn=self.wallet.PayInOut(-forPLN)
        if moneyIn!=0:
            forPLN+=moneyIn


        b=0
        for i in self.resources.base.attributes:
            if(i==resource):
                break
            b+=1
        exchange=self.exchangeRates[b]
        eq=forPLN/exchange
        self.wallet.SellAndBuy(amount=eq,attribute=resource)
        self.actualize()
        return eq

    def SellResource(self,resource, forPLN):
        if (not (resource in ["Oil","Gold","Copper","Silver","USD","EUR","CHF","Bitcoin","Etherum","Lisk","Litecoin"])):
            raise Exception ("Wrong resource")
        if((type(forPLN)!=int)and(type(forPLN)!=float)):
            raise Exception ("Wrong type of data")
        if(forPLN>0):
            raise Exception ("Wrong amount of money")

        b=0
        for i in self.resources.base.attributes:
            if(i==resource):
                break
            b+=1
        exchange=self.exchangeRates[b]

        eq=forPLN/exchange
        c=self.wallet.SellAndBuy(amount=eq,attribute=resource)
        if c!=0:
            val=c*exchange
            val=(-forPLN)+val
        else:
            eq=eq*(-1)
            val=eq*exchange
        if val!=0:
            self.PayIn(val)
        self.actualize()
        return eq

    def actualize(self):
        self.resourcesAmount=self.getAmountsFromWallet()
        self.exchangeRates=self.getCurrentValues()
        self.money=self.MoneyInWallet()

    def menu(self):
        lista=["wplac","wyplac","kup","sprzedaj","p zeszly","diff zeszly","p dzien","diff dzien"
        ,"p tydzien","diff tydzien","hajs","kursy"]
        for i in lista:
            print(i)


    def interface(self):
        self.menu()
        

o=ControlPanel()
print(o.getDiff(2))
print(o.getPercentageDiff(2))

'''
print(o.wallet.base.attributes)
print("kursy: "+str(o.getCurrentValues()))
print("ile w portfelu: "+str(o.getAmountsFromWallet()))
print("ile pieniędzy w czym: "+str(o.MoneyInWallet()))
o.PayIn(4000)
o.BuyResource(resource="Oil",forPLN=2000)
print("ile pieniędzy w czym: "+str(o.MoneyInWallet()))
o.BuyResource(resource="Litecoin",forPLN=1000)
print("ile pieniędzy w czym: "+str(o.MoneyInWallet()))
o.BuyResource(resource="Oil",forPLN=1000)
print("ile pieniędzy w czym: "+str(o.MoneyInWallet()))
o.SellResource(resource="Oil",forPLN=-1500)
print("ile pieniędzy w czym: "+str(o.MoneyInWallet()))
o.SellResource(resource="Oil",forPLN=-1500)
print("ile pieniędzy w czym: "+str(o.MoneyInWallet()))
'''




