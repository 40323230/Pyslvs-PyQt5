# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/io/overview.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:id.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_box = QtWidgets.QToolBox(Dialog)
        self.tab_box.setObjectName("tab_box")
        self.page0 = QtWidgets.QWidget()
        self.page0.setGeometry(QtCore.QRect(0, 0, 424, 345))
        self.page0.setObjectName("page0")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_expr_label = QtWidgets.QLabel(self.page0)
        self.main_expr_label.setObjectName("main_expr_label")
        self.verticalLayout_2.addWidget(self.main_expr_label)
        self.main_expr = QtWidgets.QLineEdit(self.page0)
        self.main_expr.setReadOnly(True)
        self.main_expr.setObjectName("main_expr")
        self.verticalLayout_2.addWidget(self.main_expr)
        self.storage_label = QtWidgets.QLabel(self.page0)
        self.storage_label.setObjectName("storage_label")
        self.verticalLayout_2.addWidget(self.storage_label)
        self.storage_list = QtWidgets.QListWidget(self.page0)
        self.storage_list.setObjectName("storage_list")
        self.verticalLayout_2.addWidget(self.storage_list)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons:mechanism.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_box.addItem(self.page0, icon1, "")
        self.page1 = QtWidgets.QWidget()
        self.page1.setGeometry(QtCore.QRect(0, 0, 424, 345))
        self.page1.setObjectName("page1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.variables_label = QtWidgets.QLabel(self.page1)
        self.variables_label.setObjectName("variables_label")
        self.verticalLayout_3.addWidget(self.variables_label)
        self.variables_list = QtWidgets.QListWidget(self.page1)
        self.variables_list.setObjectName("variables_list")
        self.verticalLayout_3.addWidget(self.variables_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.records_label = QtWidgets.QLabel(self.page1)
        self.records_label.setObjectName("records_label")
        self.verticalLayout_4.addWidget(self.records_label)
        self.records_list = QtWidgets.QListWidget(self.page1)
        self.records_list.setObjectName("records_list")
        self.verticalLayout_4.addWidget(self.records_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons:motor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_box.addItem(self.page1, icon2, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setGeometry(QtCore.QRect(0, 0, 424, 345))
        self.page2.setObjectName("page2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.structures_label = QtWidgets.QLabel(self.page2)
        self.structures_label.setObjectName("structures_label")
        self.verticalLayout_6.addWidget(self.structures_label)
        self.structures_list = QtWidgets.QListWidget(self.page2)
        self.structures_list.setObjectName("structures_list")
        self.verticalLayout_6.addWidget(self.structures_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.triangular_iteration_label = QtWidgets.QLabel(self.page2)
        self.triangular_iteration_label.setObjectName("triangular_iteration_label")
        self.verticalLayout_5.addWidget(self.triangular_iteration_label)
        self.triangular_iteration_list = QtWidgets.QListWidget(self.page2)
        self.triangular_iteration_list.setObjectName("triangular_iteration_list")
        self.verticalLayout_5.addWidget(self.triangular_iteration_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons:collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_box.addItem(self.page2, icon3, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setGeometry(QtCore.QRect(0, 0, 424, 345))
        self.page3.setObjectName("page3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.results_label = QtWidgets.QLabel(self.page3)
        self.results_label.setObjectName("results_label")
        self.verticalLayout_7.addWidget(self.results_label)
        self.results_list = QtWidgets.QListWidget(self.page3)
        self.results_list.setObjectName("results_list")
        self.verticalLayout_7.addWidget(self.results_list)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons:dimensional_synthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_box.addItem(self.page3, icon4, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 424, 345))
        self.page.setObjectName("page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.image_path_label = QtWidgets.QLabel(self.page)
        self.image_path_label.setObjectName("image_path_label")
        self.verticalLayout_8.addWidget(self.image_path_label)
        self.image_path = QtWidgets.QLineEdit(self.page)
        self.image_path.setReadOnly(True)
        self.image_path.setObjectName("image_path")
        self.verticalLayout_8.addWidget(self.image_path)
        self.background_preview = QtWidgets.QLabel(self.page)
        self.background_preview.setObjectName("background_preview")
        self.verticalLayout_8.addWidget(self.background_preview)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons:picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_box.addItem(self.page, icon5, "")
        self.verticalLayout.addWidget(self.tab_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.main_expr_label.setText(_translate("Dialog", "Current:"))
        self.storage_label.setText(_translate("Dialog", "Storage:"))
        self.tab_box.setItemText(self.tab_box.indexOf(self.page0), _translate("Dialog", "Mechanism"))
        self.variables_label.setText(_translate("Dialog", "Variables:"))
        self.records_label.setText(_translate("Dialog", "Records:"))
        self.tab_box.setItemText(self.tab_box.indexOf(self.page1), _translate("Dialog", "Inputs"))
        self.structures_label.setText(_translate("Dialog", "Structures:"))
        self.triangular_iteration_label.setText(_translate("Dialog", "Triangular iteration:"))
        self.tab_box.setItemText(self.tab_box.indexOf(self.page2), _translate("Dialog", "Collections"))
        self.results_label.setText(_translate("Dialog", "Results:"))
        self.tab_box.setItemText(self.tab_box.indexOf(self.page3), _translate("Dialog", "Dimensional Synthesis"))
        self.image_path_label.setText(_translate("Dialog", "Image path:"))
        self.tab_box.setItemText(self.tab_box.indexOf(self.page), _translate("Dialog", "Background Image"))
