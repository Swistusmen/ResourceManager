import openpyxl, os, datetime

class resourceDataBase:
    def __init__(self):
        self.attributes=["Oil","Gold","Copper","Silver","USD","EUR","CHF","Bitcoin","Etherum","Lisk","Litecoin"]
        self.name="Resources.xlsx"
        self.max_height=181
        self.max_width=12

    def start(self):
        sheet=None
        if(not(os.path.exists(self.name))):
            sheet=self.createWorkbook()
        else:
            sheet=openpyxl.load_workbook(self.name)
        return sheet #zwracamy modulowi ktory operuje na bazie


    def actualize(self): #funkcja wywolywana co odstep czasu, powoduje uaktualnienie bazy danych
        pass


    def createWorkbook(self):
        sheet=openpyxl.Workbook()
        current=sheet.active

        Font=openpyxl.styles.Font(name="title",bold=True,size=14)
        styl=openpyxl.styles.NamedStyle(name='title',font=Font)

        iterator=1
        for i in self.attributes:
            current.cell(row=1, column=iterator).value=i
            current.cell(row=1, column=iterator).style=styl
            iterator+=1
        sheet.save(self.name)
        return sheet

o=resourceDataBase()
o.start()
