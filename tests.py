from sheets import Sheet, Trimdek, Kliplok


def test_custom_orb():
    sheet_class = Sheet.factory('Custom Orb')
    assert sheet_class == Sheet
    sheet = sheet_class(1, 1800)
    assert sheet.get_batten_row_count() == 3
    assert sheet.get_total_screws() == 13
    assert sheet.get_batten_screws() == 12
    assert sheet.get_total_battens() == 1


def test_trimdek():
    sheet_class = Sheet.factory('Trimdek')
    assert sheet_class == Trimdek
    sheet = sheet_class(1, 1800)
    assert sheet.get_batten_row_count() == 3
    assert sheet.get_total_screws() == 10
    assert sheet.get_batten_screws() == 12
    assert sheet.get_total_battens() == 1


def test_kliplok():
    sheet_class = Sheet.factory('Kliplok')
    assert sheet_class == Kliplok
    sheet = sheet_class(1, 1800)
    assert sheet.get_batten_row_count() == 3
    assert sheet.get_total_screws() == 0
    assert sheet.get_batten_screws() == 12
    assert sheet.get_total_battens() == 1


if __name__ == "__main__":
    test_custom_orb()
    test_trimdek()
    test_kliplok()

    print("tests pass")
