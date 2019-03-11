def mymax(a):
    assert len(a) != 0
    maxnum = a[0]
    for element in a:
        assert type(element) is int or type(element) is float
        if element > maxnum:
            maxnum = element
    return maxnum


def mymaxtest():
    lst1 = [0, 1 , 2, 3, 4, 5, 6, 99, 3, 4]
    lst2 = []
    lst3 = ["ohai", 3]
    lst4 = [13]
    lst5 = [88, 1, 2]
    testlists = [lst1, lst2, lst3, lst4, lst5]
    for test in testlists:
        try:
            print(mymax(test))
        except AssertionError:
            print("Invalid entry for mymax function")


mymaxtest()
