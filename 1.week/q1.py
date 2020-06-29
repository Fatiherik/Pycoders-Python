name=input("name and surname: ")
mid=int(input("midterm exam score (0-100): "))
final=int(input("final exam score (0-100): "))
attendance=int(input("number of class you attend (0-20): "))
course_grade=mid*0.3+final*0.5+attendance*5*0.2
print(name)
print("midterm exam grade: "+str(mid))
print("final exam grade: "+str(final))
print("number of class you attend: "+str(attendance))
print("course grade: "+ str(course_grade))


