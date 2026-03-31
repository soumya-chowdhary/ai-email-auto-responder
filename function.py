#average of three numbers
"""
def average(num1,num2,num3):
    sum=num1+num2+num3
    avg=sum/3
    return avg
output=average(2,4,6)
print(output)
#default parameter
def cal_prod(a=1,b=1):
    print(a*b)
    return a*b
output=cal_prod(2,4)
print(output)
#wap to print the length of the list 
def length_list(list):
    length=len(list)
    print(length)
list1=[10,20,30,45,88]
length_list(list1)
#waf to print the element of list inn a single line
def singleline_list(list):
   for i in list:
       print(i,end=" ")
list1=[20,30,25,88,90,22]
singleline_list(list1)
#write a function to  print factorial of n(n is parameter)
def factorial(number):
    i=1
    fact=1
    while i<=number:
        fact=fact*i
        i+=1
    print(fact)
number=int(input("enter the number:"))
factorial(number)
#convert USD$ to INR 
def usd_inr(usd):
    rupee=usd+91.8
    print(rupee)
usd=float(input("enter the amount to be converted:"))
usd_inr(usd)"""
#print a series of  number in reverse order
def show(n):
    if(n==0):
        return 1
    else: 
        print(n,end=" ")
        show(n-1)
show(10)
#print factorial of a number using recursion
def fact(number):
    if(number==0):
        return 1
    else:
        return number*fact(number-1)
print("\n")
print(fact(5))

#write a recursive function to calculate the sum of first n natural numbers
def sum(num):
    if(num==0):
        return 1
    else:
        return num+sum(num-1)
print(sum(5))
#write a recursive call to print all the elements in a list
def print_el(list,index ):
    if(index==len(list)):
        return
    else:
        print(list[index],end=" ")
        print_el(list,index+1)
list=[10,20,67,88,99,100,56]
idx=0
print_el(list,idx)