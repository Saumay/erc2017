# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sp10.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
import PySide
import datetime



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main_Window(QtGui.QDialog, QtGui.QMainWindow):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName(_fromUtf8("Main_Window"))
        Main_Window.resize(703, 510)
        Main_Window.move(380,100)

        """global silver  # seat count of each class per booking
        global gold
        global plt

        silver = 0
        gold = 0
        plt = 0"""

        self.silver=0
        self.gold = 0
        self.plt = 0
        #self.hour = 13


        self.now = datetime.datetime.now()
        self.centralwidget = QtGui.QWidget(Main_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.TabWidget = QtGui.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 711, 481))
        self.TabWidget.setStyleSheet(_fromUtf8(""))
        self.TabWidget.setObjectName(_fromUtf8("TabWidget"))
        self.Home = QtGui.QWidget()
        self.Home.setObjectName(_fromUtf8("Home"))
        self.Label_background_0 = QtGui.QLabel(self.Home)
        self.Label_background_0.setGeometry(QtCore.QRect(0, -10, 701, 901))
        self.Label_background_0.setText(_fromUtf8(""))
        self.Label_background_0.setPixmap(QtGui.QPixmap(_fromUtf8("Home2.png")))
        self.Label_background_0.setObjectName(_fromUtf8("Label_background_0"))
        self.Cancel_0 = QtGui.QPushButton(self.Home)
        self.Cancel_0.setGeometry(QtCore.QRect(590, 396, 99, 31))
        self.Cancel_0.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color: #555555;\n"
"    color: white;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"font-size:15px;\n"
"}\n"
""))
        self.Cancel_0.setDefault(True)
        self.Cancel_0.setObjectName(_fromUtf8("Cancel_0"))
        self.Label2_0 = QtGui.QLabel(self.Home)
        self.Label2_0.setGeometry(QtCore.QRect(370, 190, 291, 51))
        self.Label2_0.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-family:Calibri;\n"
"}"))
        self.Label2_0.setObjectName(_fromUtf8("Label2_0"))
        self.radio1_0 = QtGui.QRadioButton(self.Home)
        self.radio1_0.setGeometry(QtCore.QRect(380, 250, 181, 41))
        self.radio1_0.setStyleSheet(_fromUtf8("QRadioButton\n"
"{\n"
"font-size:25px;\n"
"}\n"
""))
        self.radio1_0.setObjectName(_fromUtf8("radio1_0"))
        self.OK_0 = QtGui.QPushButton(self.Home)
        self.OK_0.setGeometry(QtCore.QRect(490, 396, 99, 31))
        self.OK_0.setStyleSheet(_fromUtf8("QPushButton\n"
"{ background-color: white;\n"
"    color: black;\n"
"    border-radius:4px;\n"
"border: 2px solid #e7e7e7;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: #e7e7e7;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"font-size:15px;\n"
"}"))
        self.OK_0.setObjectName(_fromUtf8("OK_0"))
        self.Label1_0 = QtGui.QLabel(self.Home)
        self.Label1_0.setGeometry(QtCore.QRect(60, 310, 300, 51))
        self.Label1_0.setStyleSheet(_fromUtf8("QLineEdit:hover\n"
"{\n"
"font-size:40px;\n"
"}"))
        self.Label1_0.setObjectName(_fromUtf8("Label1_0"))
        self.setCurrentMovie()

        self.radio2_0 = QtGui.QRadioButton(self.Home)
        self.radio2_0.setGeometry(QtCore.QRect(380, 280, 281, 61))
        self.radio2_0.setStyleSheet(_fromUtf8("QRadioButton\n"
"{\n"
"font-size:25px;\n"
"}\n"
""))
        self.radio2_0.setObjectName(_fromUtf8("radio2_0"))
        self.line_5 = QtGui.QFrame(self.Home)
        self.line_5.setGeometry(QtCore.QRect(10, 300, 331, 16))
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setLineWidth(4)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.Home)
        self.line_6.setGeometry(QtCore.QRect(10, 360, 331, 16))
        self.line_6.setStyleSheet(_fromUtf8("QFrame HLine\n"
"{\n"
"color:black;\n"
"}"))
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setLineWidth(4)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.TabWidget.addTab(self.Home, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.Label_background_1 = QtGui.QLabel(self.tab_2)
        self.Label_background_1.setGeometry(QtCore.QRect(0, 0, 711, 451))
        self.Label_background_1.setStyleSheet(_fromUtf8(""))
        self.Label_background_1.setText(_fromUtf8(""))
        self.Label_background_1.setPixmap(QtGui.QPixmap(_fromUtf8("theatre_blur3.jpeg")))
        self.Label_background_1.setObjectName(_fromUtf8("Label_background_1"))
        self.radio1_1 = QtGui.QRadioButton(self.tab_2)
        self.radio1_1.setGeometry(QtCore.QRect(170, 110, 351, 21))
        self.radio1_1.setStyleSheet(_fromUtf8("QRadioButton\n"
                                              "{\n"
                                              "font-size:18px;\n"
                                              "}"))
        self.radio1_1.setObjectName(_fromUtf8("radio1_1"))
        self.radio2_1 = QtGui.QRadioButton(self.tab_2)
        self.radio2_1.setGeometry(QtCore.QRect(170, 150, 351, 21))
        self.radio2_1.setStyleSheet(_fromUtf8("QRadioButton\n"
"{\n"
"font-size:18px;\n"
"}"))
        self.radio2_1.setObjectName(_fromUtf8("radio2_1"))
        self.radio4_1 = QtGui.QRadioButton(self.tab_2)
        self.radio4_1.setGeometry(QtCore.QRect(170, 230, 351, 21))
        self.radio4_1.setStyleSheet(_fromUtf8("QRadioButton\n"
"{\n"
"font-size:18px;\n"
"}"))
        self.radio4_1.setObjectName(_fromUtf8("radio4_1"))
        self.Label2_1 = QtGui.QLabel(self.tab_2)
        self.Label2_1.setGeometry(QtCore.QRect(450, 70, 41, 21))
        self.Label2_1.setObjectName(_fromUtf8("Label2_1"))
        self.Label4_1 = QtGui.QLabel(self.tab_2)
        self.Label4_1.setGeometry(QtCore.QRect(20, 340, 461, 71))
        self.Label4_1.setObjectName(_fromUtf8("Label4_1"))

        self.Label3_1 = QtGui.QLabel(self.tab_2)
        self.Label3_1.setGeometry(QtCore.QRect(260, 270, 261, 51))
        self.Label3_1.setObjectName(_fromUtf8("Label3_1"))
        self.line_4 = QtGui.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(400, 60, 16, 201))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.Label1_1 = QtGui.QLabel(self.tab_2)
        self.Label1_1.setGeometry(QtCore.QRect(260, 70, 59, 21))
        self.Label1_1.setObjectName(_fromUtf8("Label1_1"))
        self.radio3_1 = QtGui.QRadioButton(self.tab_2)
        self.radio3_1.setGeometry(QtCore.QRect(170, 190, 351, 21))
        self.radio3_1.setStyleSheet(_fromUtf8("QRadioButton\n"
"{\n"
"font-size:18px;\n"
"}"))
        self.radio3_1.setObjectName(_fromUtf8("radio3_1"))
        self.OK_1 = QtGui.QPushButton(self.tab_2)
        self.OK_1.setGeometry(QtCore.QRect(490, 400, 99, 31))
        self.OK_1.setStyleSheet(_fromUtf8("QPushButton\n"
"{ background-color: white;\n"
"    color: black;\n"
"    border-radius:4px;\n"
"border: 2px solid #e7e7e7;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: #e7e7e7;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"font-size:15px;\n"
"}"))
        self.OK_1.setObjectName(_fromUtf8("OK_1"))
        self.Cancel_1 = QtGui.QPushButton(self.tab_2)
        self.Cancel_1.setGeometry(QtCore.QRect(590, 400, 99, 31))
        self.Cancel_1.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color: #555555;\n"
