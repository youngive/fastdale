#!/bin/bash

DB_NAME="daisy"

# Установка MariaDB
install_mariadb() {
    echo "Установка MariaDB..."
    sudo apt update
    sudo apt install -y mariadb-server

    # Запуск MariaDB
    sudo systemctl start mariadb
    sudo systemctl enable mariadb

    echo "Настройка MariaDB и сброс пароля root..."

    # Сброс пароля root
    sudo mysql -u root <<EOF
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY '';
EOF

    echo "Сброс пароля root завершен."

    echo "Создание базы данных $DB_NAME..."
    sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS $DB_NAME"

    echo "Скачивание дампа базы данных..."
    wget -O dump.sql https://raw.githubusercontent.com/123jjck/ddplusplus/master/dump.sql

    echo "Импорт базы данных из dump.sql в $DB_NAME..."

    # Импорт дампа базы данных
    sudo mysql -u root $DB_NAME < dump.sql

    echo "Импорт базы данных завершен."
}

# Установка Python
install_python() {
    echo "Проверка наличия Python..."
    if ! command -v python &> /dev/null; then
        echo "Python не найден. Проверка наличия Python 3..."
        if command -v python3 &> /dev/null; then
            echo "Python 3 найден. Создание символической ссылки..."
            sudo ln -s $(command -v python3) /usr/bin/python
            echo "Символическая ссылка на Python 3 создана."
        else
            echo "Python 3 не найден. Установка Python 3..."
            sudo apt update
            sudo apt install -y python3
            sudo ln -s $(command -v python3) /usr/bin/python
            echo "Python 3 установлен и символическая ссылка создана."
        fi
    else
        echo "Python уже установлен."
    fi
}

# Установка python-venv
install_python_venv() {
    echo "Проверка установки python3-venv..."
    if ! dpkg -l | grep -qw python3-venv; then
        echo "Установка python3-venv..."
        sudo apt update
        sudo apt install -y python3-venv
    else
        echo "python3-venv уже установлен."
    fi
}

# Основной процесс установки
main() {
    install_mariadb
    install_python
    install_python_venv
}

# Выполнение основного процесса
main