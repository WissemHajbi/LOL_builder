# Form implementation generated from reading ui file 'c:\Users\wisse\projects\LOL Builder\a.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1222, 832)
        Form.setStyleSheet("QWidget {\n"
"    background-color:#1F1B24;\n"
"}\n"
"")
        self.l2 = QtWidgets.QLabel(Form)
        self.l2.setGeometry(QtCore.QRect(620, 280, 71, 61))
        self.l2.setText("")
        self.l2.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l2.setScaledContents(True)
        self.l2.setObjectName("l2")
        self.pushButtonSearch1 = QtWidgets.QPushButton(Form)
        self.pushButtonSearch1.setGeometry(QtCore.QRect(485, 29, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearch1.setFont(font)
        self.pushButtonSearch1.setStyleSheet("QPushButton {\n"
"    background-color:#FF0266;\n"
"    color:#1F1B24;\n"
"}")
        self.pushButtonSearch1.setObjectName("pushButtonSearch1")
        self.errorsLabel = QtWidgets.QLabel(Form)
        self.errorsLabel.setGeometry(QtCore.QRect(280, 110, 161, 31))
        self.errorsLabel.setStyleSheet("")
        self.errorsLabel.setText("")
        self.errorsLabel.setObjectName("errorsLabel")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 23, 203, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.labelname.setFont(font)
        self.labelname.setStyleSheet("QLabel {\n"
"    color:#FFFFFF;\n"
"}")
        self.labelname.setObjectName("labelname")
        self.horizontalLayout_2.addWidget(self.labelname)
        self.lineName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineName.setFont(font)
        self.lineName.setStyleSheet("QLineEdit {\n"
"    color:#FFFFFF;\n"
"}")
        self.lineName.setObjectName("lineName")
        self.horizontalLayout_2.addWidget(self.lineName)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(154, 17, 101, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.role1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.role1.setFont(font)
        self.role1.setStyleSheet("QLabel {\n"
"    color:#FFFFFF;\n"
"}")
        self.role1.setText("")
        self.role1.setObjectName("role1")
        self.verticalLayout.addWidget(self.role1)
        self.role2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.role2.setFont(font)
        self.role2.setStyleSheet("QLabel {\n"
"    color:#FFFFFF;\n"
"}")
        self.role2.setText("")
        self.role2.setObjectName("role2")
        self.verticalLayout.addWidget(self.role2)
        self.role3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.role3.setFont(font)
        self.role3.setStyleSheet("QLabel {\n"
"    color:#FFFFFF;\n"
"}")
        self.role3.setText("")
        self.role3.setObjectName("role3")
        self.verticalLayout.addWidget(self.role3)
        self.rolesymbol1 = QtWidgets.QLabel(Form)
        self.rolesymbol1.setGeometry(QtCore.QRect(110, 21, 30, 30))
        self.rolesymbol1.setText("")
        self.rolesymbol1.setScaledContents(True)
        self.rolesymbol1.setObjectName("rolesymbol1")
        self.rolesymbol2 = QtWidgets.QLabel(Form)
        self.rolesymbol2.setGeometry(QtCore.QRect(110, 61, 30, 30))
        self.rolesymbol2.setText("")
        self.rolesymbol2.setScaledContents(True)
        self.rolesymbol2.setObjectName("rolesymbol2")
        self.rolesymbol3 = QtWidgets.QLabel(Form)
        self.rolesymbol3.setGeometry(QtCore.QRect(110, 103, 30, 30))
        self.rolesymbol3.setText("")
        self.rolesymbol3.setScaledContents(True)
        self.rolesymbol3.setObjectName("rolesymbol3")
        self.l9 = QtWidgets.QLabel(Form)
        self.l9.setGeometry(QtCore.QRect(730, 430, 35, 35))
        self.l9.setText("")
        self.l9.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l9.setScaledContents(True)
        self.l9.setObjectName("l9")
        self.l10 = QtWidgets.QLabel(Form)
        self.l10.setGeometry(QtCore.QRect(730, 480, 35, 35))
        self.l10.setText("")
        self.l10.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l10.setScaledContents(True)
        self.l10.setObjectName("l10")
        self.l3 = QtWidgets.QLabel(Form)
        self.l3.setGeometry(QtCore.QRect(630, 360, 51, 51))
        self.l3.setText("")
        self.l3.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l3.setScaledContents(True)
        self.l3.setObjectName("l3")
        self.l7 = QtWidgets.QLabel(Form)
        self.l7.setGeometry(QtCore.QRect(720, 290, 51, 51))
        self.l7.setText("")
        self.l7.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l7.setScaledContents(True)
        self.l7.setObjectName("l7")
        self.l8 = QtWidgets.QLabel(Form)
        self.l8.setGeometry(QtCore.QRect(720, 360, 51, 51))
        self.l8.setText("")
        self.l8.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l8.setScaledContents(True)
        self.l8.setObjectName("l8")
        self.l4 = QtWidgets.QLabel(Form)
        self.l4.setGeometry(QtCore.QRect(630, 430, 51, 51))
        self.l4.setText("")
        self.l4.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l4.setScaledContents(True)
        self.l4.setObjectName("l4")
        self.l5 = QtWidgets.QLabel(Form)
        self.l5.setGeometry(QtCore.QRect(630, 500, 51, 51))
        self.l5.setText("")
        self.l5.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l5.setScaledContents(True)
        self.l5.setObjectName("l5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(640, 140, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.sum1 = QtWidgets.QLabel(Form)
        self.sum1.setGeometry(QtCore.QRect(290, 190, 30, 30))
        self.sum1.setText("")
        self.sum1.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\abilities/1.jpg"))
        self.sum1.setScaledContents(True)
        self.sum1.setObjectName("sum1")
        self.sum2 = QtWidgets.QLabel(Form)
        self.sum2.setGeometry(QtCore.QRect(330, 190, 30, 30))
        self.sum2.setText("")
        self.sum2.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\abilities/2.jpg"))
        self.sum2.setScaledContents(True)
        self.sum2.setObjectName("sum2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 235, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.ab1 = QtWidgets.QLabel(Form)
        self.ab1.setGeometry(QtCore.QRect(290, 285, 30, 30))
        self.ab1.setText("")
        self.ab1.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\abilities/1.jpg"))
        self.ab1.setScaledContents(True)
        self.ab1.setObjectName("ab1")
        self.ab2 = QtWidgets.QLabel(Form)
        self.ab2.setGeometry(QtCore.QRect(345, 285, 30, 30))
        self.ab2.setText("")
        self.ab2.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\abilities/2.jpg"))
        self.ab2.setScaledContents(True)
        self.ab2.setObjectName("ab2")
        self.ab3 = QtWidgets.QLabel(Form)
        self.ab3.setGeometry(QtCore.QRect(400, 285, 30, 30))
        self.ab3.setText("")
        self.ab3.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\abilities and Summoners/5.jpg"))
        self.ab3.setScaledContents(True)
        self.ab3.setObjectName("ab3")
        self.abdash1 = QtWidgets.QLabel(Form)
        self.abdash1.setGeometry(QtCore.QRect(325, 290, 15, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.abdash1.setFont(font)
        self.abdash1.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.abdash1.setText("")
        self.abdash1.setObjectName("abdash1")
        self.abdash2 = QtWidgets.QLabel(Form)
        self.abdash2.setGeometry(QtCore.QRect(380, 290, 15, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.abdash2.setFont(font)
        self.abdash2.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.abdash2.setText("")
        self.abdash2.setObjectName("abdash2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 440, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.l6 = QtWidgets.QLabel(Form)
        self.l6.setGeometry(QtCore.QRect(710, 200, 41, 41))
        self.l6.setText("")
        self.l6.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l6.setScaledContents(True)
        self.l6.setObjectName("l6")
        self.l1 = QtWidgets.QLabel(Form)
        self.l1.setGeometry(QtCore.QRect(630, 200, 41, 41))
        self.l1.setText("")
        self.l1.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l1.setScaledContents(True)
        self.l1.setObjectName("l1")
        self.l11 = QtWidgets.QLabel(Form)
        self.l11.setGeometry(QtCore.QRect(730, 530, 35, 35))
        self.l11.setText("")
        self.l11.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.l11.setScaledContents(True)
        self.l11.setObjectName("l11")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 340, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"    color:#FF0266;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.sitem2 = QtWidgets.QLabel(Form)
        self.sitem2.setGeometry(QtCore.QRect(150, 400, 39, 39))
        self.sitem2.setText("")
        self.sitem2.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\profile.jpg"))
        self.sitem2.setScaledContents(True)
        self.sitem2.setObjectName("sitem2")
        self.sitem1 = QtWidgets.QLabel(Form)
        self.sitem1.setGeometry(QtCore.QRect(100, 400, 39, 39))
        self.sitem1.setText("")
        self.sitem1.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.sitem1.setScaledContents(True)
        self.sitem1.setObjectName("sitem1")
        self.sitem3 = QtWidgets.QLabel(Form)
        self.sitem3.setGeometry(QtCore.QRect(200, 400, 39, 39))
        self.sitem3.setText("")
        self.sitem3.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.sitem3.setScaledContents(True)
        self.sitem3.setObjectName("sitem3")
        self.sitem4 = QtWidgets.QLabel(Form)
        self.sitem4.setGeometry(QtCore.QRect(250, 400, 39, 39))
        self.sitem4.setText("")
        self.sitem4.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.sitem4.setScaledContents(True)
        self.sitem4.setObjectName("sitem4")
        self.item1 = QtWidgets.QLabel(Form)
        self.item1.setGeometry(QtCore.QRect(100, 510, 45, 45))
        self.item1.setText("")
        self.item1.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.item1.setScaledContents(True)
        self.item1.setObjectName("item1")
        self.item2 = QtWidgets.QLabel(Form)
        self.item2.setGeometry(QtCore.QRect(165, 510, 45, 45))
        self.item2.setText("")
        self.item2.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.item2.setScaledContents(True)
        self.item2.setObjectName("item2")
        self.item3 = QtWidgets.QLabel(Form)
        self.item3.setGeometry(QtCore.QRect(230, 510, 45, 45))
        self.item3.setText("")
        self.item3.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.item3.setScaledContents(True)
        self.item3.setObjectName("item3")
        self.item4 = QtWidgets.QLabel(Form)
        self.item4.setGeometry(QtCore.QRect(300, 510, 45, 45))
        self.item4.setText("")
        self.item4.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.item4.setScaledContents(True)
        self.item4.setObjectName("item4")
        self.item5 = QtWidgets.QLabel(Form)
        self.item5.setGeometry(QtCore.QRect(370, 510, 45, 45))
        self.item5.setText("")
        self.item5.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.item5.setScaledContents(True)
        self.item5.setObjectName("item5")
        self.item6 = QtWidgets.QLabel(Form)
        self.item6.setGeometry(QtCore.QRect(440, 510, 45, 45))
        self.item6.setText("")
        self.item6.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\x.png"))
        self.item6.setScaledContents(True)
        self.item6.setObjectName("item6")
        self.pushButtonSearch2 = QtWidgets.QPushButton(Form)
        self.pushButtonSearch2.setGeometry(QtCore.QRect(463, 70, 103, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearch2.setFont(font)
        self.pushButtonSearch2.setStyleSheet("QPushButton {\n"
"    background-color:#FF0266;\n"
"    color:#1F1B24;\n"
"}")
        self.pushButtonSearch2.setObjectName("pushButtonSearch2")
        self.labelrole = QtWidgets.QLabel(Form)
        self.labelrole.setGeometry(QtCore.QRect(303, 70, 42, 39))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(14)
        self.labelrole.setFont(font)
        self.labelrole.setStyleSheet("QLabel {\n"
"    color:#FFFFFF;\n"
"}")
        self.labelrole.setObjectName("labelrole")
        self.lineRole = QtWidgets.QLineEdit(Form)
        self.lineRole.setGeometry(QtCore.QRect(360, 75, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineRole.setFont(font)
        self.lineRole.setStyleSheet("QLineEdit {\n"
"    color:#FFFFFF;\n"
"}")
        self.lineRole.setObjectName("lineRole")
        self.ProfilePicLabel = QtWidgets.QLabel(Form)
        self.ProfilePicLabel.setGeometry(QtCore.QRect(100, 160, 141, 141))
        self.ProfilePicLabel.setText("")
        self.ProfilePicLabel.setPixmap(QtGui.QPixmap("c:\\Users\\wisse\\projects\\LOL Builder\\profile.jpg"))
        self.ProfilePicLabel.setScaledContents(True)
        self.ProfilePicLabel.setObjectName("ProfilePicLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonSearch1.setText(_translate("Form", "Roles search"))
        self.labelname.setText(_translate("Form", "Champion"))
        self.lineName.setText(_translate("Form", "sylas"))
        self.label.setText(_translate("Form", "Runes"))
        self.label_2.setText(_translate("Form", "Summoner spells"))
        self.label_3.setText(_translate("Form", "Skill leveling"))
        self.label_4.setText(_translate("Form", "Full build"))
        self.label_5.setText(_translate("Form", "Strating items"))
        self.pushButtonSearch2.setText(_translate("Form", "Build"))
        self.labelrole.setText(_translate("Form", "Role"))
        self.lineRole.setText(_translate("Form", "mid"))
