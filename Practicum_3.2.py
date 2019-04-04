class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current is not None:
            s = s + str(current)
            current = current.next
        while current is not None:
            s = s + " -> " + str(current)
            current = current.next
        if not s:  # s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if not self.head:  # self.head == None:
            self.head = ListNode(e, None)
            self.tail = self.head
        else:
            n = ListNode(e, None)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self, e):
        if self.head:  # self.head != None:
            if self.head.data == e:
                self.head = self.head.next
                if self.head is not None:
                    self.tail = None
            else:
                current = self.head
                while current.next is not None and current.next.data != e:
                    current = current.next
                if current.next is not None:
                    current.next = current.next.next
                if current.next is None:
                    self.tail = current


class MyCircularLinkedList:
    """
    Class that acts as a list structure using nodes.

    Attributes
    ----------
    self.tail : ListNode
        Node that always points to the first node and has data.
    Methods
    ----------
    __init__(self)
        Class constructor that initializes self.tail as None
    __repr__(self)
        Returns a string of all the data in the list within order, unless there is no data, when it returns "empty list"
    append(self, e)
        Adds a new node to the list.
    delete(self, e)
        Deletes a node from the list which data contents match "e"
    """

    def __init__(self):
        """
        Class constructor
        """
        self.tail = None

    def __repr__(self):
        """
        Function that returns the internal data as a string when class is printed.

        Return
        ----------
        s: str
            String with all the data in the nodes of the list, or as "empty list" when there is none.
        """
        s = ''
        if self.tail is not None:
            s = s + str(self.tail)
        current = self.tail.next
        while current is not self.tail:
            s = s + " -> " + str(current)
            current = current.next
        if not s:  # s == '':
            s = 'empty list'
        return s

    def append(self, e):
        """
        Function that adds a new node to the circular list, upholding the rule that the tail points to the first node.

        Parameters
        ----------
        e:
         Any data that the new node will hold.

        """
        if self.tail is None:  # self.head == None:
            self.tail = ListNode(e, None)
            self.tail.next = self.tail
        else:
            nextnode = self.tail
            while nextnode.next != self.tail:
                nextnode = nextnode.next
            nextnode.next = ListNode(e, self.tail)

    def delete(self, e):
        """
        Function that deletes a node from the circular list which contents match "e", upholding the rule that the tail
        points to the first node.

        Parameters
        ----------
        e:
         Data with which a node is associated that needs to be deleted.

        """
        if self.tail:  # self.tail != None:
            if self.tail.data == e:
                if self.tail != self.tail.next:
                    current = self.tail
                    while current != self.tail:
                        current = current.next
                    self.tail = self.tail.next
                    current.next = self.tail
                else:
                    self.tail = None
            current = self.tail
            while current.next.data != e and current.next != self.tail:
                current = current.next
            if current.next.data == e:
                current.next = current.next.next


def testlinkedlists():
    mylist = MyLinkedList()
    print(mylist)
    mylist.addLast(1)
    mylist.addLast(2)
    mylist.addLast(3)
    mylist.addLast(4)
    mylist.addLast(5)
    mylist.addLast(6)
    mylist.addLast(7)
    mylist.addLast(8)
    mylist.addLast(9)
    mylist.addLast(10)

    mylist.delete(8)
    mylist.delete(7)

    myclist = MyCircularLinkedList()
    myclist.append(1)
    myclist.append(2)
    myclist.append(3)
    myclist.append(4)
    myclist.append(5)
    myclist.append(6)
    myclist.append(7)
    myclist.append(8)
    myclist.append(9)
    myclist.append(10)

    myclist.delete(8)
    myclist.delete(7)
    print("Linkedlist: ", mylist)
    print("Circularlist", myclist)


testlinkedlists()