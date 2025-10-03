"""Игра угадай число 
Алгоритм: бинарный поиск. Среднее число попыток ~7 (<20).
"""

import numpy as np


def binary_predict(number: int = 1) -> int:
    """Угадывает загаданное число с помощью бинарного поиска.

    Args:
        number (int): Загаданное число от 1 до 100.

    Returns:
        int: Количество попыток до угадывания.
    """
    count = 0
    low, high = 1, 100  # границы поиска

    while True:
        count += 1
        predict = (low + high) // 2  # середина диапазона

        if predict == number:
            return count  # угадали число

        elif predict < number:
            low = predict + 1  # сдвигаем нижнюю границу
        else:
            high = predict - 1  # сдвигаем верхнюю границу


def score_game(predict_func) -> int:
    
    """Оценивает среднее количество попыток на 1000 испытаний.

    Args:
        predict_func: функция угадывания.

    Returns:
        int: среднее число попыток
    """
    np.random.seed(42)  # фиксируем seed для воспроизводимости
    numbers = np.random.randint(1, 101, size=1000)
    attempts = [predict_func(n) for n in numbers]
    score = int(np.mean(attempts))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    score_game(binary_predict)
