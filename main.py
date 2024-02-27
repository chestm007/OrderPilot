import logging
import sys

from sheets import Sheet
import math


def main(sheet_qty):
    qtys = decode_order_string(sheet_qty)
    battens, screws, blanket, batten_screws, brackets = 0, 0, 0, 0, 0
    for qty in qtys.values():
        battens += qty.get_total_battens()
        screws += qty.get_total_screws()
        blanket += qty.get_total_blanket()
        batten_screws += qty.get_batten_screws()
        brackets += qty.get_bracket_count()


    print(f"40mm battens @ 7500 {battens}")
    print(f"batten screws {batten_screws}")
    print(f"roof screws {screws}")
    print(f"{math.ceil(blanket)} bags R1.3 blanket")
    print(f"{brackets} kliplok brackets")


def decode_order_string(sheet_qty):
    qtys = dict()
    factory = None
    for line in sheet_qty.splitlines():
        line = line.strip()
        if not line:
            continue
        if factory is None:
            factory = Sheet.factory(line)
            continue
        qty, length = line.split('@')
        exist = qtys.get(length)
        if exist is not None:
            qtys[int(length)] += int(qty)
        else:
            qtys[int(length)] = int(qty)
    return_qtys = dict()
    for length, qty in qtys.items():
        return_qtys[length] = factory(qty, length)
    return return_qtys


DEBUG = False


if __name__ == "__main__":
    logger = logging.getLogger("orderpilot")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    sheets = """
    Custom orb
    48@9200p
    """

    main(sheets)
