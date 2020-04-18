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


PayInEntry=StringVar()
PayOutEntry=StringVar(root)
SellBuyResource=StringVar(root)
RadioVariable=IntVar()
RadioVariable.set(0)
MenuVariable=StringVar()
MenuVariable.set("")





def PayInEntryProcedure():
    amount=float(PayInEntry.get())
    manage.PayIn(amount)
    print(PayInEntry.get())
    PayInEntry.set("")

def PayOutEntryProcedure():
    amount=float(PayOutEntry.get())
    manage.PauOut(-amount)
    print(PayOutEntry.get())
    PayOutEntry.set("")

def SellBuyResourceProcedure():
    '''
    print(MenuVariable.get())
    MenuVariable.set("")
    print(SellBuyResource.get())
    SellBuyResource.set("")
    print(RadioVariable.get())
    '''

    amount=float(SellBuyResource.get())
    if(RadioVariable.get()==0):
        print("Error, no option has been choosed")
        return
    elif RadioVariable.get()==1: #buy
        manage.BuyResource(MenuVariable.get(),amount)
    else: #sell
        manage.SellResource(MenuVariable.get(),-amount)

    MenuVariable.set("")
    SellBuyResource.set("")
    RadioVariable.set("0")



    

def SetRadioVariable( var):
    RadioVariable=var

class ResourceNameBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=1)

class ResourceCourseBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=2)

class ResourceAmountBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=3)

class ValueOfRecourseInWalletBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=4)

class AmountOfMoney(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.variable=StringVar()
        self.variable=str(manage.GetMoney())
        self.Screen=Label(root,text=self.variable)

        self.Screen.grid(column=0, row=7, rowspan=2, columnspan=2, sticky=NSEW)

class PayInArea(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.variable=StringVar(root)
        self.Screen=Entry(root,textvariable=PayInEntry)
        self.accept=Button(root,text="Pay In",command=PayInEntryProcedure)

        self.Screen.grid(column=2, row=7)
        self.accept.grid(column=4, row=7, columnspan=2, sticky=EW)

class PayOutArea(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.variable=StringVar(root)
        self.Screen=Entry(root,textvariable=PayOutEntry)
        self.accept=Button(root,text="Pay Out", command=PayOutEntryProcedure)

        self.Screen.grid(column=2, row=8)
        self.accept.grid(column=4, row=8, columnspan=2, sticky=EW)

class ChangeDayResourceCourseBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=9)

class ChangeWeekResourceCourseBar(Frame):
    def __init__(self, lista):
        Frame.__init__(self)

        self.names=[]
        for i in range(len(lista)):
            self.names.append(Label(root,text=lista[i]))
        
        for i in range(len(self.names)):
            self.names[i].grid(column=i, row=10)

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
        
        for i in lista:
            #self.choice.menu.add_radiobutton(label=i, command=lambda:(SetMenuVar(i)))
            self.choice.menu.add_radiobutton(label=i, variable=MenuVariable)
        

        self.choice.grid(column=1, row=11)



class ChooseOperation(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.optionBuy=Radiobutton(root, text="Buy", variable=RadioVariable, value=1)
        self.optionSell=Radiobutton(root,text="Sell", variable=RadioVariable, value=2)
        self.variable=StringVar()
        self.entry=Entry(root,textvariable=SellBuyResource)
        self.Accept=Button(root, text="Accept", command=SellBuyResourceProcedure)

        self.optionBuy.grid(column=0, row=12)
        self.optionSell.grid(column=1, row=12)
        self.entry.grid(column=2, row=12)
        self.Accept.grid(column=3, row=12)


lista=list()
var=97
for i in range(12):
    lista.append(chr(var))
    var+=1
lista=["PLN","Oil","Gold","Copper","Silver","USD","EUR","CHF","Bitcoin","Etherum","Lisk","Litecoin"]
label1=Label(root,text="-----Resources-----").grid(row=0, column=0, columnspan=12, sticky=W+E)
o1=ResourceNameBar(lista)
lista1=manage.getAmountsFromWallet()
o2=ResourceCourseBar(lista1)
lista2=manage.getCurrentValues()
o3=ResourceAmountBar(lista2)
lista3=manage.MoneyInWallet()
o4=ValueOfRecourseInWalletBar(lista3)
label2=Label(root,text="-----Operations-----").grid(row=6, column=0, columnspan=12, sticky=W+E)
o5=AmountOfMoney()
o6=PayInArea()
o7=PayOutArea()
o9=Operations(lista)
o10=ChooseOperation()

root.mainloop()


#TODO autoactualization of data when somethings change
#TODO add descriptions what is what
#TODO add widget presenting current resource, value of this resource in PLN
#TODO better presentation



#TODO options with comparasing several measurements
