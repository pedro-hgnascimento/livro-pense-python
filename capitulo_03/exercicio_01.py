def right_justify(s):
    """Return a right-justified string of length 70."""
    print(' ' * (70 - len(s)) + s)

right_justify('monty')

def do_twice(f, n):
    """Call the function f twice."""
    f(n)
    f(n)

def print_spam(s):
    """Print 'spam'."""
    print(s)

do_twice(print_spam, 'spam')

def do_four(f, n):
    """Call the function f four times."""
    do_twice(f, n)
    do_twice(f, n)

do_four(print_spam, 'spam')
print()

