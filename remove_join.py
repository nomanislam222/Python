#task 5
list_one = [1, 4, 7, 5]
list_two = [6, 1, 3, 9]

list_one = list_one[0:len(list_one)-1]
for i in list_two:
    list_one.append(i)
print(list_one)
