import random


class SeparateChainingHashing:
    """
    Class that performs seperate chaining hashing.

    Attributes
    ---------
    len: int


    Methods
    ---------
    search(self, e)
        Function that searches for element "e" in list and returns its index.
    insert(self, e)
        Inserts element "e" into hashtable, rehashing if fill threshold has been reached.
    delete(self, e)
        Deletes element "e" from list if possible.
    rehash(self, newlen)
        Rehashes the table and increases its size.
    """

    def __init__(self):
        self.len = 8
        self.hash_table = [set()] * self.len
        self.current_items = 0

    def search(self, e):
        """
        Function that searches for element "e" and returns the index of the list where the set is located.

        Parameters
        ---------
        e: int
            Searches the hash 'e' in the hash_table

        Return
        ---------
        : False
            Returns the index of where the set is located, or False if element 'e' is not in the list.
        """
        for item in self.hash_table[e % self.len]:
            if item is e:
                return e % self.len
        return False

    def insert(self, e):
        """
        Function that inserts element "e" into the hashtable, rehashing the table if the more than 75% has been filled
        doubling the table.

        Parameters
        ---------
        e: int
            Element to be inserted into the hash table
        """
        self.current_items = self.current_items + 1
        if self.current_items > self.len - ((self.len // 4) + 1):
            self.rehash(self.len * 2)
        self.hash_table[e % self.len].add(e)

    def delete(self, e):
        """
        Deletes element "e" from the hash table.

        Parameters
        ------
        e : int
            Element to be deleted from the hash table.

        Return
        ------
        : bool
            Returns True if an element has been deleted and False if not.
        """
        if self.search(e):
            self.hash_table[e % self.len].remove(e)
            self.current_items -= 1
            return True
        return False

    def rehash(self, newlen):
        """
        Function that rehashes the whole hash table and prints the new hash table.

        Parameters
        ----------
        newlen : int
            New size of the hash table
        """
        old_hash_table = self.hash_table[:]
        self.len = newlen
        self.hash_table = [set() for _ in range(self.len)]
        for chain in old_hash_table:
            for hash_number in chain:
                self.hash_table[hash_number % self.len].add(hash_number)
        print(self.hash_table)


def testsepchahash():
    hashlist = []
    hashtable = SeparateChainingHashing()
    for i in range(200):
        hashlist.append(hash(random.uniform(0,1)))
        hashtable.insert(hashlist[i])
    for i in range(100):
        hashtable.delete(hashlist[i])


testsepchahash()

