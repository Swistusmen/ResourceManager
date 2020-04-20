from tkinter import *
import ControlPanel

manage=ControlPanel.ControlPanel()

root=Tk()
root.wm_minsize(width=600, height=500)

root.columnconfigure(0,pad=2)
root.columnconfigure(1, pad=2)
root.columnconfigure(2,pad=2)
root.columnconfigure(3,pad=2)
root.columnconfigure(4, pad=2)
root.columnconfigure(5,pad=2)
root.columnconfigure(6,pad=2)
root.columnconfigure(7, pad=2)
root.columnconfigure(8,pad=2)
root.columnconfigure(9,pad=2)
root.columnconfigure(10, pad=2)
root.columnconfigure(11,pad=2)
root.columnconfigure(12,pad=2)
root.columnconfigure(13,pad=2)

root.rowconfigure(0,pad=2)
root.rowconfigure(1,pad=2)
root.rowconfigure(2,pad=2)
root.rowconfigure(3,pad=2)
root.rowconfigure(4,pad=2)
root.rowconfigure(5,pad=2)
root.rowconfigure(6,pad=2)
root.rowconfigure(7,pad=2)
root.rowconfigure(8,pad=2)
root.rowconfigure(9,pad=2)
root.rowconfigure(10,pad=2)
root.rowconfigure(11,pad=2)
root.rowconfigure(12,pad=2)
root.rowconfigure(13,pad=2)
root.rowconfigure(14,pad=2)
root.rowconfigure(15,pad=2)
root.rowconfigure(16,pad=2)


PayInEntry=StringVar()
PayOutEntry=StringVar(root)
SellBuyResource=StringVar(root)
RadioVariable=IntVar()
RadioVariable.set(0)
MenuVariable=StringVar()
MenuVariable.set("")

lista1=manage.getAmountsFromWallet()
lista2=manage.getCurrentValues()
lista3=manage.MoneyInWallet()
TotalMoney=StringVar()
TotalMoney=str(manage.GetMoney())

def ActualizeData():
    lista1=manage.getAmountsFromWallet()
    lista2=manage.getCurrentValues()
    lista3=manage.MoneyInWallet()


def PayInEntryProcedure():
    amount=float(PayInEntry.get())
    manage.PayIn(amount)
    fun()

def PayOutEntryProcedure():
    amount=float(PayOutEntry.get())
    manage.PauOut(-amount)
    fun()

def SellBuyResourceProcedure():
    amount=float(SellBuyResource.get())
    if(RadioVariable.get()==0):
        print("Error, no option has been choosed")
        return
    elif RadioVariable.get()==1: #buy
        manage.BuyResource(MenuVariable.get(),amount)
    else: #sell
        manage.SellResource(MenuVariable.get(),-amount)
    ActualizeData()

    MenuVariable.set("")
    SellBuyResource.set("")
    RadioVariable.set("0")
    fun()

def SetRadioVariable( var):
    RadioVariable=var

class ResourceNameBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)
        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))

        self.label=Label(text="Resource").grid(column=0, row=2)
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i+1, row=2)

class ResourceCourseBar(Frame):
    def __init__(self):
        Frame.__init__(self)


        self.names=[]
        self.names.append(Label(root,text="None"))
        for i in range(len(lista2)):
            self.names.append(Label(root,text=lista2[i]))
        self.label=Label(text="Course ").grid(column=0, row=3)
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i+1, row=3)
    

    def actualize(self):
        lista2=manage.getCurrentValues()
        for i in range(len(lista2)):
            self.names[i+1].configure(text=lista2[i])
            

class ResourceAmountBar(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista1)):
            self.names.append(Label(root,text=lista1[i]))
        self.label=Label(text="Amount").grid(column=0,row=4)
        for i in range(len(self.names)):
            self.names[i].grid(column=i+1, row=4)

    def actualize(self):
        lista1=manage.getAmountsFromWallet()
        for i in range (len(lista1)):
            self.names[i].configure(text=lista1[i])

