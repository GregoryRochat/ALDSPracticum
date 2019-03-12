def getNumbers(s):
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
