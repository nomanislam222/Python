#Task 4
List_one = [1, 4, 3, 2, 6]
List_two = [5, 6, 9, 8, 7]

flag = False
for i in List_one:
    if i in List_two:
        flag = True
        break
print(flag)
