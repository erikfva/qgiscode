from qgis.core import *
# If you are not inside a QGIS console you first need to import
# qgis and PyQt4 classes you will use in this script as shown below:
from qgis.core import QgsProject
from PyQt4.QtCore import QFileInfo
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge

# supply path to qgis install location
QgsApplication.setPrefixPath("C:\\Program Files\\QGIS Essen\\apps\\qgis", True)
# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs = QgsApplication([], True)
# load providers
qgs.initQgis()
# Write your code here to load some layers, use processing algorithms, etc.

canvas = QgsMapCanvas()
bridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), canvas)

project = QgsProject.instance()
# Load another project
project.read(QFileInfo('mapa.qgs'))
# Print the current project file name (might be empty in case no projects have been loaded)
print project.fileName()

composition = QgsComposition(canvas.mapSettings())
map_item = composition.getComposerItemById('Mapa 0')
map_item.setMapCanvas(canvas)
map_item.zoomToExtent(canvas.extent())
composition.refreshItems()
composition.exportAsPDF('mapa.pdf')
QgsProject.instance().clear()


# When your script is complete, call exitQgis() to remove the provider and
# layer registries from memory
qgs.exitQgis()
