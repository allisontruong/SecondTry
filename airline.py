"""
Model for airline
"""

class Flight:

    def __init__(self, number, aircraft):
        # Verify info " A A N N N "
        # 1) pos 0-1 Must be alpha and capital letters
        if not number[:2].isalpha():
            return ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            return ValueError("Invalid airline code in '{}'".format(number))
        # 2) Pos 2-5 must be digits and 0 < int <= 999
        if not (number[2:].isdigit() and int(number[2:]) <= 999):
            return ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

class Aircraft:

    def __init__(self, registration, model, num_rows,
                 num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        """
        Produces an iterable sequence of row numbers up to
        the number of rows in the plane.
        The string and its slice method return a string with
        one character per row.
        These two objects the range, and the string are bundle
        into a tuple
        :return:
        """
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])



def main():
    """
    Test Function
    """

    # f = Flight("AA123")
    # print(f.number())
    # print(f.airline())
    a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
    # print(a.model())
    # print(a.registration())
    # print(a.seating_plan())

    f = Flight("AA777", a)
    print(f.)

if __name__ == '__main__':
    main()
    exit(0)