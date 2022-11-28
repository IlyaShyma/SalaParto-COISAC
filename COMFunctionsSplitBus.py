
import csv
import os


from main import *


import logging
from logging.handlers import RotatingFileHandler
from emailer import *

dest = "madtech@tin.it"
subject = "Schede offline"


class COMClass(QThread):

    def __init__(self, comUI, self2):
        print("sono qua")
        super().__init__()
        self.ui = self2.ui
        self.self = self2
        self.self.master = 0
        self.email_sent = True
        self.body = ""
        self.max_offline = 20

    def sendmail(self):
        if not self.email_sent:
            sender = Emailer()
            sender.sendmail(dest, subject, self.body)
            self.email_sent = True

    def run(self):
        self.self.calibAndImp = False
        self.self.debugMode = False
        self.self.curveLoaded = False
        self.self.feedActive = 0
        self.self.curveOnCom = False
        self.offline = []
        self.reset = False

        logFormatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        logFile = "log/app_log.log"
        my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,
                                 backupCount=5, encoding=None, delay=0)
        my_handler.setFormatter(logFormatter)
        my_handler.setLevel(logging.INFO)
        self.logger = logging.getLogger('root')
        self.logger.setLevel(logging.INFO)

        self.logger.addHandler(my_handler)

        # logging.basicConfig(filename="log/log-{}.log".format(QDateTime.currentDateTime().toString()),format='%(asctime)s %(message)s',filemode='a')
        # self.logger = modbus_tk.utils.create_logger()

        self.logger.info(f"Start app")
        while True:
            comItem = self.self.dbConf.get(doc_id = 1)
            if self.self.master == 0:
                try:
                    self.logger.info("CONNESSIONE MODBUS IN CORSO...")
                    self.self.master = modbus_rtu.RtuMaster(serial.Serial(comItem.get('comPort'), baudrate = comItem.get('comBaud'), bytesize = 8, parity='N', stopbits=1))
                    self.self.master.set_verbose(False)
                    self.self.master.set_timeout(0.1)
                    self.ui.chkHallCom.setChecked(True)
                    self.ui.chkHallCom.setEnabled(False)
                    t.sleep(1)
                except:
                    self.logger.error("CONNESSIONE NON RIUSCITA.")
                    break
            else:
                if self.self.calibAndImp == False:
                    self.logger.info("IMPOSTO ORARIO...")
                    COMClass.setTime(self)
                    self.self.calibAndImp = True
                    self.logger.info("IMPOSTAZIONE ORARIO TERMINATA")
                elif self.self.debugMode == False:
                    self.logger.info("MODALITA' DEBUG ATTIVATA...")
                    self.self.debugMode = True
                    self.logger.info("MODALITA' DEBUG IMPOSTATA")
                elif self.self.curveOnCom == False:
                    self.logger.info("CARICAMENTO CURVA IN CORSO...")
                    COMClass.sendCurveOnCom(self)
                    self.self.curveOnCom = True
                    self.logger.info("CARICAMENTO CURVA TERMINATA")
                if self.self.feedActive != self.self.activeFeed:
                    COMClass.startStopFeed(self)
                else:
                    now = QTime.currentTime()
                    seconds = int(now.toString("s"))
                    if now.hour() == 0 and now.minute() == 2 and not self.reset:
                        self.logger.info("RESET GIORNATA IN CORSO...")
                        COMClass.resetFeed(self)
                    if (seconds % 59) == 0: # ogni minuto
                        self.logger.info("LETTURA NORMALE IN CORSO...")
                        COMClass.readNowFeed(self)
                        COMClass.startStopFeed(self)
            t.sleep(1)

    def resetFeed(self):
