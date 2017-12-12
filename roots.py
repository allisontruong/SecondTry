import sys


def sqrt(x):
    """
    Compute the square root using the method of
    Heron Alexandria
    :param x: The number for which the square root is to be computed
    :return: The square root of x
    :raise ValueError on DivisionByZero
    """
    if x < 0:
        raise ValueError("Cannot compute the square root "
                         "of a negative number {}".format(x))
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess



def main():
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
        print("This is never printed")
    except ValueError as e:
       print(e, file=sys.stderr)
      #  print("Cannot compute square root of a negative number")

    print("Program execution continues here")


if __name__ == '__main__':
    main()
