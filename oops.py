class student:
    name="soumya"
    roll_number=14
s1=student()  
print(s1.name) 
#constructor and methods qestions
#ques1 create a student class that takes name and maks of three students as arguments in constructor then create method to print average
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        avg=sum/len(self.marks)
        return avg

s1=student("english",[90,80,85])
print(s1.average())
class account:
     def __init__(self,account,balance):
         self.balance=balance
         self.account=account
     def debit(self,amountdeb):
         if self.balance<amountdeb :
             print("balace is low to be debitted")
         else:
             new_amount=self.balance-amountdeb
         return new_amount
     def credit(self, amountcred):
         new_amount=self.balance+amountcred
         return new_amount
customer1=account(905747,10000)
print(customer1.debit(5000))
print(customer1.credit(10000))
#inheritence
class car:
    def __init__(self,type):
        self.type=type 
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("cat stopped")
class toyota(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

car1=toyota("prius","electric")
print(car1.type)
         


         
        
         

         
        

       