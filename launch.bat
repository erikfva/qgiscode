REM Change OSGEO4W_ROOT to point to the base install folder
SET OSGEO4W_ROOT=C:\OSGeo4W64
SET QGISNAME=qgis
REM SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%

set QGIS_PREFIX_PATH=%QGIS%
REM Gdal Setup
set GDAL_DATA=C:\Program Files\QGIS Essen\share\gdal\
REM Python Setup
set PATH=%OSGEO4W_ROOT%\bin;%QGIS%;%PATH%
SET PYTHONHOME=C:\Program Files\QGIS Essen\apps\Python27
set PYTHONPATH=%QGIS%;%PYTHONHOME%
SET QGIS=C:\Program Files\QGIS Essen
call "%QGIS%\bin\o4w_env.bat"
path %QGIS%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%QGIS:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%QGIS%\apps\qgis\qtplugins;%QGIS%\apps\qt4\plugins
set PYTHONPATH=%QGIS%\apps\qgis\python;%PYTHONPATH%
REM "%QGIS%"\bin\python.exe %*
python test2.py
