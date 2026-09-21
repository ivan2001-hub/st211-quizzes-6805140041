from shopping import calculate_item_total, calculate_total


def test_calculate_item_total():
    assert calculate_item_total(100, 2) == 200


def test_calculate_total():
    prices = [100, 50, 20]
    quantities = [2, 3, 1]

    assert calculate_total(prices, quantities) == 370