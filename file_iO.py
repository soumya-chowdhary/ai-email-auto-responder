#reading data of a file
"""f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
line1=f.read()
print(line1)
f.close()
#writing data from a txt file
f=open("demo.txt","w")#it will overwrite the data
f.write("hello my name is soumya \n i am living in punjab India")
#reading and writing simultaneously
f=open("demo.txt","r+")
f.write("good morning my name is")# it will overwrite the text in initial of the prevoisly written text
data=f.read()#it will start reding fromwhere the last text has ended
print(data)
#withsyntax
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
#remove 
import os
os.remove("demo.txt")
#question1
with open("practise.txt","w") as f:
    f.write("hi everyone\nwe are learning file i/o \n using Java \n i like programming in Java")
with open("practise.txt","r")as f:
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)
with open("practise.txt","w") as f:
    f.write(new_data)"""
#question2 
with open("practise.txt","r") as f:
    data=f.read()
search=input("write the string needs to be searched:")
if search in data:
    print("yes")
else:
    print('no')
def check_for_line():
    word=input("enter the word:")
    with open("practise.txt","r")as f:
        line_no=1
        while data:
            data=f.readline()
            if (word in data):
                print("yes the word is present in",line_no)
                line_no+=1
            else:
                print("word doesn't exist in the file")
check_for_line()





 