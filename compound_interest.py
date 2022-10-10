
Principle=int(input("Enter priciple amount:"))
Rate=int(input("Enter rate here:"))
Time=int(input("Enter time here:"))

Amount=Principle*(1+Rate/100)**Time
CI=Amount-Principle
print("compond interest:",CI)