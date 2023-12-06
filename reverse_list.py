#Task 2
input_list = input("Enter a list:").split(',')
reversed_list = []

for i in range(len(input_list) - 1, -1, -1):
    reversed_list.append(input_list[i])
print("Reversed list:", reversed_list)
