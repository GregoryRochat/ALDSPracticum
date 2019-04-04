def findprimes(primerange=1000):
    """
    Function that determines all primes of numbers 2 to primerange, default being 1000. It does this using the
    sieve of Eratosthenes as a method for finding primes, foregoing the use of sqrt, // and %. It asserts that the
    parameter passed into the function is an int, throwing an AssertionError if not. The sieve is implemented as such:
    After a numberlist has been generated, starting with the lowest possible prime number, 2, up to a given range, all
    numbers are looped through. For every number, it is first checked if it is already in the nonprimelist, if so the
    number is skipped. If not all multiples of that number are then added to the nonprimelist as according to how the
    sieve works. Once all numbers have been checked, all numbers in the numberlist that are in the nonprimelist are
    removed, leaving only a list of primes.

    Parameters: primerange
    ----------
    primerange : int
        Integer representing upper search range for primes.

    Return
    ------
    primelist : list of integers
        list of all the primes found.
    """
    assert type(primerange) is int
    primelist = []
    for n in range(2, primerange + 1):
        primelist.append(n)
    nonprimelist = []
    for entry in primelist:
        multiplesofentry = entry
        if entry not in nonprimelist:
            while multiplesofentry <= primelist[-1]:
                multiplesofentry += entry
                if multiplesofentry not in nonprimelist:
                    nonprimelist.append(multiplesofentry)
    for i in range(len(primelist) - 1, -1, -1):
        if primelist[i] in nonprimelist:
            primelist.pop(i)
    return primelist


def isprime(n):
    """
    Function that check a given integer if it is a prime by performing a modulo operation on it with all numbers lower
    than it and checking if a remainder of 0 (and therefore wholly divisable by it) is found, returning False if it does
    so and True if none of the numbers below it do. It only accepts integers, throwing an AssertionError if otherwise is
    given.

    Parameters: n
    ----------
    n : int
        Integer tested if it is a prime.

    Return
    ------
    primelist : list of integers
        list of all the primes found.

    """
    assert type(n) is int
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def testfindprimes(primerange):
    """
    Function that tests the findprimes() function for its default value and the primerange value. The standard mode is
    tested with a validation set of all primes up to 1000 while an isprime() function is used to check all the primes
    generated in the second non-standard test for their validity.

    Parameters:
    ----------
    primerange : int
        Integer representing upper search range for primes passed into the findprimes() function.

    """

    primelist = findprimes()
    allprimesunderthousand = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                              83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                              179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
                              271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
                              379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
                              479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593,
                              599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                              701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
                              823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
                              941, 947, 953, 967, 971, 977, 983, 991, 997]
    try:
        assert allprimesunderthousand == primelist
        print("The correct primelist has been generated! Primelist:\n", primelist)
    except AssertionError:
        print("Not all primes have been found!")
    primelist = findprimes(primerange)
    try:
        for entry in primelist:
            assert isprime(entry)
        print("All entries in list are primes! Primelist generated:\n", primelist)
    except AssertionError:
        print("Not all entries are primes!")


testfindprimes(10001)
