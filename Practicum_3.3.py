class Queue:
    """
    Class that functions as a queue, working with a first in first out principle.

    Attributes
    ---------
    queue: list
        List that will be used as a queue.

    Methods
    ---------
    add(self, e)
        Adds a new element to the queue.
    remove(self)
        Remove and returns first item in the queue.
    peek(self)
        Returns first item in the queue.
    isempty(self)
        Returns whether the queue is empty or not.

    """
    def __init__(self):
        self.queue = []

    def add(self, e):
        """
        Add element to queue

        Parameters
        ---------
        e:
            Element to be added to the queue.
        """
        self.queue.append(e)

    def remove(self):
        """
        Function that removes first element from the queue and returns it

        Return
        ---------
        firstelement:
            Data that the first element in the queue held.
        """
        firstelement = self.queue[0]
        del self.queue[0]
        return firstelement

    def peek(self):
        """
        Function that returns first element in the queue

        Return
        ---------
        self.queue[0]
            Data that the first element in the queue holds.
        """
        return self.queue[0]

    def isempty(self):
        """
        Function that evaluates whether the queue is empty or not.

        Return
        ---------
        : bool
            True if queue is empty or false if not.
        """
        return len(self.queue) == 0


class BSTNode:
    """
    Class that functions as a node for a binary search trees.

    Attributes
    ---------
    element:
        Data of the node
    left: BSTNode, None
        Node to the left of this node in the tree, None if if there is none.
    right: BSTNode, None
        Node to the right of this node in the tree, None if if there is none.

    Methods
    ---------
    __init__(self, element, left, right)
        Constructor for the node.
    __repr__(self, nspaces=0)
        Special function for printing the node.
    insert(self, e)
        Inserts a new node to the left or the right of it.
    rinsert(self, e, parent=None, current=None)
        Recursively inserts a new node to the left or the right of it.
    insertarray(self,a, low=0, high=-1)
        Recursively inserts nodes with values in the array in the tree.
    search(self, e)
        Search for element in the nodes in the tree.
    rsearch(self, e)
        Recursively searches for element in the nodes in the tree.
    max()
        Recursively searches for max value in tree.

    """
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self, nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right is not None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + '\n'
        if self.left is not None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def insert(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)
        return not found

    def rinsert(self, e, parent=None, current=None):
        """
        Function that inserts an element into the tree, recursively.

        Parameters
        ---------
        e:
            Element to be inserted.
        parent:
            Represents parent node, or None if there is none.
        current: BSTNode
            Current node being evaluated for insertion

        Return
        ---------
        : bool
            Returns False if element already exists or True if it doesn't and has been inserted.

        """
        if parent is None:
            parent = self
            current = parent
        if current:
            if current.element < e:
                return current.rinsert(e, current, current.right)
            elif current.element > e:
                return current.rinsert(e, current, current.left)
            else:
                return False
        else:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)

            return True

    def insertarray(self, a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
        mid = (low+high+1)//2
        self.rinsert(a[mid])
        if mid > low:
            self.insertarray(a, low, mid-1)
        if high > mid:
            self.insertarray(a, mid + 1, high)

    def search(self, e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def rsearch(self, e):
        """
        Function that searches for an element and returns that node.

        Parameters
        ---------
        e:
            Element to be inserted.

        Return
        ---------
        : bool
            Returns False if element already exists or True if it doesn't and has been inserted.

        """
        current = self
        if current.element < e and current.right is not None:
            return current.right.rsearch(e)
        elif current.element > e and current.left is not None:
            return current.left.rsearch(e)
        elif current.element == e:
            return current
        else:
            return None

    def max(self):
        """
        Recursive function that returns the max value of the tree.

        Return
        ---------
        self.element, self.right.max()
            Highest value in the tree.

        """
        if self.right:
            return self.right.max()
        else:
            return self.element


class BST:
    """
    Class that functions as a node for a binary search trees.

    Attributes
    ---------
    root
        Root element of the tree.

    Methods
    ---------
    __init__(self, a=None)
        Constructor for the tree.
    __repr__(self)
        Special function for printing the contents of the tree.
    search(self, e)
        Search for element in the nodes in the tree.
    insert(self, e)
        Inserts a new node in the tree, currently using rinsert of the root node.
    max()
        Recursively searches for max value in tree.
    rsearch(self, e)
        Recursively searches for element in the nodes in the tree.
    showLevelOrder()
        Prints the elements in the tree in order

    """
    def __init__(self, a=None):
        if a:
            mid = len(a)//2
            self.root = BSTNode(a[mid], None, None)
            self.root.insertarray(a[:mid])
            self.root.insertarray(a[mid+1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def search(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def insert(self, e):
        if e:
            if self.root:
                return self.root.rinsert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False

    def max(self):
        if self.root:
            return self.root.max()

    def rsearch(self, e, startpoint=None):
        if self.root and e:
            return self.root.rsearch(e)
        else:
            return None

    def showLevelOrder(self):
        """
        Function that prints the elements in the tree in order.

        """
        queue = Queue()
        queue.add(self.root)
        print("showLevelOrder ->", end="\t")
        print(self.root.element, end="\t")
        while not queue.isempty():
            current_node = queue.remove()
            if current_node.right is not None:
                queue.add(current_node.right)
                print(current_node.right.element, end="\t")
            if current_node.left is not None:
                queue.add(current_node.left)
                print(current_node.left.element, end="\t")
        print()


def testbst():
    print("################### Testing bst initialization and printing with arrays ###################\n")
    bst = BST([1, 2, 3, 4, 5, 6])
    print("Binary search tree 1:")
    print(bst)
    print("-------------------------------------------------------------------")
    bst = BST([1, 2, 3, 4, 9])
    print("Binary search tree 2:")
    print(bst)
    print("-------------------------------------------------------------------")

    print("\n################### Testing rsearch function and max function ###################\n")
    bst = BST([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    print("New search tree:")
    print(bst)
    searchlist = [3, 4, 8, 11, 16]
    print("Searched for", searchlist, "and found: ")
    for entry in searchlist:
        result = bst.rsearch(entry)
        if result is not None:
            print(result.element)
        else:
            print("Entry not found!")
    print("\nMax value in tree: ", bst.max(), " should be: 12")
    print(bst.max())
    print("-------------------------------------------------------------------")
    print("Updating search tree with entry 17: \n")
    bst.insert(17)
    print(bst)
    print("\nMax value in tree: ", bst.max(), " should be: 17")
    print("-------------------------------------------------------------------")

    print("\n################### Testing non array initialization and insertions ###################\n")
    bst = BST()
    for i in range(1, 6):
        bst.insert(i)
    bst.insert(-1)

    print(bst)
    print("-------------------------------------------------------------------")

    print("\n################### Testing empty search tree initialization###################\n")
    bst = BST(None)
    print(bst)
    print("-------------------------------------------------------------------")
    bst = BST([])
    print(bst)
    print("-------------------------------------------------------------------")


testbst()
