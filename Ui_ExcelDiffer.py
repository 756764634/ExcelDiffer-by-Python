# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExcelDiffer_v2.0.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_ExcelDiffer(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1419, 733)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mainWindowLayout = QtGui.QGridLayout()
        self.mainWindowLayout.setObjectName(_fromUtf8("mainWindowLayout"))
        self.resultViewLayout = QtGui.QGridLayout()
        self.resultViewLayout.setObjectName(_fromUtf8("resultViewLayout"))
        self.SheetAddDelLayout = QtGui.QGridLayout()
        self.SheetAddDelLayout.setObjectName(_fromUtf8("SheetAddDelLayout"))
        self.SheetAddDelLabel = QtGui.QLabel(Form)
        self.SheetAddDelLabel.setStyleSheet(_fromUtf8("font: 12pt \"楷体\";\n"
"background-color: rgb(85, 255, 127);"))
        self.SheetAddDelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SheetAddDelLabel.setObjectName(_fromUtf8("SheetAddDelLabel"))
        self.SheetAddDelLayout.addWidget(self.SheetAddDelLabel, 0, 0, 1, 1)
        self.sheetAddDelTabWidget = QtGui.QTabWidget(Form)
        self.sheetAddDelTabWidget.setStyleSheet(_fromUtf8("font: 12pt \"楷体\";"))
        self.sheetAddDelTabWidget.setObjectName(_fromUtf8("sheetAddDelTabWidget"))
        self.sheetListTab = QtGui.QWidget()
        self.sheetListTab.setObjectName(_fromUtf8("sheetListTab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.sheetListTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.sheetListLabel = QtGui.QLabel(self.sheetListTab)
        self.sheetListLabel.setObjectName(_fromUtf8("sheetListLabel"))
        self.gridLayout_3.addWidget(self.sheetListLabel, 0, 0, 1, 1)
        self.sheetListTableWidget = QtGui.QTableWidget(self.sheetListTab)
        self.sheetListTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.sheetListTableWidget.setObjectName(_fromUtf8("sheetListTableWidget"))
        self.sheetListTableWidget.setColumnCount(1)
        self.sheetListTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.sheetListTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.sheetListTableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_3.addWidget(self.sheetListTableWidget, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.sheetAddDelTabWidget.addTab(self.sheetListTab, _fromUtf8(""))
        self.sheetAddTab = QtGui.QWidget()
        self.sheetAddTab.setObjectName(_fromUtf8("sheetAddTab"))
        self.gridLayout_9 = QtGui.QGridLayout(self.sheetAddTab)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.sheetAddLabel = QtGui.QLabel(self.sheetAddTab)
        self.sheetAddLabel.setObjectName(_fromUtf8("sheetAddLabel"))
        self.gridLayout_4.addWidget(self.sheetAddLabel, 0, 0, 1, 1)
        self.sheetAddTableWidget = QtGui.QTableWidget(self.sheetAddTab)
        self.sheetAddTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.sheetAddTableWidget.setObjectName(_fromUtf8("sheetAddTableWidget"))
        self.sheetAddTableWidget.setColumnCount(1)
        self.sheetAddTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.sheetAddTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.sheetAddTableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_4.addWidget(self.sheetAddTableWidget, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.sheetAddDelTabWidget.addTab(self.sheetAddTab, _fromUtf8(""))
        self.delSheetTab = QtGui.QWidget()
        self.delSheetTab.setObjectName(_fromUtf8("delSheetTab"))
        self.gridLayout_10 = QtGui.QGridLayout(self.delSheetTab)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.sheetDelLabel = QtGui.QLabel(self.delSheetTab)
        self.sheetDelLabel.setObjectName(_fromUtf8("sheetDelLabel"))
        self.gridLayout_5.addWidget(self.sheetDelLabel, 0, 0, 1, 1)
        self.sheetDelTableWidget = QtGui.QTableWidget(self.delSheetTab)
        self.sheetDelTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.sheetDelTableWidget.setObjectName(_fromUtf8("sheetDelTableWidget"))
        self.sheetDelTableWidget.setColumnCount(1)
        self.sheetDelTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.sheetDelTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.sheetDelTableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_5.addWidget(self.sheetDelTableWidget, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.sheetAddDelTabWidget.addTab(self.delSheetTab, _fromUtf8(""))
        self.SheetAddDelLayout.addWidget(self.sheetAddDelTabWidget, 1, 0, 1, 1)
        self.SheetAddDelLayout.setRowStretch(0, 1)
        self.SheetAddDelLayout.setRowStretch(1, 10)
        self.resultViewLayout.addLayout(self.SheetAddDelLayout, 0, 0, 1, 1)
        self.sheetResultLayout = QtGui.QGridLayout()
        self.sheetResultLayout.setObjectName(_fromUtf8("sheetResultLayout"))
        self.sheetResultLabel = QtGui.QLabel(Form)
        self.sheetResultLabel.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);\n"
"font: 12pt \"楷体\";"))
        self.sheetResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sheetResultLabel.setObjectName(_fromUtf8("sheetResultLabel"))
        self.sheetResultLayout.addWidget(self.sheetResultLabel, 0, 0, 1, 1)
        self.sheetResultTabWidget = QtGui.QTabWidget(Form)
        self.sheetResultTabWidget.setStyleSheet(_fromUtf8("font: 12pt \"楷体\";"))
        self.sheetResultTabWidget.setObjectName(_fromUtf8("sheetResultTabWidget"))
        self.rowAddDelTab = QtGui.QWidget()
        self.rowAddDelTab.setObjectName(_fromUtf8("rowAddDelTab"))
        self.gridLayout_13 = QtGui.QGridLayout(self.rowAddDelTab)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.rowAddDelLabel = QtGui.QLabel(self.rowAddDelTab)
        self.rowAddDelLabel.setObjectName(_fromUtf8("rowAddDelLabel"))
        self.gridLayout_6.addWidget(self.rowAddDelLabel, 0, 0, 1, 1)
        self.rowAddDelTableWidget = QtGui.QTableWidget(self.rowAddDelTab)
        self.rowAddDelTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.rowAddDelTableWidget.setObjectName(_fromUtf8("rowAddDelTableWidget"))
        self.rowAddDelTableWidget.setColumnCount(1)
        self.rowAddDelTableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.rowAddDelTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.rowAddDelTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.rowAddDelTableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_6.addWidget(self.rowAddDelTableWidget, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.sheetResultTabWidget.addTab(self.rowAddDelTab, _fromUtf8(""))
        self.columnAddDelTab = QtGui.QWidget()
        self.columnAddDelTab.setObjectName(_fromUtf8("columnAddDelTab"))
        self.gridLayout_14 = QtGui.QGridLayout(self.columnAddDelTab)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.columnAddDelLabel = QtGui.QLabel(self.columnAddDelTab)
        self.columnAddDelLabel.setObjectName(_fromUtf8("columnAddDelLabel"))
        self.gridLayout_11.addWidget(self.columnAddDelLabel, 0, 0, 1, 1)
        self.columnAddDelTableWidget = QtGui.QTableWidget(self.columnAddDelTab)
        self.columnAddDelTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.columnAddDelTableWidget.setObjectName(_fromUtf8("columnAddDelTableWidget"))
        self.columnAddDelTableWidget.setColumnCount(1)
        self.columnAddDelTableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.columnAddDelTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.columnAddDelTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.columnAddDelTableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_11.addWidget(self.columnAddDelTableWidget, 1, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.sheetResultTabWidget.addTab(self.columnAddDelTab, _fromUtf8(""))
        self.cellModifyTab = QtGui.QWidget()
        self.cellModifyTab.setObjectName(_fromUtf8("cellModifyTab"))
        self.gridLayout_15 = QtGui.QGridLayout(self.cellModifyTab)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.cellModifyLabel = QtGui.QLabel(self.cellModifyTab)
        self.cellModifyLabel.setObjectName(_fromUtf8("cellModifyLabel"))
        self.gridLayout_12.addWidget(self.cellModifyLabel, 0, 0, 1, 1)
        self.cellModifyTableWidget = QtGui.QTableWidget(self.cellModifyTab)
        self.cellModifyTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.cellModifyTableWidget.setObjectName(_fromUtf8("cellModifyTableWidget"))
        self.cellModifyTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.cellModifyTableWidget.setColumnCount(3)
        self.cellModifyTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.cellModifyTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.cellModifyTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.cellModifyTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.cellModifyTableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_12.addWidget(self.cellModifyTableWidget, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.sheetResultTabWidget.addTab(self.cellModifyTab, _fromUtf8(""))
        self.sheetResultLayout.addWidget(self.sheetResultTabWidget, 1, 0, 1, 1)
        self.sheetResultLayout.setRowStretch(0, 1)
        self.sheetResultLayout.setRowStretch(1, 10)
        self.resultViewLayout.addLayout(self.sheetResultLayout, 0, 1, 1, 1)
        self.resultViewLayout.setColumnStretch(0, 1)
        self.resultViewLayout.setColumnStretch(1, 2)
        self.mainWindowLayout.addLayout(self.resultViewLayout, 1, 0, 1, 1)
        self.excelDifferLayout = QtGui.QGridLayout()
        self.excelDifferLayout.setObjectName(_fromUtf8("excelDifferLayout"))
        self.excelDifferOperateLayout = QtGui.QGridLayout()
        self.excelDifferOperateLayout.setObjectName(_fromUtf8("excelDifferOperateLayout"))
        self.excelFileChooseGroupBox = QtGui.QGroupBox(Form)
        self.excelFileChooseGroupBox.setStyleSheet(_fromUtf8("font: 12pt \"楷体\";"))
        self.excelFileChooseGroupBox.setObjectName(_fromUtf8("excelFileChooseGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.excelFileChooseGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.excelFileChooseLayout_2 = QtGui.QGridLayout()
        self.excelFileChooseLayout_2.setObjectName(_fromUtf8("excelFileChooseLayout_2"))
        self.operateLayout = QtGui.QGridLayout()
        self.operateLayout.setObjectName(_fromUtf8("operateLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.operateLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.refreshButton = QtGui.QPushButton(self.excelFileChooseGroupBox)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.operateLayout.addWidget(self.refreshButton, 0, 3, 1, 1)
        self.excelDiffButton = QtGui.QPushButton(self.excelFileChooseGroupBox)
        self.excelDiffButton.setObjectName(_fromUtf8("excelDiffButton"))
        self.operateLayout.addWidget(self.excelDiffButton, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.operateLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.operateLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.excelFileChooseLayout_2.addLayout(self.operateLayout, 1, 0, 1, 1)
        self.fileChooseLayout = QtGui.QGridLayout()
        self.fileChooseLayout.setObjectName(_fromUtf8("fileChooseLayout"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.fileChooseLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.fileChooseLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.originExcelLabel = QtGui.QLabel(self.excelFileChooseGroupBox)
        self.originExcelLabel.setObjectName(_fromUtf8("originExcelLabel"))
        self.fileChooseLayout.addWidget(self.originExcelLabel, 1, 0, 1, 1)
        self.newExcelChooseButton = QtGui.QPushButton(self.excelFileChooseGroupBox)
        self.newExcelChooseButton.setObjectName(_fromUtf8("newExcelChooseButton"))
        self.fileChooseLayout.addWidget(self.newExcelChooseButton, 3, 2, 1, 1)
        self.originExcelChooseButton = QtGui.QPushButton(self.excelFileChooseGroupBox)
        self.originExcelChooseButton.setObjectName(_fromUtf8("originExcelChooseButton"))
        self.fileChooseLayout.addWidget(self.originExcelChooseButton, 1, 2, 1, 1)
        self.newExcelLabel = QtGui.QLabel(self.excelFileChooseGroupBox)
        self.newExcelLabel.setObjectName(_fromUtf8("newExcelLabel"))
        self.fileChooseLayout.addWidget(self.newExcelLabel, 3, 0, 1, 1)
        self.originExcelUrlLineEdit = QtGui.QLineEdit(self.excelFileChooseGroupBox)
        self.originExcelUrlLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.originExcelUrlLineEdit.setObjectName(_fromUtf8("originExcelUrlLineEdit"))
        self.fileChooseLayout.addWidget(self.originExcelUrlLineEdit, 1, 1, 1, 1)
        self.newExcelUrlLineEdit = QtGui.QLineEdit(self.excelFileChooseGroupBox)
        self.newExcelUrlLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newExcelUrlLineEdit.setObjectName(_fromUtf8("newExcelUrlLineEdit"))
        self.fileChooseLayout.addWidget(self.newExcelUrlLineEdit, 3, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.fileChooseLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.fileChooseLayout.setRowStretch(0, 1)
        self.fileChooseLayout.setRowStretch(1, 1)
        self.fileChooseLayout.setRowStretch(2, 1)
        self.fileChooseLayout.setRowStretch(3, 1)
        self.fileChooseLayout.setRowStretch(4, 1)
        self.excelFileChooseLayout_2.addLayout(self.fileChooseLayout, 0, 0, 1, 1)
        self.excelFileChooseLayout_2.setRowStretch(0, 6)
        self.excelFileChooseLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.addLayout(self.excelFileChooseLayout_2, 0, 0, 1, 1)
        self.excelDifferOperateLayout.addWidget(self.excelFileChooseGroupBox, 0, 0, 1, 1)
        self.excelDifferLayout.addLayout(self.excelDifferOperateLayout, 0, 0, 1, 1)
        self.excelViewLayout = QtGui.QGridLayout()
        self.excelViewLayout.setObjectName(_fromUtf8("excelViewLayout"))
        self.newExcelSheetLabel = QtGui.QLabel(Form)
        self.newExcelSheetLabel.setStyleSheet(_fromUtf8("font: 12pt \"楷体\";\n"
"background-color: rgb(85, 170, 255);"))
        self.newExcelSheetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newExcelSheetLabel.setObjectName(_fromUtf8("newExcelSheetLabel"))
        self.excelViewLayout.addWidget(self.newExcelSheetLabel, 0, 1, 1, 1)
        self.originExcelSheetLabel = QtGui.QLabel(Form)
        self.originExcelSheetLabel.setStyleSheet(_fromUtf8("font: 12pt \"楷体\";\n"
"background-color: rgb(255, 170, 127);"))
        self.originExcelSheetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originExcelSheetLabel.setObjectName(_fromUtf8("originExcelSheetLabel"))
        self.excelViewLayout.addWidget(self.originExcelSheetLabel, 0, 0, 1, 1)
        self.originExcelViewTableWidget = QtGui.QTableWidget(Form)
        self.originExcelViewTableWidget.setStyleSheet(_fromUtf8("selection-background-color: rgb(170, 170, 255);"))
        self.originExcelViewTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.originExcelViewTableWidget.setObjectName(_fromUtf8("originExcelViewTableWidget"))
        self.originExcelViewTableWidget.setColumnCount(1)
        self.originExcelViewTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.originExcelViewTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.originExcelViewTableWidget.setHorizontalHeaderItem(0, item)
        self.excelViewLayout.addWidget(self.originExcelViewTableWidget, 1, 0, 1, 1)
        self.newExcelViewTableWidget = QtGui.QTableWidget(Form)
        self.newExcelViewTableWidget.setStyleSheet(_fromUtf8("selection-background-color: rgb(170, 170, 255);"))
        self.newExcelViewTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.newExcelViewTableWidget.setObjectName(_fromUtf8("newExcelViewTableWidget"))
        self.newExcelViewTableWidget.setColumnCount(1)
        self.newExcelViewTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.newExcelViewTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.newExcelViewTableWidget.setHorizontalHeaderItem(0, item)
        self.excelViewLayout.addWidget(self.newExcelViewTableWidget, 1, 1, 1, 1)
        self.excelViewLayout.setRowStretch(0, 1)
        self.excelViewLayout.setRowStretch(1, 10)
        self.excelDifferLayout.addLayout(self.excelViewLayout, 0, 1, 1, 1)
        self.excelDifferLayout.setColumnStretch(0, 1)
        self.excelDifferLayout.setColumnStretch(1, 2)
        self.mainWindowLayout.addLayout(self.excelDifferLayout, 0, 0, 1, 1)
        self.mainWindowLayout.setRowStretch(0, 1)
        self.mainWindowLayout.setRowStretch(1, 1)
        self.gridLayout.addLayout(self.mainWindowLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.sheetAddDelTabWidget.setCurrentIndex(0)
        self.sheetResultTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ExcelDiffer-v1.0", None))
        self.SheetAddDelLabel.setText(_translate("Form", "Sheet增删情况汇总", None))
        self.sheetListLabel.setText(_translate("Form", "Sheet增删情况", None))
        item = self.sheetListTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.sheetListTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sheet名", None))
        self.sheetAddDelTabWidget.setTabText(self.sheetAddDelTabWidget.indexOf(self.sheetListTab), _translate("Form", "Sheet列表", None))
        self.sheetAddLabel.setText(_translate("Form", "Sheet新增情况", None))
        item = self.sheetAddTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.sheetAddTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sheet名", None))
        self.sheetAddDelTabWidget.setTabText(self.sheetAddDelTabWidget.indexOf(self.sheetAddTab), _translate("Form", "新增Sheet", None))
        self.sheetDelLabel.setText(_translate("Form", "Sheet删除情况", None))
        item = self.sheetDelTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.sheetDelTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sheet名", None))
        self.sheetAddDelTabWidget.setTabText(self.sheetAddDelTabWidget.indexOf(self.delSheetTab), _translate("Form", "删除Sheet", None))
        self.sheetResultLabel.setText(_translate("Form", "Sheet内部改动汇总", None))
        self.rowAddDelLabel.setText(_translate("Form", "行增删情况", None))
        item = self.rowAddDelTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "新增行", None))
        item = self.rowAddDelTableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "删除行", None))
        item = self.rowAddDelTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        self.sheetResultTabWidget.setTabText(self.sheetResultTabWidget.indexOf(self.rowAddDelTab), _translate("Form", "行增删", None))
        self.columnAddDelLabel.setText(_translate("Form", "列增删情况", None))
        item = self.columnAddDelTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "新增列", None))
        item = self.columnAddDelTableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "删除列", None))
        item = self.columnAddDelTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        self.sheetResultTabWidget.setTabText(self.sheetResultTabWidget.indexOf(self.columnAddDelTab), _translate("Form", "列增删", None))
        self.cellModifyLabel.setText(_translate("Form", "单元格改动情况", None))
        item = self.cellModifyTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.cellModifyTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "坐标", None))
        item = self.cellModifyTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "旧值", None))
        item = self.cellModifyTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "新值", None))
        self.sheetResultTabWidget.setTabText(self.sheetResultTabWidget.indexOf(self.cellModifyTab), _translate("Form", "单元格改动", None))
        self.excelFileChooseGroupBox.setTitle(_translate("Form", "ExcelDiffer", None))
        self.refreshButton.setText(_translate("Form", "清空数据", None))
        self.excelDiffButton.setText(_translate("Form", "差异对比", None))
        self.originExcelLabel.setText(_translate("Form", "旧Excel:", None))
        self.newExcelChooseButton.setText(_translate("Form", "请选择文件...", None))
        self.originExcelChooseButton.setText(_translate("Form", "请选择文件...", None))
        self.newExcelLabel.setText(_translate("Form", "新Excel:", None))
        self.newExcelSheetLabel.setText(_translate("Form", "新Excel名：sheet名", None))
        self.originExcelSheetLabel.setText(_translate("Form", "旧Excel名：sheet名", None))
        item = self.originExcelViewTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.originExcelViewTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "A", None))
        item = self.newExcelViewTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.newExcelViewTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "A", None))

