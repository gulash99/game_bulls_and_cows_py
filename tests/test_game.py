import pytest
from game import Game  # Предположим, что реализация игры в файле game.py


@pytest.mark.parametrize(
    "secret_number, guess, expected_bulls, expected_cows",
    [
        ("1234", "1243", 2, 2),  # 2 быка, 2 коровы
        ("5678", "1234", 0, 0),  # 0 быков, 0 коров
        ("4567", "5678", 2, 0),  # 2 быка, 0 коров
        ("1234", "1234", 4, 0),  # 4 быка, 0 коров (угадывание числа)
    ]
)
def test_bulls_and_cows(secret_number, guess, expected_bulls, expected_cows):
    """Тестируем функцию подсчета быков и коров"""
    game = Game(number_length=4)


@pytest.mark.parametrize(
    "guess, expected_exception",
    [
        ("123", ValueError),  # Слишком короткое число
        ("1123", ValueError),  # Повторяющиеся цифры
    ]
)

def test_gameplay():
    """Тестируем игровой процесс с несколькими попытками"""
    game = Game(number_length=4)

    # Загаданное число
    game.secret_number = "4567"

    # Набор попыток
    attempts = [
        ("1234", 1, 1),  # 1 бык, 1 корова
        ("5678", 2, 0),  # 2 быка, 0 коров
        ("4567", 4, 0),  # 4 быка, 0 коров (угадывание числа)
    ]

    for guess, expected_bulls, expected_cows in attempts:
        bulls, cows = game.bulls_and_cows(guess)
