import matplotlib.pyplot as plt
import pandas as pd
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from main import *


class UIFunctions():

    def defineUI(self):
        self.ui.tblHall.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tblHall.verticalHeader().hide()
        self.ui.tblCurve.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tblCurve.setRowCount(50)
        self.ui.tblTime.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tblSow.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tblBox.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        QScroller.grabGesture(self.ui.tblCurve, QScroller.LeftMouseButtonGesture)
        self.ui.tblCurve.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        QScroller.grabGesture(self.ui.tblTime, QScroller.LeftMouseButtonGesture)
        self.ui.tblTime.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        QScroller.grabGesture(self.ui.scrollAreaSettingsMain, QScroller.LeftMouseButtonGesture)
        self.ui.spiAddSelEntryDate.setCalendarPopup(True)
        self.ui.spiAddSelEntryDate.setMaximumDate(QDate.currentDate())
        self.ui.spiAddSelPigDate.setCalendarPopup(True)
        self.ui.spiAddSelPigDate.setMaximumDate(QDate.currentDate())
        self.ui.radAddBirthN.setChecked(True)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # add the shadow object to the frame
        self.ui.fr1Top.raise_()
        self.ui.fr1Top.setGraphicsEffect(self.shadow)

    def animazioneMenu(self):
        width = self.ui.frLeftMenu.width()
        maxExtend = 300
        standard = 75

        if width == 75:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        self.animation = QPropertyAnimation(self.ui.frLeftMenu, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def animazioneMenuData(self):
        height = self.ui.frDataAdd.height()
        maxExtend = 200
        standard = 0

        if height == 0:
            heightExtended = maxExtend
        else:
            heightExtended = standard

        self.animation = QPropertyAnimation(self.ui.frDataAdd, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setStartValue(height)
        self.animation.setEndValue(heightExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def animazioneMenuParto(self, val):
        height = self.ui.frAddBirth.height()
        maxExtend = 200
        standard = 0
        if val:
            heightExtended = maxExtend
            self.ui.txtAddCurType.setText("Parto")
            self.ui.spiAddSelCurDay.setMinimum(1)
            self.ui.spiAddSelCurDay.setMaximum(35)
            self.ui.spiAddSelCurDay.setValue(1)

        else:
            heightExtended = standard
            self.ui.txtAddCurType.setText("Gestazione")
            self.ui.spiAddSelCurDay.setMinimum(101)
            self.ui.spiAddSelCurDay.setMaximum(114)
            self.ui.spiAddSelCurDay.setValue(101)

        self.animation = QPropertyAnimation(self.ui.frAddBirth, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setStartValue(height)
        self.animation.setEndValue(heightExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def loadCurveUI(self):
        for i in range(50):
            if i < 15:
                self.ui.tblCurve.setItem(i, 0, QTableWidgetItem("Gestazione"))
                self.ui.tblCurve.setItem(i, 1, QTableWidgetItem(str(i + 101)))
            else:
                self.ui.tblCurve.setItem(i, 0, QTableWidgetItem("Parto"))
                self.ui.tblCurve.setItem(i, 1, QTableWidgetItem(str(i - 14)))

    def sowGraph(self):
        plt.cla()
        plt.clf()

        gestazione = [None] * 15
        parto = [None] * 35
        curva = self.dbCurve.get(doc_id=self.ui.spiCurve.value())
        for i in range(15):
            gestazione[i] = float(curva.get('{}'.format(i)))
        for i in range(15, 50):
            parto[i - 15] = float(curva.get('{}'.format(i)))
        layout = QVBoxLayout()
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#3f3c5b'
        colors = [
            '#08F7FE',  # teal/cyan
            '#FE53BB',  # pink
            '#F5D300',  # yellow
            '#00ff41',  # matrix green
        ]
        self.df = pd.DataFrame({'Gestazione': gestazione})
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

        # self.fig, self.ax = plt.subplots()
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        self.df.plot(marker='o', color=colors,
                     ax=self.ax)  # Redraw the data with low alpha and slighty increased linewidth:
        n_shades = 10
        diff_linewidth = 1.05
        alpha_value = 0.3 / n_shades
        for n in range(1, n_shades + 1):
            self.df.plot(marker='o', linewidth=2 + (diff_linewidth * n), alpha=alpha_value, legend=False, ax=self.ax,
                         color=colors)  # Color the areas below the lines:
        for column, color in zip(self.df, colors):
            self.ax.fill_between(x=self.df.index, y1=self.df[column].values, y2=[0] * len(self.df), color=color,
                                 alpha=0.1)
        self.ax.grid(color='#2d2b42')
        self.ax.set_xlim([self.ax.get_xlim()[0] - 0.2, self.ax.get_xlim()[1] + 0.2])
        plt.subplots_adjust(top=0.9, bottom=0.1, right=0.95, left=0.05, hspace=1, wspace=0)
        plt.margins(0, 0)
        plt.box(False)
        plotWidget = FigureCanvas(self.fig)
        layout.addWidget(plotWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.curveGraph.setLayout(layout)

    def updateGraph(self):
        colors = [
            '#08F7FE',  # teal/cyan
            '#FE53BB',  # pink
            '#F5D300',  # yellow
            '#00ff41',  # matrix green
        ]
        self.ax.cla()
        try:
            curva = self.dbCurve.get(doc_id=self.ui.spiCurve.value())
            if self.ui.tblCurve.currentRow() < 15:
                gestazione = [None] * 15
                for i in range(15):
                    gestazione[i] = float(curva.get('{}'.format(i)))
                self.df = pd.DataFrame({'Gestazione': gestazione})
                colorato = colors[0]
            else:
                parto = [None] * 35
                for i in range(15, 50):
                    parto[i - 15] = float(curva.get('{}'.format(i)))
                self.df = pd.DataFrame({'Parto': parto})
                colorato = colors[1]
            self.df.plot(marker='o', color=colorato, ax=self.ax)
            n_shades = 10
            diff_linewidth = 1.05
            alpha_value = 0.3 / n_shades
            for n in range(1, n_shades + 1):
                self.df.plot(marker='o', linewidth=2 + (diff_linewidth * n), alpha=alpha_value, legend=False,
                             ax=self.ax, color=colorato)
            for column, color in zip(self.df, colors):
                self.ax.fill_between(x=self.df.index, y1=self.df[column].values, y2=[0] * len(self.df), color=colorato,
                                     alpha=0.1)
            self.ax.grid(color='#2d2b42')
            self.ax.set_xlim([self.ax.get_xlim()[0] - 0.2, self.ax.get_xlim()[1] + 0.2])
            plt.subplots_adjust(top=0.9, bottom=0.1, right=0.95, left=0.05, hspace=1, wspace=0)
            plt.ylabel("KILOGRAMMI")
            plt.xlabel("GIORNI")
            plt.margins(0.2, 0.2)
            plt.box(False)
            self.fig.canvas.draw_idle()
        except:
            self.ui.lblCurveStatus.setText("CURVA NON VALIDA.")

    def base_sow_graph(self):
        layout = QVBoxLayout()
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#3f3c5b'
        colors = [
            '#08F7FE',  # teal/cyan
            '#FE53BB',  # pink
            '#F5D300',  # yellow
            '#00ff41',  # matrix green
        ]
        gestazione = UIFunctions.get_base_df(self)
        self.data_frame = pd.DataFrame(gestazione)
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
        # self.figura, self.axxx = plt.subplots()
        self.figura = Figure()
        self.axxx = self.figura.add_subplot(111)

        # self.data_frame.plot(x="giorni", y="gestazione", marker='o', color=colors, ax=self.axxx)
        self.df.plot(marker='o', color=colors, ax=self.ax)

        n_shades = 10
        diff_linewidth = 1.05
        alpha_value = 0.3 / n_shades
        for n in range(1, n_shades + 1):
            self.data_frame.plot(marker='o', linewidth=2 + (diff_linewidth * n), alpha=alpha_value, legend=False,
                                 ax=self.axxx,
                                 color=colors)  # Color the areas below the lines:
        for column, color in zip(self.data_frame, colors):
            self.axxx.fill_between(x=self.data_frame.index, y1=self.data_frame[column].values,
                                   y2=[0] * len(self.data_frame), color=color, alpha=0.1)
        self.axxx.grid(color='#2d2b42')

        self.axxx.set_xlim([self.axxx.get_xlim()[0] - 0.2, self.axxx.get_xlim()[1] + 0.2])
        plt.subplots_adjust(top=0.9, bottom=0.1, right=0.95, left=0.05, hspace=1, wspace=0)
        plt.margins(0, 0)
        plt.box(False)
        plotWidget = FigureCanvas(self.figura)
        layout.addWidget(plotWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.figura.canvas.draw_idle()
        # plotWidget.draw()
        # plotWidget.show()

        self.ui.pigGraph.setLayout(layout)

    def draw_sow_graph(self, df_ideal, df_real):
        colors = [
            '#08F7FE',  # teal/cyan
            '#FE53BB',  # pink
            '#F5D300',  # yellow
            '#00ff41',  # matrix green
        ]

        self.axxx.cla()

        # df_ideal = UIFunctions.get_dataframes_parto(self)
        # df_real = UIFunctions.get_real_curve(self)

        self.data_frame = pd.DataFrame(df_ideal)
        # self.data_frame.plot(x="giorni", y="parto", kind ="line", marker="o", ax = self.axxx)

        self.data_frame.plot(x="giorni", y="teorico", marker='o', ax=self.axxx)

        self.data_frame = pd.DataFrame(df_real)
        self.data_frame.plot(x="giorni", y="consumato", marker='o', ax=self.axxx)

        plt.ylabel("KILOGRAMMI")
        plt.xlabel("GIORNI")
        plt.margins(0.2, 0.2)
        plt.box(False)
        self.figura.canvas.draw_idle()

    def get_ideal_curve(self):
        current_row = self.ui.tblSowRecord.currentRow()
        current_column = self.ui.tblSowRecord.currentColumn()
        if self.ui.cboxPigBox.currentIndex() == 0:
            name = self.ui.searchPanel.text().lstrip().rstrip()
        else:
            name = self.ui.tblSowRecord.item(current_row, 0).text()

        entry_date = self.ui.tblSowRecord.item(current_row, 1).text()
        exit_date = self.ui.tblSowRecord.item(current_row, 3).text()

        exit_date = QDate.fromString(exit_date, "dd/MM/yyyy")

        nr_curve = -1
        if not exit_date.isValid():
            try:
                hall_data = self.dbHall.get(self.query.sowName == name)
                nr_curve = hall_data.get("nrCurve")
            except:
                pass
        else:
            try:
                history_data = self.dbSowHistory.get((self.query.sowName == name) & (self.query.entryDate == entry_date))
                nr_curve = history_data.get("nrCurve")

            except:
                pass

        if nr_curve == -1:
            return False

        curve = self.dbCurve.get(doc_id=int(nr_curve))

        ideal_curve_gestazione = [None] * 15
        for i in range(15):
            ideal_curve_gestazione[i] = float(curve.get(str(i)))

        ideal_curve_parto = [None] * 35
        for i in range(15, 50):
            ideal_curve_parto[i - 15] = float(curve.get(str(i)))

        df_ideal_gestazione = {"teorico": ideal_curve_gestazione}
        df_ideal_gestazione.update({"giorni": [i for i in range(1, 16)]})

        df_ideal_parto = {"teorico": ideal_curve_parto}
        df_ideal_parto.update({"giorni": [i for i in range(1, 36)]})

        return df_ideal_gestazione, df_ideal_parto

    def get_real_curve(self):

        current_row = self.ui.tblSowRecord.currentRow()
        current_column = self.ui.tblSowRecord.currentColumn()

        if self.ui.cboxPigBox.currentIndex() == 0:
            name = self.ui.searchPanel.text().lstrip().rstrip()
        else:
            name = self.ui.tblSowRecord.item(current_row, 0).text()

        entry_date = self.ui.tblSowRecord.item(current_row, 1).text()
        exit_date = self.ui.tblSowRecord.item(current_row, 3).text()

        exit_date = QDate.fromString(exit_date, "dd/MM/yyyy")

        real_gestazione_kg = []
        real_gestazione_day = []
        real_parto_kg = []
        real_parto_day = []

        nr_curve = None
        sow_sit = None
        cur_day = None
        cur_day = None

        # sow is in hall
        if not exit_date.isValid():
            try:
                hall_data = self.dbHall.get(self.query.sowName == name)
                nr_curve = hall_data.get("nrCurve")
                sow_sit = hall_data.get("sowSit")
                cur_day = hall_data.get("curDay")
                cur_day = QDate.fromString(cur_day, "dd/MM/yyyy")
            except Exception as e:
                print(e)
        else:
            try:
                history_data = self.dbSowHistory.get((self.query.sowName == name) & (self.query.entryDate == entry_date))
                nr_curve = history_data.get("nrCurve")
                sow_sit = history_data.get("sowSit")
                cur_day = history_data.get("curDay")
                cur_day = history_data.get("curDay")
                cur_day = QDate.fromString(cur_day, "dd/MM/yyyy")
            except Exception as e:
                print(e)

        sow_record = self.dbSowRecord.search(
            (self.query.sowName == name) & (self.query.entryDate == entry_date))
        print(sow_record)

        for element in sow_record:
            day_recorded = QDate.fromString(element.get("day_recorded"), "dd/MM/yyyy")
            consumedKG = float(element.get("consumedKG"))
            print(str(sow_sit) + " " +day_recorded.toString("dd/MM/yyyy") + " " + cur_day.toString("dd/MM/yyyy") + " " + str(
                consumedKG))
            if sow_sit == 1:
                if day_recorded >= cur_day:
                    real_parto_kg.append(consumedKG)
                    real_parto_day.append(cur_day.daysTo(day_recorded) + 1)
                else:
                    real_gestazione_kg.append(consumedKG)
                    real_gestazione_day.append(day_recorded.daysTo(cur_day) + 1)
            elif sow_sit == 0:
                real_gestazione_kg.append(consumedKG)
                real_gestazione_day.append(cur_day.daysTo(day_recorded) + 1)

        df_real_parto = {"consumato": real_parto_kg}
        df_real_parto.update({"giorni": real_parto_day})

        df_real_gestazione = {"consumato": real_gestazione_kg}
        df_real_gestazione.update({"giorni": real_gestazione_day})

        return df_real_gestazione, df_real_parto

    def get_base_df(self):
        curve = self.dbCurve.get(doc_id=int(1))

        ideal_curve_gestazione = [None] * 15
        for i in range(15):
            ideal_curve_gestazione[i] = float(curve.get(str(i)))

        df_ideal_gestazione = {"gestazione": ideal_curve_gestazione}
        # df_ideal_gestazione.update({"giorni": [i for i in range(0, 15)]})
        ideal_curve_parto = [None] * 35
        for i in range(15, 50):
            ideal_curve_parto[i - 15] = float(curve.get(str(i)))

        df_ideal_parto = {"parto": ideal_curve_parto}
        df_ideal_parto.update({"giorni": [i for i in range(0, 35)]})
        return df_ideal_gestazione

    def sow_graph_cbox_changed(self):
        if self.ui.tblSowRecord.currentRow() >= 0:

            df_ideal_gestazione, df_ideal_parto = UIFunctions.get_ideal_curve(self)
            df_real_gestazione, df_real_parto = UIFunctions.get_real_curve(self)

            if self.ui.cboxCurve.currentIndex() == 0:
                UIFunctions.draw_sow_graph(self, df_ideal_gestazione, df_real_gestazione)
            else:
                UIFunctions.draw_sow_graph(self, df_ideal_parto, df_real_parto)
