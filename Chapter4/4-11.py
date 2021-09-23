def intervalOverlap(a1, a2, b1, b2):
    return (b1 <= a2) if (b1 >= a1) else (a1 <= b2)
def getIntersect(a1, a2, b1, b2):
    return (b1, min(b2, a2)) if (b1 >= a1) else (a1, min(a2, b2))
def rectIntersection(r1, r2):
    r1_x1, r1_x2 = r1[0], r1[0] + r1[2]
    r1_y1, r1_y2 = r1[1], r1[1] + r1[3]

    r2_x1, r2_x2 = r2[0], r2[0] + r2[2]
    r2_y1, r2_y2 = r2[1], r2[1] + r2[3]
    if intervalOverlap(r1_x1, r1_x2, r2_x1, r2_x2) and intervalOverlap(r1_y1, r1_y2, r2_y1, r2_y2):
        t1 = getIntersect(r1_x1, r1_x2, r2_x1, r2_x2)
        t2 = getIntersect(r1_y1, r1_y2, r2_y1, r2_y2)
        return (t1[0], t1[1] - t1[0], t2[0], t2[1] - t2[0])
    else:
        return None

r1 = (0, 0, 2, 3)
r2 = (1, 1, 1, 1)
print(rectIntersection(r1, r2))
