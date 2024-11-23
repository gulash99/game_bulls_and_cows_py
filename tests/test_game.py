import pytest
from logic.game import BullsAndCows


@pytest.mark.parametrize(
    "secret_number, guess, expected_bulls, expected_cows",
    [
        ("1234", "1243", 2, 2),  # 2 быка, 2 коровы
        ("5678", "1234", 0, 0),  # 0 быков, 0 коров
        ("4567", "5678", 0, 3),  # 0 быков, 3 коровы
        ("1234", "1234", 4, 0),  # 4 быка, 0 коров (угадывание числа)
    ]
)
def test_bulls_and_cows(secret_number, guess, expected_bulls, expected_cows):
    """Тестируем функцию подсчета быков и коров."""
    game = BullsAndCows(length=4)
    game.secret_number = secret_number
    bulls, cows = game.guess(guess)
    assert bulls == expected_bulls, f"Для {guess}: ожидалось {expected_bulls} Б"
    assert cows == expected_cows, f"Для {guess}: ожидалось {expected_cows} К"


@pytest.mark.parametrize(
    "guess, expected_exception",
    [
        ("123", ValueError),  # Слишком короткое число
        ("1123", ValueError),  # Повторяющиеся цифры
    ]
)
def test_invalid_input(guess, expected_exception):
    """Тестируем обработку неправильных вводов."""
    game = BullsAndCows(length=4)
    with pytest.raises(expected_exception):
        game.guess(guess)


def test_generate_number():
    """Тестируем генерацию случайного числа с уникальными цифрами."""
    game = BullsAndCows(length=4)
    generated_number = game._generate_number()
    assert len(generated_number) == 4, "Число должно быть длиной 4"
    assert len(set(generated_number)) == len(generated_number), \
        "Цифры в числе должны быть уникальными"


def test_gameplay():
    """Тестируем игровой процесс с несколькими попытками."""
    game = BullsAndCows(length=4)

    # Загаданное число
    game.secret_number = "4567"

    # Набор попыток
    attempts = [
        ("1234", 0, 1),  # 0 быков, 1 корова
        ("5678", 0, 3),  # 0 быков, 3 коровы
        ("6547", 2, 2),  # 2 быка, 2 коровы
        ("4567", 4, 0),  # 4 быка, 0 коров (угадывание числа)
    ]

    for guess, expected_bulls, expected_cows in attempts:
        bulls, cows = game.guess(guess)
        assert bulls == expected_bulls, f"Для {guess}: ожидалось {expected_bulls} Б"
        assert cows == expected_cows, f"Для {guess}: ожидалось {expected_cows} К"

    assert game.secret_number == "4567", "Секр.число должно остаться неизменным"


def test_game_over():
    """Тестируем завершение игры при угадывании числа."""
    game = BullsAndCows(length=4)

    # Загаданное число
    game.secret_number = "1234"

    # Игрок угадывает с первой попытки
    guess = "1234"
    bulls, cows = game.guess(guess)

    assert bulls == 4, "Должно быть 4 быка"
    assert cows == 0, "Коров должно быть 0"
