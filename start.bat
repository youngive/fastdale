@echo off

REM Проверка наличия Python
CALL python --version 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python не найден. Пожалуйста, загрузите его с сайта https://www.python.org/downloads/ и установите для работы FastDale.
    pause
    exit /b
)

REM Активация виртуального окружения
CALL venv\Scripts\activate

REM Запуск FastAPI сервера через uvicorn
CALL uvicorn main:app --reload --port 80
