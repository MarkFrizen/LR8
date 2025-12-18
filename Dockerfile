# Шаг 1: Выбираем базовый образ с Python
FROM python:3.12-slim

# Шаг 2: Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Шаг 3: Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Шаг 4: Отключаем создание виртуального окружения внутри контейнера
RUN poetry config virtualenvs.create false

# Шаг 5: Устанавливаем рабочую директорию
WORKDIR /app

# Шаг 6: Копируем ВЕСЬ проект сразу
COPY . /app

# Шаг 7: Устанавливаем зависимости через Poetry
# Используем --no-root чтобы сначала установить только зависимости
RUN poetry install --no-root --no-interaction --no-ansi

# Шаг 8: Устанавливаем сам проект в режиме разработки
RUN poetry install --no-interaction --no-ansi

# Шаг 9: Команда запуска приложения
CMD ["poetry", "run", "myapp"]