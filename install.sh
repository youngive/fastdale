#!/bin/bash

# Установка кодировки UTF-8
export LANG=en_US.UTF-8

# Проверка наличия Python
echo "Проверка наличия Python..."
if ! command -v python &> /dev/null; then
    echo "Python не найден. Пожалуйста, загрузите его с сайта https://www.python.org/downloads/ и установите для работы FastDale."
    read -p "Нажмите Enter для выхода..."
    exit 1
fi

echo "Найден:"
python --version

# Создание виртуального окружения
echo "Создание виртуального окружения..."
if ! python -m venv venv; then
    echo "Не удалось создать виртуальное окружение."
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Виртуальное окружение создано."

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Не удалось активировать виртуальное окружение."
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Виртуальное окружение активировано."

# Установка pip-tools
echo "Установка pip-tools..."
if ! pip install pip-tools; then
    echo "Не удалось установить pip-tools."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "pip-tools установлены."

# Проверка наличия файла requirements.in
if [ ! -f requirements.in ]; then
    echo "Файл requirements.in не найден. Создайте файл requirements.in с необходимыми зависимостями."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi

# Генерация requirements.txt
echo "Генерация requirements.txt..."
if ! pip-compile; then
    echo "Не удалось сгенерировать requirements.txt."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "requirements.txt сгенерирован."

# Установка зависимостей из requirements.txt
echo "Установка зависимостей из requirements.txt..."
if ! pip-sync; then
    echo "Не удалось установить зависимости."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Зависимости установлены."

# Проверка наличия Alembic
if ! command -v alembic &> /dev/null; then
    echo "Alembic не установлен. Установите Alembic для выполнения миграций."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi

# Создание первой ревизии Alembic
echo "Создание первой ревизии Alembic..."
if ! alembic revision --autogenerate -m "First commit"; then
    echo "Не удалось создать первую ревизию Alembic."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Первая ревизия Alembic создана."

# Применение миграций Alembic
echo "Применение миграций Alembic..."
if ! alembic downgrade base; then
    echo "Не удалось применить миграции Alembic."
    deactivate
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Миграции Alembic применены."

# Деактивация виртуального окружения
echo "Деактивация виртуального окружения..."
deactivate
if [ $? -ne 0 ]; then
    echo "Не удалось деактивировать виртуальное окружение."
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Виртуальное окружение деактивировано."

echo "Установка завершена."

read -p "Нажмите Enter для выхода..."
