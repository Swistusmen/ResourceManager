import webScraper, openpyxl, resourceDB, os


class rbd:
    def __init__(self, test=None):
        if(not(test is None)):
            self.max_height=4
        else:
            self.max_height=180
        self.engine=webScraper.webScrapper()
        self.base=resourceDB.resourceDataBase(test)
        self.wb=self.base.start()
        if(self.base.isFresh()==1):
            self.actualize

    def actualize(self): 
        sheet=self.wb.active
        if(sheet.max_row>self.max_height):
            i=2
            while i<self.max_height:
                for ii in range(len(self.base.attributes)):
                    sheet.cell(row=i,column=ii+1).value=sheet.cell(row=i+1,column=ii+1).value
                i+=1
            sheet.delete_rows(sheet.max_row)
            self.wb.save(self.base.name)
        b=1
        lista=self.engine.getActualData()
        max_r=sheet.max_row
        for i in lista:
            sheet.cell(row=max_r+1,column=b).value=(i)
            b+=1
        self.wb.save(self.base.name)

    def getCurrentData(self): 
        sheet=self.wb.active
        if(sheet.max_row<2):
            raise Exception ("There is no data for read")
        currentRow=sheet.max_row
        lista=[]
        for i in range(len(self.base.attributes)):
            lista.append(sheet.cell(row=currentRow, column=i+1).value)
        return lista
    
    def getNamesOfAttributes(self):
        return self.base.attributes

    def getPointedData(self, number):
        if(type(number)!=int):
            raise Exception ("Wrong type of data")
        if(number<2):
            raise Exception ("The index of row is too small")
        if(number>self.wb.active.max_row):
            raise Exception ("The index of row is too big")
        lista=[]
        sheet=self.wb.active
        for i in range(len(self.getNamesOfAttributes())):
            lista.append(sheet.cell(row=number, column=i+1).value)
        return lista

    def getSize(self):
        sheet=self.wb.active
        return sheet.max_row

def unitTest():
    mistakes=0

    if(webScraper.unitTest()==0):
        return
    if(resourceDB.unitTest()==0):
        return

    if os.path.exists("test.xlsx"):
        os.remove("test.xlsx")
    
    db=rbd(test=1)
    if(db.max_height!=4):
        mistakes+=1

    for i in range(3):
        db.actualize()
    if db.wb.active.max_row!=4:
        mistakes+=1
    db.actualize()
    if db.wb.active.max_row!=5:
        mistakes+=1

    db.actualize()
    db.actualize()
    if db.wb.active.max_row!=5:
        mistakes+=1

    lista=db.getCurrentData()
    sum=0
    for i in lista:
        try:
            sum+=i
        except Exception as err:
            mistakes+=1
    
    mistakes+=1
    try:
        db.getPointedData(7)
    except Exception as err:
        mistakes-=1

    mistakes+=1
    try:
        db.getPointedData(0)
    except Exception as err:
        mistakes-=1

    mistakes+=1
    try:
        db.getPointedData(-1)
    except Exception as err:
        mistakes-=1

    if(mistakes==0):
        print("unit test for resourceRDB has been passed")
        return 1
    else:
        print("unit test for manageRDB has been failed")
        print("mistakes: "+str(mistakes))
        return 0

'''        
db=rbd()
atrybuty=db.getNamesOfAttributes()
print(atrybuty)
obecne=db.getCurrentData()
print(obecne)
wskazana=db.getPointedData(3)
print(wskazana)
co=""
try:
    co=db.getPointedData(-1)
except Exception as err:
    print(err)
try:
    co=db.getPointedData(14)
except Exception as err:
    print(err)
'''