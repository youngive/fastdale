@echo off


REM Проверка наличия Python
echo Проверка наличия Python...
call python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не найден. Пожалуйста, загрузите его с сайта https://www.python.org/downloads/ и установите для работы FastDale.
    pause
    exit /b 1
)

echo Найден:
call python --version

REM Создание виртуального окружения
echo Создание виртуального окружения...
call python -m venv venv
if %errorlevel% neq 0 (
    echo Не удалось создать виртуальное окружение.
    pause
    exit /b 1
)
echo Виртуальное окружение создано.

REM Активация виртуального окружения
echo Активация виртуального окружения...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Не удалось активировать виртуальное окружение.
    pause
    exit /b 1
)
echo Виртуальное окружение активировано.

REM Обновление pip в виртуальном окружении
echo Обновление pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Не удалось обновить pip.
    pause
    exit /b 1
)
echo pip обновлен.

REM Установка pip-tools
echo Установка pip-tools...
call pip install pip-tools
if %errorlevel% neq 0 (
	call deactivate
	pause
	exit /b 1
)
echo pip-tools установлены.

REM Проверка наличия файла requirements.in
if not exist requirements.in (
    echo Файл requirements.in не найден. Создайте файл requirements.in с необходимыми зависимостями.
    deactivate
    pause
    exit /b 1
)

REM Генерация requirements.txt
echo Генерация requirements.txt...
call pip-compile
if %errorlevel% neq 0 (
    echo Не удалось сгенерировать requirements.txt.
    deactivate
    pause
    exit /b 1
)
echo requirements.txt сгенерирован.

REM Установка зависимостей из requirements.txt
echo Установка зависимостей из requirements.txt...
call pip-sync
if %errorlevel% neq 0 (
    echo Не удалось установить зависимости.
    deactivate
    pause
    exit /b 1
)
echo Зависимости установлены.

REM Проверка наличия Alembic
call where alembic >nul 2>&1
if %errorlevel% neq 0 (
    echo Alembic не установился. Установите Alembic для выполнения миграций.
    deactivate
    pause
    exit /b 1
)

REM Создание первой ревизии
echo Создание первой ревизии Alembic...
call alembic revision --autogenerate -m "First commit"
if %errorlevel% neq 0 (
    echo Не удалось создать первую ревизию Alembic.
    deactivate
    pause
    exit /b 1
)
echo Первая ревизия Alembic создана.

REM Применение миграций
echo Применение миграций Alembic...
call alembic downgrade base
if %errorlevel% neq 0 (
    echo Не удалось применить миграции Alembic.
    deactivate
    pause
    exit /b 1
)
echo Миграции Alembic применены.

REM Деактивация виртуального окружения
call venv\Scripts\deactivate.bat
echo Виртуальное окружение деактивировано.

echo Установка завершена.

pause