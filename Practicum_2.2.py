class mystack(list):
    """
    A class that is an extension of the "list" class and acts as a stack.

    Attributes
    ----------
    a : list
        list from which this class will based on, default being an empty list
    pop returns last value on the stack and removes it

    Methods
    ----------
    __init__(self, a=None)
        Class constructor that takes a parameter "a" with standard value of None which equals "a = []"
    push(self, value)
        Takes a value and pushes it on top of the stack.
    pop_(self)
        Returns and removes the value on top of the stack.
    peek(self)
        Returns the value on top of the stack.
    is_empty(self)
        Checks whether the stack is empty and returns a bool accordingly

    """

    def __init__(self, a=None):
        """
        Parameters
        ----------
        a : list or None
            list with defaultvalue of None, resulting in an empty list
        """
        if a is None:
            a = []
        list.__init__(self, a)

    def push(self, value):
        """
        Function that takes a value and pushes it on top of the stack.

        Parameters
        ----------
        value :
            A value of any datatype compatible with the "list" class to be pushed unto the stack
        """
        self.append(value)

    def pop_(self):
        """
        Function that returns and removes the value on top of the stack

        Return
        ----------
        self.pop()
            value that was on top of the stack
        """
        assert self.is_empty() is False
        return self.pop()

    def peek(self):
        """
        Function that returns the value on top of the stack

        Return
        ----------
        self[-1]
            Value that is on top of the stack
        """
        if len(self) > 0:
            return self[-1]

    def is_empty(self):
        """
        Function that checks if the stack is empty, returning the resulting bool.

        Return
        ----------
        len(self) == 0 : bool
            Boolean that is True if stack is empty or False if stack is not empty.
        """
        return len(self) == 0


def testmystack():
    """
    Function that tests the mystack class.

    """
    stack = mystack()
    try:
        assert stack.is_empty() is True
        try:
            stack.pop_()
            print("Class working incorrectly!")
        except AssertionError:
            pass
        stack.push(5)
        stack.push(9)
        assert stack.peek() == 9
        assert stack.pop_() == 9
        assert stack.peek() == 5
        assert stack.is_empty() is False
        assert stack.pop_() == 5
        assert stack.peek() is None
        assert stack.is_empty() is True
        print("Class working correctly!")
    except AssertionError:
        print("Class working incorrectly!")


testmystack()
