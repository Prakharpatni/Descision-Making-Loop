num1=int(input("Enter 1st no."))
num2=int(input("Enter 2nd no."))
num3=int(input("Enter 3rd no."))

if(num1>num2 and num1>num3):
    print("{0} is greatest.".format(num1))
elif(num2>num1 and num2>num3):
    print("{0} is greatest.".format(num2))
else:
    print("{0} is greatest.".format(num3))
