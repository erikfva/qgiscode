@echo off
SET OSGEO4W_ROOT=C:\Program Files\QGIS 3.4
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
call qt5_env.bat
call py3_env.bat
@echo off
path %OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
 
set PYTHONPATH=C:\Program Files\QGIS 3.4\apps\qgis\python
set PYTHONHOME=C:\Program Files\QGIS 3.4\apps\Python37
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python37\Lib\site-packages;
set PYTHONWARNINGS=ignore::DeprecationWarning
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
