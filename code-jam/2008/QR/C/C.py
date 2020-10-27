import math

def circle_segment(rad, th):
    return rad*rad*(th - math.sin(th))/2


N = int(input())
for i in range(1, N+1):
    row = input()
    f = float(row.split(' ')[0])
    R = float(row.split(' ')[1])
    t = float(row.split(' ')[2])
    r = float(row.split(' ')[3])
    g = float(row.split(' ')[4])

    rad = R-t-f
    ar = 0

    square_per_line = math.ceil(((R-t-f)-(r+f))/(g+2*r))
    for j in range(square_per_line):
        x1 = (r + f) + j * (g + 2 * r)
        for k in range(square_per_line):
            y1 = (r+f) + k*(g+2*r)
            x2 = x1 + g - 2*f
            y2 = y1 + g - 2*f
            if x2 <= x1 or y2 <= y1:
                continue
            if x1*x1 + y1*y1 >= rad*rad:
                continue
            if x2*x2 + y2*y2 <= rad*rad:
                # All points are inside circle.
                ar += (x2-x1)*(y2-y1)
            elif x1*x1 + y2*y2 >= rad*rad and x2*x2 + y1*y1 >= rad*rad:
                # Only (x1,y1) inside circle.
                ar += circle_segment(rad, math.acos(x1/rad) - math.asin(y1/rad)) + \
                      (math.sqrt(rad*rad - x1*x1)-y1) * (math.sqrt(rad*rad - y1*y1)-x1) / 2
            elif x1*x1 + y2*y2 >= rad*rad:
                # (x1,y1) and (x2,y1) inside circle.
                ar += circle_segment(rad, math.acos(x1/rad) - math.acos(x2/rad)) + \
                      (x2-x1) * (math.sqrt(rad*rad - x1*x1)-y1 + math.sqrt(rad*rad - x2*x2)-y1) / 2
            elif x2*x2 + y1*y1 >= rad*rad:
                # (x1,y1) and (x1,y2) inside circle.
                ar += circle_segment(rad, math.asin(y2/rad) - math.asin(y1/rad)) + \
                      (y2-y1) * (math.sqrt(rad*rad - y1*y1)-x1 + math.sqrt(rad*rad - y2*y2)-x1) / 2
            else:
                # All except (x2,y2) inside circle.
                ar += circle_segment(rad, math.asin(y2/rad) - math.acos(x2/rad)) + \
                      (x2-x1)*(y2-y1) - (y2-math.sqrt(rad*rad - x2*x2)) * (x2-math.sqrt(rad*rad - y2*y2)) / 2;
    print("Case #{}: {:f}".format(i, 1.0 - ar / (math.pi*R*R/4)))
