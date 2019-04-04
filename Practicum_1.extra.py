def nex_las_seq(numlist):
    """
    Function that scans a list of numbers and returns a list of the amount of numbers and corresponding numbers in
    sequence. It does this by looping through the list looking at the current number and following number in the list,
    toggling firstnumber to determine if it is on a new number and keeping track how many of that number have been in
    that sequence in numbercount. If a sequence is broken the current number and its count are appended to a new list
    and the values reset. Parameter is asserted to be a non empty list containing integers, throwing an AssertionError
    otherwise.

    Parameters
    ------

    numlist : list of int
        Contains a sequence of numbers.

    Return
    ------

    seqlist : list of int
        Holds the tallied numbers sequenced from numlist.

    """
    assert type(numlist) is list and len(numlist) != 0
    seqlist = []
    firstnumber = True
    numbercount = 1
    size = len(numlist)
    for i in range(0, size):
        assert type(numlist[i]) == int
        if firstnumber and i != size - 1:
            if numlist[i] == numlist[i+1]:
                numbercount += 1
                firstnumber = False
            else:
                seqlist.append(numbercount)
                seqlist.append(numlist[i])
        elif firstnumber and i == size - 1:
            seqlist.append(numbercount)
            seqlist.append(numlist[i])
        elif not firstnumber and i != size -1:
            if numlist[i] == numlist[i+1]:
                numbercount += 1
            else:
                seqlist.append(numbercount)
                seqlist.append(numlist[i])
                firstnumber = True
                numbercount = 1
        else:
            seqlist.append(numbercount)
            seqlist.append(numlist[i])
    return seqlist


def testnex_las_seq():
    """
    Function that tests the nex_las_seq() function, testing different testlists with corresponding validationlists and
    checking if erronous parameters are handled correctly, printing all test results.


    """
    testlist = [[3, 3, 4, 1, 1, 6, 6, 6, 1], [1],  [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], [0, 38, 3, 3, 0]]
    validationlist = [[2, 3, 1, 4, 2, 1, 3, 6, 1, 1] , [1, 1], [2, 2, 3, 3, 4, 4, 5, 5], [1, 0, 1, 38, 2, 3, 1, 0]]
    incorrectlist = [[], ["a", "b", "c"], [1, 2, "test"], 88]
    for i in range(0, len(testlist)):
        try:
            testresult = nex_las_seq(testlist[i])
            assert testresult == validationlist[i]
            print("las_nex_seq function working correctly! Input was: ", testlist[i], " Output was: ", testresult)
        except AssertionError:
            print("next_las_sequence function working incorrectly!")
    for test in incorrectlist:
        try:
            nex_las_seq(test)
            print("next_las_sequence function working incorrectly!")
        except AssertionError:
            print("Wrong parameter input for las_nex_seq function! las_nex_seq function working correctly!")


testnex_las_seq()

