# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(250, 250))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Intel = QtWidgets.QWidget()
        self.Intel.setObjectName("Intel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Intel)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchFrame = QtWidgets.QFrame(self.Intel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFrame.sizePolicy().hasHeightForWidth())
        self.searchFrame.setSizePolicy(sizePolicy)
        self.searchFrame.setMaximumSize(QtCore.QSize(5000, 5000))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.charSearch = QtWidgets.QLineEdit(self.searchFrame)
        self.charSearch.setObjectName("charSearch")
        self.horizontalLayout.addWidget(self.charSearch)
        self.searchBtn = QtWidgets.QPushButton(self.searchFrame)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lcdNumber = QtWidgets.QLCDNumber(self.searchFrame)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout_2.addWidget(self.searchFrame)
        self.frame_2 = QtWidgets.QFrame(self.Intel)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.charDetail = QtWidgets.QToolBox(self.frame_2)
        self.charDetail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.charDetail.setFrameShadow(QtWidgets.QFrame.Plain)
        self.charDetail.setObjectName("charDetail")
        self.summary = QtWidgets.QWidget()
        self.summary.setGeometry(QtCore.QRect(0, 0, 447, 413))
        self.summary.setObjectName("summary")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.summary)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.summary)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.charName = QtWidgets.QLabel(self.tab)
        self.charName.setObjectName("charName")
        self.verticalLayout_11.addWidget(self.charName)
        self.corpName = QtWidgets.QLabel(self.tab)
        self.corpName.setObjectName("corpName")
        self.verticalLayout_11.addWidget(self.corpName)
        self.corpMembers = QtWidgets.QLabel(self.tab)
        self.corpMembers.setObjectName("corpMembers")
        self.verticalLayout_11.addWidget(self.corpMembers)
        self.secStatus = QtWidgets.QLabel(self.tab)
        self.secStatus.setObjectName("secStatus")
        self.verticalLayout_11.addWidget(self.secStatus)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 403, 69))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.charBio = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.charBio.setWordWrap(True)
        self.charBio.setObjectName("charBio")
        self.verticalLayout_9.addWidget(self.charBio)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.addWidget(self.scrollArea_2)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget_2)
        self.charDetail.addItem(self.summary, "")
        self.charInfo = QtWidgets.QWidget()
        self.charInfo.setGeometry(QtCore.QRect(0, 0, 447, 413))
        self.charInfo.setObjectName("charInfo")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.charInfo)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.charInfo)
        self.tabWidget_3.setStyleSheet("/*QTabBar::tab {\n"
"    min-width: 21ex;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; \n"
"}\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; \n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; \n"
"}*/")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 128))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.corpLogo = QtWidgets.QLabel(self.frame)
        self.corpLogo.setMaximumSize(QtCore.QSize(128, 128))
        self.corpLogo.setText("")
        self.corpLogo.setScaledContents(True)
        self.corpLogo.setObjectName("corpLogo")
        self.horizontalLayout_2.addWidget(self.corpLogo)
        self.charLogo = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.charLogo.sizePolicy().hasHeightForWidth())
        self.charLogo.setSizePolicy(sizePolicy)
        self.charLogo.setMaximumSize(QtCore.QSize(128, 128))
        self.charLogo.setText("")
        self.charLogo.setScaledContents(True)
        self.charLogo.setObjectName("charLogo")
        self.horizontalLayout_2.addWidget(self.charLogo)
        self.allianceLogo = QtWidgets.QLabel(self.frame)
        self.allianceLogo.setMaximumSize(QtCore.QSize(128, 128))
        self.allianceLogo.setText("")
        self.allianceLogo.setScaledContents(True)
        self.allianceLogo.setObjectName("allianceLogo")
        self.horizontalLayout_2.addWidget(self.allianceLogo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_12.addWidget(self.frame)
        self.charName_2 = QtWidgets.QLabel(self.tab_3)
        self.charName_2.setObjectName("charName_2")
        self.verticalLayout_12.addWidget(self.charName_2)
        self.secStatus_2 = QtWidgets.QLabel(self.tab_3)
        self.secStatus_2.setWordWrap(False)
        self.secStatus_2.setObjectName("secStatus_2")
        self.verticalLayout_12.addWidget(self.secStatus_2)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 403, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.charBio_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.charBio_2.setWordWrap(True)
        self.charBio_2.setObjectName("charBio_2")
        self.verticalLayout_8.addWidget(self.charBio_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_12.addWidget(self.scrollArea)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setMaximumSize(QtCore.QSize(302, 167))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(77)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout_13.addWidget(self.tableWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.snuggly = QtWidgets.QProgressBar(self.groupBox_2)
        self.snuggly.setAutoFillBackground(False)
        self.snuggly.setStyleSheet("QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: #00a005;\n"
"    font: bold;\n"
"}\n"
"QProgressBar::chunk{ \n"
"    background-color: #750000;\n"
"}\n"
"")
        self.snuggly.setProperty("value", 50)
        self.snuggly.setTextVisible(True)
        self.snuggly.setOrientation(QtCore.Qt.Horizontal)
        self.snuggly.setInvertedAppearance(False)
        self.snuggly.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.snuggly.setObjectName("snuggly")
        self.verticalLayout_14.addWidget(self.snuggly)
        self.verticalLayout_13.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_15.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.solo = QtWidgets.QProgressBar(self.groupBox)
        self.solo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.solo.setAutoFillBackground(False)
        self.solo.setStyleSheet("QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: #00a005;\n"
"    font: bold;\n"
"}\n"
"QProgressBar::chunk{ \n"
"    background-color: #750000;\n"
"}\n"
"")
        self.solo.setProperty("value", 50)
        self.solo.setTextVisible(True)
        self.solo.setObjectName("solo")
        self.verticalLayout_15.addWidget(self.solo)
        self.verticalLayout_13.addWidget(self.groupBox)
        self.verticalLayout_16.addWidget(self.frame_4)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget_3)
        self.charDetail.addItem(self.charInfo, "")
        self.corpInfo = QtWidgets.QWidget()
        self.corpInfo.setGeometry(QtCore.QRect(0, 0, 447, 413))
        self.corpInfo.setObjectName("corpInfo")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.corpInfo)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.corpInfo)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 128))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.corpLogo_2 = QtWidgets.QLabel(self.frame_3)
        self.corpLogo_2.setMaximumSize(QtCore.QSize(128, 128))
        self.corpLogo_2.setText("")
        self.corpLogo_2.setScaledContents(True)
        self.corpLogo_2.setWordWrap(False)
        self.corpLogo_2.setObjectName("corpLogo_2")
        self.horizontalLayout_3.addWidget(self.corpLogo_2)
        self.allianceLogo_2 = QtWidgets.QLabel(self.frame_3)
        self.allianceLogo_2.setMaximumSize(QtCore.QSize(128, 128))
        self.allianceLogo_2.setText("")
        self.allianceLogo_2.setScaledContents(True)
        self.allianceLogo_2.setWordWrap(False)
        self.allianceLogo_2.setObjectName("allianceLogo_2")
        self.horizontalLayout_3.addWidget(self.allianceLogo_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.corpName_2 = QtWidgets.QLabel(self.corpInfo)
        self.corpName_2.setWordWrap(True)
        self.corpName_2.setObjectName("corpName_2")
        self.verticalLayout_7.addWidget(self.corpName_2)
        self.alliance = QtWidgets.QLabel(self.corpInfo)
        self.alliance.setText("")
        self.alliance.setWordWrap(True)
        self.alliance.setObjectName("alliance")
        self.verticalLayout_7.addWidget(self.alliance)
        self.corpMembers_2 = QtWidgets.QLabel(self.corpInfo)
        self.corpMembers_2.setWordWrap(True)
        self.corpMembers_2.setObjectName("corpMembers_2")
        self.verticalLayout_7.addWidget(self.corpMembers_2)
        self.corpCeo = QtWidgets.QLabel(self.corpInfo)
        self.corpCeo.setWordWrap(True)
        self.corpCeo.setObjectName("corpCeo")
        self.verticalLayout_7.addWidget(self.corpCeo)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.corpInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scrollArea_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 425, 69))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.corpDescription = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.corpDescription.setText("")
        self.corpDescription.setWordWrap(True)
        self.corpDescription.setObjectName("corpDescription")
        self.verticalLayout_10.addWidget(self.corpDescription)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.addWidget(self.scrollArea_3)
        self.charDetail.addItem(self.corpInfo, "")
        self.verticalLayout_4.addWidget(self.charDetail)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.tabWidget.addTab(self.Intel, "")
        self.Notes = QtWidgets.QWidget()
        self.Notes.setObjectName("Notes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Notes)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.noteTaker = QtWidgets.QPlainTextEdit(self.Notes)
        self.noteTaker.setFrameShadow(QtWidgets.QFrame.Raised)
        self.noteTaker.setObjectName("noteTaker")
        self.verticalLayout_3.addWidget(self.noteTaker)
        self.tabWidget.addTab(self.Notes, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setEnabled(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSupport = QtWidgets.QAction(MainWindow)
        self.actionSupport.setEnabled(True)
        self.actionSupport.setObjectName("actionSupport")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setEnabled(False)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.action_Bug_Report = QtWidgets.QAction(MainWindow)
        self.action_Bug_Report.setEnabled(False)
        self.action_Bug_Report.setObjectName("action_Bug_Report")
        self.menuHelp.addAction(self.actionSupport)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menuHelp.addAction(self.action_Bug_Report)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.charDetail.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eve Intel Tool"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.charName.setText(_translate("MainWindow", "Name: "))
        self.corpName.setText(_translate("MainWindow", "Corporation Name: "))
        self.corpMembers.setText(_translate("MainWindow", "Corporation Members: "))
        self.secStatus.setText(_translate("MainWindow", "Security Status: "))
        self.charBio.setText(_translate("MainWindow", "Bio: "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Summary"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Links"))
        self.charDetail.setItemText(self.charDetail.indexOf(self.summary), _translate("MainWindow", "Summary"))
        self.charName_2.setText(_translate("MainWindow", "Name: "))
        self.secStatus_2.setText(_translate("MainWindow", "Security Status: "))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Info"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ships"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Isk"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last 7 Days"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "This Month"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Destroyed"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lost"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Efficiency"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("MainWindow", "Dangerous"))
        self.groupBox.setTitle(_translate("MainWindow", "Gangs"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Killboard"))
        self.charDetail.setItemText(self.charDetail.indexOf(self.charInfo), _translate("MainWindow", "Character Information"))
        self.corpName_2.setText(_translate("MainWindow", "Corporation Name: "))
        self.corpMembers_2.setText(_translate("MainWindow", "Member Count: "))
        self.corpCeo.setText(_translate("MainWindow", "CEO: "))
        self.charDetail.setItemText(self.charDetail.indexOf(self.corpInfo), _translate("MainWindow", "Corporation Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Intel), _translate("MainWindow", "Intel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Notes), _translate("MainWindow", "Notes"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "&Save.."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "&Open.."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSupport.setText(_translate("MainWindow", "&Support"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "&Check for Updates"))
        self.action_Bug_Report.setText(_translate("MainWindow", "&Bug Report"))

