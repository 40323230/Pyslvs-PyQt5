# -*- coding: utf-8 -*-

"""YAML format processing function."""

from __future__ import annotations

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    TYPE_CHECKING,
    Tuple,
    List,
    Sequence,
    Dict,
    Any,
)
import yaml
from pyslvs import __version__, VJoint
from core.QtModules import (
    QObject,
    QFileInfo,
    QProgressDialog,
    QCoreApplication,
)
from .overview import OverviewDialog
if TYPE_CHECKING:
    from core.widgets import MainWindowBase


class YamlEditor(QObject):

    """YAML reader and writer."""

    def __init__(self, parent: MainWindowBase):
        super(YamlEditor, self).__init__(parent)

        # Check file changed function
        self.check_file_changed = parent.check_file_changed
        # Check workbook saved function
        self.workbook_saved = parent.workbook_saved

        # Call to get point expressions
        self.vpoints = parent.vpoint_list
        # Call to get link data
        self.vlinks = parent.vlink_list
        # Call to get storage data
        self.storage_data_func = parent.get_storage
        # Call to get collections data
        self.collect_data_func = parent.collection_tab_page.collect_data
        # Call to get triangle data
        self.triangle_data_func = parent.collection_tab_page.triangle_data
        # Call to get inputs variables data
        self.inputs_data_func = parent.inputs_widget.input_pairs
        # Call to get algorithm data
        self.algorithm_data_func = lambda: parent.dimensional_synthesis.mechanism_data
        # Call to get path data
        self.path_data_func = parent.inputs_widget.path_data

        # Add empty links function
        self.add_links_func = parent.add_empty_links
        # Add points function
        self.add_points_func = parent.add_points

        # Call to load inputs variables data
        self.load_inputs_func = parent.inputs_widget.add_inputs_variables
        # Add storage function
        self.add_storage_func = parent.add_multiple_storage
        # Call to load paths
        self.load_path_func = parent.inputs_widget.load_paths
        # Call to load collections data
        self.load_collect_func = parent.collection_tab_page.structure_widget.add_collections
        # Call to load triangle data
        self.load_triangle_func = parent.collection_tab_page.configure_widget.add_collections
        # Call to load algorithm results
        self.load_algorithm_func = parent.dimensional_synthesis.load_results

        # Clear function for main window
        self.clear_func = parent.clear

    def save(self, file_name: str):
        """Save YAML file."""
        mechanism_data = []
        for vpoint in self.vpoints:
            attr = {
                'links': vpoint.links,
                'type': vpoint.type,
                'x': vpoint.x,
                'y': vpoint.y,
            }
            if vpoint.type in {VJoint.P, VJoint.RP}:
                attr['angle'] = vpoint.angle
            mechanism_data.append(attr)

        data = {
            'mechanism': mechanism_data,
            'links': {l.name: l.color_str for l in self.vlinks},
            'input': [{'base': b, 'drive': d} for b, d, _ in self.inputs_data_func()],
            'storage': list(self.storage_data_func().items()),
            'collection': self.collect_data_func(),
            'triangle': self.triangle_data_func(),
            'algorithm': eval(str(self.algorithm_data_func())),
            'path': self.path_data_func(),
        }
        yaml_script = yaml.dump(data, default_flow_style=False)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(f"# Generated by Pyslvs {__version__}\n\n" + yaml_script)

    def load(self, file_name: str):
        """Load YAML file."""
        if self.check_file_changed():
            return

        # Clear first
        self.clear_func()

        # Load file
        dlg = QProgressDialog("Loading project", "Cancel", 0, 8, self.parent())
        dlg.setLabelText("Reading file ...")
        dlg.show()
        with open(file_name, encoding='utf-8') as f:
            yaml_script = f.read()
        data: Dict[str, Any] = yaml.load(yaml_script, Loader=yaml.FullLoader)

        # Links data
        dlg.setValue(1)
        dlg.setLabelText("Loading mechanism ...")
        if dlg.wasCanceled():
            return self.clear_func()
        links_data: Dict[str, str] = data.get('links', {})
        self.add_links_func(links_data)

        # Mechanism data
        mechanism_data: List[Dict[str, Any]] = data.get('mechanism', [])
        p_attr = []
        nan = float("nan")
        for point_attr in mechanism_data:
            QCoreApplication.processEvents()
            p_x: float = point_attr.get('x', nan)
            p_y: float = point_attr.get('y', nan)
            p_links: Tuple[str] = point_attr.get('links', ())
            p_type: int = point_attr.get('type', 0)
            p_angle: float = point_attr.get('angle', 0.)
            p_attr.append((p_x, p_y, ','.join(p_links), 'Green', p_type, p_angle))
        self.add_points_func(p_attr)

        # Input data
        dlg.setValue(2)
        dlg.setLabelText("Loading input data ...")
        if dlg.wasCanceled():
            return self.clear_func()
        input_data: List[Dict[str, int]] = data.get('input', [])
        i_attr = []
        for input_attr in input_data:
            QCoreApplication.processEvents()
            if ('base' in input_attr) and ('drive' in input_attr):
                i_base = input_attr['base']
                i_drive = input_attr['drive']
                i_attr.append((i_base, i_drive))
        self.load_inputs_func(i_attr)

        # Storage data
        dlg.setValue(3)
        dlg.setLabelText("Loading storage ...")
        if dlg.wasCanceled():
            return self.clear_func()
        storage_data: List[Tuple[str, str]] = data.get('storage', [])
        self.add_storage_func(storage_data)

        # Path data
        dlg.setValue(4)
        dlg.setLabelText("Loading paths ...")
        if dlg.wasCanceled():
            return self.clear_func()
        path_data: Dict[str, Sequence[Tuple[float, float]]] = data.get('path', {})
        self.load_path_func(path_data)

        # Collection data
        dlg.setValue(5)
        dlg.setLabelText("Loading graph collections ...")
        if dlg.wasCanceled():
            return self.clear_func()
        collection_data: List[Tuple[Tuple[int, int], ...]] = data.get('collection', [])
        self.load_collect_func(collection_data)

        # Configuration data
        dlg.setValue(6)
        dlg.setLabelText("Loading synthesis configurations ...")
        if dlg.wasCanceled():
            return self.clear_func()
        config_data: Dict[str, Dict[str, Any]] = data.get('triangle', {})
        self.load_triangle_func(config_data)

        # Algorithm data
        dlg.setValue(7)
        dlg.setLabelText("Loading synthesis configurations ...")
        if dlg.wasCanceled():
            return self.clear_func()

        algorithm_data: List[Dict[str, Any]] = data.get('algorithm', [])
        self.load_algorithm_func(algorithm_data)

        # Workbook loaded
        dlg.setValue(8)
        dlg.deleteLater()

        # Show overview dialog
        dlg = OverviewDialog(
            self.parent(),
            f"YAML project: {QFileInfo(file_name).baseName()}",
            storage_data,
            i_attr,
            path_data,
            collection_data,
            config_data,
            algorithm_data
        )
        dlg.show()
        dlg.exec_()
        dlg.deleteLater()
