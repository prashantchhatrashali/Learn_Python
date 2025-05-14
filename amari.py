
#Polymorphism
# When we use same function with inheritance but when execute program, the function display output from Child class.
# This is concept of Overriding.

class ws:
    def displayinfo(self,name):
        self.name=name
        print("Welcome to python"+name)

class pra(ws):             # Concept of Inheritance since inheriting Parent ws class inside pra class
    def displayinfo(self):
        super().displayinfo(" Prasahnt")
        print("Hello Prashant")

a=pra()
a.displayinfo()
