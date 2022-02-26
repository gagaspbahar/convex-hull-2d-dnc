import numpy as np
convexList = []

# Main convex hull function
def myConvexHull(bucket):
    # variable init
    sorted_bucket = bucket[bucket[:, 0].argsort()]
    sorted_bucket = sorted_bucket.tolist()
    p1 = sorted_bucket[0]
    pn = sorted_bucket[-1]
    # recurse, store memo in convexList.
    global convexList
    convexList = [p1, pn]
    maxtable = [point for point in sorted_bucket if pointDetermination([p1, pn], point) > 0]
    mintable = [point for point in sorted_bucket if pointDetermination([p1, pn], point) < 0]
    myConvexHullRecursion(p1, pn, maxtable, True)
    myConvexHullRecursion(p1, pn, mintable, False)
    return convexList

# recursive function
def myConvexHullRecursion(p_start, p_end, table, isUpper):
    global convexList
    # case if its the upper part (take the max)
    if(isUpper):
        if(len(table) == 0):
            # base case if 0
            return
        else:
            p_start_index = convexList.index(p_start)
            if(len(table) == 1):
                # Base case if 1
                p_max = table[0]
                convexList.insert(p_start_index+1, p_max)
                return
            else:
                # convex point determination
                points = [pointDetermination([p_start, p_end], point) for point in table]
                max_index = points.index(max(points))
                p_max = table[max_index]
                convexList.insert(p_start_index+1, p_max)
                new_table_start = [point for point in table if pointDetermination([p_start, p_max], point) > 0]
                new_table_end = [point for point in table if pointDetermination([p_max, p_end], point) > 0]
                myConvexHullRecursion(p_start, p_max, new_table_start, True)
                myConvexHullRecursion(p_max, p_end, new_table_end, True)
    else:
        if(len(table) == 0):
            return
        else:
            p_end_index = convexList.index(p_end)
            if(len(table) == 1):
                p_min = table[0]
                convexList.insert(p_end_index+1, p_min)
                return
            else:
                points = [pointDetermination([p_start, p_end], point) for point in table]
                min_index = points.index(min(points))
                p_min = table[min_index]
                convexList.insert(p_end_index+1, p_min)
                new_table_start = [point for point in table if pointDetermination([p_start, p_min], point) < 0]
                new_table_end = [point for point in table if pointDetermination([p_min, p_end], point) < 0]
                myConvexHullRecursion(p_start, p_min, new_table_start, False)
                myConvexHullRecursion(p_min, p_end, new_table_end, False)

# point determination function via determinant
def pointDetermination(line, point):
    p1 = line[0]
    p2 = line[-1]
    a = np.array([[p1[0], p1[1], 1], [p2[0], p2[1], 1], [point[0], point[1], 1]])
    return np.linalg.det(a)