"""
Object Model test scripts
"""
def modify(k):
    """
    This modifies the content of my list
    :param k: list
    :return: nothing
    """
    k.append(33)
    print("k= ",k)

def replace(g):
    """
    Replace the content of the list
    :param g: list object
    :return: nothing
    """
    g = [17, 36, 22, 33]
    print("g = ", g)

def update_info(j):
    """
    Increment mebmers by 1
    :return: nothing
    """
    #for i in j:
     #   i +=1
    #print("j = ", j)

    i = 0
    while i < len(j):
        j[i] +=1
        i +=1
    print("j = ", j)


def banner(message, border='*'):
    """
    Displays message surrounded by border
    :param message: message string
    :param border: border style <char>. optional with default value
                    of *
    :return: nothing
    """
    x = border * (len(message) + 4)
    print(x)
    print(border, message, border)
    print(x)

# Always use immutable objects such as integer
# or strings for default values
def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: Optional list object
    :return: menu
    """
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

def number_info():
    """
    Write a function that prompts the user
    for 2 intergers then it prints: The sum,
    the difference, the product, the average,
    and the distance (absolute value), the maximum,
    the minimum
    :return:
    """
    print("Please enter first integer: ")
    int1 = int(input())
    print("Please enter second integer: ")
    int2 = int(input())
    print (int1, int2)
    print("%-12s%5d" % ("Sum:", int1+int2))
    print("%-12s%5d" % ("Difference:", int1-int2))
    print("%-12s%5d" % ("Product:", int1*int2))
    print("%-12s%8.2f" % ("average:", (int1+int2)/2))
    print("%-12s%8.2f" % ("Distance:", abs(int1 - int2)))
    print("%-12s%5d" % ("Max:", max(int1, int2)))
    print("%-12s%5d" % ("Min:", min(int1, int2)))


def main():
    m = [9, 12, 45]
    print("Before m= ", m)
    modify(m)
    print("After m= ", m)
    replace(m)
    print("After Replace m = ", m)
    update_info(m)
    print("After Update info m = ", m)
    # Set parameter in order
    # Use only required parameters
    banner("WSU")
    # user parameters by name
    banner(border="@", message="Weber State")

    # When are default arguments evaluated??


if __name__ == '__main__':
    main();