class ValueOfRecourseInWalletBar(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista3)):
            self.names.append(Label(root,text=lista3[i]))
        self.label=Label(text="Value in wallet").grid(column=0,row=5)
        for i in range(len(self.names)):
            self.names[i].grid(column=i+1, row=5)
        
    def actualize(self):
        lista3=manage.MoneyInWallet()
        for i in range(len(lista3)):
            self.names[i].configure(text=lista3[i])

class AmountOfMoney(Frame):
    def __init__(self):
        Frame.__init__(self)

       
        self.Screen=Label(root,text=TotalMoney)
        self.label=Label(text="Total money").grid(column=3, row=9, columnspan=2, sticky=NSEW)
        self.Screen.grid(column=3, row=10, columnspan=2, sticky=NSEW)

    def actualize(self):
        TotalMoney=(str(manage.GetMoney()))
        self.Screen.configure(text=TotalMoney)
        

class PayInArea(Frame):        
    def __init__(self):
        Frame.__init__(self)
        self.variable=StringVar(root)
        self.Screen=Entry(root,textvariable=PayInEntry)
        self.accept=Button(root,text="Pay In",command=PayInEntryProcedure)

        self.Screen.grid(column=5, row=9)
        self.accept.grid(column=7, row=9, columnspan=2, sticky=EW)

class PayOutArea(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.variable=StringVar(root)
        self.Screen=Entry(root,textvariable=PayOutEntry)
        self.accept=Button(root,text="Pay Out", command=PayOutEntryProcedure)

        self.Screen.grid(column=5, row=10)
        self.accept.grid(column=7, row=10, columnspan=2, sticky=EW)

class ChangeDayResourceCourseBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=11)

class ChangeWeekResourceCourseBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=12)

def SetMenuVar(var):
    if MenuVariable!="":
        MenuVariable.set(var)
    else:
        MenuVariable.set("")

def GetMenuVar():
    print(MenuVariable.get())
    #MenuVariable.set("")

class Operations(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        lista=["Oil","Gold","Copper","Silver","USD","EUR","CHF","Bitcoin","Etherum","Lisk","Litecoin"]
        
        self.choice=Menubutton(root, text="Choose Resource")
        self.choice.menu=Menu(self.choice)
        self.choice["menu"]=self.choice.menu

        self.zmienna=MenuVariable.get()
        
        for i in lista:
            #self.choice.menu.add_radiobutton(label=i, command=lambda:(SetMenuVar(i)))
            self.choice.menu.add_radiobutton(label=i, variable=MenuVariable)
        

        self.choice.grid(column=4, row=13)





class ChooseOperation(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.optionBuy=Radiobutton(root, text="Buy", variable=RadioVariable, value=1)
        self.optionSell=Radiobutton(root,text="Sell", variable=RadioVariable, value=2)
        self.variable=StringVar()
        self.entry=Entry(root,textvariable=SellBuyResource)
        self.Accept=Button(root, text="Accept", command=SellBuyResourceProcedure)

        self.optionBuy.grid(column=3, row=14)
        self.optionSell.grid(column=4, row=14)
        self.entry.grid(column=5, row=14)
        self.Accept.grid(column=6, row=14)


lista=list()
var=97
for i in range(12):
    lista.append(chr(var))
    var+=1
lista=["PLN","Oil","Gold","Copper","Silver","USD","EUR","CHF","Bitcoin","Etherum","Lisk","Litecoin"]
label1=Label(root,text="-----Resources-----").grid(row=0, column=0, columnspan=12, sticky=W+E)
o1=ResourceNameBar(lista)
o2=ResourceCourseBar()
o3=ResourceAmountBar()
o4=ValueOfRecourseInWalletBar()
label2=Label(root,text="-----Operations-----").grid(row=7, column=0, columnspan=12, sticky=W+E)
o5=AmountOfMoney()
o6=PayInArea()
o7=PayOutArea()
o9=Operations(lista)
o10=ChooseOperation()

def fun():
    lista1=manage.getAmountsFromWallet()
    lista2=manage.getCurrentValues()
    lista3=manage.MoneyInWallet()
    o2.actualize()
    o3.actualize()
    o4.actualize()
    o5.actualize()

root.mainloop()



