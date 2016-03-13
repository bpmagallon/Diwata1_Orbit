#xyz to lat long
from math import atan, sin, cos, degrees, sqrt, radians

def geoc_to_geod(pt):
    x = pt[0]
    y = pt[1]
    z = pt[2]

    lamba = degrees(atan(abs(y/x)))
    if y>0 and x>0:
        lamba = lamba
    elif y>0 and x<0:
        lamba=180-lamba
    elif y<0 and x<0:
        lamba=(180+lamba)
    else:
        lamba=360-lamba
    
    e2 = 0.0066943799014
    a = 6378.137

    div = sqrt((x*x)+(y*y))
    phi = atan(z/div)
    count = 0
    
    while count<3:
        div1 = e2*((sin(phi))*(sin(phi)))
        N=a/(sqrt(1-div1))
        div2 =sqrt((x*x)+(y*y))
        h=(div2/(cos(phi)))-N
        fac1 = z/(sqrt((x*x)+(y*y)))
        div3 =(e2*N)/(N+h)
        
        new_phi = atan(fac1/(1-div3))
        
        diff = abs(degrees(new_phi)-degrees(phi))
        phi = new_phi
        count = count + 1
    return degrees(phi), lamba, h
