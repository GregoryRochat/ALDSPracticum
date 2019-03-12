import random

def runbirthdayproblem():
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
    allresults = 0
    for i in range(0, n):
        allresults += runbirthdayproblem()
    print("Average number of lists with doubles in a hundred lists: ", allresults / n)


testrunbirthdayproblem()

