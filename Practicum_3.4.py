class TrieNode:
    """
    Class that functions as a node for a Trie tree.

    Attributes
    ---------
    letter: char
        Letter on the Trie tree.
    lst_next_letters: list
        List containing all the letters that fall under this node.
    n: int
        Count of occurence of this node in the Trie.


    Methods
    ---------
    __init__(self, char)
        Constructor for the node.
    increase_count(self)
        Function that increases "n" by one.
    add_trie_node(self, next_node)
        Adds a new node to this node.
    get_next_letter_node(self, char)
        Returns the node with the same letter as char, if available.

    """
    def __init__(self, char):
        self.letter = char
        self.lst_next_letters = []
        self.n = 0

    def increase_count(self):
        """
        Function that increases count "n" by 1

        """
        self.n += 1

    def add_trie_node(self, next_node):
        """
        Function that adds a node to current node

        Parameters
        ---------
        next_node: TrieNode
            Adds node to the available next nodes
        """
        if next_node.letter not in self.lst_next_letters:
            self.lst_next_letters.append(next_node)

    def get_next_letter_node(self, char):
        """
        Function that returns the next node with the same letter as char, if available.

        Parameters
        ---------
        char: char
            Char containing letter for retrieval.

        Return
        ---------
        node: TrieNode
            If available, returns next node with the same letter as a char, else returns None.
        """
        for node in self.lst_next_letters:
            if node.letter is char:
                return node
        return None

class Trie:
    """
    Class that functions as a "Trie" tree.

    Attributes
    ---------
    root: TrieNode
        Root of the tree.
    current: TrieNode
        Node currently accessed.


    Methods
    ---------
    __init__(self)
        Constructor for the tree.
    count_words(self, filename)
        Function counts all the words in a file and logs them unto the tree.
    write_words(self, file, s="", node=None)
        Function that writes all the words and their frequencies in the tree to an output file.

    """
    def __init__(self):
        self.root = TrieNode("")
        self.current = self.root

    def count_words(self, filename):
        """
        Function that counts all words in the text file and logs them unto the tree.

        Parameters
        ---------
        filename: string
            Filename used to open the file.

        """
        char = " "
        with open(filename, "r") as file:
            for line in file:
                for char in line:
                    if char is " ":
                        if self.current is not self.root:
                            self.current.increase_count()
                        self.current = self.root

                    elif char.isalpha():
                        next_node = self.current.get_next_letter_node(char)
                        if next_node is None:
                            next_node = TrieNode(char)
                            self.current.add_trie_node(next_node)
                        self.current = next_node

                if char is not " ":
                    self.current.increase_count()

    def write_words(self, file, s="", node=None):
        """
        Function that writes all words in the tree and their frequency to an output file.

        Parameters
        ---------
        file: file
            Outputfile for the function to write in.
        s: basestring
            Basestring to which chars are added for output.
        node: TrieNode, None
            Node from which words is being written.
        """
        if node is None:
            file.write("{0:<15} {1} \n\n".format("Key", "Frequency"))
            node = self.root
        s = s + node.letter
        if node.n > 0:
            file.write("{0:<15} {1} \n".format(s, node.n))
        for next_node in node.lst_next_letters:
            self.write_words(file, s, next_node)


def count_word_frequency(dct, filename):
    """
    Function that counts how often words occurs in a file and logs those findings in a dictionary.

    Parameters
    ---------
    dct: dictionary
        Dictionary logging the words and their frequency

    filename: string
        name of the input file
    """
    with open(filename, "r") as newfile:
        for line in newfile:
            for word in line.split():
                newword = ""
                for letter in word:
                    if letter.isalpha():
                        newword += letter
                if newword not in dct.keys():
                    dct[newword] = 1
                else:
                    dct[newword] += 1


def cmpfiles():
    file = open("output.txt", "r")
    file2 = open("output2.txt", "r")
    list1 = file.readlines()
    list2 = file2.readlines()
    cmplist1 = []
    cmplist2 = []
    for n in list1:
        x = n.strip("\n")
        x = x.split(" ")
        templst = []
        for i in x:
            if i != '':
                templst.append(i)
        if len(templst) != 0:
            cmplist1.append(templst)
    cmplist1.pop(0)
    for n in list2:
        x = n.strip("\n")
        x = x.split(" ")
        templst = []
        for i in x:
            if i != '':
                templst.append(i)
        if len(templst) != 0:
            cmplist2.append(templst)
    cmplist2.pop(0)
    cmplist1 = sorted(cmplist1)
    cmplist2 = sorted(cmplist2)
    return cmplist1 == cmplist2


def testtrie():
    dct = {}
    count_word_frequency(dct, "Ghibberish.txt")
    trie = Trie()
    trie.count_words("Ghibberish.txt")

    file = open("output.txt", "w")
    file2 = open("output2.txt", "w")
    file.write("{0:<15} {1} \n\n".format("Key", "Frequency"))
    for k, v in list(dct.items()):
        file.write("{0:<15} {1} \n".format(k, v))
    trie.write_words(file2)
    file.close()
    file2.close()
    if cmpfiles():
        print("Both output files correspond!")
    else:
        print("Error, files do not correspond.")


testtrie()
