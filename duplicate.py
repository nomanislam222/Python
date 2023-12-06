
a=input("Sample input:")
list_one=a.split(",")
list_two = []

for i in range(len(list_one)):
    list_one[i]= int(list_one[i])
print(f"Input list:{list_one}")
for i in list_one:
    if i not in list_two:
        list_two.append(i)
print(f"Modified list: {list_two}")
