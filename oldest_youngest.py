#take input of age from 3 person
#determine the oldest and youngest person
person1=int(input("Enter the age of person1:"))
person2=int(input("Enter the age of person2:"))
person3=int(input("Enter the age of person3:"))
if person1>person2 and person1>person3:
    print("person1 is oldest") 
elif person2>person1 and person2>person3:
    print("person2 is oldest")
elif person3>person1 and person3>person2:
    print("person3 is oldest")
#for youngest person
if person1<person2 and person1<person3:
    print("person1 is youngest") 
elif person2<person1 and person2<person3:
    print("person2 is yougest")
elif person3<person1 and person3<person2:
    print("person3 is yougest")
        
