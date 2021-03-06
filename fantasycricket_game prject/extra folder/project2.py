# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(996, 742)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.your_selection = QtWidgets.QGraphicsView(self.centralwidget)
        self.your_selection.setGeometry(QtCore.QRect(120, 10, 721, 121))
        self.your_selection.setObjectName("your_selection")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BAT = QtWidgets.QLabel(self.centralwidget)
        self.BAT.setGeometry(QtCore.QRect(150, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BAT.setFont(font)
        self.BAT.setObjectName("BAT")
        self.BOW = QtWidgets.QLabel(self.centralwidget)
        self.BOW.setGeometry(QtCore.QRect(300, 90, 81, 21))
        self.BOW.setObjectName("BOW")
        self.AR = QtWidgets.QLabel(self.centralwidget)
        self.AR.setGeometry(QtCore.QRect(450, 90, 91, 21))
        self.AR.setObjectName("AR")
        self.WK = QtWidgets.QLabel(self.centralwidget)
        self.WK.setGeometry(QtCore.QRect(630, 90, 121, 21))
        self.WK.setObjectName("WK")
        self.bow_number = QtWidgets.QLineEdit(self.centralwidget)
        self.bow_number.setGeometry(QtCore.QRect(380, 90, 31, 22))
        self.bow_number.setObjectName("bow_number")
        self.AR_number = QtWidgets.QLineEdit(self.centralwidget)
        self.AR_number.setGeometry(QtCore.QRect(540, 90, 31, 22))
        self.AR_number.setObjectName("AR_number")
        self.WK_number = QtWidgets.QLineEdit(self.centralwidget)
        self.WK_number.setGeometry(QtCore.QRect(750, 90, 31, 22))
        self.WK_number.setObjectName("WK_number")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 101, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 160, 81, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 160, 81, 22))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(1000)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 160, 81, 22))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Bat_number = QtWidgets.QLineEdit(self.centralwidget)
        self.Bat_number.setGeometry(QtCore.QRect(240, 90, 31, 22))
        self.Bat_number.setObjectName("Bat_number")
        self.radioButton_BOW = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_BOW.setEnabled(False)
        self.radioButton_BOW.setGeometry(QtCore.QRect(170, 200, 61, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.radioButton_BOW.setFont(font)
        self.radioButton_BOW.setObjectName("radioButton_BOW")
        self.radioButton_AR = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_AR.setEnabled(False)
        self.radioButton_AR.setGeometry(QtCore.QRect(240, 200, 51, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.radioButton_AR.setFont(font)
        self.radioButton_AR.setObjectName("radioButton_AR")
        self.radioButton_WK = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_WK.setEnabled(False)
        self.radioButton_WK.setGeometry(QtCore.QRect(310, 200, 51, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.radioButton_WK.setFont(font)
        self.radioButton_WK.setObjectName("radioButton_WK")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 200, 91, 16))
        self.label_4.setObjectName("label_4")
        self.team_name = QtWidgets.QLineEdit(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(640, 200, 201, 22))
        font = QtGui.QFont()
        font.setItalic(True)
        self.team_name.setFont(font)
        self.team_name.setObjectName("team_name")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 240, 111, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radioButton_BAT = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_BAT.setEnabled(False)
        self.radioButton_BAT.setGeometry(QtCore.QRect(90, 200, 51, 26))
        font = QtGui.QFont()
        font.setItalic(True)
        self.radioButton_BAT.setFont(font)
        self.radioButton_BAT.setObjectName("radioButton_BAT")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 111, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 260, 741, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.availableplayer_lw = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.availableplayer_lw.setObjectName("availableplayer_lw")
        self.horizontalLayout.addWidget(self.availableplayer_lw)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.slectedplayer_lw = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.slectedplayer_lw.setObjectName("slectedplayer_lw")
        self.horizontalLayout.addWidget(self.slectedplayer_lw)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_teams.setObjectName("menuManage_teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.NEW_Teanm = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.NEW_Teanm.setFont(font)
        self.NEW_Teanm.setShortcutVisibleInContextMenu(True)
        self.NEW_Teanm.setObjectName("NEW_Teanm")
        self.OPEN_Team = QtWidgets.QAction(MainWindow)
        self.OPEN_Team.setObjectName("OPEN_Team")
        self.SAVE_Team = QtWidgets.QAction(MainWindow)
        self.SAVE_Team.setShortcutVisibleInContextMenu(True)
        self.SAVE_Team.setObjectName("SAVE_Team")
        self.EVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.EVALUATE_Team.setVisible(True)
        self.EVALUATE_Team.setObjectName("EVALUATE_Team")
        self.Quit = QtWidgets.QAction(MainWindow)
        self.Quit.setObjectName("Quit")
        self.menuManage_teams.addAction(self.NEW_Teanm)
        self.menuManage_teams.addAction(self.OPEN_Team)
        self.menuManage_teams.addAction(self.SAVE_Team)
        self.menuManage_teams.addAction(self.EVALUATE_Team)
        self.menuManage_teams.addAction(self.Quit)
        self.menubar.addAction(self.menuManage_teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your selection"))
        self.BAT.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.BOW.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.AR.setText(_translate("MainWindow", "Allrounder(AR)"))
        self.WK.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.bow_number.setText(_translate("MainWindow", "00"))
        self.AR_number.setText(_translate("MainWindow", "00"))
        self.WK_number.setText(_translate("MainWindow", "00"))
        self.label_2.setText(_translate("MainWindow", "Points Available"))
        self.label_3.setText(_translate("MainWindow", "Points Used"))
        self.lineEdit.setText(_translate("MainWindow", "00"))
        self.lineEdit_2.setText(_translate("MainWindow", "00"))
        self.Bat_number.setText(_translate("MainWindow", "00"))
        self.radioButton_BOW.setText(_translate("MainWindow", "BOW"))
        self.radioButton_AR.setText(_translate("MainWindow", "AR"))
        self.radioButton_WK.setText(_translate("MainWindow", "WK"))
        self.label_4.setText(_translate("MainWindow", "TEAM NAME"))
        self.label_6.setText(_translate("MainWindow", "Selected Players"))
        self.radioButton_BAT.setText(_translate("MainWindow", "BAT"))
        self.label_5.setText(_translate("MainWindow", "Available Players"))
        self.label_7.setText(_translate("MainWindow", "     >>      "))
        self.menuManage_teams.setTitle(_translate("MainWindow", "Manage teams"))
        self.NEW_Teanm.setText(_translate("MainWindow", "NEW Team"))
        self.NEW_Teanm.setStatusTip(_translate("MainWindow", "enter your team name"))
        self.NEW_Teanm.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.OPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.OPEN_Team.setStatusTip(_translate("MainWindow", "opening team"))
        self.OPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.SAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.SAVE_Team.setStatusTip(_translate("MainWindow", "saving team"))
        self.SAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.EVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.Quit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
