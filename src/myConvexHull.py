# TODO: Make the sort function
# TODO: Make the divide part
# TODO: Make the combine part
# ! Consider edge cases
import numpy as np

def myConvexHull(bucket):
    sorted_bucket = bucket(key=lambda i: i[0])
    p1 = sorted_bucket[0]
    pn = sorted_bucket[-1]
    maxtable = [point for point in sorted_bucket if pointDetermination([p1, pn], point) > 0]
    mintable = [point for point in sorted_bucket if pointDetermination([p1, pn], point) < 0]
     
    
    p_global_max = (maxtable[0] == maxtable[1]) if (calculateAngle(p1,maxtable[0],pn) > calculateAngle(p1,maxtable[1],pn) if maxtable[1] else maxtable[0]) else maxtable[0]
    p_global_min = (mintable[0] == mintable[1]) if (calculateAngle(p1, mintable[0], pn) > calculateAngle(p1, mintable[1], pn) if mintable[1] else mintable[0]) else mintable[0]

    def myConvexHullRecursion(p_start, p_max):

        pass


def calculateAngle(p1, p2, p3):
    a = np.array(p1)
    b = np.array(p2)
    c = np.array(p3)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine_angle)

def pointDetermination(line, point):
    p1 = line[0]
    p2 = line[-1]
    res = p1[0] * p2[1] + point[0] * p1[1] + p1[0] * point[1] - \
        point[0] * p2[1] - p2[0] * p1[1] - p1[0] * point[1]
    return res
