def listDivide(numbers, divide=2):
    y = []
    for i in numbers:
        if i % divide is 0:
            y.append(i)
    x = len(y)
    print(x)

class ListDivideException(Exception):
    pass

def testListDivide():
    listDivide([1,2,3,4,5])
    listDivide([2,4,6,8,10])
    listDivide([30,54,63,98,100], divide=10)
    listDivide([])
    listDivide([1,2,3,4,5], 1)
    
testListDivide()
