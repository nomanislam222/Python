#task8
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
list_three = []
for i in list_one:
    if i%2==0:
        list_three.append(i)
for i in list_two:
    if i%2==0:
        list_three.append(i)
print(list_three)
