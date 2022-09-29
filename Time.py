class Time():

    def __init__(self,hours1,minutes1,hours2,minutes2):
        self.hours1=hours1
        self.minutes1=minutes1
        self.hours2 = hours2
        self.minutes2 = minutes2

    def addTime(self):
        self.hours=self.hours1 + self.hours2
        self.minutes=self.minutes1 +self.minutes2
        self.hours+=self.minutes//60
        self.minutes=self.minutes%60
        print((self.hours,"hrs", self.minutes,"min"))

    def displayTime(self):
        return print(self.hours,"Hours", self.minutes,"minutes")

    def DisplayTime(self):
        print("total minutes=",self.hours*60+self.minutes)

x=int(input("Enter hours of time 1:"))
y=int(input("Enter minutes of time 1:"))
z=int(input("Enter hours of time 2:"))
a=int(input("Enter minutes of time 2:"))
t=Time(x,y,z,a)
t.addTime()
t.displayTime()
t.DisplayTime()
