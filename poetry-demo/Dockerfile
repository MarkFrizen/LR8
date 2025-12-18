# Шаг 1: Выбираем базовый образ с Python
# Используем официальный легкий образ Python 3.11
FROM python:3.12-slim

# Шаг 2: Устанавливаем системные зависимости
# 1) Обновляем список пакетов
# 2) Устанавливаем пакеты, которые нужны для сборки Python-пакетов и работы Poetry
# 3) Устанавливаем сам Poetry (через pip)
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Шаг 3: Добавляем Poetry в PATH (чтобы команда `poetry` была доступна)
ENV PATH="/root/.local/bin:$PATH"

# Шаг 4: Отключаем создание виртуального окружения внутри контейнера
# В Docker-контейнере и так изоляция, поэтому виртуальное окружение не нужно
RUN poetry config virtualenvs.create false

# Шаг 5: Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Шаг 6: Копируем файлы зависимостей
# Сначала копируем только файлы с зависимостями для лучшего кэширования
COPY pyproject.toml poetry.lock* /app/

# Шаг 7: Устанавливаем зависимости через Poetry
# --no-root не устанавливает само приложение (только зависимости)
RUN poetry install --only=main --no-interaction --no-ansi

# Шаг 8: Копируем весь исходный код приложения
COPY ./app /app/app

# Шаг 9: Команда запуска приложения
# Используем команду, объявленную в pyproject.toml в секции [tool.poetry.scripts]
CMD ["myapp"]