import sys
sys.setrecursionlimit(10000)
a = [[1]]
m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]


def F(n):
    """
    Function that generates a table with all possiblities for paying "n".

    Parameters
    ----------
    n : int
        Value for which possible ways of payout are calculated.

    Return
    ------
        Returns the possible ways of paying 'n'.
    """
    global m
    global a

    i = 0
    while len(m) > i+1 and m[i+1] < n:
        i += 1
    if len(a) <= i:
        for _ in range(len(a) - 1, i + 1):
            a.append([1])
    if len(a[0]) <= n:
        for _ in range(len(a[0]) - 1, n + 1):
            a[0].append(1)

    def _F(i=None, j=None):
        if len(a[i]) < j:
            for _ in range(len(a[i]), j + 1):
                a[i].append(None)

        if a[i][j] is None:
            if j >= m[i]:
                a[i][j] = _F(i - 1, j) + _F(i, j - m[i])
            elif j < m[i]:
                a[i][j] = _F(i - 1, j)
        return a[i][j]

    return _F(i, n)


def testF():
    print(F(7))
    print(F(1))
    print(F(10000))


testF()

