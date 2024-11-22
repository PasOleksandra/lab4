# Використовуємо базовий образ Alpine з Python
FROM python:3.9
# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо локальні файли у робочу директорію контейнера
COPY . /app

# Команда для запуску скрипта
CMD ["python", "lab2.py"]
