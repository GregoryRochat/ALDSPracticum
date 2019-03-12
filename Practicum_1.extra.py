def nex_las_seq(numlist):
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


def testnext_las_seq():
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

testnext_las_seq()


