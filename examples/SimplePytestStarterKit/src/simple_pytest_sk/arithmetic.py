def sign(x):
    '''
    Computes sign of number

    >>> sign(2)
    1
    >>> sign(-2)
    -1
    '''
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def lerp(x, y, t):
    '''
    Linearly interpolate between two numbers.

    >>> lerp(1, 3, 0)
    1

    >>> lerp(1, 3, 1)
    3
    '''
    return (1 - t) * x + t * y


def negate(x):
    """Return the negative value of x.
    
    >>> negate(1)
    -1

    >>> negate(-1)
    1

    >>> negate(0)
    0
        
    """
    return -x


def my_abs(x):
    """Return the absolute value of x.

    >>> my_abs(2)
    2

    >>> my_abs(-2)
    2

    >>> my_abs(0)
    0
    """
    if x <= 0:
        return -x
    else:
        return x

print(my_abs(2))
print(my_abs(-2))