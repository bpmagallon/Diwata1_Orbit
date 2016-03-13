import math

def closest(pt, array):
    distance = 99999999999999999
    count=0
    close_pt = []
    location = 0
    for i in array:
        dist_sat_grs = math.sqrt(((pt[0]-i[0])**2)+((pt[1]-i[1])**2)+((pt[2]-i[2])**2))
        if dist_sat_grs<distance:
            close_pt = i
            distance = dist_sat_grs
            location=count
        else:
            pass
        count+=1
    return close_pt,distance,location
"""
def shotted(pt, array):
    count = 0
    for i in array:
        if (pt[0]==i[0]) and (pt[1]==i[1]) and (pt[2]==i[2]):
            count+=1
        else:
            pass
    if count>0:
        return True
    else:
        return False
"""
