# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Oct 20 14:59:23 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.main_tabbed_pane = QtGui.QTabWidget(self.centralwidget)
        self.main_tabbed_pane.setGeometry(QtCore.QRect(10, 10, 781, 531))
        self.main_tabbed_pane.setObjectName(_fromUtf8("main_tabbed_pane"))
        self.execute_tab = QtGui.QWidget()
        self.execute_tab.setObjectName(_fromUtf8("execute_tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.execute_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.source_code_editor = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.source_code_editor.setObjectName(_fromUtf8("source_code_editor"))
        self.verticalLayout.addWidget(self.source_code_editor)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.error_message_label = QtGui.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 141, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.error_message_label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error_message_label.setFont(font)
        self.error_message_label.setText(_fromUtf8(""))
        self.error_message_label.setObjectName(_fromUtf8("error_message_label"))
        self.horizontalLayout_2.addWidget(self.error_message_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.execute_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.execute_button.setObjectName(_fromUtf8("execute_button"))
        self.horizontalLayout_2.addWidget(self.execute_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.input_text_edit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.input_text_edit.setObjectName(_fromUtf8("input_text_edit"))
        self.verticalLayout_2.addWidget(self.input_text_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.output_text_edit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.output_text_edit.setObjectName(_fromUtf8("output_text_edit"))
        self.verticalLayout_3.addWidget(self.output_text_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.main_tabbed_pane.addTab(self.execute_tab, _fromUtf8(""))
        self.setup_tab = QtGui.QWidget()
        self.setup_tab.setObjectName(_fromUtf8("setup_tab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.setup_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 481))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.controller_list_view = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.controller_list_view.setObjectName(_fromUtf8("controller_list_view"))
        self.verticalLayout_4.addWidget(self.controller_list_view)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.add_controller_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.add_controller_button.setObjectName(_fromUtf8("add_controller_button"))
        self.horizontalLayout_4.addWidget(self.add_controller_button)
        self.remove_controller_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.remove_controller_button.setObjectName(_fromUtf8("remove_controller_button"))
        self.horizontalLayout_4.addWidget(self.remove_controller_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.input_list_view = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.input_list_view.setObjectName(_fromUtf8("input_list_view"))
        self.verticalLayout_5.addWidget(self.input_list_view)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.add_input_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.add_input_button.setObjectName(_fromUtf8("add_input_button"))
        self.horizontalLayout_5.addWidget(self.add_input_button)
        self.remove_input_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.remove_input_button.setObjectName(_fromUtf8("remove_input_button"))
        self.horizontalLayout_5.addWidget(self.remove_input_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_6.addWidget(self.label_5)
        self.output_list_view = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.output_list_view.setObjectName(_fromUtf8("output_list_view"))
        self.verticalLayout_6.addWidget(self.output_list_view)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.add_output_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.add_output_button.setObjectName(_fromUtf8("add_output_button"))
        self.horizontalLayout_6.addWidget(self.add_output_button)
        self.remove_output_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.remove_output_button.setObjectName(_fromUtf8("remove_output_button"))
        self.horizontalLayout_6.addWidget(self.remove_output_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.main_tabbed_pane.addTab(self.setup_tab, _fromUtf8(""))
        self.about_tab = QtGui.QWidget()
        self.about_tab.setObjectName(_fromUtf8("about_tab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.about_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 751, 481))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_7.addWidget(self.label_6)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_7.addWidget(self.line)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_7.addWidget(self.label_8)
        self.main_tabbed_pane.addTab(self.about_tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDatei = QtGui.QMenu(self.menubar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName(_fromUtf8("actionBeenden"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuDatei.addAction(self.actionQuit)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        self.main_tabbed_pane.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.execute_button.setText(_translate("MainWindow", "Execute", None))
        self.label.setText(_translate("MainWindow", "Input:", None))
        self.label_2.setText(_translate("MainWindow", "Output:", None))
        self.main_tabbed_pane.setTabText(self.main_tabbed_pane.indexOf(self.execute_tab), _translate("MainWindow", "Execute code (ST)", None))
        self.label_3.setText(_translate("MainWindow", "Controller", None))
        self.add_controller_button.setText(_translate("MainWindow", "+", None))
        self.remove_controller_button.setText(_translate("MainWindow", "-", None))
        self.label_4.setText(_translate("MainWindow", "Inputs", None))
        self.add_input_button.setText(_translate("MainWindow", "+", None))
        self.remove_input_button.setText(_translate("MainWindow", "-", None))
        self.label_5.setText(_translate("MainWindow", "Outputs", None))
        self.add_output_button.setText(_translate("MainWindow", "+", None))
        self.remove_output_button.setText(_translate("MainWindow", "-", None))
        self.main_tabbed_pane.setTabText(self.main_tabbed_pane.indexOf(self.setup_tab), _translate("MainWindow", "Setup controller", None))
        self.label_6.setText(_translate("MainWindow", "SPotS", None))
        self.label_9.setText(_translate("MainWindow", "SoftPLC for using I/O controller via ModbusTCP", None))
        self.label_7.setText(_translate("MainWindow", "Author: Christian Wichmann", None))
        self.label_8.setText(_translate("MainWindow", "Licensed under GNU GPL v2 or newer.", None))
        self.main_tabbed_pane.setTabText(self.main_tabbed_pane.indexOf(self.about_tab), _translate("MainWindow", "About", None))
        self.menuDatei.setTitle(_translate("MainWindow", "File", None))
        self.actionBeenden.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

