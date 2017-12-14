import sys
from itertools import count, islice

def sequence():
    """
    Recaman series: a_0 = 0,
     a_n=a_(n-1) - n. If the result is positive
                       and not already in the list.
        Otherwise a_n = a_(n-1) + n
    :return:
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n  #a_n=a_(n-1) + n
        # a_n = a_(n - 1) - n.If the result is positive
        # and not already in the list.
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """
    Write Recaman's sequence to a text file
    :param filename: file name to create
    :param num: maximum number to write
    :return: nothing
    """
    f = open(filename, mode='wt', encoding='utf-8')
    # write info
    f.writelines("{0}\n".format(r) for r in islice(sequence(), num+1))
    f.close()


def read_series(filename):
    """
    Read Recaman series from file. Create a list of each record
    on the file
    :param filename: list with file records
    :return:
    """
    f = open(filename, mode='rt', encoding='utf-8')
    # read sequence write to list read list
    series = []
    for line in f:
        #print(type(line))
        a = int(line.strip())
        series.append(a)

    f.close()
    return series


def read_series_with_block(filename):
    """
    The with-block will automatically close the file for you
    :param filename:
    :return: list with file records
    """
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


def main():
    with open('test.txt', mode='rt', encoding='utf-8') as rf:
        wpl = words_per_line(rf)
    print(wpl, type(rf))
    # f = "recamanSeries.txt"
    # n = 100
    # #write_sequence(f, n)
    # s = read_series(f)
    # print(s)
    #
    # z = read_series_with_block(f)
    # print(z)



if __name__ == '__main__':
    main()
    exit(0)
