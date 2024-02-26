# Официальный образ Python 3.11
FROM python:3.11

# Рабочая директория
WORKDIR /store

# Копируем файл зависимостей
COPY ./requirements.txt requirements.txt

# Создаем виртуальное окружение и активируем его
RUN python -m venv venv
RUN . venv/bin/activate

# Устанавливаем все зависимости
RUN pip install -r requirements.txt

# Копируем все оставшиеся файлы в рабочую директорию
COPY . .

# Запуск микросервиса
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]