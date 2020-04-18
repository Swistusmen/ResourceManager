import calculations, userDB, manageRDB, os, shutil, time


class ControlPanel:
    def __init__(self,test=None):
        self.resources=manageRDB.rbd(test)
        self.wallet=userDB.userWallet(test)

        self.resourcesAmount=self.getAmountsFromWallet()
        self.exchangeRates=self.getCurrentValues()
        self.money=self.MoneyInWallet()

    def getCurrentValues(self): #get current exchange rates from the wallet
        lista=self.resources.getCurrentData()
        return lista

    def getAmountsFromWallet(self): #get current amounts of resources from wallet
        lista=self.wallet.CurrentRow()
        return lista

    def getPercentageDiff(self, measurement=1): #get percentage diffrence between this and past measurement
        if self.resources.wb.active.max_row-1>measurement:
            number=self.resources.wb.active.max_row-measurement
            return calculations.retThePercentage(self.exchangeRates,self.resources.getPointedData(number))
        else:
            lista=[0,0,0,0,0,0,0,0,0,0,0]
            return lista

    def getDiff(self, measurement=1): #get diffrence between current exchange rates and exchanges from the past measuement
        if self.resources.wb.active.max_row-1>measurement:
            number=int(self.resources.wb.active.max_row-measurement)
            return calculations.retTheDiffrence(self.exchangeRates,self.resources.getPointedData(number))
        else:
            lista=[0,0,0,0,0,0,0,0,0,0,0]
            return lista


    def MoneyInWallet(self): #used to get current value of stored resources
        lista1=self.getCurrentValues()
        lista2=self.getAmountsFromWallet()
        buf=lista2[0]
        lista2.remove(buf)
        lista3=[buf]
        lista3+=calculations.getRealValues(lista1,lista2)
        return lista3

    def PayIn(self, amount): #used to add money to PLN field in user wallet
        if((type(amount)!=int)and(type(amount)!=float)):
            raise Exception ("Wrong data type")
        if(amount<=0):
            raise Exception ("Wrong operation")
        self.wallet.PayInOut(amount)
        self.actualize()
        
    def PauOut(self, amount): #used to pay out money from wallet- sub money from pln field
        if((type(amount)!=int)and(type(amount)!=float)):
            raise Exception ("Wrong data type")
        if(amount>=0):
            raise Exception ("Wrong operation")
        self.wallet.PayInOut(amount)
        self.actualize()

    def BuyResource(self, resource, forPLN): #used to buy resource
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

    def SellResource(self,resource, forPLN): #use to sell resource
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

    def actualize(self): #actualize data- used in another module, to auto actualize code
        self.resourcesAmount=self.getAmountsFromWallet()
        self.exchangeRates=self.getCurrentValues()
        self.money=self.MoneyInWallet()

    def menu(self): #prints option to choose in interface function
        lista=["0.payIn","1.payOut","2.Buy","3.Sell","4.show last measeure perc. changes",
        "5.show last measeure diff changes","6.show day perc. changes","7.show day diff. changes",
        "8.show week perc. changes","9.show week diff. changes",
        "10.courses","11.money in resources","12.total money","13.quit"]
        for i in lista:
            print(i)
        return len(lista)

    def myInput(self):
        while 1:
            try:
                var=float(input(": "))
            except Exception as err:
                pass
            if(type(var)==float):
                break
        return var

    def interface(self, test=None, param1=None, param2=None): #text interface if u want to use code from console
        if test is None:
            size=self.menu()
        a=0
        while a==0:
            if test is None: 
                while 1:
                    try:
                        choice=int(input("option: "))
                    except Exception as err:
                        pass
                    if((choice>=0)and(size)):
                        break
            else:
                choice=test

            if choice==0:
                try:
                    if(param1 is None):
                        self.PayIn(self.myInput())
                    else:
                        self.PayIn(param1)
                        break
                except Exception as err:
                    print(err)
            elif choice==1:
                try:
                    if(param1 is None):
                        self.PauOut(self.myInput())
                    else:
                        self.PauOut(param1)
                        break
                except Exception as err:
                    print(err)
            elif choice==2:
                if ((param1 is None) and (param2 is None)):
                    var=input("resource: ")
                    var1=self.myInput()
                else:
                    var=param2
                    var1=float(param1)
                try:
                    self.BuyResource(resource=var,forPLN=var1)
                except Exception as err:
                    print(err)
                    break
                if(not(test is None)):
                    break
            elif choice==3:
                if ((param1 is None)and(param2 is None)):
                    var=input("resource: ")
                    var1=self.myInput()
                else:
                    var=param2
                    var1=param1
                try:
                    self.SellResource(resource=var,forPLN=var1)
                except Exception as err:
                    print(err)
                if (not(test is None)):
                    break
            elif choice==4:
                var=self.getPercentageDiff()
                print(var)
                return var
            elif choice==5:
                var=self.getDiff()
                print(var)
                return var
            elif choice==6:
                var=self.getPercentageDiff(2)
                print(var)
                return var
            elif choice==7:
                var=self.getDiff(2)
                print(var)
                return var
            elif choice==8:
                var=self.getPercentageDiff(20)
                print(var)
                return var
            elif choice==9:
                var=self.getDiff(20)
                print(var)
                return var
            elif choice==10:
                print(self.exchangeRates)
                return self.exchangeRates
            elif choice==11:
                print(self.money)
                return self.money
            elif choice==12:
                var=calculations.sum(self.money)
                print(var)
                return var
            else:
                break
            if (test is None):
                break

    def GetMoney(self): #returns value of wallet
        myList=self.MoneyInWallet()
        cash=float(0)
        for i in myList:
            cash+=i
        return cash

