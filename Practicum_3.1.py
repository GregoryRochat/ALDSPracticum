def check(a, i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or  # niet in dezelfde kolom
                i + n in [a[j] + j for j in range(n)] or  # niet op dezelfde diagonaal
                i - n in [a[j] - j for j in range(n)])  # niet op dezelfde diagonaal


def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X", end=" ")
            else:
                print("*", end=" ")
        print()
    print()


def rsearch(N, solutions=[], a=[]):
    """
    Function that uses recursion to find all possible solutions for the queensproblem of board size N

    Parameters
    ---------
    N: int
        Size of chessboard
    solutions: list
        List passed by reference to which all solutions are added.
    a: list
        List that gives column position for each row.
    """

    for i in range(N):
        if check(a, i):
            a.append(i)
            if len(a) == N:
                solutions.append(a[:])
            else:
                if rsearch(N, solutions, a):
                    return
            del a[-1]
    return


def testrsearch():
    solutions = []
    rsearch(5, solutions)
    for solution in solutions:
        printQueens(solution)


testrsearch()
