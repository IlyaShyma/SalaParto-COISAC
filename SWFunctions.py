from PySide6.QtCore import QTime

from main import *
from FDFunctions import *



class SWFunctions():

    def updateTime(self):
        self.ui.lblTimer.setText(QTime.currentTime().toString())
        FDFunctions.checkFeedTime(self)
        if self.ui.lblTimer.text() == "00:00:00":
            self.curveOnCom = False


    def loadDB(self):
        self.dbHall =  TinyDB('DB/Hall.json', storage=CachingMiddleware(JSONStorage))
        self.dbCurve = TinyDB('DB/Curve.json', storage=CachingMiddleware(JSONStorage))
        self.dbTime = TinyDB('DB/Time.json')
        self.dbSow = TinyDB('DB/Sow.json')
        self.dbBox = TinyDB('DB/Box.json', storage=CachingMiddleware(JSONStorage))
        self.dbConf = TinyDB('DB/Conf.json', storage=CachingMiddleware(JSONStorage))
        self.query = Query()


    def saveSow(self):
        sowToInsert = self.ui.txtDataSow.text()
        if self.dbSow.search(self.query.sowName == sowToInsert):
            self.ui.lblDataStatus.setText("IMPOSSIBILE AGGIUNGERE. "+sowToInsert+" GIA' ESISTENTE.")
        else:
            self.dbSow.insert({'sowName':sowToInsert})
            SWFunctions.loadSow(self)

    def loadSow(self):
        self.ui.tblSow.setRowCount(len(self.dbSow))
        i = 0
        for item in self.dbSow:
            self.ui.tblSow.setItem(i,0,QTableWidgetItem(item.get('sowName')))
            i += 1
        self.ui.txtDataTotSow.setText(str(len(self.dbSow)))

    def removeBox(self):
        boxToRemove = self.ui.tblBox.item(self.ui.tblBox.currentRow(), 0).text()
        if self.dbHall.search(self.query.boxName == boxToRemove):
            self.ui.lblDataStatus.setText("IMPOSSIBILE RIMUOVERE. "+boxToRemove+" IN UTILIZZO.")
        else:
            self.dbBox.remove(self.query.boxName == boxToRemove)
            SWFunctions.loadBox(self)


    def removeSow(self):
        sowToRemove = self.ui.tblSow.item(self.ui.tblSow.currentRow(), 0).text()
        if self.dbHall.search(self.query.sowName == sowToRemove):
            self.ui.lblDataStatus.setText("IMPOSSIBILE RIMUOVERE. "+sowToRemove+" IN UTILIZZO.")
        else:
            self.dbSow.remove(self.query.sowName == sowToRemove)
            SWFunctions.loadSow(self)

    def saveBox(self):
        hallToFill = self.ui.spiDataHallAdd.value()
        boxInHall = self.ui.spiDataBoxAdd.value()
        for i in range(boxInHall):
            boxName = "S"+str(hallToFill)+"B"+str(i+1)
            hallPos = hallToFill
            boxPos = i+1
            comPos = -1
            if self.dbBox.search(self.query.boxName == boxName):
                pass
            else:
                self.dbBox.insert({'boxName':boxName, 'hallPos':hallPos, 'boxPos':boxPos, 'comPos':comPos})
        SWFunctions.loadBox(self)

    def loadBox(self):
        self.ui.tblBox.setRowCount(len(self.dbBox))
        i = 0
        for item in self.dbBox:
            self.ui.tblBox.setItem(i,0,QTableWidgetItem(item.get('boxName')))
            self.ui.tblBox.setItem(i,1,QTableWidgetItem(str(item.get('hallPos'))))
            self.ui.tblBox.setItem(i,2,QTableWidgetItem(str(item.get('boxPos'))))
            self.ui.tblBox.setItem(i,3,QTableWidgetItem(str(item.get('comPos'))))
            i += 1
        self.ui.txtDataTotBox.setText(str(len(self.dbBox)))

    def loadSowInBox(self):
        self.ui.comAddSelBox.clear()
        self.ui.comAddSelSow.clear()
        self.ui.comAddSelCur.clear()
        self.ui.spiAddSelEntryDate.setDate(QDate.currentDate())
        self.ui.spiAddSelPigDate.setDate(QDate.currentDate())

    def correctCurve(self):
        try:
            valToCorrect = self.ui.tblCurve.currentItem().text()
            if "." in valToCorrect:
                pass
            else:
                try:
                    valToCorrect = float(valToCorrect)
                    self.ui.tblCurve.setItem(self.ui.tblCurve.currentRow(), self.ui.tblCurve.currentColumn(), QTableWidgetItem(str(valToCorrect)))
                except:
                    self.ui.lblCurveStatus.setText("VALORE NON NUMERICO")
        except:
            pass
    def saveCurve(self):
        curveToUpdate = self.ui.spiCurve.value()
        for i in range(50):
            self.dbCurve.upsert(Document({'{}'.format(i):self.ui.tblCurve.item(i,2).text()}, doc_id=curveToUpdate))
        self.ui.lblCurveStatus.setText("CURVA SALVATA")
        # except:
        #     self.ui.lblCurveStatus.setText("CURVA NON INSERITA, CONTROLLARE")

    def loadCurve(self):
        curveToLoad = self.ui.spiCurve.value()
        curveLoaded = self.dbCurve.get(doc_id = curveToLoad)
        if curveLoaded == None:
            for i in range(50):
                self.ui.tblCurve.setItem(i,2,QTableWidgetItem("0.0"))
        else:
            for i in range(50):
                self.ui.tblCurve.setItem(i,2,QTableWidgetItem(curveLoaded.get('{}'.format(i))))

    def autocompleteTime(self):
        try:
            if self.ui.tblTime.currentColumn() == 0 or self.ui.tblTime.currentColumn() == 1:
                if ":" in self.ui.tblTime.currentItem().text() or self.ui.tblTime.currentItem().text() == "":
                    self.ui.lblTimeStatus.setText("")
                else:
                    self.ui.tblTime.currentItem().setText(self.ui.tblTime.currentItem().text()+":00")
            else:
                if (self.ui.tblTime.currentItem().text().upper())[0] == "S":
                    self.ui.tblTime.currentItem().setText("SI")
                else:
                    self.ui.tblTime.currentItem().setText("NO")
        except:
            pass

    def saveTime(self):
        for row in range(self.ui.tblTime.rowCount()):
            if self.ui.tblTime.item(row,0):
                try:
                    fr = self.ui.tblTime.item(row,0).text()
                    to = self.ui.tblTime.item(row,1).text()
                    active = self.ui.tblTime.item(row,2).text()
                    if fr != "" and to != "" and active != "":
                        self.dbTime.upsert(Document({'fr':fr, 'to':to, 'active':active},doc_id=row+1))
                        self.ui.lblTimeStatus.setText("ORARI SALVATI CORRETTAMENTE")
                    else:
                        self.ui.lblTimeStatus.setText("DATI MANCANTI, RICONTROLLARE")
                except:
                    pass
        SWFunctions.loadTime(self)

    def loadAddSowInBox(self):
        self.ui.comAddSelBox.clear()
        self.ui.comAddSelSow.clear()
        self.ui.comAddSelCur.clear()
        for box in self.dbBox:
            self.ui.comAddSelBox.addItem(box.get('boxName'))
        for sow in self.dbSow:
            self.ui.comAddSelSow.addItem(sow.get('sowName'))
        for i in range(5):
            self.ui.comAddSelCur.addItem(str(i+1))

    def removeTime(self):
        self.dbTime.remove(doc_ids=[self.ui.tblTime.currentRow()+1])
        SWFunctions.loadTime(self)

    def loadTime(self):
        for item in self.dbTime:
            self.ui.tblTime.setItem(item.doc_id-1, 0, QTableWidgetItem(item.get('fr')))
            self.ui.tblTime.setItem(item.doc_id-1, 1, QTableWidgetItem(item.get('to')))
            self.ui.tblTime.setItem(item.doc_id-1, 2, QTableWidgetItem(item.get('active')))


    def loadHall(self):
        i = 0
        self.ui.tblHall.setRowCount(i)
        self.ui.tblHall.setRowCount(self.dbBox.count(self.query.hallPos == self.ui.spiHall.value()))
        for item in self.dbBox:
            if item.get('hallPos') == self.ui.spiHall.value():
                boxName = item.get('boxName')
                self.ui.tblHall.setItem(i,0,QTableWidgetItem(boxName))
                hallData = self.dbHall.get(self.query.boxName == boxName)
                if hallData != None:
                    sowName = hallData.get('sowName')
                    sowSit = hallData.get('sowSit')
                    nrCurve = hallData.get('nrCurve')
                    curDay = (QDate.fromString(hallData.get('curDay'), "dd/MM/yyyy").daysTo(QDate.currentDate()))
                    curve = self.dbCurve.get(doc_id = int(nrCurve))
                    if sowSit == 0:
                        sowSit = "Gestazione"
                        curDay = curDay + 101
                        if curDay > 115:
                        	curDay = 115
                        curValue = curve.get(str(int('{}'.format(curDay))-100))
                    else:
                        curDay = curDay + 1
                        if curDay > 35:
                        	curDay = 35
                        curValue = curve.get(str(int('{}'.format(curDay))+14))
                        sowSit = "Parto"
                    pigBirth = hallData.get('pigBirth')
                    pigRealBirth = hallData.get('pigRealBirth')
                    pigWeight = hallData.get('pigWeight')
                    curKG = str(int(float(curValue)*1000))
                    self.ui.tblHall.setItem(i,1,QTableWidgetItem(sowName))
                    self.ui.tblHall.setItem(i,2,QTableWidgetItem(sowSit))
                    self.ui.tblHall.setItem(i,3,QTableWidgetItem(nrCurve))
                    self.ui.tblHall.setItem(i,4,QTableWidgetItem(str(curDay)))
                    self.ui.tblHall.setItem(i,5,QTableWidgetItem(curKG))
                    self.dbHall.upsert({'curKGToday':curKG},self.query.boxName == boxName)
                    
                    num_pasti = self.dbTime.count(self.query.active == "SI")
                    if num_pasti == 0:
                    	num_pasti = 1
                    self.ui.tblHall.setItem(i,6,QTableWidgetItem(str(int(int(curKG)/num_pasti))))
                    self.ui.tblHall.setItem(i,7,QTableWidgetItem(str(hallData.get('readNowFeedKG'))))
                i += 1

    def saveSowInBox(self):
        boxName = self.ui.comAddSelBox.currentText()
        sowName = self.ui.comAddSelSow.currentText()
        nrCurve = self.ui.comAddSelCur.currentText()
        entryDate = self.ui.spiAddSelEntryDate.date().toString("dd/MM/yyyy")
        if self.ui.txtAddCurType.text() == "Gestazione":
            curDay = QDate.currentDate().addDays(101-int(self.ui.spiAddSelCurDay.value())).toString("dd/MM/yyyy")
            sowSit = 0
            parDate = 0
            pigBirth = 0
            pigRealBirth = 0
            pigWeight = 0
        else:
            curDay = QDate.currentDate().addDays(1-int(self.ui.spiAddSelCurDay.value())).toString("dd/MM/yyyy")
            sowSit = 1
            parDate = self.ui.spiAddSelPigDate.date().toString("dd/MM/yyyy")
            pigBirth = self.ui.spiAddSelPigBirth.value()
            pigRealBirth = self.ui.spiAddSelPigRealBirth.value()
            pigWeight = self.ui.spiAddSelPigWeight.value()
        self.dbHall.upsert({'boxName':boxName, 'sowName':sowName, 'entryDate':entryDate, 'sowSit':sowSit, 'nrCurve':nrCurve,'curDay':curDay, 'parDate':parDate, 'pigBirth':pigBirth, 'pigRealBirth':pigRealBirth, 'pigWeight':pigWeight}, self.query.boxName == boxName)
        SWFunctions.loadHall(self)


    def updateDaysInBirth(self):
        if self.ui.txtAddCurType.text() == "Parto":
            parDay = -1 * (QDate.currentDate().daysTo(self.ui.spiAddSelPigDate.date())) + 1
            self.ui.spiAddSelCurDay.setValue(parDay)

    def checkBoxExisting(self):
        getBox = self.dbHall.get(self.query.boxName == self.ui.comAddSelBox.currentText())
        if getBox:
            self.ui.lblAddStatus.setText("STAI MODIFICANDO UNA GABBIA GESTITA")
            self.ui.comAddSelSow.setCurrentText(getBox.get('sowName'))
            self.ui.comAddSelCur.setCurrentText(getBox.get('nrCurve'))
            self.ui.spiAddSelEntryDate.setDate(QDate.fromString(getBox.get('entryDate'), "dd/MM/yyyy"))
            self.ui.spiAddSelPigBirth.setValue(getBox.get('pigBirth'))
            self.ui.spiAddSelPigRealBirth.setValue(getBox.get('pigRealBirth'))
            self.ui.spiAddSelPigWeight.setValue(getBox.get('pigWeight'))
            if getBox.get('sowSit'):
                self.ui.radAddBirthY.setChecked(True)
                self.ui.spiAddSelPigDate.setDate(QDate.fromString(getBox.get('parDate'), "dd/MM/yyyy"))
            else:
                self.ui.radAddBirthN.setChecked(True)
        else:

            self.ui.lblAddStatus.setText("")

    def removeHall(self):
        try:
            hallToRemove = self.ui.tblHall.item(self.ui.tblHall.currentRow(), 1).text()
            self.dbHall.remove(self.query.sowName == hallToRemove)
            SWFunctions.loadHall(self)
        except:
            print("NON HAI SELEZIONATO LA SCROFA DA RIMUOVERE")

    def boxSelected(self):
        try:
            boxToSelect = self.ui.tblHall.item(self.ui.tblHall.currentRow(), 0).text()
            self.ui.comAddSelBox.setCurrentText(boxToSelect)
            SWFunctions.checkBoxExisting(self)
        except:
            pass

    def saveBoxCom(self):
        for i in range(self.ui.tblBox.rowCount()):
            if int(self.ui.tblBox.item(i,3).text()) != -1:
                self.dbBox.upsert({'comPos':int(self.ui.tblBox.item(i,3).text())},self.query.boxName == self.ui.tblBox.item(i,0).text())
        SWFunctions.loadBox(self)



    def saveConf(self,val):
        if val == 0:
            value = self.ui.comSetComPort.currentText()
            self.dbConf.upsert(Document({"comPort":value},doc_id=1))
        elif val == 1:
            value = self.ui.comSetComBaud.currentText()
            self.dbConf.upsert(Document({"comBaud":int(value)},doc_id=1))
        elif val == 2:
            value = self.ui.spiSetComImp.value()
            self.dbConf.upsert(Document({"comImp":value},doc_id=1))
            self.calibAndImp = False
        elif val == 3:
            value = self.ui.spiSetComCal.value()
            self.dbConf.upsert(Document({"comCalib":value},doc_id=1))
            self.calibAndImp = False
        SWFunctions.loadConf(self)

    def loadConf(self):
        conf = self.dbConf.get(doc_id=1)
        if len(conf) == 4:
            self.ui.comSetComPort.setCurrentText(conf.get('comPort'))
            self.ui.comSetComBaud.setCurrentText(str(conf.get('comBaud')))
            self.ui.spiSetComImp.setValue(conf.get('comImp'))
            self.ui.spiSetComCal.setValue(conf.get('comCalib'))
