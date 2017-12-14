def swap(val):
    """
    Swap the first half withe the second half of the list
    :param val: a list of objects
    :return: nothing
    """
    #a = val[0:4]
    #b = val[4:]
    #val = b.copy() + a.copy()
   #print(val)

    m = len(val)//2
    n = len(val) % 2
    if n == 1:
        print("Odd number")
        g = m + 1
        print(val[m:0])
        return val[g:] + val[m:0] + val[:m]
    # TODO: make sure it works for odd number of elements
    return val[m:] + val[:m]



def main():
    val = [9, 13, 21, 4, 8, 11, 7, 1, 3]
    print(val)
    val = swap(val)
    print(val)


if __name__ == '__main__':
    main()