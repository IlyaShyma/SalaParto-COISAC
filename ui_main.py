# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1230, 757)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"#fr1Top {\n"
"background-color: #3f3c5b;\n"
"border-bottom: 3px solid #bd93f9;\n"
"}\n"
"\n"
"#fr1Top .QPushButton {	\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 5px;\n"
"background-color: transparent;\n"
"color: #f8f8f2;\n"
"}\n"
"\n"
"#fr1Top .QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #bd93f9;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"#fr1Top .QComboBox {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"#fr1Top .QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"}\n"
"#fr1Top .QPushButton:pressed {	\n"
"background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#frClose {\n"
"background-color: #bd93f9\n"
"}\n"
"\n"
"#fr3Bottom {\n"
"background-color: #3f3c5b;\n"
"border-top: 3px solid #bd93f9;\n"
"}\n"
"\n"
"#fr3Bottom .QLabel{\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"#frLeftMenu {\n"
"background-color: #323048;\n"
"}\n"
"\n"
"#frL"
                        "eftMenu .QPushButton {\n"
"background-color: #323048;\n"
"border: none;\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"}\n"
"\n"
"#frLeftMenu .QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.stylesheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frBg = QFrame(self.stylesheet)
        self.frBg.setObjectName(u"frBg")
        self.frBg.setFrameShape(QFrame.NoFrame)
        self.frBg.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr1Top = QFrame(self.frBg)
        self.fr1Top.setObjectName(u"fr1Top")
        self.fr1Top.setMinimumSize(QSize(0, 50))
        self.fr1Top.setMaximumSize(QSize(16777215, 50))
        self.fr1Top.setFrameShape(QFrame.NoFrame)
        self.fr1Top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.fr1Top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frLogo = QFrame(self.fr1Top)
        self.frLogo.setObjectName(u"frLogo")
        self.frLogo.setMinimumSize(QSize(75, 0))
        self.frLogo.setMaximumSize(QSize(75, 16777215))
        self.frLogo.setStyleSheet(u"background-image: url(:/resources/resources/logo/GT.png);")
        self.frLogo.setFrameShape(QFrame.NoFrame)
        self.frLogo.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frLogo)

        self.frName = QFrame(self.fr1Top)
        self.frName.setObjectName(u"frName")
        self.frName.setFrameShape(QFrame.NoFrame)
        self.frName.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frName)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblTimer = QLabel(self.frName)
        self.lblTimer.setObjectName(u"lblTimer")
        self.lblTimer.setStyleSheet(u"color: white;\n"
"font-size: 15pt;")

        self.horizontalLayout_3.addWidget(self.lblTimer)

        self.spcrTopMenu = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.spcrTopMenu)

        self.comLanguage = QComboBox(self.frName)
        self.comLanguage.addItem("")
        self.comLanguage.addItem("")
        self.comLanguage.addItem("")
        self.comLanguage.setObjectName(u"comLanguage")
        self.comLanguage.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_3.addWidget(self.comLanguage)


        self.horizontalLayout.addWidget(self.frName)

        self.frWindow = QFrame(self.fr1Top)
        self.frWindow.setObjectName(u"frWindow")
        self.frWindow.setMaximumSize(QSize(120, 16777215))
        self.frWindow.setFrameShape(QFrame.NoFrame)
        self.frWindow.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frWindow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnMinimize = QPushButton(self.frWindow)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMaximumSize(QSize(28, 28))
        self.btnMinimize.setStyleSheet(u"background-image: url(:/menu/resources/menu/icon_minimize.png);")

        self.horizontalLayout_2.addWidget(self.btnMinimize)

        self.btnMaximize = QPushButton(self.frWindow)
        self.btnMaximize.setObjectName(u"btnMaximize")
        self.btnMaximize.setMaximumSize(QSize(28, 28))
        self.btnMaximize.setStyleSheet(u"background-image: url(:/menu/resources/menu/icon_maximize.png);")

        self.horizontalLayout_2.addWidget(self.btnMaximize)

        self.btnClose = QPushButton(self.frWindow)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMaximumSize(QSize(28, 28))
        self.btnClose.setStyleSheet(u"background-image: url(:/menu/resources/menu/icon_close.png);")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.horizontalLayout.addWidget(self.frWindow)


        self.verticalLayout_2.addWidget(self.fr1Top)

        self.fr2Content = QFrame(self.frBg)
        self.fr2Content.setObjectName(u"fr2Content")
        self.fr2Content.setMaximumSize(QSize(16777215, 16777215))
        self.fr2Content.setFrameShape(QFrame.NoFrame)
        self.fr2Content.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.fr2Content)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.fr3Bottom = QFrame(self.fr2Content)
        self.fr3Bottom.setObjectName(u"fr3Bottom")
        self.fr3Bottom.setMinimumSize(QSize(0, 30))
        self.fr3Bottom.setMaximumSize(QSize(16777215, 20))
        self.fr3Bottom.setStyleSheet(u"")
        self.fr3Bottom.setFrameShape(QFrame.NoFrame)
        self.fr3Bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.fr3Bottom)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(40, 0, 40, 9)
        self.lblCompany = QLabel(self.fr3Bottom)
        self.lblCompany.setObjectName(u"lblCompany")
        self.lblCompany.setFrameShape(QFrame.NoFrame)
        self.lblCompany.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.lblCompany)

        self.lblVersion = QLabel(self.fr3Bottom)
        self.lblVersion.setObjectName(u"lblVersion")
        self.lblVersion.setFrameShape(QFrame.NoFrame)
        self.lblVersion.setFrameShadow(QFrame.Plain)
        self.lblVersion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblVersion)


        self.gridLayout.addWidget(self.fr3Bottom, 2, 1, 1, 1)

        self.frLeftMenu = QFrame(self.fr2Content)
        self.frLeftMenu.setObjectName(u"frLeftMenu")
        self.frLeftMenu.setMinimumSize(QSize(75, 0))
        self.frLeftMenu.setMaximumSize(QSize(75, 16777215))
        self.frLeftMenu.setStyleSheet(u"QPushButton {\n"
"background-position: left center;\n"
"padding-left: 60px;\n"
"text-align: left;\n"
"border: none;\n"
"border-left: 22px solid transparent;\n"
"font-size: 15pt;\n"
"color: white;\n"
"}")
        self.frLeftMenu.setFrameShape(QFrame.NoFrame)
        self.frLeftMenu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frLeftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMenu = QPushButton(self.frLeftMenu)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setMinimumSize(QSize(0, 60))
        self.btnMenu.setStyleSheet(u"background-image: url(:/menu/resources/menu/icon_menu.png);\n"
"background-color: #2d2b42;")

        self.verticalLayout_3.addWidget(self.btnMenu)

        self.btnHome = QPushButton(self.frLeftMenu)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 75))
        self.btnHome.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-home.png);")

        self.verticalLayout_3.addWidget(self.btnHome)

        self.btnHall = QPushButton(self.frLeftMenu)
        self.btnHall.setObjectName(u"btnHall")
        self.btnHall.setMinimumSize(QSize(0, 75))
        self.btnHall.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-briefcase.png);")

        self.verticalLayout_3.addWidget(self.btnHall)

        self.btnCurve = QPushButton(self.frLeftMenu)
        self.btnCurve.setObjectName(u"btnCurve")
        self.btnCurve.setMinimumSize(QSize(0, 75))
        self.btnCurve.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-arrow-right.png);")

        self.verticalLayout_3.addWidget(self.btnCurve)

        self.btnTime = QPushButton(self.frLeftMenu)
        self.btnTime.setObjectName(u"btnTime")
        self.btnTime.setMinimumSize(QSize(0, 75))
        self.btnTime.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-alarm.png);")

        self.verticalLayout_3.addWidget(self.btnTime)

        self.btnStock = QPushButton(self.frLeftMenu)
        self.btnStock.setObjectName(u"btnStock")
        self.btnStock.setMinimumSize(QSize(0, 75))
        self.btnStock.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-medical-cross.png);")

        self.verticalLayout_3.addWidget(self.btnStock)

        self.btnData = QPushButton(self.frLeftMenu)
        self.btnData.setObjectName(u"btnData")
        self.btnData.setMinimumSize(QSize(0, 75))
        self.btnData.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-data.png);")

        self.verticalLayout_3.addWidget(self.btnData)

        self.btnCom = QPushButton(self.frLeftMenu)
        self.btnCom.setObjectName(u"btnCom")
        self.btnCom.setMinimumSize(QSize(0, 75))
        self.btnCom.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/cil-link.png);")

        self.verticalLayout_3.addWidget(self.btnCom)

        self.btnPig = QPushButton(self.frLeftMenu)
        self.btnPig.setObjectName(u"btnPig")
        self.btnPig.setMinimumSize(QSize(75, 75))
        self.btnPig.setStyleSheet(u"background-image: url(:/leftMenu/resources/leftMenu/pig.png);")
        self.btnPig.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btnPig)

        self.spcrLeftMenu = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.spcrLeftMenu)

        self.btnSettings = QPushButton(self.frLeftMenu)
        self.btnSettings.setObjectName(u"btnSettings")

        self.verticalLayout_3.addWidget(self.btnSettings)


        self.gridLayout.addWidget(self.frLeftMenu, 0, 0, 3, 1)

        self.frPages = QFrame(self.fr2Content)
        self.frPages.setObjectName(u"frPages")
        self.frPages.setMaximumSize(QSize(16777215, 16777215))
        self.frPages.setStyleSheet(u"QLabel {\n"
"border-left: 2px solid #3f3c5b;\n"
"padding-left: 5px;\n"
"font-size: 20pt;\n"
"font-family: \"Segoe UI\"\n"
"}\n"
"\n"
"QHeaderView {\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"font-size: 15pt;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(237,85,101);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(237,85,101);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgba(72,207,173,255);\n"
"	border: 3px solid rgba(72,207,173,255);	\n"
"}\n"
"\n"
"QSpinBox {\n"
"	padding-left: 18px;\n"
"	font-size: 20pt;\n"
"	border: none;\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-position: right; width: 40px; height: 40px;\n"
"	image: url(:/addons/resources/addons/right.png);\n"
"	border: 1px outset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QSpinBox::up-button::pressed {\n"
"	border: 1px inset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QSpinBox::down-b"
                        "utton {\n"
"	subcontrol-position: left; width: 40px; height: 40px;\n"
"	image: url(:/addons/resources/addons/left.png);\n"
"	border: 1px outset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QSpinBox::down-button::pressed {\n"
"	border: 1px inset rgb(222, 221, 218)\n"
"}\n"
"QDoubleSpinBox {\n"
"	padding-left: 18px;\n"
"	font-size: 20pt;\n"
"	border: none;\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"	subcontrol-position: right; width: 40px; height: 40px;\n"
"	image: url(:/addons/resources/addons/right.png);\n"
"	border: 1px outset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button::pressed {\n"
"	border: 1px inset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	subcontrol-position: left; width: 40px; height: 40px;\n"
"	image: url(:/addons/resources/addons/left.png);\n"
"	border: 1px outset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button::pressed {\n"
"	border: 1px inset rgb(222, 221, 218)\n"
"}\n"
"QWidget {\n"
"background-color: rgb(242,243,248);\n"
"}\n"
"")
        self.frPages.setFrameShape(QFrame.NoFrame)
        self.frPages.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frPages)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.frPages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pgHome = QWidget()
        self.pgHome.setObjectName(u"pgHome")
        self.pgHome.setStyleSheet(u"background-color: #f2f3f8;")
        self.verticalLayout_6 = QVBoxLayout(self.pgHome)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 0)
        self.frHome = QFrame(self.pgHome)
        self.frHome.setObjectName(u"frHome")
        self.frHome.setFrameShape(QFrame.NoFrame)
        self.frHome.setFrameShadow(QFrame.Plain)

        self.verticalLayout_6.addWidget(self.frHome)

        self.stackedWidget.addWidget(self.pgHome)
        self.pgHall = QWidget()
        self.pgHall.setObjectName(u"pgHall")
        self.pgHall.setStyleSheet(u"background-color: #f2f3f8;")
        self.verticalLayout_5 = QVBoxLayout(self.pgHall)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.frHall = QFrame(self.pgHall)
        self.frHall.setObjectName(u"frHall")
        self.frHall.setFrameShape(QFrame.NoFrame)
        self.frHall.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frHall)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setContentsMargins(0, 10, 0, 0)
        self.hallSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hallSpacer, 0, 2, 1, 1)

        self.frame = QFrame(self.frHall)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(300, 50))
        self.frame.setStyleSheet(u"font-size: 15pt;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(0)
        self.lblHallCom = QLabel(self.frame)
        self.lblHallCom.setObjectName(u"lblHallCom")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.lblHallCom)

        self.chkHallCom = QCheckBox(self.frame)
        self.chkHallCom.setObjectName(u"chkHallCom")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.chkHallCom)


        self.horizontalLayout_15.addLayout(self.formLayout_9)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_11.setHorizontalSpacing(0)
        self.formLayout_11.setVerticalSpacing(0)
        self.chkHallFeed = QCheckBox(self.frame)
        self.chkHallFeed.setObjectName(u"chkHallFeed")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.chkHallFeed)

        self.lblHallFeed = QLabel(self.frame)
        self.lblHallFeed.setObjectName(u"lblHallFeed")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.lblHallFeed)


        self.horizontalLayout_15.addLayout(self.formLayout_11)


        self.gridLayout_2.addWidget(self.frame, 0, 3, 1, 1)

        self.spiHall = QSpinBox(self.frHall)
        self.spiHall.setObjectName(u"spiHall")
        self.spiHall.setMinimumSize(QSize(137, 50))
        font = QFont()
        font.setPointSize(20)
        self.spiHall.setFont(font)
        self.spiHall.setStyleSheet(u"")
        self.spiHall.setMinimum(1)
        self.spiHall.setMaximum(30)

        self.gridLayout_2.addWidget(self.spiHall, 0, 1, 1, 1)

        self.lblHall = QLabel(self.frHall)
        self.lblHall.setObjectName(u"lblHall")
        self.lblHall.setMinimumSize(QSize(250, 50))

        self.gridLayout_2.addWidget(self.lblHall, 0, 0, 1, 1)

        self.tblHall = QTableWidget(self.frHall)
        if (self.tblHall.columnCount() < 14):
            self.tblHall.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblHall.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        if (self.tblHall.rowCount() < 1):
            self.tblHall.setRowCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblHall.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblHall.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblHall.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblHall.setItem(0, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblHall.setItem(0, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tblHall.setItem(0, 5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tblHall.setItem(0, 7, __qtablewidgetitem20)
        self.tblHall.setObjectName(u"tblHall")
        self.tblHall.setStyleSheet(u"")
        self.tblHall.setFrameShape(QFrame.NoFrame)
        self.tblHall.setFrameShadow(QFrame.Plain)
        self.tblHall.setGridStyle(Qt.SolidLine)

        self.gridLayout_2.addWidget(self.tblHall, 1, 0, 1, 6)

        self.frHallExtra = QFrame(self.frHall)
        self.frHallExtra.setObjectName(u"frHallExtra")
        self.frHallExtra.setMinimumSize(QSize(0, 0))
        self.frHallExtra.setMaximumSize(QSize(0, 16777215))
        self.frHallExtra.setStyleSheet(u"QLabel, QLineEdit {\n"
"font-size: 11pt;\n"
"color: black;\n"
"background: transparent;\n"
"}\n"
"\n"
"#frHallExtra {\n"
"background-color: rgba(230,230,240,255);\n"
"}")
        self.frHallExtra.setFrameShape(QFrame.NoFrame)
        self.frHallExtra.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.frHallExtra)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lblHallExtra = QLabel(self.frHallExtra)
        self.lblHallExtra.setObjectName(u"lblHallExtra")
        self.lblHallExtra.setMaximumSize(QSize(16777215, 50))
        self.lblHallExtra.setStyleSheet(u"background-color: #3f3c5b;\n"
"font-size: 15pt;\n"
"color: white;")
        self.lblHallExtra.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lblHallExtra)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(25)
        self.formLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.lblHallSit = QLabel(self.frHallExtra)
        self.lblHallSit.setObjectName(u"lblHallSit")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lblHallSit)

        self.lblHallStat = QLabel(self.frHallExtra)
        self.lblHallStat.setObjectName(u"lblHallStat")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.lblHallStat)

        self.lblHallRation = QLabel(self.frHallExtra)
        self.lblHallRation.setObjectName(u"lblHallRation")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.lblHallRation)

        self.lblHallEntry = QLabel(self.frHallExtra)
        self.lblHallEntry.setObjectName(u"lblHallEntry")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.lblHallEntry)

        self.lblHallBirth = QLabel(self.frHallExtra)
        self.lblHallBirth.setObjectName(u"lblHallBirth")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.lblHallBirth)

        self.lblHallNrBirth = QLabel(self.frHallExtra)
        self.lblHallNrBirth.setObjectName(u"lblHallNrBirth")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.lblHallNrBirth)

        self.lblHallNrDeath = QLabel(self.frHallExtra)
        self.lblHallNrDeath.setObjectName(u"lblHallNrDeath")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.lblHallNrDeath)

        self.label_8 = QLabel(self.frHallExtra)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 25))
        self.label_8.setStyleSheet(u"border: none;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.label_8)

        self.label_9 = QLabel(self.frHallExtra)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 25))
        self.label_9.setStyleSheet(u"border: none;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setIndent(0)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(self.frHallExtra)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 25))
        self.label_10.setStyleSheet(u"border: none;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.label_10)

        self.label_11 = QLabel(self.frHallExtra)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 25))
        self.label_11.setStyleSheet(u"border: none;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.label_11)

        self.label_12 = QLabel(self.frHallExtra)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 25))
        self.label_12.setStyleSheet(u"border: none;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.label_12)

        self.label_13 = QLabel(self.frHallExtra)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 25))
        self.label_13.setStyleSheet(u"border: none;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.label_13)

        self.spinBox = QSpinBox(self.frHallExtra)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.spinBox.setFont(font1)
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"	padding-left: 0px;\n"
"	font-size: 11pt;\n"
"	border: none;\n"
"	background: transparent;\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-position: right; width: 20px; height: 20px;\n"
"	image: url(:/addons/resources/addons/right.png);\n"
"}\n"
"\n"
"QSpinBox::up-button::pressed {\n"
"	border: 1px inset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	subcontrol-position: left; width: 20px; height: 20px;\n"
"	image: url(:/addons/resources/addons/left.png);\n"
"	border: 1px outset rgb(222, 221, 218)\n"
"}\n"
"\n"
"QSpinBox::down-button::pressed {\n"
"	border: 1px inset rgb(222, 221, 218)\n"
"}")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(150)
        self.spinBox.setValue(100)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.spinBox)


        self.verticalLayout_11.addLayout(self.formLayout_4)


        self.gridLayout_2.addWidget(self.frHallExtra, 0, 7, 2, 1)


        self.verticalLayout_5.addWidget(self.frHall)

        self.menuHall = QFrame(self.pgHall)
        self.menuHall.setObjectName(u"menuHall")
        self.menuHall.setMinimumSize(QSize(0, 70))
        self.menuHall.setMaximumSize(QSize(16777215, 70))
        self.menuHall.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuHall.setFrameShape(QFrame.NoFrame)
        self.menuHall.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.menuHall)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnHallRem = QPushButton(self.menuHall)
        self.btnHallRem.setObjectName(u"btnHallRem")
        self.btnHallRem.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_5.addWidget(self.btnHallRem)

        self.btnHallAdd = QPushButton(self.menuHall)
        self.btnHallAdd.setObjectName(u"btnHallAdd")
        self.btnHallAdd.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_5.addWidget(self.btnHallAdd)

        self.btnHallExp = QPushButton(self.menuHall)
        self.btnHallExp.setObjectName(u"btnHallExp")
        self.btnHallExp.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_5.addWidget(self.btnHallExp)

        self.btnHallLoadCur = QPushButton(self.menuHall)
        self.btnHallLoadCur.setObjectName(u"btnHallLoadCur")
        self.btnHallLoadCur.setMinimumSize(QSize(0, 70))
        self.btnHallLoadCur.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.btnHallLoadCur)


        self.verticalLayout_5.addWidget(self.menuHall)

        self.stackedWidget.addWidget(self.pgHall)
        self.pgCurve = QWidget()
        self.pgCurve.setObjectName(u"pgCurve")
        self.verticalLayout_7 = QVBoxLayout(self.pgCurve)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 0)
        self.frCurve = QFrame(self.pgCurve)
        self.frCurve.setObjectName(u"frCurve")
        self.frCurve.setFrameShape(QFrame.NoFrame)
        self.frCurve.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frCurve)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(30)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tblCurve = QTableWidget(self.frCurve)
        if (self.tblCurve.columnCount() < 3):
            self.tblCurve.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tblCurve.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblCurve.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tblCurve.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        if (self.tblCurve.rowCount() < 50):
            self.tblCurve.setRowCount(50)
        self.tblCurve.setObjectName(u"tblCurve")
        self.tblCurve.setMaximumSize(QSize(16777215, 16777215))
        self.tblCurve.setFrameShape(QFrame.NoFrame)
        self.tblCurve.setFrameShadow(QFrame.Plain)
        self.tblCurve.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tblCurve.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tblCurve.setRowCount(50)
        self.tblCurve.verticalHeader().setVisible(False)
        self.tblCurve.verticalHeader().setHighlightSections(True)

        self.gridLayout_3.addWidget(self.tblCurve, 1, 0, 1, 2)

        self.spiCurve = QSpinBox(self.frCurve)
        self.spiCurve.setObjectName(u"spiCurve")
        self.spiCurve.setMinimumSize(QSize(137, 50))
        self.spiCurve.setFont(font)
        self.spiCurve.setStyleSheet(u"")
        self.spiCurve.setMinimum(1)
        self.spiCurve.setMaximum(5)

        self.gridLayout_3.addWidget(self.spiCurve, 0, 1, 1, 1)

        self.curveGraph = QWidget(self.frCurve)
        self.curveGraph.setObjectName(u"curveGraph")

        self.gridLayout_3.addWidget(self.curveGraph, 1, 2, 1, 1)

        self.curveSpacer = QSpacerItem(757, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.curveSpacer, 0, 2, 1, 1)

        self.lblCurve = QLabel(self.frCurve)
        self.lblCurve.setObjectName(u"lblCurve")
        self.lblCurve.setMinimumSize(QSize(250, 50))

        self.gridLayout_3.addWidget(self.lblCurve, 0, 0, 1, 1)

        self.lblCurveStatus = QLabel(self.frCurve)
        self.lblCurveStatus.setObjectName(u"lblCurveStatus")
        self.lblCurveStatus.setStyleSheet(u"font-size: 11pt;\n"
"border: none;\n"
"")
        self.lblCurveStatus.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblCurveStatus, 2, 0, 1, 2)


        self.verticalLayout_7.addWidget(self.frCurve)

        self.menuCurve = QFrame(self.pgCurve)
        self.menuCurve.setObjectName(u"menuCurve")
        self.menuCurve.setMaximumSize(QSize(16777215, 70))
        self.menuCurve.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuCurve.setFrameShape(QFrame.NoFrame)
        self.menuCurve.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.menuCurve)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnCurveSave = QPushButton(self.menuCurve)
        self.btnCurveSave.setObjectName(u"btnCurveSave")
        self.btnCurveSave.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_6.addWidget(self.btnCurveSave)

        self.btnCurveRem = QPushButton(self.menuCurve)
        self.btnCurveRem.setObjectName(u"btnCurveRem")
        self.btnCurveRem.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_6.addWidget(self.btnCurveRem)

        self.btnCurveExp = QPushButton(self.menuCurve)
        self.btnCurveExp.setObjectName(u"btnCurveExp")
        self.btnCurveExp.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_6.addWidget(self.btnCurveExp)

        self.btnCurveMen = QPushButton(self.menuCurve)
        self.btnCurveMen.setObjectName(u"btnCurveMen")
        self.btnCurveMen.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_6.addWidget(self.btnCurveMen)


        self.verticalLayout_7.addWidget(self.menuCurve)

        self.stackedWidget.addWidget(self.pgCurve)
        self.pgTime = QWidget()
        self.pgTime.setObjectName(u"pgTime")
        self.verticalLayout_8 = QVBoxLayout(self.pgTime)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 0)
        self.frTime = QFrame(self.pgTime)
        self.frTime.setObjectName(u"frTime")
        self.frTime.setFrameShape(QFrame.NoFrame)
        self.frTime.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frTime)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(30)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lblTimeStatus = QLabel(self.frTime)
        self.lblTimeStatus.setObjectName(u"lblTimeStatus")
        self.lblTimeStatus.setStyleSheet(u"font-size: 11pt;\n"
"border: none;\n"
"")
        self.lblTimeStatus.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lblTimeStatus, 2, 0, 1, 1)

        self.lblTime = QLabel(self.frTime)
        self.lblTime.setObjectName(u"lblTime")
        self.lblTime.setMinimumSize(QSize(400, 50))
        self.lblTime.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_4.addWidget(self.lblTime, 0, 0, 1, 1)

        self.timeSpacer = QSpacerItem(744, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.timeSpacer, 0, 2, 1, 1)

        self.tblTime = QTableWidget(self.frTime)
        if (self.tblTime.columnCount() < 3):
            self.tblTime.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tblTime.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblTime.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tblTime.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        if (self.tblTime.rowCount() < 24):
            self.tblTime.setRowCount(24)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(9, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(10, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(11, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(12, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(13, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(14, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(15, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(16, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(17, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(18, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(19, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(20, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(21, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(22, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tblTime.setVerticalHeaderItem(23, __qtablewidgetitem50)
        self.tblTime.setObjectName(u"tblTime")
        self.tblTime.setMinimumSize(QSize(397, 0))
        self.tblTime.setMaximumSize(QSize(397, 16777215))
        self.tblTime.setFrameShape(QFrame.NoFrame)
        self.tblTime.setFrameShadow(QFrame.Plain)
        self.tblTime.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tblTime.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tblTime.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tblTime, 1, 0, 1, 2)

        self.frTimeLeft = QFrame(self.frTime)
        self.frTimeLeft.setObjectName(u"frTimeLeft")
        self.frTimeLeft.setFrameShape(QFrame.NoFrame)
        self.frTimeLeft.setFrameShadow(QFrame.Plain)
        self.formLayout = QFormLayout(self.frTimeLeft)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.lblTimeDur = QLabel(self.frTimeLeft)
        self.lblTimeDur.setObjectName(u"lblTimeDur")
        self.lblTimeDur.setStyleSheet(u"font-size: 15pt;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblTimeDur)

        self.txtTimeDur = QLabel(self.frTimeLeft)
        self.txtTimeDur.setObjectName(u"txtTimeDur")
        self.txtTimeDur.setStyleSheet(u"font-size: 15pt;border: none;")
        self.txtTimeDur.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtTimeDur)

        self.lblTimeAct = QLabel(self.frTimeLeft)
        self.lblTimeAct.setObjectName(u"lblTimeAct")
        self.lblTimeAct.setStyleSheet(u"font-size: 15pt;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblTimeAct)

        self.txtTimeAct = QLabel(self.frTimeLeft)
        self.txtTimeAct.setObjectName(u"txtTimeAct")
        self.txtTimeAct.setStyleSheet(u"font-size: 15pt;border: none;")
        self.txtTimeAct.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtTimeAct)

        self.lblTimeNrAct = QLabel(self.frTimeLeft)
        self.lblTimeNrAct.setObjectName(u"lblTimeNrAct")
        self.lblTimeNrAct.setStyleSheet(u"font-size: 15pt;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblTimeNrAct)

        self.txtTimeNrAct = QLabel(self.frTimeLeft)
        self.txtTimeNrAct.setObjectName(u"txtTimeNrAct")
        self.txtTimeNrAct.setStyleSheet(u"font-size: 15pt;border: none;")
        self.txtTimeNrAct.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtTimeNrAct)

        self.lblTimeRat = QLabel(self.frTimeLeft)
        self.lblTimeRat.setObjectName(u"lblTimeRat")
        self.lblTimeRat.setStyleSheet(u"font-size: 15pt;")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lblTimeRat)

        self.txtTimeRat = QLineEdit(self.frTimeLeft)
        self.txtTimeRat.setObjectName(u"txtTimeRat")
        font2 = QFont()
        font2.setPointSize(15)
        self.txtTimeRat.setFont(font2)
        self.txtTimeRat.setStyleSheet(u"border: none;")
        self.txtTimeRat.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtTimeRat.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txtTimeRat)

        self.lblTimeTotFeed = QLabel(self.frTimeLeft)
        self.lblTimeTotFeed.setObjectName(u"lblTimeTotFeed")
        self.lblTimeTotFeed.setStyleSheet(u"font-size: 15pt;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblTimeTotFeed)

        self.txtTimeTotFeed = QLabel(self.frTimeLeft)
        self.txtTimeTotFeed.setObjectName(u"txtTimeTotFeed")
        self.txtTimeTotFeed.setStyleSheet(u"font-size: 15pt;border: none;")
        self.txtTimeTotFeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txtTimeTotFeed)


        self.gridLayout_4.addWidget(self.frTimeLeft, 1, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frTime)

        self.menuTime = QFrame(self.pgTime)
        self.menuTime.setObjectName(u"menuTime")
        self.menuTime.setMaximumSize(QSize(16777215, 70))
        self.menuTime.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuTime.setFrameShape(QFrame.NoFrame)
        self.menuTime.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.menuTime)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btnTimeUpd = QPushButton(self.menuTime)
        self.btnTimeUpd.setObjectName(u"btnTimeUpd")
        self.btnTimeUpd.setMinimumSize(QSize(0, 70))
        self.btnTimeUpd.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_7.addWidget(self.btnTimeUpd)

        self.btnTimeSave = QPushButton(self.menuTime)
        self.btnTimeSave.setObjectName(u"btnTimeSave")
        self.btnTimeSave.setMinimumSize(QSize(0, 70))
        self.btnTimeSave.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_7.addWidget(self.btnTimeSave)

        self.btnTimeRem = QPushButton(self.menuTime)
        self.btnTimeRem.setObjectName(u"btnTimeRem")
        self.btnTimeRem.setMinimumSize(QSize(0, 70))
        self.btnTimeRem.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_7.addWidget(self.btnTimeRem)

        self.btnTimeMen = QPushButton(self.menuTime)
        self.btnTimeMen.setObjectName(u"btnTimeMen")
        self.btnTimeMen.setMinimumSize(QSize(0, 70))
        self.btnTimeMen.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_7.addWidget(self.btnTimeMen)


        self.verticalLayout_8.addWidget(self.menuTime)

        self.stackedWidget.addWidget(self.pgTime)
        self.pgStock = QWidget()
        self.pgStock.setObjectName(u"pgStock")
        self.verticalLayout_12 = QVBoxLayout(self.pgStock)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 0)
        self.frStock = QFrame(self.pgStock)
        self.frStock.setObjectName(u"frStock")
        self.frStock.setLayoutDirection(Qt.LeftToRight)
        self.frStock.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(220,221,240);\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"QProgressBar::chunk:vertical {\n"
"background: rgb(63,60,91);\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"}")
        self.frStock.setFrameShape(QFrame.NoFrame)
        self.frStock.setFrameShadow(QFrame.Plain)
        self.gridLayout_11 = QGridLayout(self.frStock)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 10)
        self.frSilo = QFrame(self.frStock)
        self.frSilo.setObjectName(u"frSilo")
        self.frSilo.setMinimumSize(QSize(300, 0))
        self.frSilo.setMaximumSize(QSize(300, 16777215))
        self.frSilo.setFrameShape(QFrame.NoFrame)
        self.frSilo.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frSilo)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(45, 30, 0, 0)
        self.widSilo = QProgressBar(self.frSilo)
        self.widSilo.setObjectName(u"widSilo")
        self.widSilo.setMinimumSize(QSize(0, 0))
        self.widSilo.setMaximumSize(QSize(200, 400))
        self.widSilo.setStyleSheet(u"")
        self.widSilo.setMinimum(0)
        self.widSilo.setMaximum(100)
        self.widSilo.setValue(30)
        self.widSilo.setTextVisible(False)
        self.widSilo.setOrientation(Qt.Vertical)

        self.verticalLayout_13.addWidget(self.widSilo)

        self.lblWidSilo = QLabel(self.frSilo)
        self.lblWidSilo.setObjectName(u"lblWidSilo")
        self.lblWidSilo.setMinimumSize(QSize(200, 0))
        self.lblWidSilo.setMaximumSize(QSize(200, 16777215))
        self.lblWidSilo.setStyleSheet(u"border: none;")
        self.lblWidSilo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.lblWidSilo)


        self.gridLayout_11.addWidget(self.frSilo, 1, 1, 1, 1)

        self.lblStock = QLabel(self.frStock)
        self.lblStock.setObjectName(u"lblStock")
        self.lblStock.setMinimumSize(QSize(0, 50))
        self.lblStock.setMaximumSize(QSize(400, 50))

        self.gridLayout_11.addWidget(self.lblStock, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.frStock)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font-size: 15pt;\n"
"font-family: \"Segoe UI\";")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setVerticalSpacing(25)
        self.lblStockSiloSel = QLabel(self.frame_2)
        self.lblStockSiloSel.setObjectName(u"lblStockSiloSel")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.lblStockSiloSel)

        self.spiStockSiloNr = QSpinBox(self.frame_2)
        self.spiStockSiloNr.setObjectName(u"spiStockSiloNr")
        self.spiStockSiloNr.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(15)
        self.spiStockSiloNr.setFont(font3)
        self.spiStockSiloNr.setStyleSheet(u"qproperty-alignment: AlignCenter;")
        self.spiStockSiloNr.setAlignment(Qt.AlignCenter)
        self.spiStockSiloNr.setMinimum(1)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.spiStockSiloNr)

        self.lblStockQtaNow = QLabel(self.frame_2)
        self.lblStockQtaNow.setObjectName(u"lblStockQtaNow")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.lblStockQtaNow)

        self.txtStockQtaNow = QLabel(self.frame_2)
        self.txtStockQtaNow.setObjectName(u"txtStockQtaNow")
        self.txtStockQtaNow.setMinimumSize(QSize(0, 0))
        self.txtStockQtaNow.setMaximumSize(QSize(16777215, 16777215))
        self.txtStockQtaNow.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.txtStockQtaNow.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.txtStockQtaNow)

        self.lblStockQtaMax = QLabel(self.frame_2)
        self.lblStockQtaMax.setObjectName(u"lblStockQtaMax")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.lblStockQtaMax)

        self.txtStockQtaMax = QLabel(self.frame_2)
        self.txtStockQtaMax.setObjectName(u"txtStockQtaMax")
        self.txtStockQtaMax.setMinimumSize(QSize(0, 0))
        self.txtStockQtaMax.setMaximumSize(QSize(16777215, 16777215))
        self.txtStockQtaMax.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.txtStockQtaMax.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.txtStockQtaMax)

        self.lblStockBoxGest = QLabel(self.frame_2)
        self.lblStockBoxGest.setObjectName(u"lblStockBoxGest")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.lblStockBoxGest)

        self.txtStockBoxGest = QLabel(self.frame_2)
        self.txtStockBoxGest.setObjectName(u"txtStockBoxGest")
        self.txtStockBoxGest.setMinimumSize(QSize(0, 0))
        self.txtStockBoxGest.setMaximumSize(QSize(16777215, 16777215))
        self.txtStockBoxGest.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.txtStockBoxGest.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.txtStockBoxGest)

        self.lblStockPrevDur = QLabel(self.frame_2)
        self.lblStockPrevDur.setObjectName(u"lblStockPrevDur")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.lblStockPrevDur)

        self.txtStockPrevDur = QLabel(self.frame_2)
        self.txtStockPrevDur.setObjectName(u"txtStockPrevDur")
        self.txtStockPrevDur.setMinimumSize(QSize(0, 0))
        self.txtStockPrevDur.setMaximumSize(QSize(16777215, 16777215))
        self.txtStockPrevDur.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.txtStockPrevDur.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.txtStockPrevDur)

        self.lblStockLastLoadQta = QLabel(self.frame_2)
        self.lblStockLastLoadQta.setObjectName(u"lblStockLastLoadQta")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.lblStockLastLoadQta)

        self.lblStockLastLoadDate = QLabel(self.frame_2)
        self.lblStockLastLoadDate.setObjectName(u"lblStockLastLoadDate")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.lblStockLastLoadDate)

        self.txtStockLastLoadQta = QLabel(self.frame_2)
        self.txtStockLastLoadQta.setObjectName(u"txtStockLastLoadQta")
        self.txtStockLastLoadQta.setMinimumSize(QSize(0, 0))
        self.txtStockLastLoadQta.setMaximumSize(QSize(16777215, 16777215))
        self.txtStockLastLoadQta.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.txtStockLastLoadQta.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.txtStockLastLoadQta)

        self.txtStockLastLoadDate = QLabel(self.frame_2)
        self.txtStockLastLoadDate.setObjectName(u"txtStockLastLoadDate")
        self.txtStockLastLoadDate.setMinimumSize(QSize(0, 0))
        self.txtStockLastLoadDate.setMaximumSize(QSize(16777215, 16777215))
        self.txtStockLastLoadDate.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.txtStockLastLoadDate.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.txtStockLastLoadDate)


        self.gridLayout_12.addLayout(self.formLayout_5, 0, 0, 1, 1)

        self.silosGraph = QWidget(self.frame_2)
        self.silosGraph.setObjectName(u"silosGraph")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.silosGraph.sizePolicy().hasHeightForWidth())
        self.silosGraph.setSizePolicy(sizePolicy1)
        self.silosGraph.setMaximumSize(QSize(16777215, 16777215))
        self.silosGraph.setSizeIncrement(QSize(100, 100))
        self.silosGraph.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.silosGraph, 1, 0, 1, 2)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(20)
        self.lblStockModQtaNow = QLabel(self.frame_2)
        self.lblStockModQtaNow.setObjectName(u"lblStockModQtaNow")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.lblStockModQtaNow)

        self.spiStockModQtaNow = QSpinBox(self.frame_2)
        self.spiStockModQtaNow.setObjectName(u"spiStockModQtaNow")
        self.spiStockModQtaNow.setMinimumSize(QSize(0, 0))
        self.spiStockModQtaNow.setMaximumSize(QSize(16777215, 16777215))
        self.spiStockModQtaNow.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.spiStockModQtaNow.setMinimum(50)
        self.spiStockModQtaNow.setMaximum(20000)
        self.spiStockModQtaNow.setSingleStep(10)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.spiStockModQtaNow)

        self.lblStockModQtaMax = QLabel(self.frame_2)
        self.lblStockModQtaMax.setObjectName(u"lblStockModQtaMax")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.lblStockModQtaMax)

        self.spiStockModQtaMax = QSpinBox(self.frame_2)
        self.spiStockModQtaMax.setObjectName(u"spiStockModQtaMax")
        self.spiStockModQtaMax.setMinimumSize(QSize(0, 0))
        self.spiStockModQtaMax.setMaximumSize(QSize(16777215, 16777215))
        self.spiStockModQtaMax.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.spiStockModQtaMax.setAlignment(Qt.AlignCenter)
        self.spiStockModQtaMax.setMinimum(50)
        self.spiStockModQtaMax.setMaximum(20000)
        self.spiStockModQtaMax.setSingleStep(10)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.spiStockModQtaMax)

        self.lblStockModBoxGest = QLabel(self.frame_2)
        self.lblStockModBoxGest.setObjectName(u"lblStockModBoxGest")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.lblStockModBoxGest)

        self.spiStockModBoxGest = QSpinBox(self.frame_2)
        self.spiStockModBoxGest.setObjectName(u"spiStockModBoxGest")
        self.spiStockModBoxGest.setMinimumSize(QSize(0, 0))
        self.spiStockModBoxGest.setMaximumSize(QSize(16777215, 16777215))
        self.spiStockModBoxGest.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.spiStockModBoxGest.setMaximum(200)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.spiStockModBoxGest)

        self.spiStockLoadQta = QSpinBox(self.frame_2)
        self.spiStockLoadQta.setObjectName(u"spiStockLoadQta")
        self.spiStockLoadQta.setMinimumSize(QSize(0, 0))
        self.spiStockLoadQta.setMaximumSize(QSize(16777215, 16777215))
        self.spiStockLoadQta.setStyleSheet(u"border: none;\n"
"qproperty-alignment: AlignCenter;")
        self.spiStockLoadQta.setMinimum(50)
        self.spiStockLoadQta.setMaximum(20000)
        self.spiStockLoadQta.setSingleStep(10)

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.spiStockLoadQta)

        self.lblStockLoadQta = QLabel(self.frame_2)
        self.lblStockLoadQta.setObjectName(u"lblStockLoadQta")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.lblStockLoadQta)

        self.btnStockSaveEdit = QPushButton(self.frame_2)
        self.btnStockSaveEdit.setObjectName(u"btnStockSaveEdit")

        self.formLayout_6.setWidget(3, QFormLayout.SpanningRole, self.btnStockSaveEdit)

        self.lblStockLoadDate = QLabel(self.frame_2)
        self.lblStockLoadDate.setObjectName(u"lblStockLoadDate")

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.lblStockLoadDate)

        self.spiStockLoadDate = QDateEdit(self.frame_2)
        self.spiStockLoadDate.setObjectName(u"spiStockLoadDate")
        self.spiStockLoadDate.setMinimumSize(QSize(0, 0))
        self.spiStockLoadDate.setMaximumSize(QSize(16777215, 16777215))
        self.spiStockLoadDate.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.spiStockLoadDate)

        self.btnStockRegLoad = QPushButton(self.frame_2)
        self.btnStockRegLoad.setObjectName(u"btnStockRegLoad")

        self.formLayout_6.setWidget(6, QFormLayout.SpanningRole, self.btnStockRegLoad)


        self.gridLayout_12.addLayout(self.formLayout_6, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.frame_2, 1, 2, 1, 1)


        self.verticalLayout_12.addWidget(self.frStock)

        self.menuStock = QFrame(self.pgStock)
        self.menuStock.setObjectName(u"menuStock")
        self.menuStock.setMinimumSize(QSize(0, 70))
        self.menuStock.setMaximumSize(QSize(16777215, 70))
        self.menuStock.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuStock.setFrameShape(QFrame.NoFrame)
        self.menuStock.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.menuStock)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btnStockUpd = QPushButton(self.menuStock)
        self.btnStockUpd.setObjectName(u"btnStockUpd")
        self.btnStockUpd.setMinimumSize(QSize(0, 70))
        self.btnStockUpd.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_11.addWidget(self.btnStockUpd)

        self.btnStockConf = QPushButton(self.menuStock)
        self.btnStockConf.setObjectName(u"btnStockConf")
        self.btnStockConf.setMinimumSize(QSize(0, 70))
        self.btnStockConf.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_11.addWidget(self.btnStockConf)

        self.btnStockLoad = QPushButton(self.menuStock)
        self.btnStockLoad.setObjectName(u"btnStockLoad")
        self.btnStockLoad.setMinimumSize(QSize(0, 70))
        self.btnStockLoad.setMaximumSize(QSize(16777215, 70))
        self.btnStockLoad.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnStockLoad)

        self.btnStockMen = QPushButton(self.menuStock)
        self.btnStockMen.setObjectName(u"btnStockMen")
        self.btnStockMen.setMinimumSize(QSize(0, 70))
        self.btnStockMen.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_11.addWidget(self.btnStockMen)


        self.verticalLayout_12.addWidget(self.menuStock)

        self.stackedWidget.addWidget(self.pgStock)
        self.pgHistory = QWidget()
        self.pgHistory.setObjectName(u"pgHistory")
        self.verticalLayout_9 = QVBoxLayout(self.pgHistory)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 0)
        self.frHistory = QFrame(self.pgHistory)
        self.frHistory.setObjectName(u"frHistory")
        self.frHistory.setMaximumSize(QSize(16777215, 16777215))
        self.frHistory.setFrameShape(QFrame.NoFrame)
        self.frHistory.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frHistory)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 10)
        self.frHistoryLeft = QFrame(self.frHistory)
        self.frHistoryLeft.setObjectName(u"frHistoryLeft")
        self.frHistoryLeft.setStyleSheet(u"font-size: 15pt;")
        self.frHistoryLeft.setFrameShape(QFrame.NoFrame)
        self.frHistoryLeft.setFrameShadow(QFrame.Plain)
        self.formLayout_2 = QFormLayout(self.frHistoryLeft)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblHistorySel = QLabel(self.frHistoryLeft)
        self.lblHistorySel.setObjectName(u"lblHistorySel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblHistorySel)

        self.comHistorySel = QComboBox(self.frHistoryLeft)
        self.comHistorySel.setObjectName(u"comHistorySel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comHistorySel.sizePolicy().hasHeightForWidth())
        self.comHistorySel.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comHistorySel)

        self.lblHistoryGestDal = QLabel(self.frHistoryLeft)
        self.lblHistoryGestDal.setObjectName(u"lblHistoryGestDal")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblHistoryGestDal)

        self.txtHistoryGestDal = QLabel(self.frHistoryLeft)
        self.txtHistoryGestDal.setObjectName(u"txtHistoryGestDal")
        self.txtHistoryGestDal.setStyleSheet(u"border: none;")
        self.txtHistoryGestDal.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.txtHistoryGestDal)

        self.lblHistoryCons = QLabel(self.frHistoryLeft)
        self.lblHistoryCons.setObjectName(u"lblHistoryCons")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lblHistoryCons)

        self.tableWidget = QTableWidget(self.frHistoryLeft)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.tableWidget)

        self.lblHistoryConsTot = QLabel(self.frHistoryLeft)
        self.lblHistoryConsTot.setObjectName(u"lblHistoryConsTot")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lblHistoryConsTot)

        self.txtHistoryConsTot = QLabel(self.frHistoryLeft)
        self.txtHistoryConsTot.setObjectName(u"txtHistoryConsTot")
        self.txtHistoryConsTot.setStyleSheet(u"border: none;")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.txtHistoryConsTot)

        self.lblHistoryGestAl = QLabel(self.frHistoryLeft)
        self.lblHistoryGestAl.setObjectName(u"lblHistoryGestAl")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lblHistoryGestAl)

        self.txtHistoryGestAl = QLabel(self.frHistoryLeft)
        self.txtHistoryGestAl.setObjectName(u"txtHistoryGestAl")
        self.txtHistoryGestAl.setStyleSheet(u"border: none;")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.txtHistoryGestAl)


        self.gridLayout_5.addWidget(self.frHistoryLeft, 1, 0, 1, 1)

        self.lblTest = QLabel(self.frHistory)
        self.lblTest.setObjectName(u"lblTest")
        self.lblTest.setMinimumSize(QSize(400, 50))
        self.lblTest.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_5.addWidget(self.lblTest, 0, 0, 1, 2)

        self.frHistoryRight = QFrame(self.frHistory)
        self.frHistoryRight.setObjectName(u"frHistoryRight")
        self.frHistoryRight.setStyleSheet(u"font-size: 15pt;")
        self.frHistoryRight.setFrameShape(QFrame.NoFrame)
        self.frHistoryRight.setFrameShadow(QFrame.Plain)
        self.formLayout_3 = QFormLayout(self.frHistoryRight)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(20)
        self.formLayout_3.setVerticalSpacing(20)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frHistoryRight)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(self.frHistoryRight)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)


        self.gridLayout_5.addWidget(self.frHistoryRight, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frHistory)

        self.menuCom = QFrame(self.pgHistory)
        self.menuCom.setObjectName(u"menuCom")
        self.menuCom.setMinimumSize(QSize(0, 70))
        self.menuCom.setMaximumSize(QSize(16777215, 70))
        self.menuCom.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuCom.setFrameShape(QFrame.NoFrame)
        self.menuCom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.menuCom)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnTestStr = QPushButton(self.menuCom)
        self.btnTestStr.setObjectName(u"btnTestStr")
        self.btnTestStr.setMinimumSize(QSize(0, 70))
        self.btnTestStr.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_8.addWidget(self.btnTestStr)

        self.btnTestSto = QPushButton(self.menuCom)
        self.btnTestSto.setObjectName(u"btnTestSto")
        self.btnTestSto.setMinimumSize(QSize(0, 70))
        self.btnTestSto.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_8.addWidget(self.btnTestSto)

        self.btnTestRes = QPushButton(self.menuCom)
        self.btnTestRes.setObjectName(u"btnTestRes")
        self.btnTestRes.setMinimumSize(QSize(0, 70))
        self.btnTestRes.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_8.addWidget(self.btnTestRes)

        self.btnTestMenu = QPushButton(self.menuCom)
        self.btnTestMenu.setObjectName(u"btnTestMenu")
        self.btnTestMenu.setMinimumSize(QSize(0, 70))
        self.btnTestMenu.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_8.addWidget(self.btnTestMenu)


        self.verticalLayout_9.addWidget(self.menuCom)

        self.stackedWidget.addWidget(self.pgHistory)
        self.pgData = QWidget()
        self.pgData.setObjectName(u"pgData")
        self.verticalLayout_10 = QVBoxLayout(self.pgData)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 0)
        self.frData = QFrame(self.pgData)
        self.frData.setObjectName(u"frData")
        self.frData.setStyleSheet(u"QLineEdit {\n"
"font-size: 11pt;\n"
"}")
        self.frData.setFrameShape(QFrame.NoFrame)
        self.frData.setFrameShadow(QFrame.Plain)
        self.gridLayout_6 = QGridLayout(self.frData)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 10)
        self.tblBox = QTableWidget(self.frData)
        if (self.tblBox.columnCount() < 5):
            self.tblBox.setColumnCount(5)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tblBox.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tblBox.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tblBox.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tblBox.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tblBox.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        self.tblBox.setObjectName(u"tblBox")

        self.gridLayout_6.addWidget(self.tblBox, 1, 2, 1, 1)

        self.lblBox = QLabel(self.frData)
        self.lblBox.setObjectName(u"lblBox")
        self.lblBox.setMinimumSize(QSize(400, 50))
        self.lblBox.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_6.addWidget(self.lblBox, 0, 2, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(0)
        self.lblDataTotSow = QLabel(self.frData)
        self.lblDataTotSow.setObjectName(u"lblDataTotSow")
        self.lblDataTotSow.setStyleSheet(u"font-size: 15pt;")

        self.gridLayout_7.addWidget(self.lblDataTotSow, 0, 0, 1, 1)

        self.lblDataFreeSow = QLabel(self.frData)
        self.lblDataFreeSow.setObjectName(u"lblDataFreeSow")
        self.lblDataFreeSow.setStyleSheet(u"font-size: 15pt;")

        self.gridLayout_7.addWidget(self.lblDataFreeSow, 0, 2, 1, 1)

        self.txtDataTotSow = QLineEdit(self.frData)
        self.txtDataTotSow.setObjectName(u"txtDataTotSow")
        self.txtDataTotSow.setMaximumSize(QSize(100, 16777215))
        self.txtDataTotSow.setAlignment(Qt.AlignCenter)
        self.txtDataTotSow.setReadOnly(True)

        self.gridLayout_7.addWidget(self.txtDataTotSow, 0, 1, 1, 1)

        self.txtDataFreeSow = QLineEdit(self.frData)
        self.txtDataFreeSow.setObjectName(u"txtDataFreeSow")
        self.txtDataFreeSow.setMaximumSize(QSize(100, 16777215))
        self.txtDataFreeSow.setAlignment(Qt.AlignCenter)
        self.txtDataFreeSow.setReadOnly(True)

        self.gridLayout_7.addWidget(self.txtDataFreeSow, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 5, 0, 1, 1)

        self.lblSow = QLabel(self.frData)
        self.lblSow.setObjectName(u"lblSow")
        self.lblSow.setMinimumSize(QSize(400, 50))
        self.lblSow.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_6.addWidget(self.lblSow, 0, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(20)
        self.btnDataRemBox = QPushButton(self.frData)
        self.btnDataRemBox.setObjectName(u"btnDataRemBox")

        self.gridLayout_14.addWidget(self.btnDataRemBox, 0, 0, 1, 1)

        self.btnDataSaveCom = QPushButton(self.frData)
        self.btnDataSaveCom.setObjectName(u"btnDataSaveCom")

        self.gridLayout_14.addWidget(self.btnDataSaveCom, 0, 1, 1, 1)

        self.btnDataTestCom = QPushButton(self.frData)
        self.btnDataTestCom.setObjectName(u"btnDataTestCom")

        self.gridLayout_14.addWidget(self.btnDataTestCom, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_14, 3, 2, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btnDataRemSow = QPushButton(self.frData)
        self.btnDataRemSow.setObjectName(u"btnDataRemSow")

        self.gridLayout_13.addWidget(self.btnDataRemSow, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_13, 3, 0, 1, 1)

        self.tblSow = QTableWidget(self.frData)
        if (self.tblSow.columnCount() < 2):
            self.tblSow.setColumnCount(2)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tblSow.setHorizontalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tblSow.setHorizontalHeaderItem(1, __qtablewidgetitem57)
        self.tblSow.setObjectName(u"tblSow")

        self.gridLayout_6.addWidget(self.tblSow, 1, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(0)
        self.lblDataFreeBox = QLabel(self.frData)
        self.lblDataFreeBox.setObjectName(u"lblDataFreeBox")
        self.lblDataFreeBox.setStyleSheet(u"font-size: 15pt;")

        self.gridLayout_8.addWidget(self.lblDataFreeBox, 0, 2, 1, 1)

        self.txtDataTotBox = QLineEdit(self.frData)
        self.txtDataTotBox.setObjectName(u"txtDataTotBox")
        self.txtDataTotBox.setMaximumSize(QSize(100, 16777215))
        self.txtDataTotBox.setAlignment(Qt.AlignCenter)
        self.txtDataTotBox.setReadOnly(True)

        self.gridLayout_8.addWidget(self.txtDataTotBox, 0, 1, 1, 1)

        self.lblDataTotBox = QLabel(self.frData)
        self.lblDataTotBox.setObjectName(u"lblDataTotBox")
        self.lblDataTotBox.setStyleSheet(u"font-size: 15pt;")

        self.gridLayout_8.addWidget(self.lblDataTotBox, 0, 0, 1, 1)

        self.txtDataFreeBox = QLineEdit(self.frData)
        self.txtDataFreeBox.setObjectName(u"txtDataFreeBox")
        self.txtDataFreeBox.setMaximumSize(QSize(100, 16777215))
        self.txtDataFreeBox.setAlignment(Qt.AlignCenter)
        self.txtDataFreeBox.setReadOnly(True)

        self.gridLayout_8.addWidget(self.txtDataFreeBox, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_8, 5, 2, 1, 1)

        self.lblDataStatus = QLabel(self.frData)
        self.lblDataStatus.setObjectName(u"lblDataStatus")
        self.lblDataStatus.setStyleSheet(u"border: none;\n"
"font-size: 11pt;")
        self.lblDataStatus.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lblDataStatus, 2, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.frData)

        self.frDataAdd = QFrame(self.pgData)
        self.frDataAdd.setObjectName(u"frDataAdd")
        self.frDataAdd.setMinimumSize(QSize(0, 0))
        self.frDataAdd.setMaximumSize(QSize(16777215, 0))
        self.frDataAdd.setStyleSheet(u"QLabel {\n"
"font-size: 15pt;\n"
"}")
        self.frDataAdd.setFrameShape(QFrame.NoFrame)
        self.frDataAdd.setFrameShadow(QFrame.Plain)
        self.frDataAdd.setMidLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.frDataAdd)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frAddSow = QFrame(self.frDataAdd)
        self.frAddSow.setObjectName(u"frAddSow")
        self.frAddSow.setFrameShape(QFrame.NoFrame)
        self.frAddSow.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frAddSow)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.btnDataSowAdd = QPushButton(self.frAddSow)
        self.btnDataSowAdd.setObjectName(u"btnDataSowAdd")

        self.gridLayout_9.addWidget(self.btnDataSowAdd, 3, 0, 1, 2)

        self.lblDataSow = QLabel(self.frAddSow)
        self.lblDataSow.setObjectName(u"lblDataSow")
        self.lblDataSow.setMinimumSize(QSize(0, 30))
        self.lblDataSow.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_9.addWidget(self.lblDataSow, 0, 0, 1, 1)

        self.txtDataSow = QLineEdit(self.frAddSow)
        self.txtDataSow.setObjectName(u"txtDataSow")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txtDataSow.sizePolicy().hasHeightForWidth())
        self.txtDataSow.setSizePolicy(sizePolicy3)
        self.txtDataSow.setMinimumSize(QSize(141, 0))
        self.txtDataSow.setMaximumSize(QSize(141, 16777215))
        font4 = QFont()
        self.txtDataSow.setFont(font4)

        self.gridLayout_9.addWidget(self.txtDataSow, 1, 1, 1, 1)

        self.sowSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.sowSpacer, 2, 0, 1, 1)

        self.lblDataSowName = QLabel(self.frAddSow)
        self.lblDataSowName.setObjectName(u"lblDataSowName")
        self.lblDataSowName.setStyleSheet(u"font-size: 11pt;")

        self.gridLayout_9.addWidget(self.lblDataSowName, 1, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.frAddSow)

        self.frAddBox = QFrame(self.frDataAdd)
        self.frAddBox.setObjectName(u"frAddBox")
        self.frAddBox.setFrameShape(QFrame.NoFrame)
        self.frAddBox.setFrameShadow(QFrame.Plain)
        self.gridLayout_10 = QGridLayout(self.frAddBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.spiDataHallAdd = QSpinBox(self.frAddBox)
        self.spiDataHallAdd.setObjectName(u"spiDataHallAdd")
        self.spiDataHallAdd.setMinimumSize(QSize(141, 0))
        self.spiDataHallAdd.setMaximumSize(QSize(141, 16777215))
        self.spiDataHallAdd.setFont(font)

        self.gridLayout_10.addWidget(self.spiDataHallAdd, 1, 1, 1, 1)

        self.lblDataBoxAdd = QLabel(self.frAddBox)
        self.lblDataBoxAdd.setObjectName(u"lblDataBoxAdd")
        self.lblDataBoxAdd.setMinimumSize(QSize(0, 30))
        self.lblDataBoxAdd.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.lblDataBoxAdd, 0, 0, 1, 2)

        self.lblDataNrBoxAdd = QLabel(self.frAddBox)
        self.lblDataNrBoxAdd.setObjectName(u"lblDataNrBoxAdd")
        self.lblDataNrBoxAdd.setStyleSheet(u"font-size: 11pt;")

        self.gridLayout_10.addWidget(self.lblDataNrBoxAdd, 2, 0, 1, 1)

        self.lblDataNrHallAdd = QLabel(self.frAddBox)
        self.lblDataNrHallAdd.setObjectName(u"lblDataNrHallAdd")
        self.lblDataNrHallAdd.setStyleSheet(u"font-size: 11pt;")

        self.gridLayout_10.addWidget(self.lblDataNrHallAdd, 1, 0, 1, 1)

        self.spiDataBoxAdd = QSpinBox(self.frAddBox)
        self.spiDataBoxAdd.setObjectName(u"spiDataBoxAdd")
        self.spiDataBoxAdd.setMinimumSize(QSize(141, 0))
        self.spiDataBoxAdd.setMaximumSize(QSize(141, 16777215))
        self.spiDataBoxAdd.setFont(font)
        self.spiDataBoxAdd.setMaximum(300)

        self.gridLayout_10.addWidget(self.spiDataBoxAdd, 2, 1, 1, 1)

        self.btnDataBoxAdd = QPushButton(self.frAddBox)
        self.btnDataBoxAdd.setObjectName(u"btnDataBoxAdd")

        self.gridLayout_10.addWidget(self.btnDataBoxAdd, 4, 0, 1, 2)

        self.boxSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.boxSpacer, 3, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.frAddBox)


        self.verticalLayout_10.addWidget(self.frDataAdd)

        self.menuData = QFrame(self.pgData)
        self.menuData.setObjectName(u"menuData")
        self.menuData.setMinimumSize(QSize(0, 70))
        self.menuData.setMaximumSize(QSize(16777215, 70))
        self.menuData.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuData.setFrameShape(QFrame.NoFrame)
        self.menuData.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.menuData)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btnDataUpd = QPushButton(self.menuData)
        self.btnDataUpd.setObjectName(u"btnDataUpd")
        self.btnDataUpd.setMinimumSize(QSize(0, 70))
        self.btnDataUpd.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_9.addWidget(self.btnDataUpd)

        self.btnDataAdd = QPushButton(self.menuData)
        self.btnDataAdd.setObjectName(u"btnDataAdd")
        self.btnDataAdd.setMinimumSize(QSize(0, 70))
        self.btnDataAdd.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_9.addWidget(self.btnDataAdd)

        self.btnDataRem = QPushButton(self.menuData)
        self.btnDataRem.setObjectName(u"btnDataRem")
        self.btnDataRem.setMinimumSize(QSize(0, 70))
        self.btnDataRem.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_9.addWidget(self.btnDataRem)

        self.btnDataMen = QPushButton(self.menuData)
        self.btnDataMen.setObjectName(u"btnDataMen")
        self.btnDataMen.setMinimumSize(QSize(0, 70))
        self.btnDataMen.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_9.addWidget(self.btnDataMen)


        self.verticalLayout_10.addWidget(self.menuData)

        self.stackedWidget.addWidget(self.pgData)
        self.pgAdd = QWidget()
        self.pgAdd.setObjectName(u"pgAdd")
        self.verticalLayout_14 = QVBoxLayout(self.pgAdd)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 0)
        self.frAdd = QFrame(self.pgAdd)
        self.frAdd.setObjectName(u"frAdd")
        self.frAdd.setMaximumSize(QSize(16777215, 16777215))
        self.frAdd.setFrameShape(QFrame.NoFrame)
        self.frAdd.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frAdd)
        self.verticalLayout_15.setSpacing(30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lblAdd = QLabel(self.frAdd)
        self.lblAdd.setObjectName(u"lblAdd")
        self.lblAdd.setMinimumSize(QSize(400, 50))
        self.lblAdd.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_15.addWidget(self.lblAdd)

        self.frAddMiddle = QFrame(self.frAdd)
        self.frAddMiddle.setObjectName(u"frAddMiddle")
        self.frAddMiddle.setStyleSheet(u"font-family: \"Segoe UI\";\n"
"font-size: 15pt;")
        self.frAddMiddle.setFrameShape(QFrame.NoFrame)
        self.frAddMiddle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frAddMiddle)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frAddLeft = QFrame(self.frAddMiddle)
        self.frAddLeft.setObjectName(u"frAddLeft")
        self.frAddLeft.setFrameShape(QFrame.NoFrame)
        self.frAddLeft.setFrameShadow(QFrame.Plain)
        self.formLayout_7 = QFormLayout(self.frAddLeft)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_7.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_7.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_7.setHorizontalSpacing(70)
        self.formLayout_7.setVerticalSpacing(20)
        self.formLayout_7.setContentsMargins(10, 0, 10, 0)
        self.lblAddSelBox = QLabel(self.frAddLeft)
        self.lblAddSelBox.setObjectName(u"lblAddSelBox")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.lblAddSelBox)

        self.comAddSelBox = QComboBox(self.frAddLeft)
        self.comAddSelBox.setObjectName(u"comAddSelBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comAddSelBox.sizePolicy().hasHeightForWidth())
        self.comAddSelBox.setSizePolicy(sizePolicy4)
        self.comAddSelBox.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.comAddSelBox)

        self.lblAddSelSow = QLabel(self.frAddLeft)
        self.lblAddSelSow.setObjectName(u"lblAddSelSow")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.lblAddSelSow)

        self.comAddSelSow = QComboBox(self.frAddLeft)
        self.comAddSelSow.setObjectName(u"comAddSelSow")
        sizePolicy4.setHeightForWidth(self.comAddSelSow.sizePolicy().hasHeightForWidth())
        self.comAddSelSow.setSizePolicy(sizePolicy4)
        self.comAddSelSow.setMaximumSize(QSize(16777215, 16777215))
        self.comAddSelSow.setInputMethodHints(Qt.ImhNone)
        self.comAddSelSow.setEditable(True)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.comAddSelSow)

        self.lblAddSelCur = QLabel(self.frAddLeft)
        self.lblAddSelCur.setObjectName(u"lblAddSelCur")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.lblAddSelCur)

        self.comAddSelCur = QComboBox(self.frAddLeft)
        self.comAddSelCur.setObjectName(u"comAddSelCur")
        sizePolicy4.setHeightForWidth(self.comAddSelCur.sizePolicy().hasHeightForWidth())
        self.comAddSelCur.setSizePolicy(sizePolicy4)
        self.comAddSelCur.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.comAddSelCur)

        self.lblAddSelEntryDate = QLabel(self.frAddLeft)
        self.lblAddSelEntryDate.setObjectName(u"lblAddSelEntryDate")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.lblAddSelEntryDate)

        self.spiAddSelEntryDate = QDateEdit(self.frAddLeft)
        self.spiAddSelEntryDate.setObjectName(u"spiAddSelEntryDate")
        sizePolicy4.setHeightForWidth(self.spiAddSelEntryDate.sizePolicy().hasHeightForWidth())
        self.spiAddSelEntryDate.setSizePolicy(sizePolicy4)
        self.spiAddSelEntryDate.setMaximumSize(QSize(16777215, 16777215))
        self.spiAddSelEntryDate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.spiAddSelEntryDate)

        self.lblAddSelCurDate = QLabel(self.frAddLeft)
        self.lblAddSelCurDate.setObjectName(u"lblAddSelCurDate")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.lblAddSelCurDate)

        self.spiAddSelCurDay = QSpinBox(self.frAddLeft)
        self.spiAddSelCurDay.setObjectName(u"spiAddSelCurDay")
        sizePolicy4.setHeightForWidth(self.spiAddSelCurDay.sizePolicy().hasHeightForWidth())
        self.spiAddSelCurDay.setSizePolicy(sizePolicy4)
        self.spiAddSelCurDay.setAlignment(Qt.AlignCenter)
        self.spiAddSelCurDay.setMinimum(101)
        self.spiAddSelCurDay.setMaximum(115)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.spiAddSelCurDay)

        self.lblAddCurType = QLabel(self.frAddLeft)
        self.lblAddCurType.setObjectName(u"lblAddCurType")

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.lblAddCurType)

        self.txtAddCurType = QLabel(self.frAddLeft)
        self.txtAddCurType.setObjectName(u"txtAddCurType")
        sizePolicy.setHeightForWidth(self.txtAddCurType.sizePolicy().hasHeightForWidth())
        self.txtAddCurType.setSizePolicy(sizePolicy)
        self.txtAddCurType.setStyleSheet(u"border: none;")
        self.txtAddCurType.setAlignment(Qt.AlignCenter)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.txtAddCurType)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_7.setItem(6, QFormLayout.SpanningRole, self.verticalSpacer)

        self.lblAddStatus = QLabel(self.frAddLeft)
        self.lblAddStatus.setObjectName(u"lblAddStatus")
        self.lblAddStatus.setStyleSheet(u"border: none;\n"
"font-size: 12pt;")
        self.lblAddStatus.setAlignment(Qt.AlignCenter)

        self.formLayout_7.setWidget(7, QFormLayout.SpanningRole, self.lblAddStatus)


        self.horizontalLayout_13.addWidget(self.frAddLeft)

        self.frAddRight = QFrame(self.frAddMiddle)
        self.frAddRight.setObjectName(u"frAddRight")
        self.frAddRight.setMinimumSize(QSize(0, 0))
        self.frAddRight.setMaximumSize(QSize(16777215, 16777215))
        self.frAddRight.setFrameShape(QFrame.NoFrame)
        self.frAddRight.setFrameShadow(QFrame.Plain)
        self.formLayout_8 = QFormLayout(self.frAddRight)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_8.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_8.setHorizontalSpacing(70)
        self.formLayout_8.setVerticalSpacing(20)
        self.formLayout_8.setContentsMargins(10, 0, 10, 0)
        self.lblAddBirth = QLabel(self.frAddRight)
        self.lblAddBirth.setObjectName(u"lblAddBirth")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.lblAddBirth)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, -1, 10, -1)
        self.radAddBirthY = QRadioButton(self.frAddRight)
        self.radAddBirthY.setObjectName(u"radAddBirthY")

        self.horizontalLayout_14.addWidget(self.radAddBirthY)

        self.radAddBirthN = QRadioButton(self.frAddRight)
        self.radAddBirthN.setObjectName(u"radAddBirthN")

        self.horizontalLayout_14.addWidget(self.radAddBirthN)


        self.formLayout_8.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_14)

        self.frAddBirth = QFrame(self.frAddRight)
        self.frAddBirth.setObjectName(u"frAddBirth")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frAddBirth.sizePolicy().hasHeightForWidth())
        self.frAddBirth.setSizePolicy(sizePolicy5)
        self.frAddBirth.setMinimumSize(QSize(0, 200))
        self.frAddBirth.setMaximumSize(QSize(16777215, 0))
        self.frAddBirth.setFrameShape(QFrame.NoFrame)
        self.frAddBirth.setFrameShadow(QFrame.Plain)
        self.formLayout_10 = QFormLayout(self.frAddBirth)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(92)
        self.formLayout_10.setVerticalSpacing(20)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lblAddSelPigDate = QLabel(self.frAddBirth)
        self.lblAddSelPigDate.setObjectName(u"lblAddSelPigDate")
        self.lblAddSelPigDate.setMinimumSize(QSize(0, 32))
        self.lblAddSelPigDate.setMaximumSize(QSize(16777215, 32))

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.lblAddSelPigDate)

        self.spiAddSelPigDate = QDateEdit(self.frAddBirth)
        self.spiAddSelPigDate.setObjectName(u"spiAddSelPigDate")
        sizePolicy4.setHeightForWidth(self.spiAddSelPigDate.sizePolicy().hasHeightForWidth())
        self.spiAddSelPigDate.setSizePolicy(sizePolicy4)
        self.spiAddSelPigDate.setMinimumSize(QSize(0, 0))
        self.spiAddSelPigDate.setMaximumSize(QSize(16777215, 32))
        self.spiAddSelPigDate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.spiAddSelPigDate)

        self.lblAddSelPigBirth = QLabel(self.frAddBirth)
        self.lblAddSelPigBirth.setObjectName(u"lblAddSelPigBirth")
        self.lblAddSelPigBirth.setMinimumSize(QSize(0, 32))

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.lblAddSelPigBirth)

        self.spiAddSelPigBirth = QSpinBox(self.frAddBirth)
        self.spiAddSelPigBirth.setObjectName(u"spiAddSelPigBirth")
        sizePolicy4.setHeightForWidth(self.spiAddSelPigBirth.sizePolicy().hasHeightForWidth())
        self.spiAddSelPigBirth.setSizePolicy(sizePolicy4)
        self.spiAddSelPigBirth.setMinimumSize(QSize(0, 32))
        self.spiAddSelPigBirth.setMaximumSize(QSize(16777215, 16777215))
        self.spiAddSelPigBirth.setAlignment(Qt.AlignCenter)

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.spiAddSelPigBirth)

        self.lblAddSelPigRealBirth = QLabel(self.frAddBirth)
        self.lblAddSelPigRealBirth.setObjectName(u"lblAddSelPigRealBirth")
        self.lblAddSelPigRealBirth.setMinimumSize(QSize(0, 32))

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.lblAddSelPigRealBirth)

        self.spiAddSelPigRealBirth = QSpinBox(self.frAddBirth)
        self.spiAddSelPigRealBirth.setObjectName(u"spiAddSelPigRealBirth")
        sizePolicy4.setHeightForWidth(self.spiAddSelPigRealBirth.sizePolicy().hasHeightForWidth())
        self.spiAddSelPigRealBirth.setSizePolicy(sizePolicy4)
        self.spiAddSelPigRealBirth.setMinimumSize(QSize(0, 32))
        self.spiAddSelPigRealBirth.setMaximumSize(QSize(16777215, 16777215))
        self.spiAddSelPigRealBirth.setAlignment(Qt.AlignCenter)

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.spiAddSelPigRealBirth)

        self.lblAddSelPigWeight = QLabel(self.frAddBirth)
        self.lblAddSelPigWeight.setObjectName(u"lblAddSelPigWeight")
        self.lblAddSelPigWeight.setMinimumSize(QSize(0, 32))

        self.formLayout_10.setWidget(3, QFormLayout.LabelRole, self.lblAddSelPigWeight)

        self.spiAddSelPigWeight = QDoubleSpinBox(self.frAddBirth)
        self.spiAddSelPigWeight.setObjectName(u"spiAddSelPigWeight")
        self.spiAddSelPigWeight.setMinimumSize(QSize(0, 32))
        self.spiAddSelPigWeight.setAlignment(Qt.AlignCenter)
        self.spiAddSelPigWeight.setMaximum(200.000000000000000)
        self.spiAddSelPigWeight.setSingleStep(0.500000000000000)
        self.spiAddSelPigWeight.setValue(0.000000000000000)

        self.formLayout_10.setWidget(3, QFormLayout.FieldRole, self.spiAddSelPigWeight)


        self.formLayout_8.setWidget(1, QFormLayout.SpanningRole, self.frAddBirth)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_8.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer_2)

        self.lblAddNotes = QLabel(self.frAddRight)
        self.lblAddNotes.setObjectName(u"lblAddNotes")
        self.lblAddNotes.setMaximumSize(QSize(16777215, 32))

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.lblAddNotes)

        self.txtAddNotes = QTextEdit(self.frAddRight)
        self.txtAddNotes.setObjectName(u"txtAddNotes")
        self.txtAddNotes.setMaximumSize(QSize(16777215, 100))

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.txtAddNotes)


        self.horizontalLayout_13.addWidget(self.frAddRight)


        self.verticalLayout_15.addWidget(self.frAddMiddle)


        self.verticalLayout_14.addWidget(self.frAdd)

        self.menuAdd = QFrame(self.pgAdd)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuAdd.setMinimumSize(QSize(0, 70))
        self.menuAdd.setMaximumSize(QSize(16777215, 70))
        self.menuAdd.setStyleSheet(u"QPushButton {\n"
"background-color: #3f3c5b;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #bd93f9;\n"
"color: white;\n"
"}")
        self.menuAdd.setFrameShape(QFrame.NoFrame)
        self.menuAdd.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.menuAdd)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnAddUpd = QPushButton(self.menuAdd)
        self.btnAddUpd.setObjectName(u"btnAddUpd")
        self.btnAddUpd.setMinimumSize(QSize(0, 70))
        self.btnAddUpd.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_12.addWidget(self.btnAddUpd)

        self.btnAddAdd = QPushButton(self.menuAdd)
        self.btnAddAdd.setObjectName(u"btnAddAdd")
        self.btnAddAdd.setMinimumSize(QSize(0, 70))
        self.btnAddAdd.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_12.addWidget(self.btnAddAdd)

        self.btnAddRes = QPushButton(self.menuAdd)
        self.btnAddRes.setObjectName(u"btnAddRes")
        self.btnAddRes.setMinimumSize(QSize(0, 70))
        self.btnAddRes.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_12.addWidget(self.btnAddRes)

        self.btnAddMen = QPushButton(self.menuAdd)
        self.btnAddMen.setObjectName(u"btnAddMen")
        self.btnAddMen.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_12.addWidget(self.btnAddMen)


        self.verticalLayout_14.addWidget(self.menuAdd)

        self.stackedWidget.addWidget(self.pgAdd)
        self.pgSettings = QWidget()
        self.pgSettings.setObjectName(u"pgSettings")
        self.verticalLayout_16 = QVBoxLayout(self.pgSettings)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 0)
        self.frSettings = QFrame(self.pgSettings)
        self.frSettings.setObjectName(u"frSettings")
        self.frSettings.setFrameShape(QFrame.NoFrame)
        self.frSettings.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.frSettings)
        self.verticalLayout_17.setSpacing(20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 10)
        self.lblSettings = QLabel(self.frSettings)
        self.lblSettings.setObjectName(u"lblSettings")
        self.lblSettings.setMinimumSize(QSize(400, 50))
        self.lblSettings.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_17.addWidget(self.lblSettings)

        self.scrollAreaSettingsMain = QScrollArea(self.frSettings)
        self.scrollAreaSettingsMain.setObjectName(u"scrollAreaSettingsMain")
        self.scrollAreaSettingsMain.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaSettingsMain.setFrameShape(QFrame.NoFrame)
        self.scrollAreaSettingsMain.setFrameShadow(QFrame.Plain)
        self.scrollAreaSettingsMain.setWidgetResizable(True)
        self.scrollAreaSettings = QWidget()
        self.scrollAreaSettings.setObjectName(u"scrollAreaSettings")
        self.scrollAreaSettings.setGeometry(QRect(0, 0, 591, 780))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaSettings)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frSettings3 = QFrame(self.scrollAreaSettings)
        self.frSettings3.setObjectName(u"frSettings3")
        sizePolicy2.setHeightForWidth(self.frSettings3.sizePolicy().hasHeightForWidth())
        self.frSettings3.setSizePolicy(sizePolicy2)
        self.frSettings3.setMinimumSize(QSize(0, 0))
        self.frSettings3.setStyleSheet(u"font-size: 15pt;")
        self.frSettings3.setFrameShape(QFrame.NoFrame)
        self.frSettings3.setFrameShadow(QFrame.Plain)
        self.gridLayout_17 = QGridLayout(self.frSettings3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(10)
        self.gridLayout_17.setVerticalSpacing(30)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.spiSetMaxCur_2 = QSpinBox(self.frSettings3)
        self.spiSetMaxCur_2.setObjectName(u"spiSetMaxCur_2")
        self.spiSetMaxCur_2.setAlignment(Qt.AlignCenter)
        self.spiSetMaxCur_2.setMinimum(1)
        self.spiSetMaxCur_2.setMaximum(9)
        self.spiSetMaxCur_2.setValue(9)

        self.gridLayout_17.addWidget(self.spiSetMaxCur_2, 1, 1, 1, 1)

        self.lblSetMaxHall_3 = QLabel(self.frSettings3)
        self.lblSetMaxHall_3.setObjectName(u"lblSetMaxHall_3")
        self.lblSetMaxHall_3.setStyleSheet(u"border: none;")

        self.gridLayout_17.addWidget(self.lblSetMaxHall_3, 4, 0, 1, 1)

        self.spiSetMaxHall_2 = QSpinBox(self.frSettings3)
        self.spiSetMaxHall_2.setObjectName(u"spiSetMaxHall_2")
        self.spiSetMaxHall_2.setAlignment(Qt.AlignCenter)
        self.spiSetMaxHall_2.setMinimum(1)
        self.spiSetMaxHall_2.setMaximum(30)
        self.spiSetMaxHall_2.setValue(10)

        self.gridLayout_17.addWidget(self.spiSetMaxHall_2, 2, 1, 2, 1)

        self.spiSetModCur = QSpinBox(self.frSettings3)
        self.spiSetModCur.setObjectName(u"spiSetModCur")
        self.spiSetModCur.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.spiSetModCur, 1, 3, 1, 1)

        self.lblSetMaxHall_2 = QLabel(self.frSettings3)
        self.lblSetMaxHall_2.setObjectName(u"lblSetMaxHall_2")
        self.lblSetMaxHall_2.setStyleSheet(u"border: none;")

        self.gridLayout_17.addWidget(self.lblSetMaxHall_2, 2, 0, 2, 1)

        self.btnSetConfFarm = QPushButton(self.frSettings3)
        self.btnSetConfFarm.setObjectName(u"btnSetConfFarm")

        self.gridLayout_17.addWidget(self.btnSetConfFarm, 5, 3, 1, 1)

        self.lblSetConfCard_2 = QLabel(self.frSettings3)
        self.lblSetConfCard_2.setObjectName(u"lblSetConfCard_2")
        self.lblSetConfCard_2.setMaximumSize(QSize(16777215, 60))
        self.lblSetConfCard_2.setStyleSheet(u"font-size: 17pt;")
        self.lblSetConfCard_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.lblSetConfCard_2, 0, 0, 1, 2)

        self.spiSetMaxHall_3 = QSpinBox(self.frSettings3)
        self.spiSetMaxHall_3.setObjectName(u"spiSetMaxHall_3")
        self.spiSetMaxHall_3.setAlignment(Qt.AlignCenter)
        self.spiSetMaxHall_3.setMinimum(1)
        self.spiSetMaxHall_3.setMaximum(30)
        self.spiSetMaxHall_3.setValue(10)

        self.gridLayout_17.addWidget(self.spiSetMaxHall_3, 4, 1, 1, 1)

        self.radSetModEntryDate = QRadioButton(self.frSettings3)
        self.radSetModEntryDate.setObjectName(u"radSetModEntryDate")

        self.gridLayout_17.addWidget(self.radSetModEntryDate, 4, 2, 1, 1)

        self.lblSetMaxCur_2 = QLabel(self.frSettings3)
        self.lblSetMaxCur_2.setObjectName(u"lblSetMaxCur_2")
        self.lblSetMaxCur_2.setStyleSheet(u"border: none;")

        self.gridLayout_17.addWidget(self.lblSetMaxCur_2, 1, 0, 1, 1)

        self.spiSetModEntryDate = QDateEdit(self.frSettings3)
        self.spiSetModEntryDate.setObjectName(u"spiSetModEntryDate")

        self.gridLayout_17.addWidget(self.spiSetModEntryDate, 4, 3, 1, 1)

        self.radSetModCur = QRadioButton(self.frSettings3)
        self.radSetModCur.setObjectName(u"radSetModCur")

        self.gridLayout_17.addWidget(self.radSetModCur, 1, 2, 1, 1)

        self.radSetModSit = QRadioButton(self.frSettings3)
        self.radSetModSit.setObjectName(u"radSetModSit")

        self.gridLayout_17.addWidget(self.radSetModSit, 2, 2, 2, 1)

        self.comSetModSit = QComboBox(self.frSettings3)
        self.comSetModSit.addItem("")
        self.comSetModSit.addItem("")
        self.comSetModSit.setObjectName(u"comSetModSit")

        self.gridLayout_17.addWidget(self.comSetModSit, 2, 3, 2, 1)


        self.verticalLayout_18.addWidget(self.frSettings3)

        self.frSettings1 = QFrame(self.scrollAreaSettings)
        self.frSettings1.setObjectName(u"frSettings1")
        self.frSettings1.setMinimumSize(QSize(0, 200))
        self.frSettings1.setMaximumSize(QSize(16777215, 300))
        self.frSettings1.setStyleSheet(u"font-size: 15pt;")
        self.frSettings1.setFrameShape(QFrame.NoFrame)
        self.frSettings1.setFrameShadow(QFrame.Plain)
        self.gridLayout_15 = QGridLayout(self.frSettings1)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(10)
        self.gridLayout_15.setVerticalSpacing(30)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btnSetConfGen = QPushButton(self.frSettings1)
        self.btnSetConfGen.setObjectName(u"btnSetConfGen")

        self.gridLayout_15.addWidget(self.btnSetConfGen, 4, 3, 1, 1)

        self.lblSetConfGen = QLabel(self.frSettings1)
        self.lblSetConfGen.setObjectName(u"lblSetConfGen")
        self.lblSetConfGen.setMaximumSize(QSize(16777215, 60))
        self.lblSetConfGen.setStyleSheet(u"font-size: 17pt;")

        self.gridLayout_15.addWidget(self.lblSetConfGen, 1, 0, 1, 4)

        self.lblSetMaxCur = QLabel(self.frSettings1)
        self.lblSetMaxCur.setObjectName(u"lblSetMaxCur")
        self.lblSetMaxCur.setStyleSheet(u"border: none;")

        self.gridLayout_15.addWidget(self.lblSetMaxCur, 3, 0, 1, 1)

        self.lblSetMaxHall = QLabel(self.frSettings1)
        self.lblSetMaxHall.setObjectName(u"lblSetMaxHall")
        self.lblSetMaxHall.setStyleSheet(u"border: none;")

        self.gridLayout_15.addWidget(self.lblSetMaxHall, 3, 2, 1, 1)

        self.comboBox = QComboBox(self.frSettings1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_15.addWidget(self.comboBox, 3, 1, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.radioButton = QRadioButton(self.frSettings1)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_18.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.frSettings1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_18.addWidget(self.radioButton_2, 0, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_18, 3, 3, 1, 1)


        self.verticalLayout_18.addWidget(self.frSettings1)

        self.frSettings2 = QFrame(self.scrollAreaSettings)
        self.frSettings2.setObjectName(u"frSettings2")
        self.frSettings2.setMinimumSize(QSize(0, 300))
        self.frSettings2.setStyleSheet(u"font-size: 15pt;")
        self.frSettings2.setFrameShape(QFrame.NoFrame)
        self.frSettings2.setFrameShadow(QFrame.Plain)
        self.gridLayout_16 = QGridLayout(self.frSettings2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(10)
        self.gridLayout_16.setVerticalSpacing(30)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.comSetComPort = QComboBox(self.frSettings2)
        self.comSetComPort.addItem("")
        self.comSetComPort.addItem("")
        self.comSetComPort.setObjectName(u"comSetComPort")

        self.gridLayout_16.addWidget(self.comSetComPort, 1, 1, 1, 1)

        self.lblSetComPort = QLabel(self.frSettings2)
        self.lblSetComPort.setObjectName(u"lblSetComPort")
        self.lblSetComPort.setStyleSheet(u"border: none;")

        self.gridLayout_16.addWidget(self.lblSetComPort, 1, 0, 1, 1)

        self.spiSetComImp = QSpinBox(self.frSettings2)
        self.spiSetComImp.setObjectName(u"spiSetComImp")
        sizePolicy.setHeightForWidth(self.spiSetComImp.sizePolicy().hasHeightForWidth())
        self.spiSetComImp.setSizePolicy(sizePolicy)
        self.spiSetComImp.setAlignment(Qt.AlignCenter)
        self.spiSetComImp.setMinimum(10)
        self.spiSetComImp.setMaximum(120)
        self.spiSetComImp.setSingleStep(10)
        self.spiSetComImp.setValue(30)

        self.gridLayout_16.addWidget(self.spiSetComImp, 3, 3, 1, 1)

        self.btnSetConfImp = QPushButton(self.frSettings2)
        self.btnSetConfImp.setObjectName(u"btnSetConfImp")

        self.gridLayout_16.addWidget(self.btnSetConfImp, 4, 3, 1, 1)

        self.lblSetComCal = QLabel(self.frSettings2)
        self.lblSetComCal.setObjectName(u"lblSetComCal")
        self.lblSetComCal.setStyleSheet(u"border: none;")

        self.gridLayout_16.addWidget(self.lblSetComCal, 3, 0, 1, 1)

        self.lblSetComImp = QLabel(self.frSettings2)
        self.lblSetComImp.setObjectName(u"lblSetComImp")
        self.lblSetComImp.setStyleSheet(u"border: none;")

        self.gridLayout_16.addWidget(self.lblSetComImp, 3, 2, 1, 1)

        self.spiSetComCal = QSpinBox(self.frSettings2)
        self.spiSetComCal.setObjectName(u"spiSetComCal")
        sizePolicy.setHeightForWidth(self.spiSetComCal.sizePolicy().hasHeightForWidth())
        self.spiSetComCal.setSizePolicy(sizePolicy)
        self.spiSetComCal.setAlignment(Qt.AlignCenter)
        self.spiSetComCal.setMinimum(10)
        self.spiSetComCal.setMaximum(200)
        self.spiSetComCal.setSingleStep(10)
        self.spiSetComCal.setValue(60)

        self.gridLayout_16.addWidget(self.spiSetComCal, 3, 1, 1, 1)

        self.lblSetComBaud = QLabel(self.frSettings2)
        self.lblSetComBaud.setObjectName(u"lblSetComBaud")
        self.lblSetComBaud.setStyleSheet(u"border: none;")

        self.gridLayout_16.addWidget(self.lblSetComBaud, 1, 2, 1, 1)

        self.btnSetConfCalib = QPushButton(self.frSettings2)
        self.btnSetConfCalib.setObjectName(u"btnSetConfCalib")

        self.gridLayout_16.addWidget(self.btnSetConfCalib, 4, 1, 1, 1)

        self.lblSetConfCard = QLabel(self.frSettings2)
        self.lblSetConfCard.setObjectName(u"lblSetConfCard")
        self.lblSetConfCard.setMaximumSize(QSize(16777215, 60))
        self.lblSetConfCard.setStyleSheet(u"font-size: 17pt;")
        self.lblSetConfCard.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.lblSetConfCard, 0, 0, 1, 4)

        self.comSetComBaud = QComboBox(self.frSettings2)
        self.comSetComBaud.addItem("")
        self.comSetComBaud.addItem("")
        self.comSetComBaud.addItem("")
        self.comSetComBaud.addItem("")
        self.comSetComBaud.addItem("")
        self.comSetComBaud.setObjectName(u"comSetComBaud")

        self.gridLayout_16.addWidget(self.comSetComBaud, 1, 3, 1, 1)

        self.btnSetConfCom = QPushButton(self.frSettings2)
        self.btnSetConfCom.setObjectName(u"btnSetConfCom")

        self.gridLayout_16.addWidget(self.btnSetConfCom, 2, 1, 1, 1)

        self.btnSetConfBaud = QPushButton(self.frSettings2)
        self.btnSetConfBaud.setObjectName(u"btnSetConfBaud")

        self.gridLayout_16.addWidget(self.btnSetConfBaud, 2, 3, 1, 1)


        self.verticalLayout_18.addWidget(self.frSettings2)

        self.scrollAreaSettingsMain.setWidget(self.scrollAreaSettings)

        self.verticalLayout_17.addWidget(self.scrollAreaSettingsMain)


        self.verticalLayout_16.addWidget(self.frSettings)

        self.stackedWidget.addWidget(self.pgSettings)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frPages, 0, 1, 2, 1)


        self.verticalLayout_2.addWidget(self.fr2Content)


        self.verticalLayout.addWidget(self.frBg)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sala Parto - Gong Tecnology", None))
        self.lblTimer.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.comLanguage.setItemText(0, QCoreApplication.translate("MainWindow", u"Italiano", None))
        self.comLanguage.setItemText(1, QCoreApplication.translate("MainWindow", u"Espanol", None))
        self.comLanguage.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))

        self.btnMinimize.setText("")
        self.btnMaximize.setText("")
        self.btnClose.setText("")
        self.lblCompany.setText(QCoreApplication.translate("MainWindow", u"Gong Tecnology Srl - Copyright 2021", None))
        self.lblVersion.setText(QCoreApplication.translate("MainWindow", u"v1.0.4", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnHall.setText(QCoreApplication.translate("MainWindow", u"Sale", None))
        self.btnCurve.setText(QCoreApplication.translate("MainWindow", u"Curve", None))
        self.btnTime.setText(QCoreApplication.translate("MainWindow", u"Orari", None))
        self.btnStock.setText(QCoreApplication.translate("MainWindow", u"Stoccaggio", None))
        self.btnData.setText(QCoreApplication.translate("MainWindow", u"Dati Impianto", None))
        self.btnCom.setText(QCoreApplication.translate("MainWindow", u"Comunicazione", None))
        self.btnPig.setText(QCoreApplication.translate("MainWindow", u"Storico scrofa", None))
        self.btnSettings.setText("")
        self.lblHallCom.setText(QCoreApplication.translate("MainWindow", u"Com:", None))
        self.chkHallCom.setText("")
        self.chkHallFeed.setText("")
        self.lblHallFeed.setText(QCoreApplication.translate("MainWindow", u"Pasto:", None))
        self.lblHall.setText(QCoreApplication.translate("MainWindow", u"Numero Sala", None))
        ___qtablewidgetitem = self.tblHall.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Gabbia", None));
        ___qtablewidgetitem1 = self.tblHall.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Scrofa", None));
        ___qtablewidgetitem2 = self.tblHall.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Situazione", None));
        ___qtablewidgetitem3 = self.tblHall.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Curva", None));
        ___qtablewidgetitem4 = self.tblHall.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"GG Curva", None));
        ___qtablewidgetitem5 = self.tblHall.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Gr/Giorno", None));
        ___qtablewidgetitem6 = self.tblHall.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Gr/Razione", None));
        ___qtablewidgetitem7 = self.tblHall.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Distribuiti", None));
        ___qtablewidgetitem8 = self.tblHall.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Suinetti", None));
        ___qtablewidgetitem9 = self.tblHall.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"%oggi", None));
        ___qtablewidgetitem10 = self.tblHall.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"%ieri", None));
        ___qtablewidgetitem11 = self.tblHall.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"% altro ieri", None));
        ___qtablewidgetitem12 = self.tblHall.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Tot. consumato", None));
        ___qtablewidgetitem13 = self.tblHall.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"% sul teorico", None));

        __sortingEnabled = self.tblHall.isSortingEnabled()
        self.tblHall.setSortingEnabled(False)
        self.tblHall.setSortingEnabled(__sortingEnabled)

        self.lblHallExtra.setText(QCoreApplication.translate("MainWindow", u"Dati Aggiuntivi", None))
        self.lblHallSit.setText(QCoreApplication.translate("MainWindow", u"Situazione", None))
        self.lblHallStat.setText(QCoreApplication.translate("MainWindow", u"Attivo", None))
        self.lblHallRation.setText(QCoreApplication.translate("MainWindow", u"Razionamento", None))
        self.lblHallEntry.setText(QCoreApplication.translate("MainWindow", u"Data Entrata", None))
        self.lblHallBirth.setText(QCoreApplication.translate("MainWindow", u"Data Parto", None))
        self.lblHallNrBirth.setText(QCoreApplication.translate("MainWindow", u"Suini Nati", None))
        self.lblHallNrDeath.setText(QCoreApplication.translate("MainWindow", u"Suini Vivi", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gestazione", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"05/10/2021", None))
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.spinBox.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.btnHallRem.setText(QCoreApplication.translate("MainWindow", u"RIMUOVI DA GESTIONE", None))
        self.btnHallAdd.setText(QCoreApplication.translate("MainWindow", u"AGGIUNGI SCROFA", None))
        self.btnHallExp.setText(QCoreApplication.translate("MainWindow", u"ESPORTA DATI", None))
        self.btnHallLoadCur.setText(QCoreApplication.translate("MainWindow", u"CARICA CURVA AUTOM.", None))
        ___qtablewidgetitem14 = self.tblCurve.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem15 = self.tblCurve.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Giorno", None));
        ___qtablewidgetitem16 = self.tblCurve.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e0", None));
        self.lblCurve.setText(QCoreApplication.translate("MainWindow", u"Numero Curva", None))
        self.lblCurveStatus.setText("")
        self.btnCurveSave.setText(QCoreApplication.translate("MainWindow", u"SALVA CURVA", None))
        self.btnCurveRem.setText(QCoreApplication.translate("MainWindow", u"RIMUOVI CURVA", None))
        self.btnCurveExp.setText(QCoreApplication.translate("MainWindow", u"ESPORTA CURVE", None))
        self.btnCurveMen.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPALE", None))
        self.lblTimeStatus.setText("")
        self.lblTime.setText(QCoreApplication.translate("MainWindow", u"Programmazione Pasti", None))
        ___qtablewidgetitem17 = self.tblTime.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Dalle", None));
        ___qtablewidgetitem18 = self.tblTime.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Alle", None));
        ___qtablewidgetitem19 = self.tblTime.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Pasto Attivo", None));
        ___qtablewidgetitem20 = self.tblTime.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem21 = self.tblTime.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem22 = self.tblTime.verticalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem23 = self.tblTime.verticalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem24 = self.tblTime.verticalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem25 = self.tblTime.verticalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem26 = self.tblTime.verticalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem27 = self.tblTime.verticalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem28 = self.tblTime.verticalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem29 = self.tblTime.verticalHeaderItem(9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem30 = self.tblTime.verticalHeaderItem(10)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem31 = self.tblTime.verticalHeaderItem(11)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem32 = self.tblTime.verticalHeaderItem(12)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem33 = self.tblTime.verticalHeaderItem(13)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem34 = self.tblTime.verticalHeaderItem(14)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem35 = self.tblTime.verticalHeaderItem(15)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem36 = self.tblTime.verticalHeaderItem(16)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem37 = self.tblTime.verticalHeaderItem(17)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem38 = self.tblTime.verticalHeaderItem(18)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem39 = self.tblTime.verticalHeaderItem(19)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem40 = self.tblTime.verticalHeaderItem(20)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem41 = self.tblTime.verticalHeaderItem(21)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem42 = self.tblTime.verticalHeaderItem(22)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem43 = self.tblTime.verticalHeaderItem(23)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"24", None));
        self.lblTimeDur.setText(QCoreApplication.translate("MainWindow", u"Durata Pasto Attuale:", None))
        self.txtTimeDur.setText("")
        self.lblTimeAct.setText(QCoreApplication.translate("MainWindow", u"Pasto Attivo:", None))
        self.txtTimeAct.setText("")
        self.lblTimeNrAct.setText(QCoreApplication.translate("MainWindow", u"Numero Pasto Attuale:", None))
        self.txtTimeNrAct.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblTimeRat.setText(QCoreApplication.translate("MainWindow", u"Razionamento:", None))
        self.lblTimeTotFeed.setText(QCoreApplication.translate("MainWindow", u"Numero Pasti Attivi", None))
        self.txtTimeTotFeed.setText("")
        self.btnTimeUpd.setText(QCoreApplication.translate("MainWindow", u"AGGIORNA DATI", None))
        self.btnTimeSave.setText(QCoreApplication.translate("MainWindow", u"SALVA PASTI", None))
        self.btnTimeRem.setText(QCoreApplication.translate("MainWindow", u"RIMUOVI PASTO", None))
        self.btnTimeMen.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPALE", None))
        self.lblWidSilo.setText("")
        self.lblStock.setText(QCoreApplication.translate("MainWindow", u"Silos e Stoccaggio", None))
        self.lblStockSiloSel.setText(QCoreApplication.translate("MainWindow", u"Silos", None))
        self.spiStockSiloNr.setSuffix("")
        self.lblStockQtaNow.setText(QCoreApplication.translate("MainWindow", u"Qta Attuale", None))
        self.txtStockQtaNow.setText("")
        self.lblStockQtaMax.setText(QCoreApplication.translate("MainWindow", u"Qta Massima", None))
        self.txtStockQtaMax.setText("")
        self.lblStockBoxGest.setText(QCoreApplication.translate("MainWindow", u"Box Gestiti", None))
        self.txtStockBoxGest.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lblStockPrevDur.setText(QCoreApplication.translate("MainWindow", u"Previsione Durata", None))
        self.txtStockPrevDur.setText(QCoreApplication.translate("MainWindow", u"X Giorni", None))
        self.lblStockLastLoadQta.setText(QCoreApplication.translate("MainWindow", u"Ultimo Carico", None))
        self.lblStockLastLoadDate.setText(QCoreApplication.translate("MainWindow", u"Data Carico", None))
        self.txtStockLastLoadQta.setText("")
        self.txtStockLastLoadDate.setText("")
        self.lblStockModQtaNow.setText(QCoreApplication.translate("MainWindow", u"Mod Qta Attuale", None))
        self.spiStockModQtaNow.setSuffix(QCoreApplication.translate("MainWindow", u" KG", None))
        self.lblStockModQtaMax.setText(QCoreApplication.translate("MainWindow", u"Mod Qta Massima", None))
        self.spiStockModQtaMax.setSuffix(QCoreApplication.translate("MainWindow", u" KG", None))
        self.lblStockModBoxGest.setText(QCoreApplication.translate("MainWindow", u"Mod Box Gestiti", None))
        self.spiStockModBoxGest.setSuffix("")
        self.spiStockLoadQta.setSuffix(QCoreApplication.translate("MainWindow", u" KG", None))
        self.lblStockLoadQta.setText(QCoreApplication.translate("MainWindow", u"Qta Carico Silo", None))
        self.btnStockSaveEdit.setText(QCoreApplication.translate("MainWindow", u"Salva Modifiche ", None))
        self.lblStockLoadDate.setText(QCoreApplication.translate("MainWindow", u"Data Carico Silo", None))
        self.btnStockRegLoad.setText(QCoreApplication.translate("MainWindow", u"Registra Carico Silo", None))
        self.btnStockUpd.setText(QCoreApplication.translate("MainWindow", u"AGGIORNA SILOS", None))
        self.btnStockConf.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA SILOS", None))
        self.btnStockLoad.setText(QCoreApplication.translate("MainWindow", u"CARICA SILOS", None))
        self.btnStockMen.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPALE", None))
        self.lblHistorySel.setText(QCoreApplication.translate("MainWindow", u"Selezione:", None))
        self.lblHistoryGestDal.setText(QCoreApplication.translate("MainWindow", u"In gestione dal:", None))
        self.txtHistoryGestDal.setText("")
        self.lblHistoryCons.setText(QCoreApplication.translate("MainWindow", u"Consumo:", None))
        self.lblHistoryConsTot.setText(QCoreApplication.translate("MainWindow", u"Totale:", None))
        self.txtHistoryConsTot.setText("")
        self.lblHistoryGestAl.setText(QCoreApplication.translate("MainWindow", u"Fino al:", None))
        self.txtHistoryGestAl.setText("")
        self.lblTest.setText(QCoreApplication.translate("MainWindow", u"Tracciabilit\u00e0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Consumo Totale Impianto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Consumo Teorico Impianto", None))
        self.btnTestStr.setText(QCoreApplication.translate("MainWindow", u"START TEST", None))
        self.btnTestSto.setText(QCoreApplication.translate("MainWindow", u"STOP TEST", None))
        self.btnTestRes.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.btnTestMenu.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPALE", None))
        ___qtablewidgetitem44 = self.tblBox.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Gabbia", None));
        ___qtablewidgetitem45 = self.tblBox.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Pos. Sala", None));
        ___qtablewidgetitem46 = self.tblBox.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Pos. Gabbia", None));
        ___qtablewidgetitem47 = self.tblBox.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Pos. COM", None));
        ___qtablewidgetitem48 = self.tblBox.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Sit. COM", None));
        self.lblBox.setText(QCoreApplication.translate("MainWindow", u"Dati Gabbie", None))
        self.lblDataTotSow.setText(QCoreApplication.translate("MainWindow", u"Totale Scrofe", None))
        self.lblDataFreeSow.setText(QCoreApplication.translate("MainWindow", u"Non Assegnate", None))
        self.lblSow.setText(QCoreApplication.translate("MainWindow", u"Dati Scrofe", None))
        self.btnDataRemBox.setText(QCoreApplication.translate("MainWindow", u"Rimuovi Gabbia", None))
        self.btnDataSaveCom.setText(QCoreApplication.translate("MainWindow", u"Associa Pos. COM", None))
        self.btnDataTestCom.setText(QCoreApplication.translate("MainWindow", u"Test COM", None))
        self.btnDataRemSow.setText(QCoreApplication.translate("MainWindow", u"Rimuovi Scrofa", None))
        ___qtablewidgetitem49 = self.tblSow.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Nome Scrofa", None));
        ___qtablewidgetitem50 = self.tblSow.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"In Gestione", None));
        self.lblDataFreeBox.setText(QCoreApplication.translate("MainWindow", u"Non Assegnate", None))
        self.lblDataTotBox.setText(QCoreApplication.translate("MainWindow", u"Totale Gabbie", None))
        self.lblDataStatus.setText("")
        self.btnDataSowAdd.setText(QCoreApplication.translate("MainWindow", u"Inserisci Scrofe", None))
        self.lblDataSow.setText(QCoreApplication.translate("MainWindow", u"Aggiungi Scrofe", None))
        self.lblDataSowName.setText(QCoreApplication.translate("MainWindow", u"Inserisci Nome Scrofa", None))
        self.lblDataBoxAdd.setText(QCoreApplication.translate("MainWindow", u"Aggiungi Gabbie", None))
        self.lblDataNrBoxAdd.setText(QCoreApplication.translate("MainWindow", u"Numero di Gabbie da inserire", None))
        self.lblDataNrHallAdd.setText(QCoreApplication.translate("MainWindow", u"Numero Sala in cui inserire", None))
        self.btnDataBoxAdd.setText(QCoreApplication.translate("MainWindow", u"Inserisci Gabbie", None))
        self.btnDataUpd.setText(QCoreApplication.translate("MainWindow", u"AGGIORNA DATI", None))
        self.btnDataAdd.setText(QCoreApplication.translate("MainWindow", u"AGGIUNGI DATI", None))
        self.btnDataRem.setText(QCoreApplication.translate("MainWindow", u"RIMUOVI DATI", None))
        self.btnDataMen.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPALE", None))
        self.lblAdd.setText(QCoreApplication.translate("MainWindow", u"Aggiungi Scrofa in Gabbia", None))
        self.lblAddSelBox.setText(QCoreApplication.translate("MainWindow", u"Seleziona Gabbia", None))
        self.lblAddSelSow.setText(QCoreApplication.translate("MainWindow", u"Seleziona Scrofa", None))
        self.lblAddSelCur.setText(QCoreApplication.translate("MainWindow", u"Seleziona Curva", None))
        self.lblAddSelEntryDate.setText(QCoreApplication.translate("MainWindow", u"Data Entrata", None))
        self.spiAddSelEntryDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yy", None))
        self.lblAddSelCurDate.setText(QCoreApplication.translate("MainWindow", u"Giorno in Curva", None))
        self.lblAddCurType.setText(QCoreApplication.translate("MainWindow", u"TIpo Curva", None))
        self.txtAddCurType.setText(QCoreApplication.translate("MainWindow", u"Gestazione", None))
        self.lblAddStatus.setText("")
        self.lblAddBirth.setText(QCoreApplication.translate("MainWindow", u"Parto Avvenuto", None))
        self.radAddBirthY.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.radAddBirthN.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.lblAddSelPigDate.setText(QCoreApplication.translate("MainWindow", u"Data Parto", None))
        self.spiAddSelPigDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yy", None))
        self.lblAddSelPigBirth.setText(QCoreApplication.translate("MainWindow", u"Suini Nati", None))
        self.lblAddSelPigRealBirth.setText(QCoreApplication.translate("MainWindow", u"Suini Nati Vivi", None))
        self.lblAddSelPigWeight.setText(QCoreApplication.translate("MainWindow", u"Peso Totale", None))
        self.lblAddNotes.setText(QCoreApplication.translate("MainWindow", u"Note Aggiuntive", None))
        self.btnAddUpd.setText(QCoreApplication.translate("MainWindow", u"AGGIORNA DATI", None))
        self.btnAddAdd.setText(QCoreApplication.translate("MainWindow", u"INSERISCI DATI IN GABBIA", None))
        self.btnAddRes.setText(QCoreApplication.translate("MainWindow", u"INSERISCI PARTO", None))
        self.btnAddMen.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPALE", None))
        self.lblSettings.setText(QCoreApplication.translate("MainWindow", u"Impostazione Software", None))
        self.lblSetMaxHall_3.setText(QCoreApplication.translate("MainWindow", u"A Box", None))
        self.spiSetModCur.setSuffix("")
        self.lblSetMaxHall_2.setText(QCoreApplication.translate("MainWindow", u"Da Box", None))
        self.btnSetConfFarm.setText(QCoreApplication.translate("MainWindow", u"Salva Parametri Generali", None))
        self.lblSetConfCard_2.setText(QCoreApplication.translate("MainWindow", u"Configurazioni Impianto di Gruppo", None))
        self.radSetModEntryDate.setText(QCoreApplication.translate("MainWindow", u"Data Entrata", None))
        self.lblSetMaxCur_2.setText(QCoreApplication.translate("MainWindow", u"Sala nr.", None))
        self.radSetModCur.setText(QCoreApplication.translate("MainWindow", u"Curva", None))
        self.radSetModSit.setText(QCoreApplication.translate("MainWindow", u"Situazione", None))
        self.comSetModSit.setItemText(0, QCoreApplication.translate("MainWindow", u"Gestazione", None))
        self.comSetModSit.setItemText(1, QCoreApplication.translate("MainWindow", u"Parto", None))

        self.btnSetConfGen.setText(QCoreApplication.translate("MainWindow", u"Salva Parametri Generali", None))
        self.lblSetConfGen.setText(QCoreApplication.translate("MainWindow", u"Configurazioni Catenaria", None))
        self.lblSetMaxCur.setText(QCoreApplication.translate("MainWindow", u"Indirizzo Catenaria", None))
        self.lblSetMaxHall.setText(QCoreApplication.translate("MainWindow", u"Funzionamento", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"/dev/ttyUSB1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"/dev/ttyUSB0", None))

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Attivo", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Non Attivo", None))
        self.comSetComPort.setItemText(0, QCoreApplication.translate("MainWindow", u"/dev/ttyUSB0", None))
        self.comSetComPort.setItemText(1, QCoreApplication.translate("MainWindow", u"/dev/ttyUSB1", None))

        self.lblSetComPort.setText(QCoreApplication.translate("MainWindow", u"Porta COM", None))
        self.btnSetConfImp.setText(QCoreApplication.translate("MainWindow", u"Imposta Durata Impulso", None))
        self.lblSetComCal.setText(QCoreApplication.translate("MainWindow", u"Calibrazione", None))
        self.lblSetComImp.setText(QCoreApplication.translate("MainWindow", u"Durata Impulso", None))
        self.lblSetComBaud.setText(QCoreApplication.translate("MainWindow", u"Baud Rate", None))
        self.btnSetConfCalib.setText(QCoreApplication.translate("MainWindow", u"Imposta Calibrazione", None))
        self.lblSetConfCard.setText(QCoreApplication.translate("MainWindow", u"Configurazione Schede", None))
        self.comSetComBaud.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comSetComBaud.setItemText(1, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comSetComBaud.setItemText(2, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comSetComBaud.setItemText(3, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comSetComBaud.setItemText(4, QCoreApplication.translate("MainWindow", u"115200", None))

        self.comSetComBaud.setCurrentText(QCoreApplication.translate("MainWindow", u"9600", None))
        self.btnSetConfCom.setText(QCoreApplication.translate("MainWindow", u"Imposta Porta COM", None))
        self.btnSetConfBaud.setText(QCoreApplication.translate("MainWindow", u"Imposta Baud Rate", None))
    # retranslateUi

