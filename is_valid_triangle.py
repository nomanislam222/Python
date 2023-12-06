def is_valid_triangle(x, y, z):
    if x + y > z and y + z > x and x + z > y:
        return True
    else:
        return False

result = is_valid_triangle(3,2,1)
print(result)
