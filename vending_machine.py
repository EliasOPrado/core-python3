from byotest import *

def get_change(amount):
    if amount == 0:
        return []
    if amount in [100, 50, 20, 10, 5, 2, 1]:
          return [amount]
          
    change = []
    for coin in [100, 50, 20, 10, 5, 2, 1]:
        if coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change
            
#Tests from the byotest.py for all coins denominations

test_are_equal(get_change(0),[])#0 and 0
test_are_equal(get_change(1),[1])#1 and 1
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(7),[5,2])
print("ALL TEST PASSED!")