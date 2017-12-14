import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        #print(line)
        #print(line, end='')
        print(line.strip())

    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
    exit(0)