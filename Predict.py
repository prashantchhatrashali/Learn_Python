class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):  # Inheriting from Person
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Calls the parent class's constructor
        self.grade = grade

    def study(self):
        return f"{self.name} is studying for grade {self.grade}."


# Creating objects
person1 = Person("Alice", 30)
student1 = Student("Bob", 16, "10th")

# Function calls
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(student1.greet())  # Output: Hello, my name is Bob and I am 16 years old.
print(student1.study())  # Output: Bob is studying for grade 10th.