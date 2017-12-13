from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True



def main():
    """
    Test Function
    """
    l = [x for x in range(1001) if is_prime(x)]
    print(l)

if __name__ == '__main__':
    main()
    exit(0)