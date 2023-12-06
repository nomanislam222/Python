#task5
a = ["hey", "there", "", "what's", "", "up", "", "?"]
b=[]
for i in a:
    if i == "":
        continue
    else:
        b.append(i)
print(b)
