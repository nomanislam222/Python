#CW-2.2
def is_valid_triangle(x, y, z):
    if x + y > z and y + z > x and x + z > y:
        return True
    else:
        return False

def tri_area(a, b, c):
    if is_valid_triangle(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        print(area)
    else:
        print("Can't form triangle")

tri_area(7,5,10)
