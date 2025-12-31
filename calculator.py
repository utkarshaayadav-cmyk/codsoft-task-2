#Simple Calculator Program

num1=float(input("Enetr first number:"))
num2=float(input("Enetr second number:"))

print("\nSelect operation:")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

Choice = input("Enetr Choice(1/2/3/4):") 

if Choice == "1":
    print("Result:", num1+num2)
elif Choice =="2":
    print("Result:", num1-num2)
elif Choice =="3":
     print("Result:", num1*num2)
elif Choice =="4":
     if num2 !=0:
         print("Result:",num1/num2)
     else:
         print("Error:Division By Zero Is Not Allowed ")
else:
    print("invalid choice")
    