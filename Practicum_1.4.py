import random


def runbirthdayproblem():
    """
    Function that simulates the birthday problem as defined here: https://en.wikipedia.org/wiki/Birthday_problem
    It creeates a hundred lists of 23 random numbers between 1 and 365, representative for birthdays, sorts each list,
    then loops through each list, checking if any entry in that list has a double by looking at the next entry and
    tallying up the number of lists that do, returning that final number.

    Return
    ------

    numofdoubles : int
    return an int amount of doubles found

    """
    listoflists = []
    numofdoubles = 0
    for i in range(0, 100):
        birthdaylist = []
        for n in range(0, 23):
            birthdaylist.append(random.randint(1, 365))
        listoflists.append(birthdaylist)
    for birthdaylist in listoflists:
        doublebdayinlist = False
        birthdaylist = sorted(birthdaylist)
        for i in range(0, len(birthdaylist)-1):
            if birthdaylist[i] == birthdaylist[i+1]:
                doublebdayinlist = True
        if doublebdayinlist:
            numofdoubles += 1
    return numofdoubles


def testrunbirthdayproblem(n=100):
    """
    Function that tests the runbirthdayproblem() function by running it n times and take the average of those runs and
    printing that result, which should be close to 50% per the birthday problem analysis

    Parameters: n=100
    ------

    n : int
    n the int amount of tests to run

    """
    allresults = 0
    for i in range(0, n):
        allresults += runbirthdayproblem()
    print("Average number of lists with doubles in a hundred lists: ", allresults / n)


testrunbirthdayproblem()

