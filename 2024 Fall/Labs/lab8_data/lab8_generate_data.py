import random

def generate_data(output_filename):
    output_file = open(output_filename,"w")
    codes = ["CSC", "STA", "MAT"]
    output_file.write("student_id,application_grade,gpa,prog\n")
    for i in range(1200,1300):
        student_id = "student" + str(i)
        highschool = random.randint(85,100)
        gpa = random.uniform(2.5, 4.0)
        output_file.write(student_id+","+str(highschool)+","+str(round(gpa,2))+","+random.choice(codes)+"\n")
    for i in range(1000,1100):
        student_id = "student" + str(i)
        highschool = random.randint(70,80)
        gpa = random.uniform(2.0, 3.2)
        output_file.write(student_id+","+str(highschool)+","+str(round(gpa,2))+","+random.choice(codes[2:3])+"\n")
    for i in range(1100,1200):
        student_id = "student" + str(i)
        highschool = random.randint(80,100)
        gpa = random.uniform(2.8, 4.0)
        output_file.write(student_id+","+str(highschool)+","+str(round(gpa,2))+","+random.choice(codes[1:3])+"\n")
    for i in range(1300,1374):
        student_id = "student" + str(i)
        highschool = random.randint(75,100)
        gpa = random.uniform(2.0, 4.0)
        output_file.write(student_id+","+str(highschool)+","+str(round(gpa,2))+","+random.choice(codes)[1:3]+"\n")

    output_file.close()

#generate_data("lec08_grades.csv")
