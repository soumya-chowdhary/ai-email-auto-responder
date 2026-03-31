#create a list of 3 fav movie of usre bt=y taking input
"""list=[]
list.append(input("enter first fav movie"))
list.append(input("enter 2nd fav movie"))
list.append(input("enter 3rd fav movie"))
print(list)# check if a list id pelindromic or not
list=[]
list.append(input("enter first element"))
list.append(input("enter second element"))
list.append(input("enter third"))
list.append(input("enter 4th"))
list.append(input("enter 5th"))
another=list.copy()
another.reverse()
if(list==another):
    print("list is pelindromic")
else:
    print("list is non pelindromic")
#dictionary
dict={"table":["furniture used for sitting purpose","list of facts and figures"],"cat":"a small animal"}
print(dict)"""
#you are given a list of subjectts for students. assume one classroom is required for one subject. how many classrooms are needed by all the students 
set1={'python','java','c++','javascript','java','python','java','c++','c'}
length=len(set1)
print(length)
#write a program to enter marks of 3 subjects from the user and store them in a dictionary. satrt with an empty dictionary And one by  one .use subject name as key and marks as value.
marks={}
x= int(input("enter the marks of physics:"))
marks.update({"physics": x})
y= int(input("enter the marks of chem:"))
marks.update({"chem": y})
z= int(input("enter the marks of maths:"))
marks.update({"maths": z})
print(marks)
#ways to store 9 and 9.0 in a set as two different values
#way1
set1={9,"9.0"}
print(set1)
#way2
set2={("float",9.0),
      ("int",9)}
print(set2)
