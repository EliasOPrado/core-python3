"""
Write a function that accepts a list of numbers and returns True if the list contains an even number of even numbers.

Here are some tests that might suffice for testing our new function.

BE CAREFUL TO NOT TYPE IN WAYS THAT PYTHON DOEN'T UNDERSTAND.

"""
def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    evens = 0
    for n in numbers:
       if is_even(n):
            evens += 1
    if evens == 0:
        return False
    else:
        return is_even(evens)
#testing code
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"


print("All tests passed.")
