class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_numbers = []
        self.odd_numbers = []
        self._categorize_numbers()

    def _categorize_numbers(self):
        for num in self.numbers:
            if num % 2 == 0:
                self.even_numbers.append(num)
            else:
                self.odd_numbers.append(num)

    def sum_all(self):
        return sum(self.numbers)

    def sum_even(self):
        return sum(self.even_numbers)

    def sum_odd(self):
        return sum(self.odd_numbers)

    def display_info(self):
        print(f"Original numbers: {self.numbers}")
        print(f"Even numbers: {self.even_numbers}")
        print(f"Odd numbers: {self.odd_numbers}")
        print(f"Sum of all numbers: {self.sum_all()}")
        print(f"Sum of even numbers: {self.sum_even()}")
        print(f"Sum of odd numbers: {self.sum_odd()}")

my_collection = NumberCollection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Display information about the collection
my_collection.display_info()