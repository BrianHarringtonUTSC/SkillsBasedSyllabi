given_name = input("Enter student given name :")
family_name = input("Enter student family name: ")
student_number = input("Enter the student number for " + given_name + " " + family_name+":")
course_code1 = input("Enter course code #1: ")
course_code2 = input("Enter course code #2: ")
course_code3 = input("Enter course code #3: ")
course_code4 = input("Enter course code #4: ")
total_grade = 0
total_grade = total_grade + float(input("Enter grade for " + course_code1 + ": "))
total_grade = total_grade + float(input("Enter grade for " + course_code2 + ": "))
total_grade = total_grade + float(input("Enter grade for " + course_code3 + ": "))
total_grade = total_grade + float(input("Enter grade for " + course_code4 + ": "))

average = total_grade/4

print(family_name + "," + given_name + "," + student_number + "," + str(average))