"    color: white;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"font-size:15px;\n"
"}\n"
""))
        self.Cancel_1.setDefault(True)
        self.Cancel_1.setObjectName(_fromUtf8("Cancel_1"))
        self.TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.Label_background_2 = QtGui.QLabel(self.tab_7)
        self.Label_background_2.setGeometry(QtCore.QRect(0, 0, 701, 451))
        self.Label_background_2.setText(_fromUtf8(""))
        self.Label_background_2.setPixmap(QtGui.QPixmap(_fromUtf8("seats_blur.jpeg")))
        self.Label_background_2.setObjectName(_fromUtf8("Label_background_2"))
        self.gold06 = QtGui.QPushButton(self.tab_7)
        self.gold06.setGeometry(QtCore.QRect(250, 150, 41, 41))
        self.gold06.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold06.setObjectName(_fromUtf8("gold06"))
        self.silver20 = QtGui.QPushButton(self.tab_7)
        self.silver20.setGeometry(QtCore.QRect(170, 230, 41, 41))
        self.silver20.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver20.setObjectName(_fromUtf8("silver20"))
        self.gold16 = QtGui.QPushButton(self.tab_7)
        self.gold16.setGeometry(QtCore.QRect(250, 230, 41, 41))
        self.gold16.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold16.setObjectName(_fromUtf8("gold16"))
        self.plt15 = QtGui.QPushButton(self.tab_7)
        self.plt15.setGeometry(QtCore.QRect(650, 190, 41, 41))
        self.plt15.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt15.setObjectName(_fromUtf8("plt15"))
        self.plt14 = QtGui.QPushButton(self.tab_7)
        self.plt14.setGeometry(QtCore.QRect(610, 190, 41, 41))
        self.plt14.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt14.setObjectName(_fromUtf8("plt14"))
        self.gold07 = QtGui.QPushButton(self.tab_7)
        self.gold07.setGeometry(QtCore.QRect(290, 150, 41, 41))
        self.gold07.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold07.setObjectName(_fromUtf8("gold07"))
        self.silver06 = QtGui.QPushButton(self.tab_7)
        self.silver06.setGeometry(QtCore.QRect(10, 150, 41, 41))
        self.silver06.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver06.setObjectName(_fromUtf8("silver06"))
        self.gold18 = QtGui.QPushButton(self.tab_7)
        self.gold18.setGeometry(QtCore.QRect(330, 230, 41, 41))
        self.gold18.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold18.setObjectName(_fromUtf8("gold18"))
        self.plt06 = QtGui.QPushButton(self.tab_7)
        self.plt06.setGeometry(QtCore.QRect(490, 150, 41, 41))
        self.plt06.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt06.setObjectName(_fromUtf8("plt06"))
        self.gold21 = QtGui.QPushButton(self.tab_7)
        self.gold21.setGeometry(QtCore.QRect(250, 270, 41, 41))
        self.gold21.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold21.setObjectName(_fromUtf8("gold21"))
        self.gold20 = QtGui.QPushButton(self.tab_7)
        self.gold20.setGeometry(QtCore.QRect(410, 230, 41, 41))
        self.gold20.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold20.setObjectName(_fromUtf8("gold20"))
        self.plt05 = QtGui.QPushButton(self.tab_7)
        self.plt05.setGeometry(QtCore.QRect(650, 110, 41, 41))
        self.plt05.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt05.setObjectName(_fromUtf8("plt05"))
        self.gold13 = QtGui.QPushButton(self.tab_7)
        self.gold13.setGeometry(QtCore.QRect(330, 190, 41, 41))
        self.gold13.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold13.setObjectName(_fromUtf8("gold13"))
        self.gold02 = QtGui.QPushButton(self.tab_7)
        self.gold02.setGeometry(QtCore.QRect(290, 110, 41, 41))
        self.gold02.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold02.setObjectName(_fromUtf8("gold02"))
        self.silver03 = QtGui.QPushButton(self.tab_7)
        self.silver03.setGeometry(QtCore.QRect(90, 110, 41, 41))
        self.silver03.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver03.setObjectName(_fromUtf8("silver03"))
        self.plt08 = QtGui.QPushButton(self.tab_7)
        self.plt08.setGeometry(QtCore.QRect(570, 150, 41, 41))
        self.plt08.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt08.setObjectName(_fromUtf8("plt08"))
        self.plt22 = QtGui.QPushButton(self.tab_7)
        self.plt22.setGeometry(QtCore.QRect(530, 270, 41, 41))
        self.plt22.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt22.setObjectName(_fromUtf8("plt22"))
        self.spinBox3_2 = QtGui.QSpinBox(self.tab_7)
        self.spinBox3_2.setGeometry(QtCore.QRect(570, 40, 61, 27))
        self.spinBox3_2.setMaximum(25)
        self.spinBox3_2.setObjectName(_fromUtf8("spinBox3_2"))
        self.gold10 = QtGui.QPushButton(self.tab_7)
        self.gold10.setGeometry(QtCore.QRect(410, 150, 41, 41))
        self.gold10.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold10.setObjectName(_fromUtf8("gold10"))
        self.label1_2 = QtGui.QLabel(self.tab_7)
        self.label1_2.setGeometry(QtCore.QRect(20, 340, 501, 91))
        self.label1_2.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label1_2.setObjectName(_fromUtf8("label1_2"))
        self.plt12 = QtGui.QPushButton(self.tab_7)
        self.plt12.setGeometry(QtCore.QRect(530, 190, 41, 41))
        self.plt12.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt12.setObjectName(_fromUtf8("plt12"))
        self.silver16 = QtGui.QPushButton(self.tab_7)
        self.silver16.setGeometry(QtCore.QRect(10, 230, 41, 41))
        self.silver16.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver16.setObjectName(_fromUtf8("silver16"))
        self.silver13 = QtGui.QPushButton(self.tab_7)
        self.silver13.setGeometry(QtCore.QRect(90, 190, 41, 41))
        self.silver13.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver13.setObjectName(_fromUtf8("silver13"))
        self.gold25 = QtGui.QPushButton(self.tab_7)
        self.gold25.setGeometry(QtCore.QRect(410, 270, 41, 41))
        self.gold25.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold25.setObjectName(_fromUtf8("gold25"))
        self.gold11 = QtGui.QPushButton(self.tab_7)
        self.gold11.setGeometry(QtCore.QRect(250, 190, 41, 41))
        self.gold11.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold11.setObjectName(_fromUtf8("gold11"))
        self.plt17 = QtGui.QPushButton(self.tab_7)
        self.plt17.setGeometry(QtCore.QRect(530, 230, 41, 41))
        self.plt17.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt17.setObjectName(_fromUtf8("plt17"))
        self.plt21 = QtGui.QPushButton(self.tab_7)
        self.plt21.setGeometry(QtCore.QRect(490, 270, 41, 41))
        self.plt21.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt21.setObjectName(_fromUtf8("plt21"))
        self.gold17 = QtGui.QPushButton(self.tab_7)
        self.gold17.setGeometry(QtCore.QRect(290, 230, 41, 41))
        self.gold17.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold17.setObjectName(_fromUtf8("gold17"))
        self.gold22 = QtGui.QPushButton(self.tab_7)
        self.gold22.setGeometry(QtCore.QRect(290, 270, 41, 41))
        self.gold22.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold22.setObjectName(_fromUtf8("gold22"))
        self.plt25 = QtGui.QPushButton(self.tab_7)
        self.plt25.setGeometry(QtCore.QRect(650, 270, 41, 41))
        self.plt25.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt25.setObjectName(_fromUtf8("plt25"))
        self.gold19 = QtGui.QPushButton(self.tab_7)
        self.gold19.setGeometry(QtCore.QRect(370, 230, 41, 41))
        self.gold19.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold19.setObjectName(_fromUtf8("gold19"))
        self.silver05 = QtGui.QPushButton(self.tab_7)
        self.silver05.setGeometry(QtCore.QRect(170, 110, 41, 41))
        self.silver05.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver05.setObjectName(_fromUtf8("silver05"))
        self.gold15 = QtGui.QPushButton(self.tab_7)
        self.gold15.setGeometry(QtCore.QRect(410, 190, 41, 41))
        self.gold15.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold15.setObjectName(_fromUtf8("gold15"))
        self.Cancel_2 = QtGui.QPushButton(self.tab_7)
        self.Cancel_2.setGeometry(QtCore.QRect(590, 400, 99, 31))
        self.Cancel_2.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color: #555555;\n"
