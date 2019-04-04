import mystack as ms


def haakjesprobleem(string):
    """
    This function returns whether a string "string" follows the rules of "haakjesprobleem" correctly, using the
    "mystack" class which functions as a stack. It evaluates if for every opening bracket there is an appropriate
    closing bracket.

    Parameters
    ----------
    string: str
        A string containing parentheses

    Return
    ----------
    True
        Returned if the given string is correct
    False
        Returned if the given string is incorrect
    """
    stack = ms.mystack()
    for char in string:
        if char == '(' or char == '<' or char == '[':
            stack.push(char)
        elif char == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                return False
        elif char == '>':
            if stack.peek() == '<':
                stack.pop()
            else:
                return False
        elif char == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


def testhaakjesprobleem():
    """
    Function that tests the function "haakjesprobleem".

    """
    test1 = ["[<((<test>))>]", True]
    test2 = ["[]", True]
    test3 = ["[", False]
    test4 = ["[<((<test>)>]", False]
    test5 = ["[(<>)]", True]
    test6 = ["[(<>]]", False]
    test7 = ["<<<(test)>>>[()][]<>", True]
    tests = [test1, test2, test3, test4, test5, test6, test7]
    try:
        for test in tests:
            print(haakjesprobleem(test[0]), " - ", test[1])
            assert haakjesprobleem(test[0]) is test[1]
        print("Function working correctly!")
    except AssertionError:
        print("Function working incorrectly!")


testhaakjesprobleem()

