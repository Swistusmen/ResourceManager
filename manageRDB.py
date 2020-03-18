import webScraper, openpyxl, resourceDB


class rbd:
    def __init__(self):
        self.max_height=181
        self.engine=webScraper.webScrapper()
        self.base=resourceDB.resourceDataBase()
        self.wb=self.base.start()
        #if(self.base.isFresh()==1):
        #    pass
            #aktualizacja


    def actualize(self): 
        sheet=self.wb.active
        if(sheet.max_row>self.max_height):
            i=2
            while i<180:
                sheet.row[i]=sheet.row[i+1]
                i+=1
        b=1
        lista=self.engine.getActualData()
        max_r=sheet.max_row
        for i in lista:
            sheet.cell(row=max_r+1,column=b).value=(i)
            b+=1
        self.wb.save(self.base.name)


            


    def getCurrentData(self): #zwraca krotke klucza: wartosc
        pass
        


db=rbd()
for i in range(10):
    db.actualize()
