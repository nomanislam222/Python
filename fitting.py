#CW-3.3
import math
def circle(radius):
    area = math.pi * (radius ** 2)
    return area

def sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def fitting(d1, d2, dimension):
    r1 = d1 / 2
    r2 = d2 / 2

    if dimension == 2:
        area1 = circle(r1)
        area2 = circle(r2)

        if area1 < area2:
            space = area2 - area1
            print(f"Circle-1 can fit inside Circle-2 and {space} square units would be left.")

        elif area2 < area1:
            space = area1 - area2
            print(f"Circle-2 can fit inside Circle-1 and {space} square units would be left.")

        else:
            print("Impossible to fit.")


    elif dimension == 3:
        volume1 = sphere(r1)
        volume2 = sphere(r2)

        if volume1 < volume2:
            space = volume2 - volume1
            print(f"Sphere-1 can fit inside Sphere-2 and {space} cubic units would be left.")

        elif volume2 < volume1:
            space = volume1 - volume2
            print(f"Sphere-2 can fit inside Sphere-1 and {space} cubic units would be left.")

        else:
            print("Impossible to fit.")

    else:
        print("Invalid Input")

fitting(5,5,3)
