radius_req=int(input("Enter the radius of cylinder:"))
height_req=int(input("enter height of the cylinder:"))

class Cylinder():
    pi=3.14

    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def volume(self):

        return Cylinder.pi * self.radius**2 * self.height

    def TSA(self):

        return (2 * Cylinder.pi * self.radius) * (self.radius + self.height)


my_cylinder=Cylinder(radius_req,height_req)
print("Volume is",my_cylinder.volume())
print("TSA is",my_cylinder.TSA())
