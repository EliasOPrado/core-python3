"""
Write a function that accepts a list of numbers and returns True if the list contains an even number of even numbers.

Here are some tests that might suffice for testing our new function.

BE CAREFUL TO NOT TYPE IN WAYS THAT PYTHON DOEN'T UNDERSTAND.

"""
# def even_number_of_evens():
#     numbers = []
#     for i in range(2, 18, 2):
#         if i % 2 == 0:
#             numbers.append(i)
#     return numbers

# print(even_number_of_evens())

def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0
    for n in numbers:
       if n % 2 == 0:
            evens += 1
    if evens == 0:
        return False
    else:
        return evens % 2 == 0

assert [] == False, "No numbers"
assert [2] == False, "One even number"
assert [2, 4] == True, "Two even numbers"
# assert [2, 3] == False, "Two numbers, only one even"
# assert [2, 3, 9, 10, 13, 7, 8] == False, "Multiple numbers, three are even"
# assert [2, 3, 9, 10, 13, 7, 8, 5, 12] == True, "Multiple numbers, four are even"
assert [1, 3, 9] == False, "No even numbers"

print("All tests passed")