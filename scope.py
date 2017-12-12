count = 0 # global variable

def show_count():
    print(count)


def set_count(c):
    global count  # link to the global count
    count = c


