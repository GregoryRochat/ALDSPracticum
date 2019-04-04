def machtmethod3(a, n):
    """
    Function that raises number "a" to a given power "n" and returns that number "m", asserting that n is bigger than 0.
    The method used is an O(log(n)) algorithm that through repeated quadrations in a loop reduces the amount of
    calculations necesarry by halving the power "n" when divisible by 2 and quadrating "a", reducing n by 1 if otherwise
    and multiplying "m" by a. As a test for every iteration a count is kept to determine the amount of multiplications
    necessary to calculate m and proof it is indeed O(log(n))

    Parameters
    ----------
    a : int
        int that will be raised to a certain power
    n : int
        represents the power "a" will be raised to

    Return
    ----------
    m : int
        the result of "a" to the power of "n"

    """
    assert n > 0
    m = 1
    count = 0
    while n > 0:
        count += 1
        if n % 2 == 0:
            a *= a
            n = n // 2
        else:
            n -= 1
            m *= a
    print("Multiplications required: ", count, end="")
    return m


def testmachtmethod3():
    """
    Function that raises number "a" to a given power "n" and returns that number "m", asserting that n is bigger than 0.
    The method used is an O(log(n)) algorithm that through repeated quadrations in a loop reduces the amount of
    calculations necesarry by halving the power "n" when divisible by 2 and quadrating "a", reducing n by 1 if otherwise
    and multiplying "m" by a. As a test for every iteration a count is kept to determine the amount of multiplications
    necessary to calculate m and proof it is indeed O(log(n))
    """

    test1 = [2, 10]
    test2 = [2, 1000]
    test3 = [2, 0]
    test4 = [0, 2]
    tests = [test1, test2, test3, test4]
    for test in tests:
        try:
            result = machtmethod3(test[0], test[1])
            try:
                assert result == test[0] ** test[1]
                print(" - Test results are positive, function works correctly!\nResults for ", test[0],
                      "raised to the power of ", test[1], " is: ", result, "\n")
            except AssertionError:
                print("Incorrect results, machtmethod3 function works incorrectly")
        except AssertionError:
            print("\nInvalid parameters given for machmethod3, function handled invalid inputs correctly.\n")


testmachtmethod3()
