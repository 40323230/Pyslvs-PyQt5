# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/panel/DimensionalSynthesis/Path_Solving_options.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 492)
        Dialog.setMinimumSize(QtCore.QSize(409, 492))
        Dialog.setMaximumSize(QtCore.QSize(409, 492))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bezier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.planarlinkage = QtWidgets.QWidget()
        self.planarlinkage.setObjectName("planarlinkage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.planarlinkage)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.planarlinkage)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.maxGen = QtWidgets.QSpinBox(self.planarlinkage)
        self.maxGen.setMinimum(1000)
        self.maxGen.setMaximum(10000)
        self.maxGen.setSingleStep(100)
        self.maxGen.setProperty("value", 1500)
        self.maxGen.setObjectName("maxGen")
        self.horizontalLayout_2.addWidget(self.maxGen)
        self.label_17 = QtWidgets.QLabel(self.planarlinkage)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.report = QtWidgets.QSpinBox(self.planarlinkage)
        self.report.setMinimum(1)
        self.report.setMaximum(10)
        self.report.setProperty("value", 1)
        self.report.setObjectName("report")
        self.horizontalLayout_2.addWidget(self.report)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.PLTable = QtWidgets.QTableWidget(self.planarlinkage)
        self.PLTable.setObjectName("PLTable")
        self.PLTable.setColumnCount(2)
        self.PLTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.PLTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PLTable.setHorizontalHeaderItem(1, item)
        self.PLTable.horizontalHeader().setDefaultSectionSize(150)
        self.PLTable.horizontalHeader().setMinimumSectionSize(150)
        self.verticalLayout_2.addWidget(self.PLTable)
        self.tabWidget.addTab(self.planarlinkage, "")
        self.algorithm = QtWidgets.QWidget()
        self.algorithm.setObjectName("algorithm")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.algorithm)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.APTable = QtWidgets.QTableWidget(self.algorithm)
        self.APTable.setObjectName("APTable")
        self.APTable.setColumnCount(2)
        self.APTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.APTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.APTable.setHorizontalHeaderItem(1, item)
        self.APTable.horizontalHeader().setDefaultSectionSize(150)
        self.APTable.horizontalHeader().setMinimumSectionSize(150)
        self.verticalLayout_3.addWidget(self.APTable)
        self.tabWidget.addTab(self.algorithm, "")
        self.network = QtWidgets.QWidget()
        self.network.setObjectName("network")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.network)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.network)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.network)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.network, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setDefault = QtWidgets.QPushButton(Dialog)
        self.setDefault.setObjectName("setDefault")
        self.horizontalLayout.addWidget(self.setDefault)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Options"))
        self.label_16.setText(_translate("Dialog", "Max Generation: "))
        self.label_17.setText(_translate("Dialog", "Report in every: "))
        self.report.setSuffix(_translate("Dialog", "%"))
        item = self.PLTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Parameter"))
        item = self.PLTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.planarlinkage), _translate("Dialog", "Planar Linkage"))
        item = self.APTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Parameter"))
        item = self.APTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm), _translate("Dialog", "Algorithm"))
        self.label.setText(_translate("Dialog", "Local port: "))
        self.lineEdit.setInputMask(_translate("Dialog", "9999"))
        self.lineEdit.setText(_translate("Dialog", "8000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.network), _translate("Dialog", "Network"))
        self.setDefault.setText(_translate("Dialog", "Reset to Default"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

