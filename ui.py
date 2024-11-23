from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from logic.game import BullsAndCows


class BullsAndCowsUI(QWidget):
    """Класс для графического интерфейса игры."""

    def __init__(self):
        """
        Инициализация интерфейса игры.
        """
        super().__init__()
        self.setWindowTitle("Быки и Коровы")  # Установка заголовка окна

        # Основная логика игры
        self.game = None  # Переменная для хранения экземпляра игры

        # Элементы интерфейса
        self.layout = QVBoxLayout()  # Основной вертикальный макет
        self.instructions = QLabel("Введите длину числа и начните игру:")
        # Поле ввода для длины числа
        self.length_input = QLineEdit()
        # Кнопка для начала игры
        self.start_button = QPushButton("Начать игру")
        # Лейбл для отображения состояния игры
        self.status = QLabel("")
        # Поле ввода для попыток угадать число
        self.guess_input = QLineEdit()
        # Кнопка для отправки попытки
        self.submit_button = QPushButton("Угадать")
        # Текстовый виджет для журнала попыток
        self.log = QTextEdit()

        # Настройка элементов
        self.length_input.setPlaceholderText("Длина числа (например, 4)")
        self.guess_input.setPlaceholderText("Ваше число")
        self.log.setReadOnly(True)  # Поле журнала только для чтения

        # Добавление элементов в макет
        self.layout.addWidget(self.instructions)
        self.layout.addWidget(self.length_input)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.status)
        self.layout.addWidget(self.guess_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.log)
        self.setLayout(self.layout)  # Установка основного макета в окно

        # Подключение событий
        self.start_button.clicked.connect(self.start_game)
        self.submit_button.clicked.connect(self.make_guess)

    def start_game(self):
        """
        Запуск новой игры.
        Проверяет корректность длины числа и инициализирует игру.
        """
        try:
            # Считываем длину числа из поля ввода
            length = int(self.length_input.text())
            if length < 1 or length > 10:  # Проверка допустимости длины
                raise ValueError("Недопустимая длина.")

            # Создаем экземпляр игры с указанной длиной числа
            self.game = BullsAndCows(length)
            self.status.setText("Игра началась! Угадайте число.")  # Статус
            self.log.clear()  # Очищаем журнал
        except ValueError:
            # Обработка ошибки, если ввод некорректный
            self.status.setText("Ошибка: введите корректное число.")

    def make_guess(self):
        """
        Обработка попытки пользователя.
        Проверяет корректность ввода и выводит результат.
        """
        if not self.game:
            # Если игра не начата, показываем сообщение
            self.status.setText("Сначала начните игру.")
            return

        # Получаем число, введенное пользователем
        guess = self.guess_input.text()
        if len(guess) != self.game.length or not guess.isdigit():
            # Проверка длины и того, что ввод содержит только цифры
            self.status.setText("Введите корректное число.")
            return

        # Проверяем попытку пользователя с помощью логики игры
        bulls, cows = self.game.guess(guess)

        # Добавляем результат в журнал
        self.log.append(f"Число: {guess}, Быки: {bulls}, Коровы: {cows}")
        self.guess_input.clear()  # Очищаем поле ввода

        if bulls == self.game.length:
            # Если угаданы все цифры, игра завершена
            self.status.setText("Поздравляем!!!!! Вы угадали число!")
            self.game = None  # Сбрасываем текущую игру
