"""name=input("enter your name:")
length=len(name)
print(length)
#program to find the occurence of the a character
str="hello i am soumya.I am studying in btech 2nd year"
print(str.count(input("enter the character:")))
#conditionnal statements
marks=int(input("ENTER THE MARKS OBTAINED:"))
if(marks>=90):
    print('GRADE:A')
elif(marks>=80 and marks<90):
    print("GRADE:B")
elif(marks>=70 and marks<80):
    print("GRADE:C")
else:
    print("GRADE:D")
#nesting 
age=int(input("enter the age :"))
if(age>=18):
    if(age>=75):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("candidate is minor")
#even or odd
number=int(input("enter the number:"))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")"""
#greatest of three numbers entered by the user
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if(num1>num2 and num1>num3):
    print("num1 is greatest")
elif(num2 >num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")
#multiple of 7
number=int(input("enter the number:"))
if(number%7==0):
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")
