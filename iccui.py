from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pyttsx3
from ICC_ALL_ROUNDER_RANK import ALLR
from ICC_BOWL_RANK import BOWL
from ICC_BAT_RANKS import BAT

ALLR("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder")
BOWL("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
BAT("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
# remove comment from the above three functions only if you dont have the ICC_ODI_RANKING.db file in the same folder

engine = pyttsx3.init()  # Initialize Python Text To Speech module


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("ICC Rank Holder Display App")
        Form.resize(534, 397)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.ListBox = QtWidgets.QComboBox(Form)
        self.ListBox.setObjectName("ListBox")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.ListBox.addItem("")
        self.gridLayout.addWidget(self.ListBox, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.GetRank = QtWidgets.QPushButton(Form)
        self.GetRank.setObjectName("GetRank")
        self.horizontalLayout.addWidget(self.GetRank)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/luhar/Downloads/download.jpg"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.Rank = QtWidgets.QLineEdit(Form)
        self.Rank.setObjectName("Rank")
        self.gridLayout.addWidget(self.Rank, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.Result = QtWidgets.QLineEdit(Form)
        self.Result.setObjectName("Result")
        self.gridLayout.addWidget(self.Result, 6, 0, 1, 2)
        self.GetRank.clicked.connect(lambda: self.GetResult())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Select Genre:</span></p></body></html>"))
        self.ListBox.setItemText(0, _translate("Form", "ODI Batting "))
        self.ListBox.setItemText(1, _translate("Form", "ODI Bowling"))
        self.ListBox.setItemText(2, _translate("Form", "ODI All-Rounder"))
        self.GetRank.setText(_translate("Form", "Get Rank"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter Rank:</span></p></body></html>"))
        self.label_5.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Please note that ICC Ranks All-Rounder genre from 1 to 20 only, rest are upto 100.</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Welcome to ICC Rank Display</span></p></body></html>"))

    def GetResult(self):
        list_select = self.ListBox.currentIndex()
        rank = self.Rank.text()
        ICC_ODI_RANKING = sqlite3.connect('ICC_ODI_RANKING.db')
        curICC_ODI_RANKING = ICC_ODI_RANKING.cursor()

        # for batting ranks
        if list_select == 0:
            if int(rank) > 100:
                self.Result.setText("Batting ranks are only upto 20. Please select a different rank")
                engine.say("Batting ranks are only upto 20. Please select a different rank")
                engine.runAndWait()
            else:
                curICC_ODI_RANKING.execute("SELECT * from ICC_ODI_RANKING_BAT WHERE RANK ='" + rank + "';")
                record = list(curICC_ODI_RANKING.fetchone())
                self.Result.setText(
                    "Name: " + record[1] + " || Team: " + record[2] + " || Ratings: " + record[3] + "|| Career Best: " +
                    record[4])
                engine.say(
                    "Name: " + record[1] + " . Team: " + record[2] + " . Ratings: " + record[3] + ". Career Best: " +
                    record[4])
                engine.runAndWait()
        # for bowling ranks
        elif list_select == 1:
            if int(rank) > 100:
                self.Result.setText("Bowling ranks are only upto 100. Please select a different rank")
                engine.say("Bowling ranks are only upto 20. Please select a different rank")
                engine.runAndWait()
            else:
                curICC_ODI_RANKING.execute("SELECT * from ICC_ODI_RANKING_BOWL WHERE RANK ='" + rank + "';")
                record = list(curICC_ODI_RANKING.fetchone())
                self.Result.setText(
                    "Name: " + record[1] + " || Team: " + record[2] + " || Ratings: " + record[3] + "|| Career Best: " +
                    record[4])
                engine.say(
                    "Name: " + record[1] + " . Team: " + record[2] + " . Ratings: " + record[3] + ". Career Best: " +
                    record[4])
                engine.runAndWait()
        # for all-rounder ranks
        elif list_select == 2:
            if int(rank) > 20:
                self.Result.setText("All Rounder ranks are only upto 20. Please select a different rank")
                engine.say("All Rounder ranks are only upto 20. Please select a different rank")
                engine.runAndWait()
            else:
                curICC_ODI_RANKING.execute("SELECT * from ICC_ODI_RANKING_ALL_R WHERE RANK ='" + rank + "';")
                record = list(curICC_ODI_RANKING.fetchone())
                self.Result.setText(
                    "Name: " + record[1] + " || Team: " + record[2] + " || Ratings: " + record[3] + "|| Career Best: " +
                    record[4])
                engine.say(
                    "Name: " + record[1] + " . Team: " + record[2] + " . Ratings: " + record[3] + ". Career Best: " +
                    record[4])
                engine.runAndWait()


# check if __name__ == __main__ and only the execute the app
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
