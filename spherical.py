from math import radians, degrees, cos, sin, asin, acos

def getAngles(pos1, pos, fov):
    #use 0.95 and 0.7 for HPT
        # use 26 and 19.5 for SMI
    fov[0] = degrees(41/6378.137)
    fov[1] = degrees(31/6378.137)
    true_deltaLON1 = 0
    true_deltaLON2 = 0
    true_deltaLON3 = 0
    true_deltaLON4 = 0

    true_deltaLAT1 = 0
    true_deltaLAT2 = 0
    true_deltaLAT3 = 0
    true_deltaLAT4 = 0

    if pos1[0] > pos[0]:
        
        deltaLAT = radians(abs(pos[0] - pos1[0])) #a
        deltaLON = radians(abs(pos[1] - pos1[1])) #b


        c = (acos((cos(deltaLAT))*(cos(deltaLON))))
        alpha = degrees(asin((sin(deltaLAT))/(sin(c))))
        a = asin((sin(radians(alpha)))*(sin(radians(fov[0]))))
        beta = 90 - alpha

        b = asin((sin(radians(beta)))*sin(radians(fov[0])))


        psi = radians(90-alpha)

        b_1 = asin((sin(psi))*(sin(radians(fov[1]))))
        true_deltaLAT1 = (degrees(a) + degrees(b_1))*-1
        a_1 = asin((sin(radians(alpha)))*(sin(radians(fov[1]))))

        true_deltaLON1 = degrees(b) - degrees(a_1)

        true_deltaLAT2 = (degrees(a) - degrees(b_1))*-1
        true_deltaLON2 = degrees(b) + degrees(a_1)

        true_deltaLAT3 = true_deltaLAT1 * -1
        true_deltaLON3 = true_deltaLON1 * -1

        true_deltaLAT4 = true_deltaLAT2 * -1
        true_deltaLON4 = true_deltaLON2 * -1

    else:

        deltaLAT = radians(abs(pos[0] - pos1[0])) #b
        deltaLON = radians(abs(pos[1] - pos1[1])) #a

        c = (acos((cos(deltaLAT))*(cos(deltaLON))))
        alpha = degrees(asin(sin(deltaLON)/sin(c)))
        beta = 90 - alpha
        b = asin(sin(radians(beta))*sin(radians(fov[0])))
        a = asin((sin(radians(alpha)))*sin(radians(fov[0])))

        psi = radians(90-alpha)

        b_1 = asin((sin(psi))*(sin(radians(fov[1]))))
        a_1 = asin((sin(radians(alpha)))*(sin(radians(fov[1]))))

        true_deltaLAT1 = degrees(b) - degrees(a_1)
        true_deltaLON1 = degrees(a) + degrees(b_1)

        true_deltaLAT2 = degrees(b) + degrees(a_1)
        true_deltaLON2 = degrees(a) - degrees(b_1)

        true_deltaLAT3 = true_deltaLAT1 * -1
        true_deltaLON3 = true_deltaLON1 * -1

        true_deltaLAT4 = true_deltaLAT2 * -1
        true_deltaLON4 = true_deltaLON2 * -1

    dir_p1 = [true_deltaLAT1,true_deltaLON1]
    dir_p2 = [true_deltaLAT2,true_deltaLON2]
    dir_p3 = [true_deltaLAT3,true_deltaLON3]
    dir_p4 = [true_deltaLAT4,true_deltaLON4]
        
    return dir_p1,dir_p2,dir_p3,dir_p4
