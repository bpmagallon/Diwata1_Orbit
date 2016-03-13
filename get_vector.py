import math

def get_dirv(pt1, pt2):
    dist = math.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2))
    x_dir = (pt2[0]-pt1[0])/dist
    y_dir = (pt2[1]-pt1[1])/dist
    z_dir = (pt2[2]-pt1[2])/dist

    return x_dir,y_dir,z_dir
