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
        self.shadow.setColor(QColor(0,0,0, 150))
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

    def animazioneMenuParto(self,val):
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
                 self.ui.tblCurve.setItem(i,0,QTableWidgetItem("Gestazione"))
                 self.ui.tblCurve.setItem(i,1,QTableWidgetItem(str(i+101)))
             else:
                 self.ui.tblCurve.setItem(i,0,QTableWidgetItem("Parto"))
                 self.ui.tblCurve.setItem(i,1,QTableWidgetItem(str(i-14)))

    def sowGraph(self):
        gestazione = [None] * 15
        parto = [None] * 35
        curva = self.dbCurve.get(doc_id=self.ui.spiCurve.value())
        for i in range(15):
            gestazione[i] = float(curva.get('{}'.format(i)))
        for i in range(15,50):
            parto[i-15] = float(curva.get('{}'.format(i)))
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
        self.fig, self.ax = plt.subplots()
        self.df.plot(marker='o', color=colors, ax=self.ax)# Redraw the data with low alpha and slighty increased linewidth:
        n_shades = 10
        diff_linewidth = 1.05
        alpha_value = 0.3 / n_shades
        for n in range(1, n_shades+1):
            self.df.plot(marker='o',linewidth=2+(diff_linewidth*n),alpha=alpha_value,legend=False,ax=self.ax,color=colors)# Color the areas below the lines:
        for column, color in zip(self.df, colors):
            self.ax.fill_between(x=self.df.index,y1=self.df[column].values,y2=[0] * len(self.df),color=color,alpha=0.1)
        self.ax.grid(color='#2d2b42')
        self.ax.set_xlim([self.ax.get_xlim()[0] - 0.2, self.ax.get_xlim()[1] + 0.2])
        plt.subplots_adjust(top = 0.9, bottom = 0.1, right = 0.95, left = 0.05, hspace = 1, wspace = 0)
        plt.margins(0,0)
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
                for i in range(15,50):
                    parto[i-15] = float(curva.get('{}'.format(i)))
                self.df = pd.DataFrame({'Parto': parto})
                colorato = colors[1]
            self.df.plot(marker='o',color=colorato, ax=self.ax)
            n_shades = 10
            diff_linewidth = 1.05
            alpha_value = 0.3 / n_shades
            for n in range(1, n_shades+1):
                self.df.plot(marker='o',linewidth=2+(diff_linewidth*n),alpha=alpha_value,legend=False,ax=self.ax,color=colorato)
            for column, color in zip(self.df, colors):
                self.ax.fill_between(x=self.df.index,y1=self.df[column].values,y2=[0] * len(self.df),color=colorato,alpha=0.1)
            self.ax.grid(color='#2d2b42')
            self.ax.set_xlim([self.ax.get_xlim()[0] - 0.2, self.ax.get_xlim()[1] + 0.2])
            plt.subplots_adjust(top = 0.9, bottom = 0.1, right = 0.95, left = 0.05, hspace = 1, wspace = 0)
            plt.ylabel("KILOGRAMMI")
            plt.xlabel("GIORNI")
            plt.margins(0.2,0.2)
            plt.box(False)
            self.fig.canvas.draw_idle()
        except:
            self.ui.lblCurveStatus.setText("CURVA NON VALIDA.")
