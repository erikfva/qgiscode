import sys
from qgis.core import *

# Initialize QGIS Application
QgsApplication.setPrefixPath("C:\\Program Files\\QGIS Essen\\apps\\qgis", True)
app = QgsApplication([], True)
QgsApplication.initQgis()

# Add the path to Processing framework
sys.path.append('C:\\Users\\SONY\\.qgis2\\python\\plugins')
sys.path.append('C:\\Program Files\\QGIS Essen\\apps\\qgis\\python\\plugins')
# Import and initialize Processing framework
from processing.core.Processing import Processing
Processing.initialize()
import processing

roads_shp_path = "brgm.shp"
ret = processing.runalg('qgis:reprojectlayer', roads_shp_path, 'EPSG:3460',
None)
output = ret['OUTPUT']
print output

processing.runalg("grass:v.clean",
                  output,
                  1,
                  1,
                  None,
                  -1,
                  0.0001,
                  'clean.shp',
                  'errors.shp')
