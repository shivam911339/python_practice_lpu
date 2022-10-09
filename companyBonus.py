#company will give bonus based on following criteria 
#time spent in company               Bonus
#>10 years                            10%
#>6 and <10                            8%
#less than 6                           5%
#ask salary and time spent from the user
#print net bonus amount accordingly
timeSpent=int(input("Enter your timeSpent:"))
salary=int(input("Enter your salary:"))
if timeSpent>10 :
    print("your net bonus is",salary*0.1)
elif timeSpent>6 and timeSpent<10:
    print("your net bonus is",salary*0.08)
elif timeSpent<6:
    print("your net bonus is",salary*0.05)    
