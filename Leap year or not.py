year=int(input("Enter the year"))
if(year%4==0 or year%400==0 and year%100!=0):
    print("Leap year")
else:
    print("not a LEap year")
