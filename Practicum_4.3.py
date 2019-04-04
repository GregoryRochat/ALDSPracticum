factorial_list = [1]
lookup = [[1]]

def factorial(n):
    """
    Function that calculates n! and stores it for further usage.

    Parameters
    ----------
    n : int
        n used in the formula

    Return
    ------
        Returns the result of n!
    """
    global factorial_list
    if n > len(factorial_list):
        factorial_list.append(factorial(n - 1) * n)
    return factorial_list[n - 1]


def assertB(n, k):
    """
    Function that calculates "n!//k!//(n-k)!"

    Parameters
    ----------
    n : int
        The value 'n', which can't be negative.
    k : int
        The value 'k', which can't be negative and can't be smaller than 'n'

    Return
    ------
    (factorial(n)//factorial(k))//factorial(n-k) : int
        An integer result of the formula.
    """
    assert 0 <= k <= n
    return (factorial(n)//factorial(k))//factorial(n-k)


def B(n, k):
    """
    Function that calculates n!//k!//(n-k)! using the rule of Pascal.

    Parameters
    ----------
    n : int
        The value 'n', which can't be negative.
    k : int
        The value 'k', which can't be negative and can't be smaller than 'n'

    Return
    ------
    lookup[n][k] : int
        The integer value of the result of the lookup.
    """
    assert 0 < k <= n
    global lookup
    for index_y in range(len(lookup), n + 1):
        lookup.append([1])
        min_value = min(index_y, k)
        for index_x in range(min_value):
            if index_x < len(lookup[index_y - 1]) - 1:
                lookup[index_y].append(lookup[index_y - 1][index_x] + lookup[index_y - 1][index_x + 1])
            else:
                lookup[index_y].append(lookup[index_y - 1][index_x])
    return lookup[n][k]


def testB():
    print(B(100, 50))
    print(assertB(100, 50))


testB()
