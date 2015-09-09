""" 
Script Name: Map_Index.py

https://github.com/npeihl/mapindextool

Description: ArcGIS Tool written in Python.  The Map Index Tool creates a geographic index of all ArcMap documents (MXDs) in a folder supplied by the user. For each MXD, the tool finds the largest dataframe on the Layout view and sends the extent of that dataframe to a shapefile in the folder (map_index.shp). Tested on ArcGIS Desktop version 10. Not tested and likely not working on ArcGIS Desktop versions 9.3.1 and below.

WARNING: This tool will destroy and overwrite any shapefile named map_index within the supplied folder. Please use with caution.

Author: Nicholas Peihl
Email: nick.peihl@gmail.com

Last Modified: 04/20/2011
"""
import arcpy
import os, sys
from datetime import datetime
from time import strftime

wp = arcpy.GetParameterAsText(0)
spatialRef = arcpy.GetParameterAsText(1)
fcName = "map_index.shp"
scriptPath = sys.path[0]
arcpy.AddMessage("Script path is %s" % scriptPath)
toolDataPath = os.path.join(scriptPath, "ToolData")
fcTemplate = os.path.join(toolDataPath, "map_index_template.shp")

arcpy.env.workspace = wp
files = arcpy.ListFiles("*.mxd")
if len(files) == 0:
	arcpy.AddError("No ArcMap Documents were found in this folder. Please try another folder.")
else:
	if arcpy.Exists(os.path.join(wp, fcName)):
		arcpy.AddWarning("Existing Map Index shapfile found. Deleting the old index file.")
		arcpy.Delete_management(fcName)

	arcpy.AddMessage("Creating the new Map Index shapefile")
	index = arcpy.CreateFeatureclass_management(wp, fcName, "POLYGON", fcTemplate,"","", spatialRef)

	for mxd in files:
		mxd = wp + "\\" + mxd
		arcpy.AddMessage("Opening map document %s" % mxd)
		mapDoc = arcpy.mapping.MapDocument(mxd)
		dataframes = arcpy.mapping.ListDataFrames(mapDoc)
		if len(dataframes) == 1:
			pFrame = dataframes[0]
		else:
			max = 0
			for frame in dataframes:
				size = frame.elementWidth * frame.elementHeight
				if size > max:
					pFrame = frame
					max = size
					
		xmin = pFrame.extent.XMin
		ymin = pFrame.extent.YMin
		xmax = pFrame.extent.XMax
		ymax = pFrame.extent.YMax
		framespatialRef = pFrame.spatialReference
		
		coords = [xmin,ymin],[xmax,ymin],[xmax,ymax],[xmin, ymax]
		point = arcpy.Point()
		array = arcpy.Array()
		
		for coord in coords:
			point.X = coord[0]
			point.Y = coord[1]
			array.append(point)
			
		polygon = arcpy.Polygon(array, framespatialRef)
		
		arcpy.AddMessage("Adding the extent of %s to the index." % mxd)
		rows = arcpy.InsertCursor(index, spatialRef)
		row = rows.newRow()
		row.PATH = mapDoc.filePath
		row.TITLE = mapDoc.title
		row.AUTHOR = mapDoc.author
		row.LASTSAVED = mapDoc.dateSaved
		row.LASTUPDATE = datetime.strftime(datetime.now(),"%Y-%m-%d")
		row.SHAPE = polygon
		rows.insertRow(row)
		
		del row
		del rows





