import random
from typing import Tuple  # Для описания типов возвращаемых значений


class BullsAndCows:
    """Класс для реализации игры 'Быки и коровы'."""

    def __init__(self, length: int):
        """
        Инициализация игры.

        Args:
            Длина числа для угадывания.
        """
        self.length = length
        self.secret_number = self._generate_number()  # Генерация числа
        self.attempts = []  # Хранение истории попыток пользователя

    def _generate_number(self) -> str:
        """
        Генерация случайного числа.

        Возвращает:
            Случайное число заданной длины без повторяющихся цифр.
        """
        # Выбираем уникальные цифры и преобразуем их в строку
        digits = random.sample(range(10), self.length)
        return ''.join(map(str, digits))

    def guess(self, number: str) -> Tuple[int, int]:
        """
        Проверка попытки пользователя.

        Args:
            Число, предложенное пользователем.

        Returns:
            Количество быков и коров.

        Raises:
            ValueError: Если число некорректно.
        """

        if len(number) != self.length:
            raise ValueError("Число должно быть длиной = {self.length} цифр.")
        if len(set(number)) != len(number):
            raise ValueError("Число не должно содержать повторяющихся цифр.")
        if not number.isdigit():
            raise ValueError("Число должно содержать только цифры.")

        # Считаем быков (совпавшие цифры на своих местах)
        bulls = sum(1 for s, n in zip(self.secret_number, number) if s == n)

        # Считаем коров (цифры, которые есть в числе, но не на своих местах)
        cows = sum(
            min(self.secret_number.count(n), number.count(n)) for n in set(number)
        ) - bulls

        # Сохраняем попытку с результатами
        self.attempts.append((number, bulls, cows))

        return bulls, cows