"    color: white;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"font-size:15px;\n"
"}\n"
""))
        self.Cancel_2.setDefault(True)
        self.Cancel_2.setObjectName(_fromUtf8("Cancel_2"))
        self.gold09 = QtGui.QPushButton(self.tab_7)
        self.gold09.setGeometry(QtCore.QRect(370, 150, 41, 41))
        self.gold09.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold09.setObjectName(_fromUtf8("gold09"))
        self.silver12 = QtGui.QPushButton(self.tab_7)
        self.silver12.setGeometry(QtCore.QRect(50, 190, 41, 41))
        self.silver12.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver12.setObjectName(_fromUtf8("silver12"))
        self.gold03 = QtGui.QPushButton(self.tab_7)
        self.gold03.setGeometry(QtCore.QRect(330, 110, 41, 41))
        self.gold03.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold03.setObjectName(_fromUtf8("gold03"))
        self.plt01 = QtGui.QPushButton(self.tab_7)
        self.plt01.setGeometry(QtCore.QRect(490, 110, 41, 41))
        self.plt01.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt01.setObjectName(_fromUtf8("plt01"))
        self.gold24 = QtGui.QPushButton(self.tab_7)
        self.gold24.setGeometry(QtCore.QRect(370, 270, 41, 41))
        self.gold24.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold24.setObjectName(_fromUtf8("gold24"))
        self.gold23 = QtGui.QPushButton(self.tab_7)
        self.gold23.setGeometry(QtCore.QRect(330, 270, 41, 41))
        self.gold23.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold23.setObjectName(_fromUtf8("gold23"))
        self.gold05 = QtGui.QPushButton(self.tab_7)
        self.gold05.setGeometry(QtCore.QRect(410, 110, 41, 41))
        self.gold05.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold05.setObjectName(_fromUtf8("gold05"))
        self.silver01 = QtGui.QPushButton(self.tab_7)
        self.silver01.setGeometry(QtCore.QRect(10, 110, 41, 41))
        self.silver01.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver01.setObjectName(_fromUtf8("silver01"))
        self.silver10 = QtGui.QPushButton(self.tab_7)
        self.silver10.setGeometry(QtCore.QRect(170, 150, 41, 41))
        self.silver10.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver10.setObjectName(_fromUtf8("silver10"))
        self.line_2 = QtGui.QFrame(self.tab_7)
        self.line_2.setGeometry(QtCore.QRect(220, 0, 20, 311))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label2_2 = QtGui.QLabel(self.tab_7)
        self.label2_2.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.label2_2.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label2_2.setObjectName(_fromUtf8("label2_2"))
        self.plt20 = QtGui.QPushButton(self.tab_7)
        self.plt20.setGeometry(QtCore.QRect(650, 230, 41, 41))
        self.plt20.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt20.setObjectName(_fromUtf8("plt20"))
        self.silver15 = QtGui.QPushButton(self.tab_7)
        self.silver15.setGeometry(QtCore.QRect(170, 190, 41, 41))
        self.silver15.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver15.setObjectName(_fromUtf8("silver15"))
        self.silver22 = QtGui.QPushButton(self.tab_7)
        self.silver22.setGeometry(QtCore.QRect(50, 270, 41, 41))
        self.silver22.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver22.setObjectName(_fromUtf8("silver22"))
        self.gold12 = QtGui.QPushButton(self.tab_7)
        self.gold12.setGeometry(QtCore.QRect(290, 190, 41, 41))
        self.gold12.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold12.setObjectName(_fromUtf8("gold12"))
        self.silver09 = QtGui.QPushButton(self.tab_7)
        self.silver09.setGeometry(QtCore.QRect(130, 150, 41, 41))
        self.silver09.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver09.setObjectName(_fromUtf8("silver09"))
        self.silver11 = QtGui.QPushButton(self.tab_7)
        self.silver11.setGeometry(QtCore.QRect(10, 190, 41, 41))
        self.silver11.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver11.setObjectName(_fromUtf8("silver11"))
        self.plt02 = QtGui.QPushButton(self.tab_7)
        self.plt02.setGeometry(QtCore.QRect(530, 110, 41, 41))
        self.plt02.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt02.setObjectName(_fromUtf8("plt02"))
        self.gold01 = QtGui.QPushButton(self.tab_7)
        self.gold01.setGeometry(QtCore.QRect(250, 110, 41, 41))
        self.gold01.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold01.setObjectName(_fromUtf8("gold01"))
        self.plt03 = QtGui.QPushButton(self.tab_7)
        self.plt03.setGeometry(QtCore.QRect(570, 110, 41, 41))
        self.plt03.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt03.setObjectName(_fromUtf8("plt03"))
        self.silver21 = QtGui.QPushButton(self.tab_7)
        self.silver21.setGeometry(QtCore.QRect(10, 270, 41, 41))
        self.silver21.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver21.setObjectName(_fromUtf8("silver21"))
        self.silver18 = QtGui.QPushButton(self.tab_7)
        self.silver18.setGeometry(QtCore.QRect(90, 230, 41, 41))
        self.silver18.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver18.setObjectName(_fromUtf8("silver18"))
        self.silver25 = QtGui.QPushButton(self.tab_7)
        self.silver25.setGeometry(QtCore.QRect(170, 270, 41, 41))
        self.silver25.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver25.setObjectName(_fromUtf8("silver25"))
        self.silver14 = QtGui.QPushButton(self.tab_7)
        self.silver14.setGeometry(QtCore.QRect(130, 190, 41, 41))
        self.silver14.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver14.setObjectName(_fromUtf8("silver14"))
        self.spinBox2_2 = QtGui.QSpinBox(self.tab_7)
        self.spinBox2_2.setGeometry(QtCore.QRect(330, 40, 61, 27))
        self.spinBox2_2.setMaximum(25)
        self.spinBox2_2.setObjectName(_fromUtf8("spinBox2_2"))
        self.gold04 = QtGui.QPushButton(self.tab_7)
        self.gold04.setGeometry(QtCore.QRect(370, 110, 41, 41))
        self.gold04.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold04.setObjectName(_fromUtf8("gold04"))
        self.spinBox1_2 = QtGui.QSpinBox(self.tab_7)
        self.spinBox1_2.setGeometry(QtCore.QRect(110, 40, 61, 27))
        self.spinBox1_2.setMaximum(25)
        self.spinBox1_2.setObjectName(_fromUtf8("spinBox1_2"))
        self.plt10 = QtGui.QPushButton(self.tab_7)
        self.plt10.setGeometry(QtCore.QRect(650, 150, 41, 41))
        self.plt10.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt10.setObjectName(_fromUtf8("plt10"))
        self.OK_2 = QtGui.QPushButton(self.tab_7)
        self.OK_2.setGeometry(QtCore.QRect(490, 400, 99, 31))
        self.OK_2.setStyleSheet(_fromUtf8("QPushButton\n"
"{ background-color: white;\n"
"    color: black;\n"
"    border-radius:4px;\n"
"border: 2px solid #e7e7e7;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: #e7e7e7;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"font-size:15px;\n"
"}"))
        self.OK_2.setObjectName(_fromUtf8("OK_2"))
        self.plt09 = QtGui.QPushButton(self.tab_7)
        self.plt09.setGeometry(QtCore.QRect(610, 150, 41, 41))
        self.plt09.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt09.setObjectName(_fromUtf8("plt09"))
        self.silver02 = QtGui.QPushButton(self.tab_7)
        self.silver02.setGeometry(QtCore.QRect(50, 110, 41, 41))
        self.silver02.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver02.setObjectName(_fromUtf8("silver02"))
        self.silver08 = QtGui.QPushButton(self.tab_7)
        self.silver08.setGeometry(QtCore.QRect(90, 150, 41, 41))
        self.silver08.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver08.setObjectName(_fromUtf8("silver08"))
        self.gold14 = QtGui.QPushButton(self.tab_7)
        self.gold14.setGeometry(QtCore.QRect(370, 190, 41, 41))
        self.gold14.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold14.setObjectName(_fromUtf8("gold14"))
        self.silver17 = QtGui.QPushButton(self.tab_7)
        self.silver17.setGeometry(QtCore.QRect(50, 230, 41, 41))
        self.silver17.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver17.setObjectName(_fromUtf8("silver17"))
        self.silver07 = QtGui.QPushButton(self.tab_7)
        self.silver07.setGeometry(QtCore.QRect(50, 150, 41, 41))
        self.silver07.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver07.setObjectName(_fromUtf8("silver07"))
        self.silver23 = QtGui.QPushButton(self.tab_7)
        self.silver23.setGeometry(QtCore.QRect(90, 270, 41, 41))
        self.silver23.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver23.setObjectName(_fromUtf8("silver23"))
        self.plt18 = QtGui.QPushButton(self.tab_7)
        self.plt18.setGeometry(QtCore.QRect(570, 230, 41, 41))
        self.plt18.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt18.setObjectName(_fromUtf8("plt18"))
        self.plt24 = QtGui.QPushButton(self.tab_7)
        self.plt24.setGeometry(QtCore.QRect(610, 270, 41, 41))
        self.plt24.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt24.setObjectName(_fromUtf8("plt24"))
        self.plt16 = QtGui.QPushButton(self.tab_7)
        self.plt16.setGeometry(QtCore.QRect(490, 230, 41, 41))
        self.plt16.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt16.setObjectName(_fromUtf8("plt16"))
        self.silver19 = QtGui.QPushButton(self.tab_7)
        self.silver19.setGeometry(QtCore.QRect(130, 230, 41, 41))
        self.silver19.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}\n"
""))
        self.silver19.setObjectName(_fromUtf8("silver19"))
        self.plt13 = QtGui.QPushButton(self.tab_7)
        self.plt13.setGeometry(QtCore.QRect(570, 190, 41, 41))
        self.plt13.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt13.setObjectName(_fromUtf8("plt13"))
        self.line_3 = QtGui.QFrame(self.tab_7)
        self.line_3.setGeometry(QtCore.QRect(460, 0, 20, 311))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.plt23 = QtGui.QPushButton(self.tab_7)
        self.plt23.setGeometry(QtCore.QRect(570, 270, 41, 41))
        self.plt23.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt23.setObjectName(_fromUtf8("plt23"))
        self.plt07 = QtGui.QPushButton(self.tab_7)
        self.plt07.setGeometry(QtCore.QRect(530, 150, 41, 41))
        self.plt07.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt07.setObjectName(_fromUtf8("plt07"))
        self.silver24 = QtGui.QPushButton(self.tab_7)
        self.silver24.setGeometry(QtCore.QRect(130, 270, 41, 41))
        self.silver24.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver24.setObjectName(_fromUtf8("silver24"))
        self.silver04 = QtGui.QPushButton(self.tab_7)
        self.silver04.setGeometry(QtCore.QRect(130, 110, 41, 41))
        self.silver04.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.silver04.setObjectName(_fromUtf8("silver04"))
        self.gold08 = QtGui.QPushButton(self.tab_7)
        self.gold08.setGeometry(QtCore.QRect(330, 150, 41, 41))
        self.gold08.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.gold08.setObjectName(_fromUtf8("gold08"))
        self.plt19 = QtGui.QPushButton(self.tab_7)
        self.plt19.setGeometry(QtCore.QRect(610, 230, 41, 41))
        self.plt19.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt19.setObjectName(_fromUtf8("plt19"))
        self.plt04 = QtGui.QPushButton(self.tab_7)
        self.plt04.setGeometry(QtCore.QRect(610, 110, 41, 41))
        self.plt04.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt04.setObjectName(_fromUtf8("plt04"))
        self.plt11 = QtGui.QPushButton(self.tab_7)
        self.plt11.setGeometry(QtCore.QRect(490, 190, 41, 41))
        self.plt11.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.plt11.setObjectName(_fromUtf8("plt11"))
        self.Button_silver_2 = QtGui.QPushButton(self.tab_7)
        self.Button_silver_2.setGeometry(QtCore.QRect(70, 80, 89, 27))
        self.Button_silver_2.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color:#C0C0C0;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"border-radius:3px;\n"
"color:black;\n"
"}"))
        self.Button_silver_2.setObjectName(_fromUtf8("Button_silver_2"))
        self.Button_gold_2 = QtGui.QPushButton(self.tab_7)
        self.Button_gold_2.setGeometry(QtCore.QRect(310, 80, 89, 27))
        self.Button_gold_2.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color:rgb(223, 199, 14);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"border-radius:3px;\n"
"color:black;\n"
"}"))
        self.Button_gold_2.setObjectName(_fromUtf8("Button_gold_2"))
        self.Button_platinum_2 = QtGui.QPushButton(self.tab_7)
        self.Button_platinum_2.setGeometry(QtCore.QRect(550, 80, 89, 27))
        self.Button_platinum_2.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color:#E5E4E2;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"border-radius:3px;\n"
"color:black;\n"
"}"))
        self.Button_platinum_2.setObjectName(_fromUtf8("Button_platinum_2"))
        self.TabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.Label_background_3 = QtGui.QLabel(self.tab_8)
        self.Label_background_3.setGeometry(QtCore.QRect(0, -10, 701, 471))
        self.Label_background_3.setText(_fromUtf8(""))
        self.Label_background_3.setPixmap(QtGui.QPixmap(_fromUtf8("popcorn_blur.jpeg")))
        self.Label_background_3.setObjectName(_fromUtf8("Label_background_3"))
        self.label4_3 = QtGui.QLabel(self.tab_8)
        self.label4_3.setGeometry(QtCore.QRect(40, 260, 150, 21))
        self.label4_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label4_3.setObjectName(_fromUtf8("label4_3"))
        self.lineEdit2_3 = QtGui.QLineEdit(self.tab_8)
        self.lineEdit2_3.setGeometry(QtCore.QRect(40, 190, 211, 41))
        self.lineEdit2_3.setObjectName(_fromUtf8("lineEdit2_3"))
        self.line = QtGui.QFrame(self.tab_8)
        self.line.setGeometry(QtCore.QRect(340, 0, 20, 451))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit3_3 = QtGui.QLineEdit(self.tab_8)
        self.lineEdit3_3.setGeometry(QtCore.QRect(40, 280, 211, 41))
        self.lineEdit3_3.setObjectName(_fromUtf8("lineEdit3_3"))
        self.Cancel_3 = QtGui.QPushButton(self.tab_8)
        self.Cancel_3.setGeometry(QtCore.QRect(460, 360, 161, 41))
        self.Cancel_3.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color: #555555;\n"
"    color: white;\n"
"border-radius:4px;\n"
"font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"font-size:18px;\n"
"background-color:white;\n"
"color:black;\n"
"}\n"
""))
        self.Cancel_3.setDefault(True)
        self.Cancel_3.setObjectName(_fromUtf8("Cancel_3"))
        self.generateTicket_3 = QtGui.QPushButton(self.tab_8)
        self.generateTicket_3.setGeometry(QtCore.QRect(70, 360, 161, 41))
        self.generateTicket_3.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    font-size:16px;\n"
