from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        return ValueError("Iterable is empty")


def gen246():
    print("About to yield2")
    yield 2
    print("About to yield4")
    yield 4
    print("About to yield6")
    yield 6
    print("About to return")



def main():
    """
    Test Function
    """
    l = [x for x in range(101) if is_prime(x)]
    print(l)






if __name__ == '__main__':
    main()
    exit(0)