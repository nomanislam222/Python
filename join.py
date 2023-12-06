#task 7
list_one = [1, 3, 5, 7, 9, 10]
list_two = [2, 4, 6, 8]
list_one = list_one[0:len(list_one)-1]
for i in list_two:
    list_one.append(i)
print(list_one)
