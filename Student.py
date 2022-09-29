n=int(input("Enter number of entries:"))

class Student():
    marklist=[]
    def initialize(self,name,marks,roll_no):
        self.name=name
        self.marks=marks
        self.roll_no=roll_no
        self.marklist.append(self.marks)

    def Display(self):
        print(self.name,"scored",self.marks,"and has roll number",self.roll_no)

    def calculateAverage(self):
        avg=0
        if n>=5:
            avg=sum(self.marklist)/n
            print("The average is:",avg)
        else:
            print("atleast 5 entries required for calculating average.")

s=Student()

for i in range (n):
    name=input("Enter name:")
    mark=int(input("Enter marks:"))
    rollno=int(input("Enter roll number:"))
    s.initialize(name,mark,rollno)
    s.Display()

s.calculateAverage()
