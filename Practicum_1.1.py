def mymax(a):
    """
    Function that determines the highest number in a list and returns that number only accepts lists
    of numbers and throws an AssertionError for incorrect paramater types, incorrect types in list and empty lists

    Parameters
    ----------
    a : list
        list of numbers

    Return
    ------
    maxnum : integer or float
        highest number of the list passed into the function
    """

    assert len(a) != 0 and type(a) == list
    maxnum = a[0]
    for element in a:
        assert type(element) is int or type(element) is float
        if element > maxnum:
            maxnum = element
    return maxnum


def mymaxtest():
    """
    Function that tests the mymax function with the builtin Python max() function as well as the correct handling
    of incorrect paramaters being passed into the function, printing all the test results.

    """
    test1 = [0, 1, 2, 3, 4, 5, 6, 99, 3, 4]
    test2 = []
    test3 = ["test", 3]
    test4 = [13]
    test5 = [88, 1, 2]
    test6 = 88

    testlists = [test1, test2, test3, test4, test5, test6]
    for test in testlists:
        print("Test result: ", end="")
        try:
            maxnum = mymax(test)
            if maxnum == max(test):
                print("Max number found: ", maxnum)
            else:
                print("Max number not found! Function working incorrectly")
        except AssertionError:
            print("Invalid paramater passed into mymax function")


mymaxtest()
