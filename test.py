from main import add
from main import multiply


def test_add():
    num1 = 3
    num2 = 2
    results = num1 + num2
    assert results == 5
    print("Add was okay")

def test_multiply():
    num1 = 2
    num2 = 3
    results = num1 * num2
    assert results == 6
    print("Multiply was okay")
    
test_add()
test_multiply()