"color:black;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:white;\n"
"background-color:#555555;\n"
"font-size:19px;\n"
"}"))
        self.generateTicket_3.setObjectName(_fromUtf8("generateTicket_3"))
        self.generateTicket_3.clicked.connect(self.handleTicket)
        self.label3_3 = QtGui.QLabel(self.tab_8)
        self.label3_3.setGeometry(QtCore.QRect(40, 170, 150, 21))
        self.label3_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label3_3.setObjectName(_fromUtf8("label3_3"))
        self.label2_3 = QtGui.QLabel(self.tab_8)
        self.label2_3.setGeometry(QtCore.QRect(40, 80, 61, 21))
        self.label2_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label2_3.setObjectName(_fromUtf8("label2_3"))
        self.label1_3 = QtGui.QLabel(self.tab_8)
        self.label1_3.setGeometry(QtCore.QRect(70, 30, 281, 31))
        self.label1_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"    font-variant: small-caps;\n"
"    color:black;\n"
"}"))
        self.label1_3.setObjectName(_fromUtf8("label1_3"))
        self.lineEdit1_3 = QtGui.QLineEdit(self.tab_8)
        self.lineEdit1_3.setGeometry(QtCore.QRect(40, 100, 211, 41))
        self.lineEdit1_3.setObjectName(_fromUtf8("lineEdit1_3"))
        self.label_cost_3 = QtGui.QLabel(self.tab_8)
        self.label_cost_3.setGeometry(QtCore.QRect(360, 90, 321, 241))
        self.label_cost_3.setText(_fromUtf8(""))
        self.label_cost_3.setPixmap(QtGui.QPixmap(_fromUtf8("bill_resized.jpeg")))
        self.label_cost_3.setObjectName(_fromUtf8("label_cost_3"))
        self.LABEL15_3 = QtGui.QLabel(self.tab_8)
        self.LABEL15_3.setGeometry(QtCore.QRect(610, 230, 59, 14))
        self.LABEL15_3.setObjectName(_fromUtf8("LABEL15_3"))
        self.LABEL15_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label5_3 = QtGui.QLabel(self.tab_8)
        self.label5_3.setGeometry(QtCore.QRect(500, 90, 171, 31))
        self.label5_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 12pt \"Noto Sans Mono CJK SC\";\n"
