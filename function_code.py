import math

def complex1(candidate):
    x, y = candidate[0], candidate[1]

    # Use rotation matrix
    x_ = x * math.cos(math.radians(35)) - y * math.sin(math.radians(35))
    y_ = x * math.sin(math.radians(35)) + y * math.cos(math.radians(35)) + 70
    x__ = x * math.cos(math.radians(90)) - y * math.sin(math.radians(90))
    y__ = x * math.sin(math.radians(90)) + y * math.cos(math.radians(90))

    if -90 <= x <= -65 or -50 <= x <= -26 or 0 <= x <= 20 or 50 <= x <= 100:
        if -75 <= y <= -45 or -5 <= y <= 15 or 35 <= y <= 55 or 72 <= y <= 85:
            z = 1/1000 * ((x_ + 100) - (y_ - 100)) ** 2
        else:
            z = 1/1000 * (x - y) ** 2
    else:
        # base plane
        if -65 <= y <= -40:
            z = 1 / 1000 * ((x__ - 20) - (y__ + 20)) ** 2
        else:
            z = 1/1000 * ((x__ - 100) - (y__ + 100)) ** 2

    # Shift every small z value +2 in y direction
    if z <= 5.0:
        z = z + 2

    # Embed global minimum
    if 13.25 <= x <= 17.9 and 13.25 <= y <= 17.9:
        z = 1.5 * (math.exp((17.9 - x) / 2) + math.exp((17.9 - y) / 2)) - 3
        if z >= 2:
            z = 2

    # Have some additional discontinuous jumps in the landscape
    if 10 <= z <= 15:
        return 120

    return z
