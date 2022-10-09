firstSide=int(input("Enter first side:"))
secondSide=int(input("Enter second side:"))
thirdSide=int(input("Enter third side:"))
s=(firstSide+secondSide+thirdSide)/2
area=(s*(s-firstSide)*(s-secondSide)*(s-thirdSide))**0.5
print("the area of triangle is" , area)