"color:black;\n"
"}"))
        self.label5_3.setObjectName(_fromUtf8("label5_3"))
        self.label7_3 = QtGui.QLabel(self.tab_8)
        self.label7_3.setGeometry(QtCore.QRect(400, 170, 140, 16))
        self.label7_3.setObjectName(_fromUtf8("label7_3"))
        self.label7_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label9_3 = QtGui.QLabel(self.tab_8)
        self.label9_3.setGeometry(QtCore.QRect(400, 230, 160, 16))
        self.label9_3.setObjectName(_fromUtf8("label9_3"))
        self.label9_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.LABEL12_3 = QtGui.QLabel(self.tab_8)
        self.LABEL12_3.setGeometry(QtCore.QRect(570, 130, 59, 16))
        self.LABEL12_3.setObjectName(_fromUtf8("LABEL12_3"))
        self.LABEL12_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label10_3 = QtGui.QLabel(self.tab_8)
        self.label10_3.setGeometry(QtCore.QRect(420, 260, 59, 31))
        self.label10_3.setObjectName(_fromUtf8("label10_3"))
        self.label10_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.LABEL14_3 = QtGui.QLabel(self.tab_8)
        self.LABEL14_3.setGeometry(QtCore.QRect(610, 200, 59, 14))
        self.LABEL14_3.setObjectName(_fromUtf8("LABEL14_3"))
        self.LABEL14_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label11_3 = QtGui.QLabel(self.tab_8)
        self.label11_3.setGeometry(QtCore.QRect(420, 310, 321, 16))
        self.label11_3.setObjectName(_fromUtf8("label11_3"))
        self.label11_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label8_3 = QtGui.QLabel(self.tab_8)
        self.label8_3.setGeometry(QtCore.QRect(400, 200, 120, 16))
        self.label8_3.setObjectName(_fromUtf8("label8_3"))
        self.label8_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label6_3 = QtGui.QLabel(self.tab_8)
        self.label6_3.setGeometry(QtCore.QRect(440, 130, 141, 16))
        self.label6_3.setObjectName(_fromUtf8("label6_3"))
        self.label6_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.LABEL13_3 = QtGui.QLabel(self.tab_8)
        self.LABEL13_3.setGeometry(QtCore.QRect(560, 170, 121, 14))
        self.LABEL13_3.setObjectName(_fromUtf8("LABEL13_3"))
        self.LABEL13_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.LABEL16_3 = QtGui.QLabel(self.tab_8)
        self.LABEL16_3.setGeometry(QtCore.QRect(610, 270, 59, 14))
        self.LABEL16_3.setObjectName(_fromUtf8("LABEL16_3"))
        self.LABEL16_3.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label_18 = QtGui.QLabel(self.tab_8)
        self.label_18.setGeometry(QtCore.QRect(360, 250, 321, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_18.setStyleSheet(_fromUtf8("QLabel\n"
                                                "{\n"
                                              "color:black;\n"
                                              "}"))

        self.label_27 = QtGui.QLabel(self.tab_8)
        self.label_27.setGeometry(QtCore.QRect(360, 150, 321, 16))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.TabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.Time = QtGui.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(640, 480, 61, 31))
        self.Time.setObjectName(_fromUtf8("Time"))
        self.Date = QtGui.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(10, 480, 120, 31))
        self.Date.setObjectName(_fromUtf8("Date"))
        self.Date_label = QtGui.QLabel(self.centralwidget)
        self.Date_label.setGeometry(QtCore.QRect(125, 480, 61, 31))
        self.Date_label.setObjectName(_fromUtf8("Date_label"))
        self.Time_label = QtGui.QLabel(self.centralwidget)
        self.Time_label.setGeometry(QtCore.QRect(590, 480, 61, 31))
        self.Time_label.setObjectName(_fromUtf8("Time_label"))
        Main_Window.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(Main_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 703, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))

        Main_Window.setMenuBar(self.menuBar)
        self.actionFont_Designer = QtGui.QAction(Main_Window)
        self.actionFont_Designer.setObjectName(_fromUtf8("actionFont_Designer"))
        self.actionChange_Background_color = QtGui.QAction(Main_Window)
        self.actionChange_Background_color.setObjectName(_fromUtf8("actionChange_Background_color"))
        self.actionDevelopers = QtGui.QAction(Main_Window)
        self.actionDevelopers.setObjectName(_fromUtf8("actionDevelopers"))
        self.menuAbout.addAction(self.actionDevelopers)
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Main_Window)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

        #####################

        self.Cost_gold_2 = QtGui.QLabel(self.tab_7)
        self.Cost_gold_2.setGeometry(QtCore.QRect(80, 310, 71, 21))
        self.Cost_gold_2.setText("Rs. 200")
        self.Cost_gold_2.setStyleSheet("font-size:18px; color:white; font-weight:bold;")

        self.Cost_silver_2 = QtGui.QLabel(self.tab_7)
        self.Cost_silver_2.setGeometry(QtCore.QRect(320, 310, 71, 21))
        self.Cost_silver_2.setText("Rs. 300")
        self.Cost_silver_2.setStyleSheet("font-size:18px; color:white; font-weight:bold;")

        self.Cost_plt_2 = QtGui.QLabel(self.tab_7)
        self.Cost_plt_2.setGeometry(QtCore.QRect(560, 310, 71, 21))
        self.Cost_plt_2.setText("Rs. 400")
        self.Cost_plt_2.setStyleSheet("font-size:18px; color:white; font-weight:bold;")

        self.Loop_3 = QtGui.QPushButton(self.tab_8)
        self.Loop_3.setGeometry(QtCore.QRect(260, 400, 170, 50))
        self.Loop_3.setStyleSheet(_fromUtf8("QPushButton\n"
                                              "{\n"
                                              "background-color: white;\n"
                                              "    color: black;\n"
                                              "border-radius:4px;\n"
                                                "font-size:15px;\n"
                                                "font-weight:bold;\n"
                                                "border: 4px solid #008CBA;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover\n"
                                              "{\n"
                                                "background-color:#008CBA;\n"
                                                "color:white;\n"
                                              "font-size:17px;\n"
                                                "font-weight:bold;\n"
                                              "}\n"
                                              ""))
        self.Loop_3.setDefault(True)
        self.Loop_3.setObjectName(_fromUtf8("Cancel_3"))
        self.Loop_3.setText("Book another ticket")
        self.Loop_3.clicked.connect(self.handleLoop)

        # OK buttons
        self.OK_0.clicked.connect(self.handleOK1)
        self.OK_1.clicked.connect(self.handleOK2)
        self.OK_2.clicked.connect(self.handleOK3)

        # Cancel buttons
        self.Cancel_0.clicked.connect(self.close_application)
        self.Cancel_1.clicked.connect(self.close_application)
        self.Cancel_2.clicked.connect(self.close_application)
        self.Cancel_3.clicked.connect(self.close_application)

        # Seat buttons
        self.gold01.setCheckable(True)
        self.gold01.toggle()
        self.gold01_text = self.gold01.text()
        self.gold01.clicked.connect(lambda: self.btnstate_gold(self.gold01, self.gold01_text))

        self.gold02.setCheckable(True)
        self.gold02.toggle()
        self.gold02_text = self.gold02.text()
        self.gold02.clicked.connect(lambda: self.btnstate_gold(self.gold02, self.gold02_text))

        self.gold04.setCheckable(True)
        self.gold04.toggle()
        self.gold04_text = self.gold04.text()
        self.gold04.clicked.connect(lambda: self.btnstate_gold(self.gold04, self.gold04_text))

        self.gold03.setCheckable(True)
        self.gold03.toggle()
        self.gold03_text = self.gold03.text()
        self.gold03.clicked.connect(lambda: self.btnstate_gold(self.gold03, self.gold03_text))

        self.gold05.setCheckable(True)
        self.gold05.toggle()
        self.gold05_text = self.gold05.text()
        self.gold05.clicked.connect(lambda: self.btnstate_gold(self.gold05, self.gold05_text))

        self.gold06.setCheckable(True)
        self.gold06.toggle()
        self.gold06_text = self.gold06.text()
        self.gold06.clicked.connect(lambda: self.btnstate_gold(self.gold06, self.gold06_text))

        self.gold07.setCheckable(True)
        self.gold07.toggle()
        self.gold07_text = self.gold07.text()
        self.gold07.clicked.connect(lambda: self.btnstate_gold(self.gold07, self.gold07_text))

        self.gold08.setCheckable(True)
        self.gold08.toggle()
        self.gold08_text = self.gold08.text()
        self.gold08.clicked.connect(lambda: self.btnstate_gold(self.gold08, self.gold08_text))

        self.gold09.setCheckable(True)
        self.gold09.toggle()
        self.gold09_text = self.gold09.text()
        self.gold09.clicked.connect(lambda: self.btnstate_gold(self.gold09, self.gold09_text))

        self.gold10.setCheckable(True)
        self.gold10.toggle()
        self.gold10_text = self.gold10.text()
        self.gold10.clicked.connect(lambda: self.btnstate_gold(self.gold10, self.gold10_text))

        self.gold11.setCheckable(True)
        self.gold11.toggle()
        self.gold11_text = self.gold11.text()
        self.gold11.clicked.connect(lambda: self.btnstate_gold(self.gold11, self.gold11_text))

        self.gold12.setCheckable(True)
        self.gold12.toggle()
        self.gold12_text = self.gold12.text()
        self.gold12.clicked.connect(lambda: self.btnstate_gold(self.gold12, self.gold12_text))

        self.gold13.setCheckable(True)
        self.gold13.toggle()
        self.gold13_text = self.gold13.text()
        self.gold13.clicked.connect(lambda: self.btnstate_gold(self.gold13, self.gold13_text))

        self.gold14.setCheckable(True)
        self.gold14.toggle()
        self.gold14_text = self.gold14.text()
        self.gold14.clicked.connect(lambda: self.btnstate_gold(self.gold14, self.gold14_text))

        self.gold15.setCheckable(True)
        self.gold15.toggle()
        self.gold15_text = self.gold06.text()
        self.gold15.clicked.connect(lambda: self.btnstate_gold(self.gold15, self.gold15_text))

        self.gold16.setCheckable(True)
        self.gold16.toggle()
        self.gold16_text = self.gold16.text()
        self.gold16.clicked.connect(lambda: self.btnstate_gold(self.gold16, self.gold16_text))

        self.gold17.setCheckable(True)
        self.gold17.toggle()
        self.gold17_text = self.gold17.text()
        self.gold17.clicked.connect(lambda: self.btnstate_gold(self.gold17, self.gold17_text))

        self.gold18.setCheckable(True)
        self.gold18.toggle()
        self.gold18_text = self.gold18.text()
        self.gold18.clicked.connect(lambda: self.btnstate_gold(self.gold18, self.gold18_text))

        self.gold19.setCheckable(True)
        self.gold19.toggle()
        self.gold19_text = self.gold19.text()
        self.gold19.clicked.connect(lambda: self.btnstate_gold(self.gold19, self.gold19_text))

        self.gold20.setCheckable(True)
        self.gold20.toggle()
        self.gold20_text = self.gold20.text()
        self.gold20.clicked.connect(lambda: self.btnstate_gold(self.gold20, self.gold20_text))

        self.gold21.setCheckable(True)
        self.gold21.toggle()
        self.gold21_text = self.gold21.text()
        self.gold21.clicked.connect(lambda: self.btnstate_gold(self.gold21, self.gold21_text))

        self.gold22.setCheckable(True)
        self.gold22.toggle()
        self.gold22_text = self.gold22.text()
        self.gold22.clicked.connect(lambda: self.btnstate_gold(self.gold22, self.gold22_text))

        self.gold23.setCheckable(True)
        self.gold23.toggle()
        self.gold23_text = self.gold23.text()
        self.gold23.clicked.connect(lambda: self.btnstate_gold(self.gold23, self.gold23_text))

        self.gold24.setCheckable(True)
        self.gold24.toggle()
        self.gold24_text = self.gold24.text()
        self.gold24.clicked.connect(lambda: self.btnstate_gold(self.gold24, self.gold24_text))

        self.gold25.setCheckable(True)
        self.gold25.toggle()
        self.gold25_text = self.gold25.text()
        self.gold25.clicked.connect(lambda: self.btnstate_gold(self.gold25, self.gold25_text))

        self.silver01.setCheckable(True)
        self.silver01.toggle()
        self.silver01_text = self.silver01.text()
        self.silver01.clicked.connect(lambda: self.btnstate_silver(self.silver01, self.silver01_text))

        self.silver02.setCheckable(True)
        self.silver02.toggle()
        self.silver02_text = self.silver02.text()
        self.silver02.clicked.connect(lambda: self.btnstate_silver(self.silver02, self.silver02_text))

        self.silver03.setCheckable(True)
        self.silver03.toggle()
        self.silver03_text = self.silver03.text()
        self.silver03.clicked.connect(lambda: self.btnstate_silver(self.silver03, self.silver03_text))

        self.silver04.setCheckable(True)
        self.silver04.toggle()
        self.silver04_text = self.silver04.text()
        self.silver04.clicked.connect(lambda: self.btnstate_silver(self.silver04, self.silver04_text))

        self.silver05.setCheckable(True)
        self.silver05.toggle()
        self.silver05_text = self.silver05.text()
        self.silver05.clicked.connect(lambda: self.btnstate_silver(self.silver05, self.silver05_text))

        self.silver06.setCheckable(True)
        self.silver06.toggle()
        self.silver06_text = self.silver06.text()
        self.silver06.clicked.connect(lambda: self.btnstate_silver(self.silver06, self.silver06_text))

        self.silver07.setCheckable(True)
        self.silver07.toggle()
        self.silver07_text = self.silver07.text()
        self.silver07.clicked.connect(lambda: self.btnstate_silver(self.silver07, self.silver07_text))

        self.silver08.setCheckable(True)
        self.silver08.toggle()
        self.silver08_text = self.silver08.text()
        self.silver08.clicked.connect(lambda: self.btnstate_silver(self.silver08, self.silver08_text))

        self.silver09.setCheckable(True)
        self.silver09.toggle()
        self.silver09_text = self.silver09.text()
        self.silver09.clicked.connect(lambda: self.btnstate_silver(self.silver09, self.silver09_text))

        self.silver10.setCheckable(True)
        self.silver10.toggle()
        self.silver10_text = self.silver10.text()
        self.silver10.clicked.connect(lambda: self.btnstate_silver(self.silver10, self.silver10_text))

        self.silver11.setCheckable(True)
        self.silver11.toggle()
        self.silver11_text = self.silver11.text()
        self.silver11.clicked.connect(lambda: self.btnstate_silver(self.silver11, self.silver11_text))

        self.silver12.setCheckable(True)
        self.silver12.toggle()
        self.silver12_text = self.silver12.text()
        self.silver12.clicked.connect(lambda: self.btnstate_silver(self.silver12, self.silver12_text))

        self.silver13.setCheckable(True)
        self.silver13.toggle()
        self.silver13_text = self.silver13.text()
        self.silver13.clicked.connect(lambda: self.btnstate_silver(self.silver13, self.silver13_text))

        self.silver14.setCheckable(True)
        self.silver14.toggle()
        self.silver14_text = self.silver14.text()
        self.silver14.clicked.connect(lambda: self.btnstate_silver(self.silver14, self.silver14_text))

        self.silver15.setCheckable(True)
        self.silver15.toggle()
        self.silver15_text = self.silver15.text()
        self.silver15.clicked.connect(lambda: self.btnstate_silver(self.silver15, self.silver15_text))

        self.silver16.setCheckable(True)
        self.silver16.toggle()
        self.silver16_text = self.silver16.text()
        self.silver16.clicked.connect(lambda: self.btnstate_silver(self.silver16, self.silver16_text))

        self.silver17.setCheckable(True)
        self.silver17.toggle()
        self.silver17_text = self.silver17.text()
        self.silver17.clicked.connect(lambda: self.btnstate_silver(self.silver17, self.silver17_text))

        self.silver18.setCheckable(True)
        self.silver18.toggle()
        self.silver18_text = self.silver18.text()
        self.silver18.clicked.connect(lambda: self.btnstate_silver(self.silver18, self.silver18_text))

        self.silver19.setCheckable(True)
        self.silver19.toggle()
        self.silver19_text = self.silver19.text()
        self.silver19.clicked.connect(lambda: self.btnstate_silver(self.silver19, self.silver19_text))

        self.silver20.setCheckable(True)
        self.silver20.toggle()
        self.silver20_text = self.silver20.text()
        self.silver20.clicked.connect(lambda: self.btnstate_silver(self.silver20, self.silver20_text))

        self.silver21.setCheckable(True)
        self.silver21.toggle()
        self.silver21_text = self.silver21.text()
        self.silver21.clicked.connect(lambda: self.btnstate_silver(self.silver21, self.silver21_text))

        self.silver22.setCheckable(True)
        self.silver22.toggle()
        self.silver22_text = self.silver22.text()
        self.silver22.clicked.connect(lambda: self.btnstate_silver(self.silver22, self.silver22_text))

        self.silver23.setCheckable(True)
        self.silver23.toggle()
        self.silver23_text = self.silver23.text()
        self.silver23.clicked.connect(lambda: self.btnstate_silver(self.silver23, self.silver23_text))

        self.silver24.setCheckable(True)
        self.silver24.toggle()
        self.silver24_text = self.silver24.text()
        self.silver24.clicked.connect(lambda: self.btnstate_silver(self.silver24, self.silver24_text))

        self.silver25.setCheckable(True)
        self.silver25.toggle()
        self.silver25_text = self.silver25.text()
        self.silver25.clicked.connect(lambda: self.btnstate_silver(self.silver25, self.silver25_text))

        self.plt01.setCheckable(True)
        self.plt01.toggle()
        self.plt01_text = self.plt01.text()
        self.plt01.clicked.connect(lambda: self.btnstate_plt(self.plt01, self.plt01_text))

        self.plt02.setCheckable(True)
        self.plt02.toggle()
        self.plt02_text = self.plt02.text()
        self.plt02.clicked.connect(lambda: self.btnstate_plt(self.plt02, self.plt02_text))

        self.plt03.setCheckable(True)
        self.plt03.toggle()
        self.plt03_text = self.plt03.text()
        self.plt03.clicked.connect(lambda: self.btnstate_plt(self.plt03, self.plt03_text))

        self.plt04.setCheckable(True)
        self.plt04.toggle()
        self.plt04_text = self.plt04.text()
        self.plt04.clicked.connect(lambda: self.btnstate_plt(self.plt04, self.plt04_text))

        self.plt05.setCheckable(True)
        self.plt05.toggle()
        self.plt05_text = self.plt05.text()
        self.plt05.clicked.connect(lambda: self.btnstate_plt(self.plt05, self.plt05_text))

        self.plt06.setCheckable(True)
        self.plt06.toggle()
        self.plt06_text = self.plt06.text()
        self.plt06.clicked.connect(lambda: self.btnstate_plt(self.plt06, self.plt06_text))

        self.plt07.setCheckable(True)
        self.plt07.toggle()
        self.plt07_text = self.plt07.text()
        self.plt07.clicked.connect(lambda: self.btnstate_plt(self.plt07, self.plt07_text))

        self.plt08.setCheckable(True)
        self.plt08.toggle()
        self.plt08_text = self.plt08.text()
        self.plt08.clicked.connect(lambda: self.btnstate_plt(self.plt08, self.plt08_text))

        self.plt09.setCheckable(True)
        self.plt09.toggle()
        self.plt09_text = self.plt09.text()
        self.plt09.clicked.connect(lambda: self.btnstate_plt(self.plt09, self.plt09_text))

        self.plt10.setCheckable(True)
        self.plt10.toggle()
        self.plt10_text = self.plt10.text()
        self.plt10.clicked.connect(lambda: self.btnstate_plt(self.plt10, self.plt10_text))

        self.plt11.setCheckable(True)
        self.plt11.toggle()
        self.plt11_text = self.plt11.text()
        self.plt11.clicked.connect(lambda: self.btnstate_plt(self.plt11, self.plt11_text))

        self.plt12.setCheckable(True)
        self.plt12.toggle()
        self.plt12_text = self.plt12.text()
        self.plt12.clicked.connect(lambda: self.btnstate_plt(self.plt12, self.plt12_text))

        self.plt13.setCheckable(True)
        self.plt13.toggle()
        self.plt13_text = self.plt13.text()
        self.plt13.clicked.connect(lambda: self.btnstate_plt(self.plt13, self.plt13_text))

        self.plt14.setCheckable(True)
        self.plt14.toggle()
        self.plt14_text = self.plt14.text()
        self.plt14.clicked.connect(lambda: self.btnstate_plt(self.plt14, self.plt14_text))

        self.plt15.setCheckable(True)
        self.plt15.toggle()
        self.plt15_text = self.plt15.text()
        self.plt15.clicked.connect(lambda: self.btnstate_plt(self.plt15, self.plt15_text))

        self.plt16.setCheckable(True)
        self.plt16.toggle()
        self.plt16_text = self.plt16.text()
        self.plt16.clicked.connect(lambda: self.btnstate_plt(self.plt16, self.plt16_text))

        self.plt17.setCheckable(True)
        self.plt17.toggle()
        self.plt17_text = self.plt17.text()
        self.plt17.clicked.connect(lambda: self.btnstate_plt(self.plt17, self.plt17_text))

        self.plt18.setCheckable(True)
        self.plt18.toggle()
        self.plt18_text = self.plt18.text()
        self.plt18.clicked.connect(lambda: self.btnstate_plt(self.plt18, self.plt18_text))

        self.plt19.setCheckable(True)
        self.plt19.toggle()
        self.plt19_text = self.plt19.text()
        self.plt19.clicked.connect(lambda: self.btnstate_plt(self.plt19, self.plt19_text))

        self.plt20.setCheckable(True)
        self.plt20.toggle()
        self.plt20_text = self.plt20.text()
        self.plt20.clicked.connect(lambda: self.btnstate_plt(self.plt20, self.plt20_text))

        self.plt21.setCheckable(True)
        self.plt21.toggle()
        self.plt21_text = self.plt21.text()
        self.plt21.clicked.connect(lambda: self.btnstate_plt(self.plt21, self.plt21_text))

        self.plt22.setCheckable(True)
        self.plt22.toggle()
        self.plt22_text = self.plt22.text()
        self.plt22.clicked.connect(lambda: self.btnstate_plt(self.plt22, self.plt22_text))

        self.plt23.setCheckable(True)
        self.plt23.toggle()
        self.plt23_text = self.plt23.text()
        self.plt23.clicked.connect(lambda: self.btnstate_plt(self.plt23, self.plt23_text))

        self.plt24.setCheckable(True)
        self.plt24.toggle()
        self.plt24_text = self.plt24.text()
        self.plt24.clicked.connect(lambda: self.btnstate_plt(self.plt24, self.plt24_text))

        self.plt25.setCheckable(True)
        self.plt25.toggle()
        self.plt25_text = self.plt25.text()
        self.plt25.clicked.connect(lambda: self.btnstate_plt(self.plt25, self.plt25_text))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        self.date=QtCore.QDate.currentDate().toString()
        self.Date.setText("%s"%(self.date))
        self.Date.setStyleSheet("QLabel\n"
                                "{\n"
                                "font-weight:bold;\n"
                                "font-size:15px;\n"
                                "}")

        QtCore.QMetaObject.connectSlotsByName(Main_Window)

        self.g_checked = 0
        self.s_checked = 0
        self.p_checked = 0

        self.spinBox1_2.setSingleStep(0)
        self.spinBox2_2.setSingleStep(0)
        self.spinBox3_2.setSingleStep(0)



    def handleTicket(self):
        if self.lineEdit1_3.text()=="":
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Please fill the name feild.")
            msg.setInformativeText("It is mandatory.")
            msg.setWindowTitle("ENTER THE NAME!!")
            msg.setEscapeButton(QtGui.QMessageBox.Ok)
            msg.exec_()
        else:
            self.Ticket = MyDialog(self)
            self.Ticket.exec_()

    def resetSeatCount(self):
        self.silver=0
        self.gold=0
        self.plt=0

    def setCost(self):
        """print self.silver
        print self.gold
        print self.plt"""
        self.totalSeats = self.silver + self.gold + self.plt
        self.sCost=self.silver*200
        self.gCost = self.gold * 300
        self.pCost = self.plt * 400
        self.tCost=self.sCost + self.gCost + self.pCost
        self.serviceTax=(self.tCost*15)/100
        self.enterTax=(self.tCost*20)/100

        self.totalCost = self.tCost + self.serviceTax + self.enterTax
        self.LABEL12_3.setText("%d" % self.totalSeats)
        if self.sCost!=0 and self.gCost!=0 and self.pCost!=0:
            self.LABEL13_3.setGeometry(QtCore.QRect(560, 170, 121, 14))
        elif self.sCost==0 or self.gCost==0 or self.pCost==0:
            self.LABEL13_3.setGeometry(QtCore.QRect(580, 170, 121, 14))
        self.LABEL13_3.setText("Rs.%d + %d + %d"%(self.sCost , self.gCost , self.pCost))
        self.LABEL14_3.setText("Rs.%d" % self.serviceTax)
        self.LABEL15_3.setText("Rs.%d" % self.enterTax)
        self.LABEL16_3.setText("Rs.%d" % self.totalCost)

    def setCurrentMovie(self):
        if 9<=self.now.hour<12:
            self.Label1_0.setText(_translate("Main_Window","<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\">S</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">UICIDE</span><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\"> S</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">QUAD</span></p></body></html>",None))
        if 12 <= self.now.hour < 15:
            self.Label1_0.setText(_translate("Main_Window","<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\">G</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">ONE</span><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\"> G</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">IRL</span></p></body></html>",None))
            self.Label1_0.move(110,310)
        elif 15 <= self.now.hour < 19:
            self.Label1_0.setText(_translate("Main_Window","<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\">T</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">HE</span><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\"> C</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">ONJURING</span></p></body></html>",None))

        elif 19 <= self.now.hour < 22:
            self.Label1_0.setText(_translate("Main_Window","<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\">T</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">HE</span><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\"> R</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">USH</span></p></body></html>",None))
            self.Label1_0.move(110, 310)
        else:
            print "Closed"#self.label1_0.setText("THEATRE CLOSED.")

    def displayTime(self):
            self.Time.setStyleSheet("QLabel\n"
"{\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}")
            self.Time.setText(QtCore.QTime.currentTime().toString())

    def btnstate_silver(self, Button, btn_text):
            if Button.isChecked():
                    self.s_checked = self.s_checked - 1
                    self.silver=self.silver-1
                    self.spinBox1_2.setValue(self.s_checked)
                    Button.setStyleSheet(_fromUtf8("QPushButton:hover\n"
                                                   "{\n"
                                                   "background-color:#C0C0C0;\n"
                                                   "font-weight:bold;\n"
                                                   "font-size:15px;\n"
                                                   "}"))
                    Button.setText("%s" % (btn_text))
            else:
                    self.s_checked=self.s_checked+1
                    self.silver=self.silver+1
                    self.spinBox1_2.setValue(self.s_checked)
                    Button.setStyleSheet(_fromUtf8("QPushButton\n"
                                                   "{\n"
                                                   "background-color:#C0C0C0;\n"
                                                   "font-weight:bold;\n"
                                                   "font-size:15px;\n"
                                                   "}"))
                    Button.setText("%s B" % btn_text)

    def btnstate_gold(self, Button, btn_text):
            if Button.isChecked():
                    self.g_checked = self.g_checked - 1
                    self.gold=self.gold-1
                    self.spinBox2_2.setValue(self.g_checked)
                    Button.setStyleSheet(_fromUtf8("QPushButton:hover\n"
                                                   "{\n"
                                                   "background-color:rgb(223, 199, 14);\n"
                                                   "font-weight:bold;\n"
                                                   "font-size:15px;\n"
                                                   "}"))
                    Button.setText("%s" % btn_text)
            else:
                    self.g_checked = self.g_checked + 1
                    self.gold=self.gold+1
                    self.spinBox2_2.setValue(self.g_checked)
                    Button.setStyleSheet(_fromUtf8("QPushButton\n"
                                                   "{\n"
                                                   "background-color:rgb(223, 199, 14);\n"
                                                   "font-weight:bold;\n"
                                                   "font-size:15px;\n"
                                                   "}"))
                    Button.setText("%s B" % btn_text)

    def btnstate_plt(self, Button, btn_text):
            if Button.isChecked():
                    self.p_checked = self.p_checked - 1
                    self.plt=self.plt-1
                    self.spinBox3_2.setValue(self.p_checked)
                    Button.setStyleSheet(_fromUtf8("QPushButton:hover\n"
                                                   "{\n"
                                                   "background-color:#E5E4E2;\n"
                                                   "font-weight:bold;\n"
                                                   "font-size:15px;\n"
                                                   "}"))
                    Button.setText("%s" % btn_text)
            else:
                    self.p_checked = self.p_checked + 1
                    self.plt=self.plt+1
                    self.spinBox3_2.setValue(self.p_checked)
                    Button.setStyleSheet(_fromUtf8("QPushButton\n"
                                                   "{\n"
                                                   "background-color:#E5E4E2;\n"
                                                   "font-weight:bold;\n"
                                                   "font-size:15px;\n"
                                                   "}"))
                    Button.setText("%s B" % btn_text)

    def close_application(self):
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Question)
            msg.setText("You clicked Cancel button")
            msg.setInformativeText("Are you sure you want to quit?")
            msg.setWindowTitle("Quit")
            # msg.setDText("The details are as follows:")
            choice = msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            retval = msg.exec_()

            if retval == QtGui.QMessageBox.Ok:
                    #print "BYEE"
                    sys.exit()

    def handleOK1(self):
            if self.radio1_0.isChecked()==True:
                self.TabWidget.setCurrentIndex(1)
            elif self.radio2_0.isChecked() == True:
                self.TabWidget.setCurrentIndex(2)
            else:
                self.radio_message_0()

    def handleOK2(self):
        #Main_Window.resize(703,650)
        if (self.now.hour) < 9 or (self.now.hour) >= 19:
            if self.radio2_1.isChecked() == True or self.radio3_1.isChecked() == True or self.radio4_1.isChecked() == True:
                self.radio_message_1()
                self.radio1_1.setChecked(True)
            elif self.radio1_1.isChecked()==True:
                self.resetSeatCount()
                self.TabWidget.setCurrentIndex(2)
            else:
                self.radio_message_0()
                self.radio1_1.setChecked(True)

        elif 9 <= (self.now.hour) < 12:
            if self.radio1_1.isChecked() == True or self.radio3_1.isChecked() == True or self.radio4_1.isChecked() == True:
                self.radio_message_1()
                self.radio2_1.setChecked(True)
            elif self.radio2_1.isChecked()==True:
                self.resetSeatCount()
                self.TabWidget.setCurrentIndex(2)
            else:
                self.radio_message_0()
                self.radio2_1.setChecked(True)

        elif 12 <= (self.now.hour) < 15:
            if self.radio2_1.isChecked() == True or self.radio1_1.isChecked() == True or self.radio4_1.isChecked() == True:
                self.radio_message_1()
                self.radio3_1.setChecked(True)
            elif self.radio3_1.isChecked()==True:
                self.resetSeatCount()
                self.TabWidget.setCurrentIndex(2)
            else:
                self.radio_message_0()
                self.radio3_1.setChecked(True)

        elif 15 <= (self.now.hour) < 19:
            if self.radio2_1.isChecked() == True or self.radio3_1.isChecked() == True or self.radio1_1.isChecked() == True:
                self.radio_message_1()
                self.radio4_1.setChecked(True)
            elif self.radio4_1.isChecked()==True:
                self.resetSeatCount()
                self.TabWidget.setCurrentIndex(2)
            else:
                self.radio_message_0()
                self.radio4_1.setChecked(True)


    def handleOK3(self):
            if self.silver==0 and self.gold==0 and self.plt==0:
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Critical)
                msg.setText("Please select any of the available seats.")
                #msg.setInformativeText("Please select any of the available seats.")
                msg.setWindowTitle("NO SEATS SELECTED!!")
                msg.setEscapeButton(QtGui.QMessageBox.Ok)
                msg.exec_()
            else:
                self.setCost()
                self.TabWidget.setCurrentIndex(3)

    def handleLoop(self):
        self.TabWidget.setCurrentIndex(1)

    def radio_message_0(self):
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("No options were selected.")
            msg.setInformativeText("Selecting an option is mandatory.")
            msg.setWindowTitle("NOTHING SELECTED!!")
            msg.setEscapeButton(QtGui.QMessageBox.Ok)
            msg.exec_()

    def radio_message_1(self):
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Sorry, tickets can't be booked for this show right now.")
            msg.setInformativeText("At this time, tickets can be booked for the marked show only.")
            msg.setWindowTitle("WRONG SHOW!!")
            msg.setEscapeButton(QtGui.QMessageBox.Ok)
            msg.exec_()

    #######################

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(_translate("Main_Window", "MainWindow", None))
        self.TabWidget.setWhatsThis(_translate("Main_Window", "<html><head/><body><p>HOME</p></body></html>", None))
        self.Cancel_0.setText(_translate("Main_Window", "Cancel", None))
        self.Label2_0.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#00557f;\">Enter your choice:</span></p></body></html>", None))
        self.radio1_0.setText(_translate("Main_Window", "Book a ticket", None))
        self.OK_0.setText(_translate("Main_Window", "OK", None))
        #self.Label1_0.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\">S</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">UICIDE</span><span style=\" font-size:28pt; font-weight:600; color:#0a064c;\"> S</span><span style=\" font-size:24pt; font-weight:600; color:#0a064c;\">QUAD</span></p></body></html>", None))
        self.radio2_0.setText(_translate("Main_Window", "Seat Availability", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Home), _translate("Main_Window", "Home", None))
        self.Label_background_1.setWhatsThis(_translate("Main_Window", "Instructions", None))
        self.radio2_1.setText(_translate("Main_Window", "Gone Girl                                          12:00", None))
        self.radio4_1.setText(_translate("Main_Window", "The Rush                                          19:00", None))
        self.Label2_1.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Time</span></p></body></html>", None))
        self.Label4_1.setToolTip(_translate("Main_Window", "Instructions", None))
        self.Label4_1.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#632603;\">*List of all the movies are displayed alongwith their timings</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#632603;\">*Tickets can only be booked for the next show.</span></p></body></html>", None))
        self.radio1_1.setText(_translate("Main_Window", "Suicide Squad                                 09:00", None))
        self.Label3_1.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:36pt; color:#101010;\">S</span><span style=\" font-size:26pt; color:#101010;\">HOWS</span><span style=\" font-size:36pt; color:#101010;\"> L</span><span style=\" font-size:26pt; color:#101010;\">IST</span></p></body></html>", None))
        self.Label1_1.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Movies</span></p></body></html>", None))
        self.radio3_1.setText(_translate("Main_Window", "The Conjuring                                 15:00", None))
        self.OK_1.setText(_translate("Main_Window", "OK", None))
        self.Cancel_1.setText(_translate("Main_Window", "Cancel", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), _translate("Main_Window", "Shows", None))
        self.gold06.setText(_translate("Main_Window", "06", None))
        self.silver20.setText(_translate("Main_Window", "20", None))
        self.gold16.setText(_translate("Main_Window", "16", None))
        self.plt15.setText(_translate("Main_Window", "15", None))
        self.plt14.setText(_translate("Main_Window", "14", None))
        self.gold07.setText(_translate("Main_Window", "07", None))
        self.silver06.setText(_translate("Main_Window", "06", None))
        self.gold18.setText(_translate("Main_Window", "18", None))
        self.plt06.setText(_translate("Main_Window", "06", None))
        self.gold21.setText(_translate("Main_Window", "21", None))
        self.gold20.setText(_translate("Main_Window", "20", None))
        self.plt05.setText(_translate("Main_Window", "05", None))
        self.gold13.setText(_translate("Main_Window", "13", None))
        self.gold02.setText(_translate("Main_Window", "02", None))
        self.silver03.setText(_translate("Main_Window", "03", None))
        self.plt08.setText(_translate("Main_Window", "08", None))
        self.plt22.setText(_translate("Main_Window", "22", None))
        self.gold10.setText(_translate("Main_Window", "10", None))
        self.label1_2.setToolTip(_translate("Main_Window", "Instructions", None))
        self.label1_2.setWhatsThis(_translate("Main_Window", "Instructions", None))
        self.label1_2.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">*Select the desired seats by clicking on the corresponding seat number.</span></p><p><span style=\" font-size:12pt; font-weight:600;\">*Deselect the seat by again clicking on it.</span></p><p><span style=\" font-size:12pt; font-weight:600;\">*No. of booked seats in a class are displayed in box above that class.</span></p></body></html>", None))
        self.plt12.setText(_translate("Main_Window", "12", None))
        self.silver16.setText(_translate("Main_Window", "16", None))
        self.silver13.setText(_translate("Main_Window", "13", None))
        self.gold25.setText(_translate("Main_Window", "25", None))
        self.gold11.setText(_translate("Main_Window", "11", None))
        self.plt17.setText(_translate("Main_Window", "17", None))
        self.plt21.setText(_translate("Main_Window", "21", None))
        self.gold17.setText(_translate("Main_Window", "17", None))
        self.gold22.setText(_translate("Main_Window", "22", None))
        self.plt25.setText(_translate("Main_Window", "25", None))
        self.gold19.setText(_translate("Main_Window", "19", None))
        self.silver05.setText(_translate("Main_Window", "05", None))
        self.gold15.setText(_translate("Main_Window", "15", None))
        self.Cancel_2.setText(_translate("Main_Window", "Cancel", None))
        self.gold09.setText(_translate("Main_Window", "09", None))
        self.silver12.setText(_translate("Main_Window", "12", None))
        self.gold03.setText(_translate("Main_Window", "03", None))
        self.plt01.setText(_translate("Main_Window", "01", None))
        self.gold24.setText(_translate("Main_Window", "24", None))
        self.gold23.setText(_translate("Main_Window", "23", None))
        self.gold05.setText(_translate("Main_Window", "05", None))
        self.silver01.setText(_translate("Main_Window", "01", None))
        self.silver10.setText(_translate("Main_Window", "10", None))
        self.label2_2.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">No. of seats-</span></p></body></html>", None))
        self.plt20.setText(_translate("Main_Window", "20", None))
        self.silver15.setText(_translate("Main_Window", "15", None))
        self.silver22.setText(_translate("Main_Window", "22", None))
        self.gold12.setText(_translate("Main_Window", "12", None))
        self.silver09.setText(_translate("Main_Window", "09", None))
        self.silver11.setText(_translate("Main_Window", "11", None))
        self.plt02.setText(_translate("Main_Window", "02", None))
        self.gold01.setText(_translate("Main_Window", "01", None))
        self.plt03.setText(_translate("Main_Window", "03", None))
        self.silver21.setText(_translate("Main_Window", "21", None))
        self.silver18.setText(_translate("Main_Window", "18", None))
        self.silver25.setText(_translate("Main_Window", "25", None))
        self.silver14.setText(_translate("Main_Window", "14", None))
        self.gold04.setText(_translate("Main_Window", "04", None))
        self.plt10.setText(_translate("Main_Window", "10", None))
        self.OK_2.setText(_translate("Main_Window", "OK", None))
        self.plt09.setText(_translate("Main_Window", "09", None))
        self.silver02.setText(_translate("Main_Window", "02", None))
        self.silver08.setText(_translate("Main_Window", "08", None))
        self.gold14.setText(_translate("Main_Window", "14", None))
        self.silver17.setText(_translate("Main_Window", "17", None))
        self.silver07.setText(_translate("Main_Window", "07", None))
        self.silver23.setText(_translate("Main_Window", "23", None))
        self.plt18.setText(_translate("Main_Window", "18", None))
        self.plt24.setText(_translate("Main_Window", "24", None))
        self.plt16.setText(_translate("Main_Window", "16", None))
        self.silver19.setText(_translate("Main_Window", "19", None))
        self.plt13.setText(_translate("Main_Window", "13", None))
        self.plt23.setText(_translate("Main_Window", "23", None))
        self.plt07.setText(_translate("Main_Window", "07", None))
        self.silver24.setText(_translate("Main_Window", "24", None))
        self.silver04.setText(_translate("Main_Window", "04", None))
        self.gold08.setText(_translate("Main_Window", "08", None))
        self.plt19.setText(_translate("Main_Window", "19", None))
        self.plt04.setText(_translate("Main_Window", "04", None))
        self.plt11.setText(_translate("Main_Window", "11", None))
        self.Button_silver_2.setText(_translate("Main_Window", "SILVER", None))
        self.Button_gold_2.setText(_translate("Main_Window", "GOLD", None))
        self.Button_platinum_2.setText(_translate("Main_Window", "PLATINUM", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_7), _translate("Main_Window", "Seats", None))
        self.label4_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt;\">Phone No.(Optional)</span></p></body></html>", None))
        self.lineEdit2_3.setPlaceholderText(_translate("Main_Window", "Enter e-mail id", None))
        self.lineEdit3_3.setPlaceholderText(_translate("Main_Window", "Enter Phone No.", None))
        self.Cancel_3.setText(_translate("Main_Window", "Exit", None))
        self.generateTicket_3.setText(_translate("Main_Window", "Generate Ticket", None))
        self.label3_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt;\">Email Id(Optional)</span></p></body></html>", None))
        self.label2_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt;\">Name</span></p></body></html>", None))
        self.label1_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">P</span><span style=\" font-size:16pt; font-weight:600;\">ERSONAL</span><span style=\" font-size:22pt; font-weight:600;\"> D</span><span style=\" font-size:18pt; font-weight:600;\">ETAILS </span></p></body></html>", None))
        self.lineEdit1_3.setPlaceholderText(_translate("Main_Window", "Enter full name", None))
        self.LABEL15_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">10</span></p></body></html>", None))
        self.label5_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">COST</span></p></body></html>", None))
        self.label7_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Tickets Cost(S+G+P)</span></p></body></html>", None))
        self.label9_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Entertainment Tax(20%)</span></p></body></html>", None))
        self.LABEL12_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">00</span></p></body></html>", None))
        self.label10_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">TOTAL-</span></p></body></html>", None))
        self.LABEL14_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">20</span></p></body></html>", None))
        self.label11_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Thank You for visiting </span><span style=\" font-size:12pt; font-weight:600;\">VITPLEX</span><span style=\" font-size:12pt;\">!</span></p></body></html>", None))
        self.label8_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Service Tax(15%)</span></p></body></html>", None))
        self.label6_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Number of Seats =</span></p></body></html>", None))
        self.LABEL13_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">00</span></p></body></html>", None))
        self.LABEL16_3.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">00</span></p></body></html>", None))
        self.label_18.setText(_translate("Main_Window", "-----------------------------------------------------------------------------------", None))
        self.label_27.setText(_translate("Main_Window", "-----------------------------------------------------------------------------------", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_8), _translate("Main_Window", "Personal Details", None))
        self.Time.setToolTip(_translate("Main_Window", "Time", None))
        self.Time.setWhatsThis(_translate("Main_Window", "Time", None))
        self.Time.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">00:00</span></p></body></html>", None))
        self.Date.setToolTip(_translate("Main_Window", "Date", None))
        self.Date.setWhatsThis(_translate("Main_Window", "Date", None))
        self.Date.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">11/11/11</span></p></body></html>", None))
        self.Date_label.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt;\">--Date</span></p></body></html>", None))
        self.Time_label.setText(_translate("Main_Window", "<html><head/><body><p><span style=\" font-size:14pt;\">Time--</span></p></body></html>", None))
        self.menuAbout.setTitle(_translate("Main_Window", "About", None))
        self.actionFont_Designer.setText(_translate("Main_Window", "Change Font Style", None))
        self.actionChange_Background_color.setText(_translate("Main_Window", "Change Background color", None))
        self.actionDevelopers.setText(_translate("Main_Window", "Developers", None))

