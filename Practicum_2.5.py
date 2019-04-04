import random
import sys
sys.setrecursionlimit(10000)
x = 0


def swap(a, i, j):
    """
    Function that swaps two elements in list "a" given index "i" and index "j".

    Parameters
    ----------
    a: list
        List of elements
    i: int
        Index for element to be swapped
    j: int
        Index for element to be swapped
    """

    a[i], a[j] = a[j], a[i]


def findindexsmallest(a, low, high):
    """
    Function that returns the index of the smallest element in a list from index "low" to index "high"

    Parameters
    ----------
    a: list
        List of elements
    low: int
        Index to start search from.
    high: int
        Index to end search on.

    Return
    ----------
    index: int
        The index of the smallest element in the list
    """

    index = low
    for i in range(low+1, high):
        if a[i] < a[index]:
            index = i
    return index


def qsort(a, low=0, high=-1):
    """
    Adjusted qsort function using the worst possible pivot, the smallest element of the list to determine the number of
    comparisons needed, which given the worst possible circumstances should approach O(n^2)

    Parameters
    ----------
    a: list
        List of elements
    low: int
        Lowest element to start comparing from
    high: int
        Highest element to compare to.
    x: global int
        Counter for the amount of comparisons made.

    """
    global x

    if high == -1:
        high = len(a) - 1
    if low < high:
        pivot = findindexsmallest(a, low, high)
        swap(a, low, pivot)
        m = low
        for j in range(low + 1, high + 1):
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
            x += 1
        swap(a, low, m)
        if m > 0:
            qsort(a, low, m-1)
        qsort(a, m + 1, high)


def testqsort(n):
    """
    Function that tests the adjusted qsort function.

    Parameters
    ----------
    n: int
        List size to test on.
    """
    print(n)
    test1 = []
    for n in range(0, n):
        test1.append(random.randint(1, 10000))
    test2 = list(range(n, 0, -1))
    validation1 = sorted(test1)
    validation2 = sorted(test2)
    tests = [[test1, validation1], [test2, validation2]]
    for test in tests:
        try:
            qsort(test[0])
            assert test[0] == test[1]
            print("Qsort working correctly")
            print("Using worst possible pivot, qsort made ", x, " comparisons of elements with a list size of ", n+1)
        except AssertionError:
            print("Qsort isnt working correctly")


testqsort(5000)

