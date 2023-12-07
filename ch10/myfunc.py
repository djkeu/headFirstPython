# p.390

def print_args1(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def print_args2(**kwargs):  # keyword args, for dicts
    for k, v in kwargs:
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()
