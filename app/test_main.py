from app.main import get_coin_combination


def test_check_that_is_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_check_penny_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_check_penny_nickel_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_check_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
