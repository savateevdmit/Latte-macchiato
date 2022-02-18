from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(493, 398)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 201, 41))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.varietyName = QLineEdit(Form)
        self.varietyName.setObjectName(u"varietyName")
        self.varietyName.setGeometry(QRect(210, 20, 271, 41))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 161, 41))
        self.label_3.setFont(font)
        self.degreeOfRoast = QLineEdit(Form)
        self.degreeOfRoast.setObjectName(u"degreeOfRoast")
        self.degreeOfRoast.setGeometry(QRect(210, 70, 271, 41))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 170, 161, 41))
        self.label_4.setFont(font)
        self.groundOrBeans = QLineEdit(Form)
        self.groundOrBeans.setObjectName(u"groundOrBeans")
        self.groundOrBeans.setGeometry(QRect(210, 120, 271, 41))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 120, 161, 41))
        self.label_5.setFont(font)
        self.description = QLineEdit(Form)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(210, 170, 271, 41))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 216, 161, 41))
        self.label_6.setFont(font)
        self.price = QLineEdit(Form)
        self.price.setObjectName(u"price")
        self.price.setGeometry(QRect(210, 220, 271, 41))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 270, 161, 41))
        self.label_7.setFont(font)
        self.volume = QLineEdit(Form)
        self.volume.setObjectName(u"volume")
        self.volume.setGeometry(QRect(210, 270, 271, 41))
        self.add = QPushButton(Form)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(290, 340, 191, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0444\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u043b\u043e\u0442\u044b\u0439/\u0412 \u0437\u0451\u0440\u043d\u0430\u0445", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0451\u043c \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438", None))
        self.add.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi