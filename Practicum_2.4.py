def mybin(n):
    """
    Function that uses recursion to determine its bits/binary equivelant by dividing the number by 2 wholly until it no
    longer can be divided as such and then returning a 1 or 0 upwards, adding the previous division module 2 result to
    it in the string.

    Parameters
    ----------
    n: int
        Integer which binary representation will be returned

    Return
    ----------
    binstr: str
        String that contains the binary representation of integer "n"

    """

    assert type(n) == int
    assert n >= 0
    binstr = ""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binstr + str(mybin(n//2) + str(n % 2))


def testmybin():
    test1 = 32
    test2 = 255
    test3 = 27
    test4 = 0
    test5 = "not a number"
    test6 = -12
    tests = [test1, test2, test3, test4, test5, test6]
    for test in tests:
        try:
            result = mybin(test)
            validate = bin(test)
            try:
                assert result == validate[2:]
                print("Correct result given, function works correctly! Binary representation of ", test, " is: ",
                      result, " Validation: ", validate[2:])
            except AssertionError:
                print("Incorrect result, function not working as intended.")
        except AssertionError:
            print("Incorrect parameter given, function gave error correctly!")


testmybin()

