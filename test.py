import main


def test_calcaulate_sq():
    assert main.calculate_squares([0, 1, 2, 4, 8]) == [0, 1, 4, 16, 64]

