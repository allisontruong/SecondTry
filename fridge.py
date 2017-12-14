from contextlib import closing

class RefrigeratorRaider:
    """
    Raid a Refrigerator
    """
    def open(self):
        print("open fridge door")

    def take(self, food):
        print("Finding {}..".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door")


def raid(food):
    #r = RefrigeratorRaider()
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        #r.close() # you do not need this close because with takes care of it
