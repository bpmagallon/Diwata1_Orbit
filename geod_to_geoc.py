from math import cos, sin, sqrt, radians

#constatns
e2= 0.0066943799014
a= 6378.137

def geod_geoc(pt):

    lat=pt[0]
    lon=pt[1]
    h=pt[2]

    N = a/(sqrt(1-(e2*(sin(radians(lat))**2))))
    x = (N+h)*(cos(radians(lat)))*(cos(radians(lon)))
    y = (N+h)*(cos(radians(lat)))*(sin(radians(lon)))
    z = ((N*(1-e2))+h)*sin(radians(lat))

    return x,y,z
