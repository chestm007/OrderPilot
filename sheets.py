import logging
import math

batten_length = 7.5

logger = logging.getLogger("orderpilot")


class Sheet:
    cover = .76
    end_screws = 5
    centre_screws = 3

    def __init__(self, qty, length):
        self.qty = qty
        self.length = length

    def get_total_battens(self):
        meters = self.qty * self.cover
        return math.ceil(self.get_batten_row_count() * meters / batten_length)

    def get_batten_row_count(self):
        batten_rows = math.ceil(self.length / 900) + 1
        logger.debug(f"batten rows: {batten_rows}")
        return batten_rows

    def get_batten_screws(self):
        return math.floor(self.get_batten_row_count() * self.qty * 2) + (self.get_batten_row_count()*2)

    def get_total_screws(self):
        battens = self.get_batten_row_count()
        logger.debug(f"battens: {battens} - ")
        return ((battens - 2) * self.qty * self.centre_screws) + (self.qty * self.end_screws * 2)

    def get_total_blanket(self):
        return self.qty * self.length / 1000 * self.cover / 18

    def get_bracket_count(self):
        return 0

    @staticmethod
    def factory(sheet_type):
        sheet_type = sheet_type.lower().lstrip()
        logger.debug(sheet_type)
        if sheet_type in ('trimdek', 'trimclad'):
            return Trimdek
        elif sheet_type in ('kliplok', ):
            return Kliplok
        elif sheet_type in ('custom orb', ):
            return Sheet
        raise TypeError(f'sheet type {sheet_type} was not matched')


class Trimdek(Sheet):
    cover = .76
    end_screws = 4
    centre_screws = 2


class Kliplok(Sheet):
    cover = .7
    end_screws = 0
    centre_screws = 0

    def get_total_screws(self):
        return 0

    def get_batten_screws(self):
        return self.get_bracket_count() * 4

    def get_bracket_count(self):
        return self.get_batten_row_count()*self.qty

