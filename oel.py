n = input("Sample Input:")
list_one = []
list_two = []
store = ""

for i in n:
  if i == ",":
    list_one.append(int(store))
    store = ""
  else:
    store += i
list_one.append(int(store))
print(f"Original list: {list_one}")
for i in list_one:
    if i%2==0:
        list_two.append(i)
print(list_two)
