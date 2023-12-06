b=[]
a=input("sample input:")
store=a.split(",")
for i in range(len(store)):
    store[i]=int(store[i])
print(f"Original List:{store}")

smallest = second_smallest = store[0]
index=second_index=0
for i in range(1,(len(store))):
    if smallest > store[i]:
        second_smallest = smallest
        second_index=index
        smallest = store[i]
        index=i
print(f"samllest number in the list is {smallest} which was found at index {index}.")
print(f" second samllest number in the list is {second_smallest} which was found at index {second_index}.")
