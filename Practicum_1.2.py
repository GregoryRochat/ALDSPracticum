def getNumbers(s):
    """
    Function that retrieves all the numbers from a string passed into it and returns those as a list.
    It throws an AssertionError for paramaters that aren't strings.

    Parameters: s
    ----------
    s : string

    Return: numberlist
    ------
    numberlist : list of integers
    None :

    If numbers are found a numberlist is returned, else None is returned.
    """
    assert type(s) == str
    numberlist = []
    number = 0
    numberactive = False
    for char in s:
        if char.isdigit():
            numberactive = True
            number = (number * 10) + int(char)
        elif numberactive:
            numberlist.append(number)
            numberactive = False
            number = 0
    if len(numberlist):
        return numberlist
    else:
        return None


def testgetNumbers():
    """
    Function that tests the getNumbers() function. It tests the passing of incorrect parameters, checking for
    AssertionErrors being thrown, as well as passing strings with and without numbers, printing all test results.

    """
    test1 = 'een123zin45 6met-632meerdere+7777getallen'
    test2 = "eenzinzonder getallen---erin"
    test3 = 89
    test4 = ['a', 'b']

    testlist = [test1, test2, test3, test4]
    for test in testlist:
        print("Test result: ", end="")
        try:
            numlist = getNumbers(test)
            if numlist is not None:
                print(numlist)
            else:
                print("No numbers found in string!")
        except AssertionError:
            print("Invalid parameter for getNumbers function!")


testgetNumbers()
