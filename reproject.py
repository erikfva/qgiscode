import sys

from qgis.core import (
    QgsMessageLog,
    QgsProcessingException,
     QgsApplication, 
     QgsProcessingFeedback, 
     QgsVectorLayer
)
from qgis.analysis import QgsNativeAlgorithms

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
#QgsApplication.setPrefixPath('/usr', True)
import os
QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX_PATH'], True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
#sys.path.append('/docs/dev/qgis/build/output/python/plugins')
sys.path.append('C:\\Program Files\\QGIS 3.4\\apps\\qgis\\python\\plugins')

import processing
from processing.core.Processing import Processing

#import warnings
#warnings.resetwarnings()
#warnings.filterwarnings("ignore", category=DeprecationWarning)

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

layer = QgsVectorLayer('brgm.shp', 'my layer', 'ogr')

# You can see what parameters are needed by the algorithm  
# using: processing.algorithmHelp("native:extractvertices")
errorMsg = ''
def write_log_message(message, tag, level):
    #with open(filename, 'a') as logfile:
    #    logfile.write('{tag}({level}): {message}'.format(tag=tag, level=level, message=message))
    global errorMsg
    if errorMsg == '' :
        errorMsg = message

QgsApplication.messageLog().messageReceived.connect(write_log_message)

params = {'INPUT': layer,'TARGET_CRS': 'EPSG:3460','OUTPUT': 'outputfile.shp'}
feedback = QgsProcessingFeedback()
try:
    
    res = processing.run("native:reprojectlayer", params, feedback=feedback)
    res['OUTPUT'] # Access your output layer
#except GeoAlgorithmExecutionException as e:
#except QgsProcessingException as e:
except Exception as e:
    print ('Error', e, errorMsg)
    errorMsg = ''
# When your script is complete, call exitQgis() to remove the
# provider and layer registries from memory
qgs.exitQgis()