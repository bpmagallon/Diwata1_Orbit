import numpy as np
import math
import dateAdd
import urllib
import geoc_geod
import getXY
import arcpy
import getNearest
import ephem
import datetime
import geod_to_geoc
import isAM
import groundtrack
import get_vector
import spherical

arcpy.env.overwriteOutput = True

celestrak = urllib.urlopen("http://www.celestrak.com/NORAD/elements/stations.txt")
tle_data = celestrak.readlines()
celestrak.close()
iss_tle1 = tle_data[1]
iss_tle2 = tle_data[2]
now = datetime.datetime.utcnow() + datetime.timedelta(11,2)
now1 = datetime.datetime.utcnow() + datetime.timedelta(11,1)
iss = ephem.readtle('GOSAT', iss_tle1, iss_tle2)
iss.compute(now)
lat=math.degrees(iss.sublat)
lon=math.degrees(iss.sublong)
h=math.degrees(iss.elevation)
pos = [lat,lon,0]
position = geod_to_geoc.geod_geoc(pos)

iss.compute(now1)
lat1=math.degrees(iss.sublat)
lon1=math.degrees(iss.sublong)
h1=(iss.elevation)
print h1

pos1 = [lat1,lon1,0]
position1 = geod_to_geoc.geod_geoc(pos)

#check if sat pos is within the effective radius
eff_rad = 41
#nadir =   32.5 ; 5deg = 1759.6248751; 15deg from horizon =  1105.2976329; 45deg from horizon = 377.3453284 60deg = 230.9401 ;75deg = 107.1797;
smi_pt = getXY.getCoords(r'C:\Users\Satellite L40D\Documents\philmicrosat_study\path_simulation\gis_files\country_reduceph4.shp')
input_pts = r'C:\Users\Satellite L40D\Documents\philmicrosat_study\path_simulation\gis_files\country_reduceph4.shp'
track = []
date_pass = []
near = []
duration = 0
ground_track = []
ground_track_pm = []
date_pass_pm = []
track_pm = []

sr = arcpy.SpatialReference(4326)
count = 0
factor = 0

while duration<=1209600:
    
    near = getNearest.closest(position, smi_pt)
    print now
    time = isAM.isMorning(str(now))
    if (near[1]<=eff_rad) and (time==True):
        while (near[1]<=eff_rad) and (time==True):
            print "time enter:"+str(now)
            print "pass"
            param = spherical.getAngles(pos1,pos,fov)

            geod_near = geoc_geod.geoc_to_geod(near[0])
            
            ground_track_1 = [geod_near[1]+param[0][1],geod_near[0]+param[0][0]]
            ground_track_2 = [geod_near[1]+param[1][1],geod_near[0]+param[1][0]]
            ground_track_3 = [geod_near[1]+param[2][1],geod_near[0]+param[2][0]]
            ground_track_4 = [geod_near[1]+param[3][1],geod_near[0]+param[3][0]]

            arcpy.CreateFeatureclass_management(r"C:\\Users\\Public\\Documents\\tracks", "groundtrack_"+str(count)+".shp", "Polygon", "", "", "", sr)
            arcpy.AddField_management("C:\\Users\\Public\\Documents\\tracks\\groundtrack_"+str(count)+".shp", 'TIME', 'TEXT')
            polygonFC = r"C:\\Users\\Public\\Documents\\tracks\\groundtrack_"+str(count)+".shp"
            c = arcpy.InsertCursor(polygonFC)
            id = count + 1
            counter=0
            array = arcpy.Array([arcpy.Point(ground_track_1[0],ground_track_1[1]),arcpy.Point(ground_track_2[0],ground_track_2[1]),
                                 arcpy.Point(ground_track_3[0],ground_track_3[1]),arcpy.Point(ground_track_4[0],ground_track_4[1])])
            polygon = arcpy.Polygon(array)
            row = c.newRow()
            row.id = id
            row.Shape = polygon

            lati = [math.degrees(iss.sublat),math.degrees(iss.sublong),iss.elevation]
            track.append(lati)

            ph_time = now + datetime.timedelta(0,28800)
            date_pass.append(str(ph_time.date())+"-"+str(ph_time.time()))
            
            row.TIME = (str(ph_time.date())+"-"+str(ph_time.time()))
            c.insertRow(row)
            id+=1
            del c, polygon

            input_pts = input_pts
            smi_pt = getXY.getCoords(input_pts)
            count = count + 1
            if duration==0:
                now = now + datetime.timedelta(0,2)
            else:
                now = now + datetime.timedelta(0,1)
                
            duration = duration + 1
            iss.compute(now)
            lat=math.degrees(iss.sublat)
            lon=math.degrees(iss.sublong)
            pos1 = pos
            pos = [lat,lon,0]
            position1 = position
            position = geod_to_geoc.geod_geoc(pos)
            near = getNearest.closest(position, smi_pt)
            time = isAM.isMorning(str(now))
            
    else:
        if duration==0:
                now = now + datetime.timedelta(0,2)
                factor=2
        else:
            if near[1]<=100:
                now = now + datetime.timedelta(0,1)
                factor=1
            else:
                now = now + datetime.timedelta(0,30)
                factor =30
        duration = duration + factor
        iss.compute(now)
        lat=math.degrees(iss.sublat)
        lon=math.degrees(iss.sublong)
        pos1 = pos
        pos = [lat,lon,0]
        position1 = position
        position = geod_to_geoc.geod_geoc(pos)
        time = isAM.isMorning(str(now))
        factor = 0   
        
sr = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(r"C:\\Users\\Public\\Documents\\tracks", "track.shp", "Point", "", "", "", sr)
arcpy.AddField_management("C:\\Users\\Public\\Documents\\tracks\\track.shp", 'LAT', 'double', '12', '3',)
arcpy.AddField_management("C:\\Users\\Public\\Documents\\tracks\\track.shp", 'LON', 'double', '12', '3',)
arcpy.AddField_management("C:\\Users\\Public\\Documents\\tracks\\track.shp", 'TIME', 'TEXT')
cur = arcpy.InsertCursor("C:\\Users\\Public\\Documents\\tracks\\track.shp")
pt = arcpy.Point()
id = 1
count=0
for i in track:
    pt.X = float(i[1])
    pt.Y = float(i[0])
    row = cur.newRow()
    row.Shape = pt
    row.id = id
    row.LAT = pt.Y
    row.LON = pt.X
    row.TIME = str(date_pass[count])
    cur.insertRow(row)
    id+=1
    count+=1
del cur, pt