def unitTest():
    path="TestCopies"
    path2="Storage"
    curr=os.getcwd()
    print(os.listdir())
    if(not(os.path.exists(path2))):
        os.mkdir("Storage")
    if(not(os.path.exists(path))):
        raise Exception("""There is no test data, impossible to make test
    Look on my github to take them:https://github.com/Swistusmen/ResourceManager """)

    shutil.move(curr+"\\"+"Resources.xlsx",curr+"\\"+path2)
    shutil.move(curr+"\\"+"User.xlsx",curr+"\\"+path2)
    shutil.copy(curr+"\\"+path+"\\"+"Resources.xlsx",os.getcwd())
    shutil.copy(curr+"\\"+path+"\\"+"User.xlsx",os.getcwd())
    mistakes=0
    o=ControlPanel()

    if(o.interface(test=10)!=[28.96, 1487.5, 4767.5, 12.48, 4.24, 4.5459, 4.3124, 27.10208, 58410.24000000001, 462.16, 16976.96]):
        mistakes+=1
    if(o.interface(test=11)!=[9000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11800.481927710844]):
        mistakes+=1
    if(o.interface(test=12)!=20800.481927710844):
        mistakes+=1
    if(o.interface(test=4)!=[100.83565459610028, 100.03362474781439, 100.03672034831874, 100.1605136436597, 100.0, 100.0, 100.0, 99.55068254203104, 99.06515173306488, 99.0909090909091, 99.35483870967741]):
        mistakes+=1
    if(o.interface(test=5)!=[0.240000000000002, 0.5, 1.75, 0.019999999999999574, 0.0, 0.0, 0.0, -0.12232399999999899, -551.1999999999898, -4.239999999999952, -110.2400000000016]):
        mistakes+=1
    if(o.interface(test=6)!=[100.83565459610028, 100.03362474781439, 100.03672034831874, 100.1605136436597, 100.0, 100.0, 100.0, 99.55068254203104, 99.06515173306488, 99.0909090909091, 99.35483870967741]):
        mistakes+=1
    if(o.interface(test=7)!=[0.240000000000002, 0.5, 1.75, 0.019999999999999574, 0.0, 0.0, 0.0, -0.12232399999999899, -551.1999999999898, -4.239999999999952, -110.2400000000016]):
        mistakes+=1
    if(o.interface(test=8)!=[101.47161878065873, 100.10094212651413, 99.979029044773, 100.08019246190858, 0.01, 0.009999999999999998, 0.01, 421.40314924145474, 418.531384350817, 420.1454545454545, 420.7425030978934]):
        mistakes+=1
    if(o.interface(test=9)!=[0.4200000000000017, 1.5, -1.0, 0.009999999999999787, -42395.76, -45454.4541, -43119.6876, 20.67069, 44454.24000000001, 352.16, 12941.96]):
        mistakes+=1

    o.interface(test=0,param1=10000)
    if(o.interface(test=11)!=[19000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11800.481927710844]):
        mistakes+=1
    if(o.interface(test=12)!=30800.481927710844):
        mistakes+=1
    o.interface(test=1,param1=-1000)
    if(o.interface(test=11)!=[18000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11800.481927710844]):
        mistakes+=1
    if(o.interface(test=12)!=29800.481927710844):
        mistakes+=1
    o.interface(test=1,param1=-20000)
    if(o.interface(test=11)!=[0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11800.481927710844]):
        mistakes+=1
    if(o.interface(test=12)!=11800.481927710844):
        mistakes+=1
    o.interface(test=0, param1=10000)
    o.interface(test=11)
    o.interface(test=12)

    o.interface(test=2, param1=5000,param2="Oil")
    o.interface(test=2, param1=3000, param2="Silver")
    if(o.interface(test=11)!=[2000.0, 5000.0, 0.0, 0.0, 3000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11800.481927710844]):
        mistakes+=1
    if(o.interface(test=12)!=21800.481927710844):
        mistakes+=1
    o.interface(test=3, param1=-2000, param2="Silver")
    if(o.interface(test=11)!=[4000.0, 5000.0, 0.0, 0.0, 1000.0000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11800.481927710844]):
        mistakes+=1
    if(o.interface(test=12)!=21800.481927710844):
        mistakes+=1
    
    os.unlink("Resources.xlsx")
    os.unlink("User.xlsx")
    shutil.move(curr+"\\"+path2+"\\"+"Resources.xlsx",os.getcwd())
    shutil.move(curr+"\\"+path2+"\\"+"User.xlsx",os.getcwd())
    if(mistakes==0):
        print("unit test for ControlPanel has been passed ")
        return 1
    else: 
        print("unit test for ControlPanel has been failed ")
        print(mistakes)
        return 0
    
#unitTest()
