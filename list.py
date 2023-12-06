#Task 1
#With append function
list1 = []
for i in range(5):
    n = int(input(f"Input{i+1}:"))
    list1.append(n)
    print(list1)


#Without append function
list1 = []
for i in range(5):
    n = int(input(f"Input{i+1}:"))
    list1 = list1 + [n]
    print(list1)
