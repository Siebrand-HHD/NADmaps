# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NADMapsDialog
                                 A QGIS plugin
 Centrale plek om handige kaarten voor waterketen en rioolbeheer te vinden en snel in te laden.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-01-09
        git sha              : $Format:%H$
        copyright            : (C) 2025 by Netwerk Waterketen Delfland
        email                : dataplatform@waterketendelfland.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'nad_maps_dialog_base.ui'))


class NADMapsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(NADMapsDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.ui = self

        self.activeMapListView = self.ui.activeMapListView
        self.activeMapListView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.activeMapListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        self.themaView = self.ui.themaView
        self.themaView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.themaView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        self.themaMapListView = self.ui.themaMapListView
        self.themaMapListView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)

        self.mapListView = self.ui.mapListView
        self.mapListView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.mapListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
