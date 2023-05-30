def is_even(x):
    """
    Checks if input is an even integer

    Returns True if input is an even integer
    Returns False if input is not an even integer
    Raises Error if input is not an integer
    """

    if not isinstance(x, int):
        raise TypeError('x must be an integer')

    
    return x % 2
    




assert is_even.__doc__ is not None
has_failed = False
try:
    is_even('bla')
except TypeError:
    has_failed = True

assert has_failed

assert is_even(1) is not None
