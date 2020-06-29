answer="Y"
while answer=="Y":
    course_name=input("enter the name of the course you want to convert grades: ")
    course_grade=int(input("enter your numerical grade for the course: "))
    if 90<=course_grade<=100:
        letter_grade="A"
    elif 80 <= course_grade <= 89:
        letter_grade = "B"
    elif 70<=course_grade<=79:
        letter_grade="C"
    elif 60<=course_grade<=69:
        letter_grade="D"
    elif course_grade<60:
        letter_grade="F"
    print("course_name: "+letter_grade)

    answer=input("press Y to continue or Q to exit: ")
    if answer=="Q":
        break


