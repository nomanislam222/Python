
b=[]
another_list=[]
for i in range(5):
    a=int(input("Enter a number:"))
    b.append(a**3)
print("Reverse:")
for i in range(len(b)-1,-1,-1):
    print(b[i])

for j in b:
    if j % 2 == 0:
        another_list.append(int(j))
print(f"Even list:{another_list}")
