# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from ..QtModules import *
from ..info.info import VERSION
from ..graphics.canvas import DynamicCanvas
from .table import (
    PointTableWidget,
    LinkTableWidget,
    SelectionLabel
)
from .rotatable import RotatableView

def initCustomWidgets(self):
    #Version text
    self.menuBar.setCornerWidget(QLabel("Version {}.{}.{} ({})".format(*VERSION)))
    #Entities tables
    self.Entities_Point = PointTableWidget(self.Entities_Point_Widget)
    self.Entities_Point.cellDoubleClicked.connect(self.on_action_Edit_Point_triggered)
    self.Entities_Point.itemSelectionChanged.connect(self.pointSelection)
    self.Entities_Point.deleteRequest.connect(self.on_action_Delete_Point_triggered)
    self.Entities_Point_Layout.addWidget(self.Entities_Point)
    self.Entities_Link = LinkTableWidget(self.Entities_Link_Widget)
    self.Entities_Link.cellDoubleClicked.connect(self.on_action_Edit_Link_triggered)
    self.Entities_Link.dragIn.connect(self.addLinkGroup)
    self.Entities_Link.deleteRequest.connect(self.on_action_Delete_Link_triggered)
    self.Entities_Link_Layout.addWidget(self.Entities_Link)
    #QPainter canvas window
    self.DynamicCanvasView = DynamicCanvas(self)
    self.FreeMoveMode.toggled.connect(self.DynamicCanvasView.setFreeMove)
    self.FreeMoveMode.toggled.connect(self.variableValueReset)
    self.DynamicCanvasView.mouse_getSelection.connect(self.Entities_Point.setSelections)
    self.DynamicCanvasView.mouse_getSelection.connect(self.inputs_points_setSelection)
    self.DynamicCanvasView.mouse_freemoveSelection.connect(self.freemove_setCoordinate)
    self.DynamicCanvasView.mouse_noSelection.connect(self.Entities_Point.clearSelection)
    self.DynamicCanvasView.mouse_noSelection.connect(self.inputs_points_clearSelection)
    cleanAction = QAction("Clean selection", self)
    cleanAction.triggered.connect(self.Entities_Point.clearSelection)
    cleanAction.setShortcut(Qt.Key_Escape)
    cleanAction.setShortcutContext(Qt.WindowShortcut)
    self.addAction(cleanAction)
    self.DynamicCanvasView.mouse_getDoubleClickAdd.connect(self.qAddPointGroup)
    self.DynamicCanvasView.mouse_getDoubleClickEdit.connect(self.on_action_Edit_Point_triggered)
    self.DynamicCanvasView.zoom_change.connect(self.ZoomBar.setValue)
    self.canvasSplitter.insertWidget(0, self.DynamicCanvasView)
    self.canvasSplitter.setSizes([600, 10, 30])
    #Panel widget will hide when not using.
    self.panelWidget.hide()
    #Console dock will hide when startup.
    self.ConsoleWidget.hide()
    #Connect to GUI button switching.
    self.disconnectConsoleButton.setEnabled(not self.args.debug_mode)
    self.connectConsoleButton.setEnabled(self.args.debug_mode)
    #Properties and canvas capture button on the Point and Link tab as corner widget.
    CanvasCaptureButton = QPushButton()
    CanvasCaptureButton.setIcon(QIcon(QPixmap(":/icons/capture.png")))
    CanvasCaptureButton.setToolTip('Capture')
    CanvasCaptureButton.setStatusTip("Make a canvas capture to the clipboard.")
    CanvasCaptureButton.clicked.connect(self.canvasCapture)
    self.PointTab.setCornerWidget(CanvasCaptureButton)
    PropertiesButton = QPushButton()
    PropertiesButton.setIcon(self.action_Property.icon())
    PropertiesButton.setToolTip('Properties')
    PropertiesButton.setStatusTip("Properties of this workbook.")
    PropertiesButton.clicked.connect(self.on_action_Property_triggered)
    self.LinkTab.setCornerWidget(PropertiesButton)
    #Add inputs QDial.
    self.inputs_Degree = QDial()
    self.inputs_Degree.setEnabled(False)
    self.inputs_Degree.valueChanged.connect(self.variableValueUpdate)
    self.inputs_dial_layout.addWidget(RotatableView(self.inputs_Degree))
    self.inputs_playShaft = QTimer(self)
    self.inputs_playShaft.setInterval(10)
    self.inputs_playShaft.timeout.connect(self.inputs_change_index)
    self.inputs_variable_stop.clicked.connect(self.variableValueReset)
    #Close all panels button on the panel tab widget.
    closeAllPanelButton = QPushButton()
    closeAllPanelButton.setIcon(QIcon(QPixmap(":/icons/close.png")))
    closeAllPanelButton.setToolTip("Close all opened panel.")
    closeAllPanelButton.clicked.connect(self.closeAllPanels)
    self.panelWidget.setCornerWidget(closeAllPanelButton)
    #Selection label on status bar right side.
    selectionLabel = SelectionLabel(self)
    self.Entities_Point.rowSelectionChanged.connect(selectionLabel.updateSelectPoint)
    self.statusBar.addPermanentWidget(selectionLabel)
    #While value change, update the canvas widget.
    self.ZoomBar.valueChanged.connect(self.DynamicCanvasView.setZoom)
    self.LineWidth.valueChanged.connect(self.DynamicCanvasView.setLinkWidth)
    self.PathWidth.valueChanged.connect(self.DynamicCanvasView.setPathWidth)
    self.Font_size.valueChanged.connect(self.DynamicCanvasView.setFontSize)
    self.action_Display_Point_Mark.toggled.connect(self.DynamicCanvasView.setPointMark)
    self.action_Display_Dimensions.toggled.connect(self.DynamicCanvasView.setShowDimension)
    self.inputs_record.currentRowChanged.connect(self.Reload_Canvas)
    #Splitter stretch factor.
    self.MainSplitter.setStretchFactor(0, 2)
    self.MainSplitter.setStretchFactor(1, 15)
    self.MechanismPanelSplitter.setStretchFactor(0, 4)
    self.MechanismPanelSplitter.setStretchFactor(1, 5)
    self.synthesis_splitter.setSizes([100, 500])
    #Enable mechanism menu actions when shows.
    self.menu_Mechanism.aboutToShow.connect(self.enableMenu)
    #SetIn function connections.
    self.action_Zoom_to_fit.triggered.connect(self.DynamicCanvasView.SetIn)
    self.ResetCanvas.clicked.connect(self.DynamicCanvasView.SetIn)
    #Undo list settings.
    self.FileState.setUndoLimit(self.UndoLimit.value())
    self.UndoLimit.valueChanged.connect(self.FileState.setUndoLimit)
    self.FileState.indexChanged.connect(self.commandReload)
    self.undoView = QUndoView(self.FileState)
    self.undoView.setEmptyLabel("~ Start Pyslvs")
    self.UndoRedoLayout.addWidget(self.undoView)
    separator = QAction(self)
    separator.setSeparator(True)
    self.menu_Edit.insertAction(self.action_Batch_moving, separator)
    self.action_Redo = self.FileState.createRedoAction(self, 'Redo')
    self.action_Undo = self.FileState.createUndoAction(self, 'Undo')
    self.action_Redo.setShortcut("Ctrl+Shift+Z")
    self.action_Redo.setStatusTip("Backtracking undo action.")
    self.action_Redo.setIcon(QIcon(QPixmap(":/icons/redo.png")))
    self.action_Undo.setShortcut("Ctrl+Z")
    self.action_Undo.setStatusTip("Recover last action.")
    self.action_Undo.setIcon(QIcon(QPixmap(":/icons/undo.png")))
    self.menu_Edit.insertAction(separator, self.action_Undo)
    self.menu_Edit.insertAction(separator, self.action_Redo)
    '''
    Entities_Point context menu
    
    + Add
    + Edit
    + Fixed [v]
    + Copy table data
    + Clone
    -------
    + Delete
    '''
    self.Entities_Point_Widget.customContextMenuRequested.connect(self.on_point_context_menu)
    self.popMenu_point = QMenu(self)
    self.popMenu_point.setSeparatorsCollapsible(True)
    self.action_point_right_click_menu_add = QAction("&Add", self)
    self.action_point_right_click_menu_add.triggered.connect(self.on_action_New_Point_triggered)
    self.popMenu_point.addAction(self.action_point_right_click_menu_add)
    self.action_point_right_click_menu_edit = QAction("&Edit", self)
    self.action_point_right_click_menu_edit.triggered.connect(self.on_action_Edit_Point_triggered)
    self.popMenu_point.addAction(self.action_point_right_click_menu_edit)
    self.action_point_right_click_menu_lock = QAction("&Fixed", self)
    self.action_point_right_click_menu_lock.setCheckable(True)
    self.action_point_right_click_menu_lock.triggered.connect(self.lockPoint)
    self.popMenu_point.addAction(self.action_point_right_click_menu_lock)
    self.action_point_right_click_menu_copydata = QAction("&Copy table data", self)
    self.action_point_right_click_menu_copydata.triggered.connect(self.tableCopy_Points)
    self.popMenu_point.addAction(self.action_point_right_click_menu_copydata)
    self.action_point_right_click_menu_copyPoint = QAction("C&lone", self)
    self.action_point_right_click_menu_copyPoint.triggered.connect(self.clonePoint)
    self.popMenu_point.addAction(self.action_point_right_click_menu_copyPoint)
    self.popMenu_point.addSeparator()
    self.action_point_right_click_menu_delete = QAction("&Delete", self)
    self.action_point_right_click_menu_delete.triggered.connect(self.on_action_Delete_Point_triggered)
    self.popMenu_point.addAction(self.action_point_right_click_menu_delete)
    '''
    Entities_Link context menu
    
    + Add
    + Edit
    + Copy table data
    + Release / Constrain
    -------
    + Delete
    '''
    self.Entities_Link_Widget.customContextMenuRequested.connect(self.on_link_context_menu)
    self.popMenu_link = QMenu(self)
    self.popMenu_link.setSeparatorsCollapsible(True)
    self.action_link_right_click_menu_add = QAction("&Add", self)
    self.action_link_right_click_menu_add.triggered.connect(self.on_action_New_Link_triggered)
    self.popMenu_link.addAction(self.action_link_right_click_menu_add)
    self.action_link_right_click_menu_edit = QAction("&Edit", self)
    self.action_link_right_click_menu_edit.triggered.connect(self.on_action_Edit_Link_triggered)
    self.popMenu_link.addAction(self.action_link_right_click_menu_edit)
    self.action_link_right_click_menu_copydata = QAction("&Copy table data", self)
    self.action_link_right_click_menu_copydata.triggered.connect(self.tableCopy_Links)
    self.popMenu_link.addAction(self.action_link_right_click_menu_copydata)
    self.action_link_right_click_menu_release = QAction("&Release", self)
    self.action_link_right_click_menu_release.triggered.connect(self.releaseGround)
    self.popMenu_link.addAction(self.action_link_right_click_menu_release)
    self.action_link_right_click_menu_constrain = QAction("C&onstrain", self)
    self.action_link_right_click_menu_constrain.triggered.connect(self.constrainLink)
    self.popMenu_link.addAction(self.action_link_right_click_menu_constrain)
    self.popMenu_link.addSeparator()
    self.action_link_right_click_menu_delete = QAction("&Delete", self)
    self.action_link_right_click_menu_delete.triggered.connect(self.on_action_Delete_Link_triggered)
    self.popMenu_link.addAction(self.action_link_right_click_menu_delete)
    '''
    DynamicCanvasView context menu
    
    + Add a Path Point [Path Solving]
    + Add
    + Add [fixed]
    -------
    + Edit
    + Fixed
    + Copy point
    -------
    + Delete
    '''
    self.DynamicCanvasView.setContextMenuPolicy(Qt.CustomContextMenu)
    self.DynamicCanvasView.customContextMenuRequested.connect(self.on_canvas_context_menu)
    self.popMenu_canvas = QMenu(self)
    self.popMenu_canvas.setSeparatorsCollapsible(True)
    self.action_canvas_right_click_menu_path = QAction("Add a Path Point [Path Solving]", self)
    self.action_canvas_right_click_menu_path.triggered.connect(self.PathSolving_add_rightClick)
    self.popMenu_canvas.addAction(self.action_canvas_right_click_menu_path)
    self.action_canvas_right_click_menu_add = QAction("&Add", self)
    self.action_canvas_right_click_menu_add.triggered.connect(self.addPointGroup)
    self.popMenu_canvas.addAction(self.action_canvas_right_click_menu_add)
    self.action_canvas_right_click_menu_fix_add = QAction("Add [fixed]", self)
    self.action_canvas_right_click_menu_fix_add.triggered.connect(self.addPointGroup_fixed)
    self.popMenu_canvas.addAction(self.action_canvas_right_click_menu_fix_add)
    self.popMenu_canvas.addSeparator()
    self.popMenu_canvas.addAction(self.action_point_right_click_menu_edit)
    self.popMenu_canvas.addAction(self.action_point_right_click_menu_lock)
    self.popMenu_canvas.addAction(self.action_point_right_click_menu_copyPoint)
    self.popMenu_canvas.addSeparator()
    self.popMenu_canvas.addAction(self.action_point_right_click_menu_delete)
    self.DynamicCanvasView.mouse_track.connect(self.context_menu_mouse_pos)
    '''
    Inputs record context menu
    
    + Copy data from Point{}
    + ...
    '''
    self.inputs_record.customContextMenuRequested.connect(self.on_inputs_record_context_menu)
    self.popMenu_inputs_record = QMenu(self)
