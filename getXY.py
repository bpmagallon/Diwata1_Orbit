import arcpy
import geod_to_geoc
#import geoc_geod

def getCoords(string):
    smi = string
    smi_xy = []

    rows = arcpy.SearchCursor(smi)
    for row in rows:
        lon = row.getValue("POINT_X")
        lat = row.getValue("POINT_Y")
        h = 0
        pt = [lat, lon, h]
        #print pt
        xyz = geod_to_geoc.geod_geoc(pt)
        #geod_near = geoc_geod.geoc_to_geod(xyz)
        #print geod_near
        smi_xy.append(xyz)

        
    del rows
    return smi_xy
"""
hpt = r'C:\Users\Satellite L40D\Documents\philmicrosat_study\path_simulation\gis_files\metro_manila_hpt_pt.shp'
hpt_xy = []

rows = arcpy.SearchCursor(hpt)
for row in rows:
    lon = row.getValue("POINT_X")
    lat = row.getValue("POINT_Y")
    h = 0
    pt = [lat, lon, h]
    xyz = geod_to_geoc.geod_geoc(pt)
    hpt_xy.append(xyz)

    
del rows
del row
"""
