a=int(input("enter the year:"))
if (a%400==0)or((a%4==0)and(a%100!=0)):
    print("leapyear:",a)
else:
    print("not a leap year:",a)
