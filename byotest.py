def number_or_even(numbers):
    return 0
#test fucntions
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(actual, expected):
    assert expected != actual, "Not expected {1}, got {0}".format(expected, actual)
    
test_are_equal(number_or_even([2,4]),2)