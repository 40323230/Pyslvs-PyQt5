# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/io/preference.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(865, 427)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settings_ui_groupbox = QtWidgets.QGroupBox(Dialog)
        self.settings_ui_groupbox.setObjectName("settings_ui_groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.settings_ui_groupbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.zoomby_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.zoomby_label.setObjectName("zoomby_label")
        self.gridLayout.addWidget(self.zoomby_label, 3, 2, 1, 1)
        self.font_size_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.font_size_option.setMinimum(1)
        self.font_size_option.setMaximum(30)
        self.font_size_option.setSingleStep(2)
        self.font_size_option.setObjectName("font_size_option")
        self.gridLayout.addWidget(self.font_size_option, 0, 3, 1, 1)
        self.tick_mark_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.tick_mark_label.setObjectName("tick_mark_label")
        self.gridLayout.addWidget(self.tick_mark_label, 4, 2, 1, 1)
        self.zoom_by_option = QtWidgets.QComboBox(self.settings_ui_groupbox)
        self.zoom_by_option.setObjectName("zoom_by_option")
        self.zoom_by_option.addItem("")
        self.zoom_by_option.addItem("")
        self.gridLayout.addWidget(self.zoom_by_option, 3, 3, 1, 1)
        self.line_width_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.line_width_option.setMinimum(1)
        self.line_width_option.setMaximum(10)
        self.line_width_option.setDisplayIntegerBase(10)
        self.line_width_option.setObjectName("line_width_option")
        self.gridLayout.addWidget(self.line_width_option, 0, 1, 1, 1)
        self.scale_factor_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.scale_factor_option.setMinimum(5)
        self.scale_factor_option.setMaximum(100)
        self.scale_factor_option.setSingleStep(5)
        self.scale_factor_option.setObjectName("scale_factor_option")
        self.gridLayout.addWidget(self.scale_factor_option, 1, 3, 1, 1)
        self.linewidth_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.linewidth_label.setObjectName("linewidth_label")
        self.gridLayout.addWidget(self.linewidth_label, 0, 0, 1, 1)
        self.fontsize_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.fontsize_label.setObjectName("fontsize_label")
        self.gridLayout.addWidget(self.fontsize_label, 0, 2, 1, 1)
        self.snap_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.snap_label.setObjectName("snap_label")
        self.gridLayout.addWidget(self.snap_label, 5, 0, 1, 1)
        self.jointsize_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.jointsize_label.setObjectName("jointsize_label")
        self.gridLayout.addWidget(self.jointsize_label, 4, 0, 1, 1)
        self.pathwidth_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.pathwidth_label.setObjectName("pathwidth_label")
        self.gridLayout.addWidget(self.pathwidth_label, 1, 0, 1, 1)
        self.linktransparency_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.linktransparency_label.setObjectName("linktransparency_label")
        self.gridLayout.addWidget(self.linktransparency_label, 2, 2, 1, 1)
        self.margin_factor_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.margin_factor_option.setMaximum(30)
        self.margin_factor_option.setSingleStep(5)
        self.margin_factor_option.setObjectName("margin_factor_option")
        self.gridLayout.addWidget(self.margin_factor_option, 3, 1, 1, 1)
        self.toolbar_pos_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.toolbar_pos_label.setObjectName("toolbar_pos_label")
        self.gridLayout.addWidget(self.toolbar_pos_label, 5, 2, 1, 1)
        self.selectionradius_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.selectionradius_label.setObjectName("selectionradius_label")
        self.gridLayout.addWidget(self.selectionradius_label, 2, 0, 1, 1)
        self.scalefactor_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.scalefactor_label.setObjectName("scalefactor_label")
        self.gridLayout.addWidget(self.scalefactor_label, 1, 2, 1, 1)
        self.nav_toolbar_pos_option = QtWidgets.QComboBox(self.settings_ui_groupbox)
        self.nav_toolbar_pos_option.setObjectName("nav_toolbar_pos_option")
        self.nav_toolbar_pos_option.addItem("")
        self.nav_toolbar_pos_option.addItem("")
        self.gridLayout.addWidget(self.nav_toolbar_pos_option, 5, 3, 1, 1)
        self.marginfactor_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.marginfactor_label.setObjectName("marginfactor_label")
        self.gridLayout.addWidget(self.marginfactor_label, 3, 0, 1, 1)
        self.joint_size_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.joint_size_option.setMinimum(1)
        self.joint_size_option.setMaximum(100)
        self.joint_size_option.setObjectName("joint_size_option")
        self.gridLayout.addWidget(self.joint_size_option, 4, 1, 1, 1)
        self.path_width_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.path_width_option.setMinimum(1)
        self.path_width_option.setMaximum(5)
        self.path_width_option.setObjectName("path_width_option")
        self.gridLayout.addWidget(self.path_width_option, 1, 1, 1, 1)
        self.link_trans_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.link_trans_option.setMaximum(80)
        self.link_trans_option.setSingleStep(10)
        self.link_trans_option.setObjectName("link_trans_option")
        self.gridLayout.addWidget(self.link_trans_option, 2, 3, 1, 1)
        self.snap_option = QtWidgets.QDoubleSpinBox(self.settings_ui_groupbox)
        self.snap_option.setMaximum(50.0)
        self.snap_option.setObjectName("snap_option")
        self.gridLayout.addWidget(self.snap_option, 5, 1, 1, 1)
        self.tick_mark_option = QtWidgets.QComboBox(self.settings_ui_groupbox)
        self.tick_mark_option.setObjectName("tick_mark_option")
        self.tick_mark_option.addItem("")
        self.tick_mark_option.addItem("")
        self.tick_mark_option.addItem("")
        self.gridLayout.addWidget(self.tick_mark_option, 4, 3, 1, 1)
        self.selection_radius_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.selection_radius_option.setMinimum(3)
        self.selection_radius_option.setMaximum(10)
        self.selection_radius_option.setObjectName("selection_radius_option")
        self.gridLayout.addWidget(self.selection_radius_option, 2, 1, 1, 1)
        self.default_zoom_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.default_zoom_label.setObjectName("default_zoom_label")
        self.gridLayout.addWidget(self.default_zoom_label, 6, 0, 1, 1)
        self.default_zoom_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.default_zoom_option.setObjectName("default_zoom_option")
        self.gridLayout.addWidget(self.default_zoom_option, 6, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.grab_no_background_option = QtWidgets.QCheckBox(self.settings_ui_groupbox)
        self.grab_no_background_option.setObjectName("grab_no_background_option")
        self.verticalLayout_3.addWidget(self.grab_no_background_option)
        self.monochrome_option = QtWidgets.QCheckBox(self.settings_ui_groupbox)
        self.monochrome_option.setObjectName("monochrome_option")
        self.verticalLayout_3.addWidget(self.monochrome_option)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.settings_ui_groupbox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_kernels_groupBox = QtWidgets.QGroupBox(Dialog)
        self.settings_kernels_groupBox.setObjectName("settings_kernels_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.settings_kernels_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.planarsolver_label = QtWidgets.QLabel(self.settings_kernels_groupBox)
        self.planarsolver_label.setObjectName("planarsolver_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.planarsolver_label)
        self.planar_solver_option = QtWidgets.QComboBox(self.settings_kernels_groupBox)
        self.planar_solver_option.setObjectName("planar_solver_option")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.planar_solver_option)
        self.pathpreview_label = QtWidgets.QLabel(self.settings_kernels_groupBox)
        self.pathpreview_label.setObjectName("pathpreview_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pathpreview_label)
        self.path_preview_option = QtWidgets.QComboBox(self.settings_kernels_groupBox)
        self.path_preview_option.setObjectName("path_preview_option")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.path_preview_option)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.console_error_option = QtWidgets.QCheckBox(self.settings_kernels_groupBox)
        self.console_error_option.setObjectName("console_error_option")
        self.verticalLayout_4.addWidget(self.console_error_option)
        self.verticalLayout.addWidget(self.settings_kernels_groupBox)
        self.settings_project_groupbox = QtWidgets.QGroupBox(Dialog)
        self.settings_project_groupbox.setObjectName("settings_project_groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.settings_project_groupbox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.undo_limit_label = QtWidgets.QLabel(self.settings_project_groupbox)
        self.undo_limit_label.setObjectName("undo_limit_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.undo_limit_label)
        self.undo_limit_option = QtWidgets.QSpinBox(self.settings_project_groupbox)
        self.undo_limit_option.setMinimum(5)
        self.undo_limit_option.setObjectName("undo_limit_option")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.undo_limit_option)
        self.open_project_actions_label = QtWidgets.QLabel(self.settings_project_groupbox)
        self.open_project_actions_label.setObjectName("open_project_actions_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.open_project_actions_label)
        self.open_project_actions_option = QtWidgets.QComboBox(self.settings_project_groupbox)
        self.open_project_actions_option.setObjectName("open_project_actions_option")
        self.open_project_actions_option.addItem("")
        self.open_project_actions_option.addItem("")
        self.open_project_actions_option.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.open_project_actions_option)
        self.file_type_label = QtWidgets.QLabel(self.settings_project_groupbox)
        self.file_type_label.setObjectName("file_type_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.file_type_label)
        self.file_type_option = QtWidgets.QComboBox(self.settings_project_groupbox)
        self.file_type_option.setObjectName("file_type_option")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.file_type_option)
        self.verticalLayout.addWidget(self.settings_project_groupbox)
        self.settings_misc_groupBox = QtWidgets.QGroupBox(Dialog)
        self.settings_misc_groupBox.setObjectName("settings_misc_groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.settings_misc_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.auto_remove_link_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.auto_remove_link_option.setObjectName("auto_remove_link_option")
        self.verticalLayout_7.addWidget(self.auto_remove_link_option)
        self.title_full_path_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.title_full_path_option.setObjectName("title_full_path_option")
        self.verticalLayout_7.addWidget(self.title_full_path_option)
        self.not_save_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.not_save_option.setObjectName("not_save_option")
        self.verticalLayout_7.addWidget(self.not_save_option)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.settings_misc_groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preference"))
        self.settings_ui_groupbox.setTitle(_translate("Dialog", "Main canvas"))
        self.zoomby_label.setText(_translate("Dialog", "Center zooming"))
        self.tick_mark_label.setText(_translate("Dialog", "Tick mark"))
        self.zoom_by_option.setItemText(0, _translate("Dialog", "Cursor"))
        self.zoom_by_option.setItemText(1, _translate("Dialog", "Cavas center"))
        self.linewidth_label.setText(_translate("Dialog", "Line width"))
        self.fontsize_label.setText(_translate("Dialog", "Font size"))
        self.snap_label.setText(_translate("Dialog", "Snap the mouse when dragging"))
        self.jointsize_label.setText(_translate("Dialog", "Joint annotation size (diameter)"))
        self.pathwidth_label.setText(_translate("Dialog", "Path width"))
        self.linktransparency_label.setText(_translate("Dialog", "Link transparency"))
        self.margin_factor_option.setSuffix(_translate("Dialog", "%"))
        self.toolbar_pos_label.setText(_translate("Dialog", "Toolbar position"))
        self.selectionradius_label.setText(_translate("Dialog", "Selection radius"))
        self.scalefactor_label.setText(_translate("Dialog", "Scale factor"))
        self.nav_toolbar_pos_option.setItemText(0, _translate("Dialog", "Top"))
        self.nav_toolbar_pos_option.setItemText(1, _translate("Dialog", "Bottom"))
        self.marginfactor_label.setText(_translate("Dialog", "Margin of \"zoom to fit\""))
        self.link_trans_option.setSuffix(_translate("Dialog", " %"))
        self.tick_mark_option.setItemText(0, _translate("Dialog", "Hide"))
        self.tick_mark_option.setItemText(1, _translate("Dialog", "Display"))
        self.tick_mark_option.setItemText(2, _translate("Dialog", "Display with number"))
        self.default_zoom_label.setText(_translate("Dialog", "Default zoom value"))
        self.default_zoom_option.setSuffix(_translate("Dialog", "%"))
        self.grab_no_background_option.setText(_translate("Dialog", "Use transparent background when capturing."))
        self.monochrome_option.setText(_translate("Dialog", "Monochrome mode for mechanism. (Excluding indicators)"))
        self.settings_kernels_groupBox.setTitle(_translate("Dialog", "Kernels"))
        self.planarsolver_label.setText(_translate("Dialog", "Planar solving"))
        self.pathpreview_label.setText(_translate("Dialog", "Path preview"))
        self.console_error_option.setText(_translate("Dialog", "Show error messages in the console."))
        self.settings_project_groupbox.setTitle(_translate("Dialog", "Project and history"))
        self.undo_limit_label.setText(_translate("Dialog", "Undo limit"))
        self.undo_limit_option.setSuffix(_translate("Dialog", " times"))
        self.open_project_actions_label.setText(_translate("Dialog", "Open project actions"))
        self.open_project_actions_option.setItemText(0, _translate("Dialog", "No undo"))
        self.open_project_actions_option.setItemText(1, _translate("Dialog", "Group with macros"))
        self.open_project_actions_option.setItemText(2, _translate("Dialog", "No group"))
        self.file_type_label.setText(_translate("Dialog", "File type"))
        self.settings_misc_groupBox.setTitle(_translate("Dialog", "Misc"))
        self.auto_remove_link_option.setText(_translate("Dialog", "Remove empty links after deleted points."))
        self.title_full_path_option.setText(_translate("Dialog", "Show full file path on window title."))
        self.not_save_option.setText(_translate("Dialog", "Don\'t save Pyslvs options to local."))
