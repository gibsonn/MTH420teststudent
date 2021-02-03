# standard_library.py
"""Python Essentials: The Standard Library.
<Jack Draney>
<MTH420>
<01/22/2021>
"""
import calculator, sys, random, time, box
from itertools import combinations

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return min(L), max(L), sum(L)/len(L)

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    #int
    a=4
    b=a
    b=5
    if a==b:
        print("int is mutable")
    else:
        print("int is immutable")
    #str
    c="ok"
    d=c
    d="mutable?"
    if c==d:
        print("str is mutable")
    else:
        print("str is immutable")
    #list
    e=[1,2,3,4,5]
    f=e
    f[1]=1000
    if e==f:
        print("list is mutable")
    else:
        print("list is immutable")
    #tuple
    g=(8,2,3)
    h=g
    h+=(1,)
    if g==h:
        print("tuple is mutable")
    else:
        print("tuple is immutable")
    #set
    l={1,2,3}
    m=l
    m.add(400)
    if l==m:
        print("set is mutable")
    else:
        print("set is immutable")


# Problem 3
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
    return calculator.sqrt(calculator.mySum(calculator.myProduct(a,a), calculator.myProduct(b,b)))


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    output=[] #could be made faster if necessary by instead initializing a list of length 2**len(A) and iterating through instead of appending
    for l in range(0,len(A)+1):
        for combo in combinations(A,l):
            s=set()
            for item in combo:
                s.add(item)
            output.append(s)
    return output
