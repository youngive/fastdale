@echo off


REM Активация виртуального окружения
echo Активация виртуального окружения...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Не удалось активировать виртуальное окружение. Убедитесь, что путь к 'venv\Scripts\activate' правильный.
    pause
    exit /b 1
)
echo Виртуальное окружение активировано.

REM Запуск FastAPI сервера через uvicorn
echo Запуск FastAPI сервера через uvicorn...
CALL uvicorn main:app --reload --port 80
if %errorlevel% neq 0 (
    echo Не удалось запустить сервер FastAPI. Проверьте логи для получения дополнительной информации.
    pause
    exit /b 1
)
echo Сервер остановлен!

pause
