import logging as log

# Настройка логгирования
log.basicConfig(
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        log.FileHandler("square.log"),
        log.StreamHandler()
    ]
)

def square(x):
    result = x ** 2
    log.debug(f"Квадрат числа {x} = {result}")
    return result

log.debug(f"***Подсчет квадратов числа***")
numbers = list(range(1, 11))
log.info(f"Исходные числа: {numbers}")

squares = list(map(square, numbers))
log.info(f"Квадраты чисел: {squares}")

print(squares)


