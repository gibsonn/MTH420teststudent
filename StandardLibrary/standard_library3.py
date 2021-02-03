# standard_library.py
"""Python Essentials: The Standard Library.
<Tik Ho Wong>
<MTH420>
<2021/01/22>
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return(min(L),max(L),sum(L)/len(L))
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    int_1 = 1
    int_2 = int_1
    int_2 = 2
    int_1 == int_2
    str_1 = "Hello World!"
    str_2 = str_1
    str_2 = "G"+str_1[2:]
    str_1 == str_2
    list_1 = [1,2]
    list_2 = list_1
    list_2[0] = [3]
    list_1 == list_2
    tuple_1 = (5,5)
    tuple_2 = tuple_1
    tuple_2 += (1,)
    tuple_1 == tuple_2
    set_1 = {"apple","banana"}
    set_2 = set_1
    set_2.add("grapes")
    set_1 == set_2
    return print("We have type int, str and tuple are immutable; list and set are mutable")
    raise NotImplementedError("Problem 2 Incomplete")



# Problem 3
import calculator


def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    x = calculator.product(a,a)
    y = calculator.product(b,b)
    z = calculator.sum1(x,y)
    return calculator.sqrt(z)
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
import itertools
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    s = list(A)
    result = itertools.chain.from_iterable(itertools.combinations(s,t)for t in range(len(s)+1))
    return list(result)
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""