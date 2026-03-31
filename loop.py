#while loop
#ques1:print numbers from 1 to 100
"""i=1
while i<=100:
    print(i)
    print("\n")
    i+=1
#ques2:print number from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
#print the multiplication table of  a number n
number=int(input("enter the number:"))
i=1
while i<=10:
    print(number,"x",i,"=",number*i)
    i+=1
#print the following elements of list using loop
#[1,4,9,16,25,36,49,64,81,100]
list1=[]
i=1
while i<=10:
    square=i*i
    list1.append(square)
    i+=1
print(list1)
#search for number x group in this tupple using loop
number=int(input("enter the number to be searched:"))
if number in list1:
    print("yes it exist in the list")
#search for a number in a tupple
tup=tuple(list1)
number=int(input("enter the numebr:"))
if number in tup:
    print("yes number exist in tuple")
else:
    print("it doesn'texist in tuple")
#FOR LOOP
#print the lements of the following list using for loop
my_list=[1,4,9,16,25,36,49,64,81,100]
for i in my_list:
    print(i)
#search for a number x in this tuple using loop
tup=tuple(my_list)
number=int(input())
idx=0
for i in my_list:
    if(i==number):
        print("element found ",idx)
        break
    idx=idx+1
#RANGE()
#print all numbers from 1 to 100
for i in range(1,101):
    print(i) 
#print all numbers bw 100 and 1
for i in range(1,100,-1):
    print(i)
#wap to find the sum of n numbers(using while loop)
number=int(input("enter the number:"))
sum=0
for i in range(1,number+1):
    sum+=i
print(sum)"""
#wap to find the factorial of n number
fact=1
num=int(input("enter the number:"))
for i in range(1,num+1):
    fact=fact*i
print(fact)