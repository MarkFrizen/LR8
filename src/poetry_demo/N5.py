import logging

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("fibonacci.log"),
        logging.StreamHandler()
    ]
)
logging.debug(f"***Подсчет чисел Фибоначчи ***")
def fibonacci():
    logging.info("Генератор Фибоначчи запущен")
    a, b = 0, 1
    count = 0
    while True:
        logging.debug(f"Сгенерировано число Фибоначчи #{count}: {a}")
        yield a
        a, b = b, a + b
        count += 1

def print_fibonacci(n):
    if n < 0:
        logging.error("Попытка вывести отрицательное количество чисел Фибоначчи")
        raise ValueError("Количество чисел должно быть неотрицательным")

    logging.info(f"Вывод первых {n} чисел Фибоначчи")
    fib_gen = fibonacci()
    for i in range(n):
        number = next(fib_gen)
        print(number)
    logging.info(f"Вывод завершён: {n} чисел Фибоначчи")

if __name__ == "__main__":
    try:

        print_fibonacci(20)
    except ValueError as e:
        logging.error(f"Ошибка ввода: {e}")