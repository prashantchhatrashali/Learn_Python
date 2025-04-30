###########################################################################################
#Object: It is a real world entity. It can be anything, a Pen, a Car, or a house.         #
#Object has two properties: Data and Method                                               #
#A car...is an object and Color, design, and models are data.                             #
#How to drive is methode.                                                                 #
###########################################################################################


class employee:
    #def putdata(self):   #methode1
    def __init__(self):   #methode2 (we can either use __init__ constructor or we can use putdata(self) method.)
        self.id=int(input("Please enter the id of employee: "))
        self.name=input("Please enter the name of Empployee: ")
        self.salary=float(input("Please enter salary of employee: "))
    def display(self): #methode2
        print("employee id: ",self.id)
        print("employee name: ",self.name)
        print("employee salary ",self.salary)
a=employee()   # We've created an object using the class. Using this class we can create n number of objects in same blueprints.
#a.putdata()    # We call this function to take input as per above example.
a.display()    # We call this function to display the above inputs that are created. Here "a" is object we can say its employee. we can use a.display to display the data about a.

'''
#Basic Example

class first:           # This is syntax of creating a class. Inside a class we create objects.
    x=50               # Define a general variable and put some value in it. It can be anything or any variable.
obj=first()            # This is syntax to create an object.
print(obj.x)           # we can print the object name. data. I.e. data was x.
'''