# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_controller_dialog.ui'
#
# Created: Mon Oct 20 17:35:27 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(403, 184)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 150, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 131))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.controller_type_combo = QtGui.QComboBox(self.formLayoutWidget)
        self.controller_type_combo.setObjectName(_fromUtf8("controller_type_combo"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.controller_type_combo)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.controller_name_text = QtGui.QLineEdit(self.formLayoutWidget)
        self.controller_name_text.setObjectName(_fromUtf8("controller_name_text"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.controller_name_text)
        self.ip_address_label = QtGui.QLabel(self.formLayoutWidget)
        self.ip_address_label.setObjectName(_fromUtf8("ip_address_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.ip_address_label)
        self.port_label = QtGui.QLabel(self.formLayoutWidget)
        self.port_label.setEnabled(False)
        self.port_label.setObjectName(_fromUtf8("port_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.port_label)
        self.ip_address_text = QtGui.QLineEdit(self.formLayoutWidget)
        self.ip_address_text.setObjectName(_fromUtf8("ip_address_text"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.ip_address_text)
        self.port_text = QtGui.QLineEdit(self.formLayoutWidget)
        self.port_text.setEnabled(False)
        self.port_text.setObjectName(_fromUtf8("port_text"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.port_text)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Change/add controller", None))
        self.label.setText(_translate("Dialog", "Controller type", None))
        self.label_2.setText(_translate("Dialog", "Controller name", None))
        self.ip_address_label.setText(_translate("Dialog", "IP address", None))
        self.port_label.setText(_translate("Dialog", "Port", None))

