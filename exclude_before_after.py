n= input("Sample Input:")
list_one = []
char = ""

for i in n:
  if i == ",":
    list_one.append(int(char))
    char = ""
  else:
    char += i
list_one.append(int(char))

if len(list_one)>=4:
    print(list_one[2:len(list_one)-2])
else:
    print("Not possible"
