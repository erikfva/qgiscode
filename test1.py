import sys
from qgis.core import *

# Initialize QGIS Application
QgsApplication.setPrefixPath("C:\\Program Files\\QGIS 3.2\\apps\\qgis", True)
app = QgsApplication([], True)
QgsApplication.initQgis()

# Add the path to Processing framework
sys.path.append('C:\\Program Files\\QGIS 3.2\\apps\\qgis\\python\\plugins')

# Import and initialize Processing framework
from processing.core.Processing import Processing
Processing.initialize()
import processing

roads_shp_path = "brgm.shp"



orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
for alg in QgsApplication.processingRegistry().algorithms():
        print(alg.id(), "->", alg.displayName())

sys.stdout = orig_stdout
f.close()

parameters = {'INPUT': roads_shp_path,'TARGET_CRS': 'EPSG:3460','OUTPUT': 'outputfile.shp'}
#ret = processing.run("native:reprojectlayer", {'INPUT':'E:/qgiscode/BRGM.shp','TARGET_CRS':'EPSG:3460','OUTPUT':'memory:'})
ret = processing.run("native:fixgeometries", {'INPUT':'E:/qgiscode/BRGM.shp','OUTPUT':'memory:'})
output = ret['OUTPUT']
print (output)

processing.run("grass:v.clean",
                  output,
                  1,
                  1,
                  None,
                  -1,
                  0.0001,
                  'clean.shp',
                  'errors.shp')

# When your script is complete, call exitQgis() to remove the
# provider and layer registries from memory
app.exitQgis()