totalLecture=int(input("Enter totalLecture:"))
lectureAttended=int(input("Enter lectureAttended:"))
attendance=(lectureAttended/totalLecture)*100
print("the percentage of your attendace is",attendance)
if attendance>= 75:
    print("you are eligible for exam")
else:
    print("you are not eligible for exam")    