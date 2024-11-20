import random
from typing import Tuple


class BullsAndCows:
    """Класс для реализации игры 'Быки и коровы'."""

    def __init__(self, length: int):
        """
        Инициализация игры.

        Args:
            Длина числа для угадывания.
        """
        self.length = length
        self.secret_number = self._generate_number()
        self.attempts = []

    def _generate_number(self) -> str:
        """Генерация случайного числа."""
        digits = random.sample(range(10), self.length)
        return ''.join(map(str, digits))

    def guess(self, number: str) -> Tuple[int, int]:
        """
        Проверка попытки пользователя.

        Args:
            Число, предложенное пользователем.

        Returns:
            Количество быков и коров.
        """
        bulls = sum(1 for s, n in zip(self.secret_number, number) if s == n)
        cows = sum(1 for n in number if n in self.secret_number) - bulls
        self.attempts.append((number, bulls, cows))
        return bulls, cows
