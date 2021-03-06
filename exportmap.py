import sys

sys.path.append('C:\\Program Files\\QGIS 3.4\\apps\\qgis\\python\\plugins')

from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from PyQt5.QtCore import *

from qgis.core import *
import os
from qgis.utils import iface

QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX_PATH'], True)
qgs = QgsApplication([], False)
qgs.initQgis()


def make_pdf():
    #PG_POP = "uploads.f20181128bdefcga96fb8da6"
    #FLD_USO = "uso_pop_1"
    PG_POP = "uploads.f20181122cdaebfga135360d"
    FLD_USO = "uso_pop"
    DB_CONN = "dbname='geodatabase' host=localhost port=5432 user='postgres' password='arma'"
    EPSG = 32720
    TEMPLATE = "hidrosanit/mapa.qgs"

    #Abriendo el template del mapa

    project = QgsProject.instance()
    canvas = QgsMapCanvas()
    bridge = QgsLayerTreeMapCanvasBridge(project.layerTreeRoot(), canvas)
    project.read(TEMPLATE)
    crs = QgsCoordinateReferenceSystem()
    crs.createFromSrid(EPSG)
    project.setCrs(crs)
    print(project.fileName())

    # Añadiendo capas PostGIS

    ## 1.- CAPA DEL POP
    sql = """
    SELECT row_number() over () AS sicob_id, uso_pop, (dp).geom as the_geom , st_area((dp).geom) * 100000 as _area FROM 
    (
        SELECT st_dump(the_geom) as dp, %s as uso_pop
        FROM
        %s
    ) t
    """ % (FLD_USO, PG_POP)
    #lyr_POP = QgsVectorLayer(DB_CONN + " key='gid' table=" + PG_POP + " (the_geom) sql=", "POP", "postgres")
    lyr_POP = QgsVectorLayer(DB_CONN + " key='sicob_id' table=\"(" + sql + ")\" (the_geom) sql=","testgeom", "postgres")
    if not lyr_POP.isValid():
        print("Layer %s did not load" % lyr_POP.name())
    lyr_POP.loadNamedStyle('pop_img.qml')
    lyr_POP.setLabelsEnabled(True)
    #lyr_POP.triggerRepaint()

    ## 2.- CAPA DEL CUADRO ROJO ALREDEDOR DEL POP
    lyr_Box = QgsVectorLayer("Polygon?crs=epsg:4326",
                          "result",
                          "memory")
    pr = lyr_Box.dataProvider()
    # add fields
    #pr.addAttributes([QgsField("name", QVariant.String),
    #                  QgsField("age", QVariant.Int),
    #                  QgsField("size", QVariant.Double)])
    #vl.updateFields()  # tell the vector layer to fetch changes from the provider
    # add a feature
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromRect(lyr_POP.extent()).buffer(0.12,-1) )
    #fet.setAttributes(["Johny", 2, 0.3])
    pr.addFeatures([fet])
    # update layer's extent when new features have been added
    # because change of extent in provider is not propagated to the layer
    lyr_Box.updateExtents()
    # fix the renderer, fill
    props = {"color": "255,0,0,0", "outline_width": "0.4", "outline_color": '255,0,0'}
    fillSymbol = QgsFillSymbol.createSimple(props)
    renderer = QgsSingleSymbolRenderer(fillSymbol)
    lyr_Box.setRenderer(renderer)

    ## 3.- CAPA DE MUNICIPIOS DONDE ESTA UBICADO EL POP
    sql = """SELECT distinct ON(lm.sicob_id) lm.sicob_id,lm.the_geom as the_geom, lm.nom_dep, lm.nom_prov, lm.nom_mun 
            FROM coberturas.lm lm INNER JOIN %s pop
            ON (st_intersects(pop.the_geom, lm.the_geom))""" % PG_POP
    lyr_municipio = QgsVectorLayer(DB_CONN + " key='sicob_id' table=\"(" + sql + ")\" (the_geom) sql=","municipio", "postgres")
    #uri = QgsDataSourceUri()
    # introducimos nombre del servidor, puerto, nombre de la base de datos, usuario y contraseña
    #uri.setConnection("localhost", "5432", "geodatabase", "postgres", "arma")
    # introducimos el nombre del esquema, nombre de la tabla, columna de geometría y opcionalmente un filtro con una clausula WHERE
    #uri.setDataSource('coberturas', "lm", "the_geom", "nom_dep = 'SANTA CRUZ' AND nom_prov='FLORIDA'")
    #layer = QgsVectorLayer(uri.uri(), "municipio", "postgres")
    if not lyr_municipio.isValid():
        print("Layer %s did not load" % lyr_municipio.name())

    #labelSettings = QgsPalLayerSettings()
    #labelSettings.fieldName = "nom_mun"
    #lyr_municipio.setLabeling(QgsVectorLayerSimpleLabeling(labelSettings))
    lyr_municipio.loadNamedStyle('municipio.qml')
    lyr_municipio.setLabelsEnabled(True)
    lyr_municipio.triggerRepaint()

    # fix the renderer, fill with green
    props = {"color": "255,255,255,0", "outline_width": "0", "outline_color": '0,0,0'}
    fillSymbol = QgsFillSymbol.createSimple(props)
    renderer = QgsSingleSymbolRenderer(fillSymbol)
    lyr_municipio.setRenderer(renderer)
    features = lyr_municipio.getFeatures()
    NOM_DEP = ""
    for fet in features:
        NOM_DEP = fet.attribute('nom_dep')
    #    print("F:", fet.attribute('nom_dep'))
    # print(lyr_municipio.crs())
    # layer.setCrs(layer.crs().createFromSrid(4326))

    ## 4.- CAPA DEL DEPARTAMENTO DONDE SE ENCUENTRA EL POP
    sql = """
        SELECT * FROM coberturas.ld WHERE nom_dep = '%s'
    """ % NOM_DEP
    lyr_departamento = QgsVectorLayer(DB_CONN + " key='sicob_id' table=\"(" + sql + ")\" (the_geom) sql=","departamento", "postgres")
    props = {"color": "0,255,0", "outline_width": "0", "outline_color": '119, 119, 119'}
    fillSymbol = QgsFillSymbol.createSimple(props)
    renderer = QgsSingleSymbolRenderer(fillSymbol)
    lyr_departamento.setRenderer(renderer)

    ## 4.- CAPA DEL PAIS
    sql = """
        SELECT * FROM coberturas.ld
    """
    lyr_pais = QgsVectorLayer(DB_CONN + " key='sicob_id' table=\"(" + sql + ")\" (the_geom) sql=","pais", "postgres")
    lyr_pais.updateExtents()
    # fix the renderer, fill
    props = {"color": "255,0,0,0", "outline_width": "0", "outline_color": '119, 119, 119'}
    fillSymbol = QgsFillSymbol.createSimple(props)
    renderer = QgsSingleSymbolRenderer(fillSymbol)
    lyr_pais.setRenderer(renderer)

    lyr_BingMap = project.instance().mapLayersByName('BingMap')[0]
    # https://gis.stackexchange.com/questions/272397/set-layer-visibility-using-qgsmapcanvaslayer-in-qgis-3
    project.layerTreeRoot().findLayer(lyr_BingMap.id()).setItemVisibilityChecked(True)
    # print(layerBingMap)

    # composition.loadFromTemplate(template_qdoc)

    # https://gis.stackexchange.com/questions/269058/export-layout-as-pdf-in-qgis3
    layoutmanager = project.layoutManager()
    layout = layoutmanager.layoutByName("Mapa1")  # Layout name
    # MAPA DE UBICACION EN EL PAIS
    ubicacion_pais = layout.itemById('ubicacion_pais')
    ubicacion_pais.setLayers([lyr_departamento,  lyr_pais])
    ubicacion_pais.zoomToExtent(lyr_pais.extent())
    ubicacion_pais.setBlendMode(2) #Force render as image

    # MAPA DE UBICACION EN EL DEPARTAMENTO
    ubicacion_departamento = layout.itemById('ubicacion_departamento')
    lyr_departamento_copy = lyr_departamento.clone()
    props = {"color": "255,0,0,0", "outline_width": "0", "outline_color": '119, 119, 119'}
    fillSymbol = QgsFillSymbol.createSimple(props)
    renderer = QgsSingleSymbolRenderer(fillSymbol)
    lyr_departamento_copy.setRenderer(renderer)
    lyr_municipio_copy = lyr_municipio.clone()
    props = {"color": "119, 119, 119", "outline_width": "0", "outline_color": '119, 119, 119'}
    fillSymbol = QgsFillSymbol.createSimple(props)
    renderer = QgsSingleSymbolRenderer(fillSymbol)
    lyr_municipio_copy.setRenderer(renderer)
    lyr_municipio_copy.setLabelsEnabled(False)
    ubicacion_departamento.setLayers([lyr_Box, lyr_POP, lyr_municipio_copy, lyr_departamento_copy])
    #xform = QgsCoordinateTransform(lyr_departamento.crs(), project.crs(), project)
    #ubicacion_departamento.zoomToExtent(xform.transform(lyr_departamento.extent()))
    ubicacion_departamento.zoomToExtent(lyr_departamento.extent())
    ubicacion_departamento.setBlendMode(2)  # Force render as image

    ubicacion_municipio = layout.itemById('ubicacion_municipio')
    #ubicacion_municipio.setFrameEnabled(True)
    ubicacion_municipio.setLayers([lyr_Box,lyr_POP,lyr_municipio])
    ubicacion_municipio.zoomToExtent(lyr_municipio.extent())
    ubicacion_municipio.setBlendMode(2)  # Force render as image

    project.addMapLayers([lyr_POP])
    mapa_principal = layout.itemById('mapa_principal')
    xform = QgsCoordinateTransform(lyr_POP.crs(), project.crs(), project) #create reproject
    #mapa_principal.zoomToExtent(xform.transform(lyr_POP.extent().buffered(0.01)))
    mapa_principal.zoomToExtent(xform.transform(lyr_POP.extent()))
    i = mapa_principal.scale()
    p1 = i // 10000
    p2 = i % 10000
    c = p2 // 1000
    s = 0
    if c > 5:
        s = (p1 + 1) * 10000
    else:
        s = (p1 * 10000) + 5000
    #print(i, p1, p2, c, s)
    mapa_principal.setScale(s, True)
    canvas.refresh()

    exporter = QgsLayoutExporter(layout)
    # setup settings
    settings = QgsLayoutExporter.PdfExportSettings()
    settings.dpi = 180
    settings.rasterizeWholeImage = False
    settings.forceVectorOutput = False
    settings.exportMetadata = False

    # exporter.exportToPdf("mapa_bing.pdf", QgsLayoutExporter.PdfExportSettings() )
    exporter.exportToPdf("mapa_bing.pdf", settings)

    project.layerTreeRoot().findLayer(lyr_BingMap.id()).setItemVisibilityChecked(False)
    layerOSM = project.instance().mapLayersByName('OSM')[0]
    project.layerTreeRoot().findLayer(layerOSM.id()).setItemVisibilityChecked(True)
    lyr_POP.loadNamedStyle('pop.qml')
    exporter.exportToPdf("mapa_osm.pdf", settings)


make_pdf()

qgs.exitQgis()
