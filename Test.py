
def reverse_string(input_string):
    """
    Function to reverse a string using different methods
    """
    # Method 1: Using string slicing
    reversed_string_1 = input_string[::-1]

    # Method 2: Using reversed() function and join
    reversed_string_2 = ''.join(reversed(input_string))

    # Method 3: Using a loop (traditional way)
    reversed_string_3 = ""
    for char in input_string:
        reversed_string_3 = char + reversed_string_3

    return {
        "using_slicing": reversed_string_1,
        "using_reversed": reversed_string_2,
        "using_loop": reversed_string_3
    }


# Test the function
if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    result = reverse_string(user_input)

    print("\nReversed string results:")
    print(f"Method 1 (Slicing): {result['using_slicing']}")
    print(f"Method 2 (reversed): {result['using_reversed']}")
    print(f"Method 3 (Loop): {result['using_loop']}")

    # Verify all methods give the same result
    if result['using_slicing'] == result['using_reversed'] == result['using_loop']:
        print("\nAll methods produced the same result!")


'''
words = ["Python", "is", "awesome"]
sentence = ":".join(words)  # Joins words with a space as the delimiter
print(sentence)  # Output: Python is awesome

numbers = [1, 2, 3]  # Integer list
result = ",".join(map(str, numbers))  # Convert each integer to a string
print(result)  # Output: 1,2,3
'''