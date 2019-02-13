<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology|Labeling" version="3.4.4-Madeira" labelsEnabled="1">
  <renderer-v2 enableorderby="0" type="RuleRenderer" forceraster="0" symbollevels="0">
    <rules key="{75caa781-7d18-4770-99b2-a05e7748d98f}">
      <rule label="medium size" key="{d1ab6a79-4c5c-462c-b569-89ee95351782}" filter="_area >=1" symbol="0"/>
      <rule label="small size" key="{25f3c0f7-59a9-4190-810b-f0cc386d1ad6}" filter="_area &lt; 1" symbol="1"/>
    </rules>
    <symbols>
      <symbol alpha="1" clip_to_extent="1" force_rhr="0" type="fill" name="0">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="141,90,153,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="155,150,154,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.03" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" force_rhr="0" type="fill" name="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="133,182,111,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="209,203,208,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.01" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{2aa089b9-7217-49b6-ba77-775704ff09f7}">
      <rule description="medium size" key="{544980df-797c-470e-8e2f-c1c83178ddb5}" filter="_area >=1">
        <settings>
          <text-style useSubstitutions="0" multilineHeight="1" fontStrikeout="0" textColor="255,255,255,255" fontWordSpacing="0" previewBkgrdColor="#ffffff" textOpacity="1" fontItalic="0" fontFamily="Arial" fontSizeUnit="Point" fontCapitals="0" fontLetterSpacing="0" isExpression="0" namedStyle="Regular" fontUnderline="0" blendMode="0" fontSize="5" fieldName="uso_pop" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50">
            <text-buffer bufferColor="0,0,0,255" bufferNoFill="1" bufferOpacity="1" bufferSize="0.2" bufferSizeUnits="MM" bufferJoinStyle="128" bufferDraw="1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <background shapeSizeType="0" shapeOffsetY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOpacity="1" shapeSizeY="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="MM" shapeRotation="0" shapeBorderWidthUnit="MM" shapeDraw="0" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetUnit="MM" shapeRadiiX="0" shapeBlendMode="0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeType="0" shapeOffsetX="0"/>
            <shadow shadowRadiusUnit="MM" shadowScale="100" shadowBlendMode="6" shadowDraw="0" shadowUnder="0" shadowOffsetAngle="135" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowRadiusAlphaOnly="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowOffsetUnit="MM" shadowOpacity="0.7"/>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" wrapChar="" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0" placeDirectionSymbol="0" formatNumbers="0" rightDirectionSymbol=">" decimals="3" multilineAlign="4294967295" leftDirectionSymbol="&lt;" autoWrapLength="0"/>
          <placement fitInPolygonOnly="0" quadOffset="4" priority="5" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" placementFlags="10" xOffset="0" dist="0" maxCurvedCharAngleOut="-25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" rotationAngle="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placement="1" offsetType="0" repeatDistance="0" repeatDistanceUnits="MM" offsetUnits="MM" preserveRotation="1" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="1" maxCurvedCharAngleIn="25" yOffset="0"/>
          <rendering drawLabels="1" maxNumLabels="3" fontMinPixelSize="3" obstacleFactor="1" limitNumLabels="0" labelPerPart="1" minFeatureSize="3" scaleMax="0" scaleVisibility="0" scaleMin="0" obstacleType="1" fontMaxPixelSize="10000" displayAll="0" obstacle="1" upsidedownLabels="0" mergeLines="0" fontLimitPixelSize="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule description="small size" key="{266f9c22-05ba-4c4f-b0ce-547d382040ee}" filter="_area > 0.01 AND _area &lt; 1 ">
        <settings>
          <text-style useSubstitutions="0" multilineHeight="1" fontStrikeout="0" textColor="255,255,255,255" fontWordSpacing="0" previewBkgrdColor="#ffffff" textOpacity="1" fontItalic="0" fontFamily="Arial" fontSizeUnit="Point" fontCapitals="0" fontLetterSpacing="0" isExpression="0" namedStyle="Regular" fontUnderline="0" blendMode="0" fontSize="1.5" fieldName="uso_pop" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50">
            <text-buffer bufferColor="0,0,0,255" bufferNoFill="1" bufferOpacity="1" bufferSize="0.05" bufferSizeUnits="MM" bufferJoinStyle="128" bufferDraw="1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <background shapeSizeType="0" shapeOffsetY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOpacity="1" shapeSizeY="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="MM" shapeRotation="0" shapeBorderWidthUnit="MM" shapeDraw="0" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetUnit="MM" shapeRadiiX="0" shapeBlendMode="0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeType="0" shapeOffsetX="0"/>
            <shadow shadowRadiusUnit="MM" shadowScale="100" shadowBlendMode="6" shadowDraw="0" shadowUnder="0" shadowOffsetAngle="135" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowRadiusAlphaOnly="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowOffsetUnit="MM" shadowOpacity="0.7"/>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" wrapChar="" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0" placeDirectionSymbol="0" formatNumbers="0" rightDirectionSymbol=">" decimals="3" multilineAlign="4294967295" leftDirectionSymbol="&lt;" autoWrapLength="0"/>
          <placement fitInPolygonOnly="0" quadOffset="4" priority="5" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" placementFlags="2" xOffset="0" dist="0" maxCurvedCharAngleOut="-25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" rotationAngle="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placement="0" offsetType="0" repeatDistance="0" repeatDistanceUnits="MM" offsetUnits="MM" preserveRotation="0" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" maxCurvedCharAngleIn="25" yOffset="0"/>
          <rendering drawLabels="1" maxNumLabels="2000" fontMinPixelSize="3" obstacleFactor="1" limitNumLabels="0" labelPerPart="0" minFeatureSize="0" scaleMax="0" scaleVisibility="0" scaleMin="0" obstacleType="0" fontMaxPixelSize="10000" displayAll="0" obstacle="1" upsidedownLabels="0" mergeLines="0" fontLimitPixelSize="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
    </rules>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>2</layerGeometryType>
</qgis>
