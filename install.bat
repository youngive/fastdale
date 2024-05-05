@echo off

REM Проверка наличия Python
CALL python --version 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python не найден. Пожалуйста, загрузите его с сайта https://www.python.org/downloads/ и установите для работы FastDale.
    pause
    exit /b
)

REM Создание виртуального окружения
CALL python -m venv venv

REM Активация виртуального окружения
CALL venv\Scripts\activate

REM Установка pip-tools
CALL pip install pip-tools

REM Генерация requirements.txt
CALL pip-compile

REM Установка зависимостей из requirements.txt
CALL pip-sync

REM Инициализация Alembic
CALL alembic init alembic

REM Создание первой ревизии
CALL alembic revision --autogenerate -m "First commit"

REM Применение миграций
CALL alembic upgrade head

echo Установка завершена.
pause