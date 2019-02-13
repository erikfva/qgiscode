import sys
sys.path.append('C:\\Program Files\\QGIS 3.4\\apps\\qgis\\python\\plugins')

def _init():
    import warnings    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

    import processing
    print ('Hello QGIS222!!!')
_init()