class MyDialog(Ui_Main_Window):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        #Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(529, 201)
        #self.setGeometry(300,300,541,221)
        #self.mainMenu = self.menuBar()

        #self.mainMenu.setNativeMenuBar(False)
        self.saveFile = QtGui.QAction("&Save File", self)
        self.saveFile.setShortcut("Ctrl+S")
        self.saveFile.setStatusTip('Save File')
        self.saveFile.triggered.connect(self.file_save)

        self.now = datetime.datetime.now()
        self.setWindowTitle("TICKET")
        self.move(490,270)
        self.label_19 = QtGui.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(-10, 0, 541, 201))
        self.label_19.setText(_fromUtf8(""))
        self.label_19.setPixmap(QtGui.QPixmap(_fromUtf8("ticket_resized2.jpg")))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(210, 30, 151, 41))
        self.label.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"font-size:20pt;\n"
"font-weight:bold;\n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 29, 100, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setStyleSheet("font-size:12px; color:white; font-weight:bold;")
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(390, 30, 61, 31))
        self.label_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(80, 75, 61, 21))
        self.label_4.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:13px;\n"
"color:black;\n"
"}"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(160, 76, 59, 20))
        self.label_5.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(230, 77, 59, 21))
        self.label_6.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(310, 76, 59, 20))
        self.label_7.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(360, 70, 91, 31))
        self.label_8.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"color:black;\n"
