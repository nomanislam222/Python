#task 2
a = input("Enter a number: ")
split = a[1:-1].split(',')
b =[]
for i in split:
  b.append(int(i))
if len(b)>= 4:
    print(b[2:-2])
else:
    print("Not possible")
