#!/bin/bash

# Установка кодировки UTF-8
export LANG=en_US.UTF-8

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Не удалось активировать виртуальное окружение. Убедитесь, что путь к 'venv/bin/activate' правильный."
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Виртуальное окружение активировано."

# Запуск FastAPI сервера через uvicorn
echo "Запуск FastAPI сервера через uvicorn..."
if ! uvicorn main:app --reload --port 80; then
    echo "Не удалось запустить сервер FastAPI. Проверьте логи для получения дополнительной информации."
    read -p "Нажмите Enter для выхода..."
    exit 1
fi
echo "Сервер остановлен!"

read -p "Нажмите Enter для выхода..."