"}"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(150, 20, 211, 20))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(150, 60, 211, 21))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(140, 80, 16, 91))
        self.line_3.setFrameShadow(QtGui.QFrame.Plain)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(200, 80, 16, 91))
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(290, 80, 16, 91))
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self)
        self.line_6.setGeometry(QtCore.QRect(340, 80, 16, 91))
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(70, 80, 81, 101))
        self.label_9.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(158, 120, 61, 20))
        self.label_10.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(230, 110, 71, 41))
        self.label_11.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(310, 120, 59, 14))
        self.label_12.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(360, 110, 59, 14))
        self.label_13.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(360, 130, 59, 14))
        self.label_14.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(360, 150, 59, 14))
        self.label_15.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(430, 110, 59, 14))
        self.label_16.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(430, 130, 59, 14))
        self.label_17.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(430, 150, 59, 14))
        self.label_18.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font-size:12pt;\n"
"}"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.line_7 = QtGui.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(140, 30, 16, 41))
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self)
        self.line_8.setGeometry(QtCore.QRect(350, 30, 16, 41))
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)
        self.setTicket()

        self.save_button=QtGui.QPushButton(self)
        self.save_button.setGeometry(220,170,120,30)
        self.save_button.clicked.connect(self.file_save)
        self.save_button.setText("SAVE TICKET")
        self.save_button.setStyleSheet("background-color:black; color:white; font-weight:bold;")

    def file_save(self):
        self.name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        self.file = open(self.name, 'w')
        self.text = self.textEdit.toPlainText()
        self.file.write(self.text)
        self.file.close()

    def setTicket(self):
        #NAME
        self.name = ui.lineEdit1_3.text()
        self.label_9.setText("%s"%self.name)

        #Cost
        self.cost = ui.totalCost
        self.label_10.setText("Rs.%d"%(self.cost))

        #TIME
        self.label_3.setText(QtCore.QTime.currentTime().toString())

        #DATE
        self.date = QtCore.QDate.currentDate().toString()
        self.label_2.setText("%s" % (self.date))

        #SHOW and TIME
        if self.now.hour<9 or self.now.hour>=19:
            self.label_11.setText("Suicide\nSquad")
            self.label_12.setText("09:00")
        elif 9<=self.now.hour<12:
            self.label_11.setText("Gone\nGirl")
            self.label_12.setText("12:00")
        elif 12<=self.now.hour<15:
            self.label_11.setText("The\nConjuring")
            self.label_12.setText("15:00")
        elif 15<=self.now.hour<19:
            self.label_11.setText("The\nRush")
            self.label_12.setText("19:00")

        #Number of seats
        self.label_16.setText("%d"%(ui.silver))
        self.label_17.setText("%d" % (ui.gold))
        self.label_18.setText("%d" % (ui.plt))

    def retranslateUi(self):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        #print ui.gold
        self.label.setText(_translate("Form", "<html><head/><body><p>                                      VITPLEX</p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Date</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Time</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline;\">NAME</span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline;\">COST</span></p></body></html>", None))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline;\">SHOW</span></p></body></html>", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline;\">TIME</span></p></body></html>", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline;\">NO. OF SEATS</span></p></body></html>", None))
        self.label_9.setText(_translate("Form", "<html><head/><body><p>Saumay </p><p>Khandelwal</p></body></html>", None))
        self.label_10.setText(_translate("Form", "Rs. 000", None))
        self.label_11.setText(_translate("Form", "<html><head/><body><p>Suicide </p><p>Squad</p></body></html>", None))
        self.label_12.setText(_translate("Form", "00:00", None))
        self.label_13.setText(_translate("Form", "Silver", None))
        self.label_14.setText(_translate("Form", "Gold", None))
        self.label_15.setText(_translate("Form", "Platinum", None))
        self.label_16.setText(_translate("Form", "00", None))
        self.label_17.setText(_translate("Form", "00", None))
        self.label_18.setText(_translate("Form", "00", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Main_Window = QtGui.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())