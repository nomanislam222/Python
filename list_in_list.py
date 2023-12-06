grade_list = []

for i in range(5):
    n = input("Enter Name and GPA:")
    n = n[1:len(n)-1]
        
    name, gpa_string = n.split(',')
    gpa = float(gpa_string)
    grade_list.append([name, gpa])
    print(grade_list)
