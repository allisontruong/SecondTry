"""
Model for airline
"""
from pprint import pprint as pp


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

        rows, seats = self._aircraft.seating_plan()
        # List of Dictionaries
        # Waste one entry to match the actual number from the map
        # To the single element list, concatenate another list containing
        # one entry for each row in teh aircraft. Done by the list
        # comprehension from the list of rows retrieve from the seating plan
        # Discard the row number (_) since you already have it from before
        # The item from the comprehension is itself a dictionary comprehension
        # use the list comprehension because we want a distinct object for each row.
        self._seating = [None] + [{letter:None for letter in seats}
                                   for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """
        Parse a seat designator into a valid row and letter
        :param seat: A seat designator such as '12A'
        :return: Tuple with an integer and a string for row and seat
        """
        row_number, seat_letter = self._aircraft.seating_plan()
        # Validate letter
        letter = seat[-1]
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter{}".format(letter))
        # Valid row format
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        # Valid Row?
        if row not in row_number:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seats(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param seat: A seat designator such as '12A', '21F'
        :param passenger: The passenger name
        :raises: ValueError if the seat is unavailable
        """
        row, letter = self._parse_seat(seat)
        # Check if it is available
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))
        # Assign seat
        self._seating[row][letter] = passenger

    def reallocate_passengers(self, from_seat, to_seat):
        """
        Reallocate a passenger seat to a different seat
        :param from_seat: existing seat designator
        :param to_seat: new seat designator
        :return: nothing
        :raises: ValueError on: Seat already occupied, or
                 No passenger to reallocate.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to reallocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))
        # Assign new seat and clear old seat
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        """
        Returns available seats
        :return: available seats
        """

        return sum(sum(1 for s in row.values() if s is None)
            for row in self._seating if row is not None)

      #  if self._seating[to_row][to_letter] is not None:

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(),
                         self.aircraft_model())

    def _passenger_seats(self):
        """ An iterable series of passengers seating allocations"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
        def model(self):
            return "Airbus 319"

        def seating_plan(self):
            return range(1,23), "ABCDEF"


class Boeing777(Aircraft):
        def model(self):
            return "Boeing 777"

        def seating_plan(self):
            return range(1, 26), "ABCDEFGHJ"

def make_flights():
    """
    Test Function
    """
    #f = Flight("AA777", AirbusA319("G-EUPT"))
    # print(f.number())
    # print(f.airline())
    #a = Aircraft("G-EUPT", "Airbus A319", num_rows=22,
    #             num_seats_per_row=6)
    # print(a.model())
    # print(a.registration())
    # print(a.seating_plan())

    f = Flight("AA777", AirbusA319("G-EUPT"))
    f.allocate_seats("12A", "Guido van Rossum") #Python
    f.allocate_seats("12B", "Rasmus Lerdorf")  #php
    f.allocate_seats("15F", "Bjarne Stroustrup")  # C++

    g = Flight("DL24", Boeing777("F-GSPS"))
    g.allocate_seats("15E", "Anders Hejlsberg")   # Turbo Pascal
    #f.allocate_seats("E27", "Yukijiro Matsumoto")  # Ruby
    g.allocate_seats("22E", "Yukijiro Matsumoto")  # Ruby
    #pp(f._seating)
    #f.reallocate_passengers("22E", "12C")

    return f


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"\
             " Flight: {1}"\
             " Seat: {2}"\
             " Aircraft: {3}"\
             "|".format(passenger, seat, flight_number, aircraft)
    banner = "+" + "-"*(len(output)-2) + "+"
    border = "|" + " "*(len(output)-2) + "|"
    lines = [banner, border , output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

def main():
    f1, g1 = make_flights()
    #pp(f1._seating)
    #f1.reallocate_passengers("22E", "12C")
    #pp(f1._seating)

    #print(f1.num_available_seats())

    #console_card_printer("Guido", "12A", "AA123", "Airbus 319")

    # Pass the function as a parameter. Do not include the (),
    # otherwise Python will try to execute the function
    #f1.make_boarding_cards(console_card_printer)

    print(f1.aircraft_model())
    print(f1.num_available_seats())


if __name__ == '__main__':
    main()
    exit(0)