###########################################################################################
#OOPs with Inheritance.                                                                   #
###########################################################################################

class Student:
    def __init__(self, my_rollnum, my_name, my_marks):
        self.rollnum = my_rollnum
        self.name = my_name
        self.marks = my_marks

    def avg(self):
        return sum(self.marks ) /len(self.marks)

    def get_sum(self):  # Renamed from 'sum' to avoid shadowing built-in
        return sum(self.marks)

class Intern(Student):
    def __init__(self, my_rollnum, my_name, my_marks, rank):
        super().__init__(my_rollnum, my_name, my_marks)
        self.rank = rank

    def update_rank(self, new_rank):  # Renamed for clarity
        self.rank = new_rank
        print("Rank is updated")

first_student = Student(1, "prashant", [10, 14, 15])
rank_student = Intern(1, "prashant", [10, 14, 15], 1)

print(first_student.name)
print(first_student.get_sum())
print(first_student.avg())

# This is the corrected method call
rank_student.update_rank(2)
print(f"Updated rank: {rank_student.rank}")

