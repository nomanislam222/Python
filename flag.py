
#Task 11
List_one = [1, 4, 3, 2, 9]
List_two = [8, 7, 6, 9]
flag = False
for i in List_one:
    if i in List_two:
        flag = True
        break
print(flag)