#        for item in self.self.dbHall:
#            boxPos = self.self.dbBox.get(self.self.query.boxName == item.get('boxName'))
#            kg = self.self.dbBox.get(self.self.query.readNowFeedKG == item.get('boxName'))
#            sec = self.self.dbBox.get(self.self.query.readNowFeedSec == item.get('boxName'))
#            self.logger.info(f"ID:{boxPos} Kg: {kg}, sec: {sec}")

        self.self.dbHall.update({'readNowFeedKG':0})
        self.self.dbHall.update({'readNowFeedSec':0})
        self.reset = True


    def startStopFeed(self):
        self.offline = []
        if self.self.feedActive != self.self.activeFeed:
            self.self.feedActive = self.self.activeFeed
            if self.self.activeFeed > 0:
                self.self.curveOnCom = False
            for item in self.self.dbHall:
                boxPos = self.self.dbBox.get(self.self.query.boxName == item.get('boxName'))
                try:
                    boxCom = int(boxPos.get('comPos'))
                    # if boxCom in [30, 40]:
                    self.self.master.execute(boxCom, cst.WRITE_SINGLE_COIL, 0, output_value=self.self.activeFeed)
                    self.logger.info(f"ID:{boxCom} Pasto attivo: {self.self.activeFeed}")
                except:
                    if boxPos:
                        boxCom = int(boxPos.get('comPos'))
                        if boxCom not in self.offline:
                            self.offline.append(boxCom)
            self.body = f"Lista ID offline {self.offline}"
            self.logger.info(self.body)
            if len(self.offline) > self.max_offline:
                self.sendmail()

    def readNowFeed(self):
        self.offline = []
        for item in self.self.dbHall:
            boxPos = self.self.dbBox.get(self.self.query.boxName == item.get('boxName'))
            try:
                boxCom = int(boxPos.get('comPos'))
                if boxCom > 0:
                # if boxCom in [30, 40]:
                    (tHi, tLo, secToRun, secTrig, secDone, numReq, waterPerc, weightTarg, readNowFeedKG, calVal, hall, cage, boot, sw) = self.self.master.execute(boxCom, cst.READ_INPUT_REGISTERS,0,14)

                    # self.logger.info(f"Old values:{self.self.dbHall.get(self.self.query.boxName == item.get('boxName'))}")

                    self.logger.info(f"id:{boxCom}, name:{item.get('boxName')}, tHi:{tHi}, tLo:{tLo}, secToRun:{secToRun}, secTrig:{secTrig}, secDone:{secDone}, numReq:{numReq}, waterPerc:{waterPerc}, weightTarg:{weightTarg}, readNowFeedKG:{readNowFeedKG}, calVal:{calVal}, hall:{hall}, cage:{cage}, boot:{boot}, sw:{sw}")

                    if (QDateTime.currentSecsSinceEpoch() - ((tHi << 16) | tLo)) > (5 * 60) or self.reset:  #differenza di orario > 5 minuti
                        sec_done = self.self.dbHall.get(self.self.query.boxName == item.get('boxName'))['readNowFeedSec']
                        weight_done = self.self.dbHall.get(self.self.query.boxName == item.get('boxName'))['readNowFeedKG']
                        self.logger.info(f"id:{boxCom}, name:{item.get('boxName')}, Sincronizzo orologio e impostato secondi erogati: {sec_done} e kg: {weight_done}")
                        self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 0, output_value=((QDateTime.currentSecsSinceEpoch() >> 16) & 0xFFFF))
                        t.sleep(0.2)
                        self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 1, output_value=((QDateTime.currentSecsSinceEpoch() & 0xFFFF)))
                        t.sleep(1)
                        self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 4, output_value=sec_done)
                        t.sleep(0.2)
                        self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 8, output_value=weight_done)
                        t.sleep(0.2)
                        self.self.master.execute(boxCom, cst.WRITE_SINGLE_COIL, 0, output_value=self.self.activeFeed)
                        t.sleep(0.2)
                        (tHi, tLo, secToRun, secTrig, secDone, numReq, waterPerc, weightTarg, readNowFeedKG, calVal, hall, cage, boot, sw) = self.self.master.execute(boxCom, cst.READ_INPUT_REGISTERS,0,14)
                        self.logger.info(f"updated id:{boxCom}, name:{item.get('boxName')}, tHi:{tHi}, tLo:{tLo}, secToRun:{secToRun}, secTrig:{secTrig}, secDone:{secDone}, numReq:{numReq}, waterPerc:{waterPerc}, weightTarg:{weightTarg}, readNowFeedKG:{readNowFeedKG}, calVal:{calVal}, hall:{hall}, cage:{cage}, boot:{boot}, sw:{sw}")
                    else:
                        self.self.dbHall.upsert({'readNowFeedKG':readNowFeedKG}, self.self.query.boxName == item.get('boxName'))
                        self.self.dbHall.upsert({'readNowFeedSec':secDone}, self.self.query.boxName == item.get('boxName'))

                    # readNowFeedKG = self.self.master.execute(boxCom, cst.READ_INPUT_REGISTERS,8,1)
                    # self.logger.info(f"id:{boxCom} NowFeedKG:{readNowFeedKG}")
                    # self.self.dbHall.upsert({'readNowFeedKG':readNowFeedKG}, self.self.query.boxName == item.get('boxName'))
                    t.sleep(0.02)
                    for i in range(self.ui.tblHall.rowCount()):
                        if self.ui.tblHall.item(i,0).text() == item.get('boxName'):
                            self.ui.tblHall.setItem(i,7,QTableWidgetItem(str(readNowFeedKG)))

                            #calc perc
                            perc = 0
                            if float(item.get("curKGToday")) > 0:
                                try:
                                    perc = int(float(readNowFeedKG)/float(item.get("curKGToday"))*100)
                                except:
                                    pass
                            self.ui.tblHall.setItem(i, 9, QTableWidgetItem(str(perc)))

            except Exception as e:
                if boxPos:
                    boxCom = int(boxPos.get('comPos'))
                    # self.logger.info(f"ID:{boxCom} offline")
                    if boxCom not in self.offline:
                            self.offline.append(boxCom)
        self.body = f"Lista ID offline {self.offline}"
        if self.reset:
        	self.reset = False
        self.logger.info(self.body)
        if len(self.offline) > self.max_offline:
            self.sendmail()

    def sendCurveOnCom(self):
        self.offline = []
        numero_pasti = self.self.dbTime.count(self.self.query.active =="SI")
        pasto_attivo = self.self.activeFeed
        for item in self.self.dbHall:
            try:
                boxPos = self.self.dbBox.get(self.self.query.boxName == item.get('boxName'))
                qty_giornaliera = int(item.get('curKGToday'))
                qty_slot = int((qty_giornaliera / numero_pasti) * pasto_attivo)
                boxCom = int(boxPos.get('comPos'))
                # if boxCom in [30, 40]:
                self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 7, output_value=qty_slot)
                self.logger.info(f"ID:{boxCom} Curva caricata, qty_slot:{qty_slot}")
            except:
                if boxPos:
                    boxCom = int(boxPos.get('comPos'))
                    if boxCom not in self.offline:
                            self.offline.append(boxCom)
        self.body = f"Lista ID offline {self.offline}"
        self.logger.info(self.body)
        if len(self.offline) > self.max_offline:
            self.sendmail()
                # pass
                # print("NON LETTO")

    def setTime(self):
        self.offline = []
        for item in self.self.dbHall:
            boxPos = self.self.dbBox.get(self.self.query.boxName == item.get('boxName'))
            try:
                now = QDateTime.currentSecsSinceEpoch()
                boxCom = int(boxPos.get('comPos'))
                self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 0, output_value=((now >> 16) & 0xFFFF))
                t.sleep(0.2)
                self.self.master.execute(boxCom, cst.WRITE_SINGLE_REGISTER, 1, output_value=((now & 0xFFFF)))
                self.logger.info(f"ID:{boxCom} Orario impostato")
            except:
                if boxPos:
                    boxCom = int(boxPos.get('comPos'))
                    # self.logger.info(f"ID:{boxCom} offline")
                    if boxCom not in self.offline:
                            self.offline.append(boxCom)
        self.body = f"Lista ID offline {self.offline}"
        self.logger.info(self.body)
        if len(self.offline) > self.max_offline:
            self.sendmail()

    def daily_report(self, file_relative_path):
        # file_name = "reports/myFile.csv"

        with open(file_relative_path, "a", newline="\n") as file:
            field_names = ["id", "boxName", "sowName", "weightTarg", "readNowFeedKG", "secDone", "date"]
            writer = csv.DictWriter(file, field_names)

            if os.stat(file_relative_path).st_size == 0:
                writer.writeheader()

            data = QDate.currentDate().addDays(-1).toString("dd/MM/yyyy")

            for row in self.self.dbHall:
                boxPos = self.self.dbBox.get(self.self.query.boxName == row.get('boxName'))
                try:
                    boxCom = int(boxPos.get('comPos'))

                    if boxCom > 0:
                        (tHi, tLo, secToRun, secTrig, secDone, numReq, waterPerc, weightTarg, readNowFeedKG, calVal,
                         hall, cage, boot, sw) = self.self.master.execute(boxCom, cst.READ_INPUT_REGISTERS, 0, 14)

                        writer.writerow({"id": str(boxCom),
                                         "boxName": row.get("boxName"),
                                         "sowName": row.get("sowName"),
                                         "weightTarg": str(weightTarg),
                                         "readNowFeedKG": str(readNowFeedKG),
                                         "secDone": str(secDone),
                                         "date": data})
                except Exception as e:
                    pass