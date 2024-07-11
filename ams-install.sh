#!/bin/bash

# Установка Adobe Media Server
install_adobe_media_server() {
    echo "Скачивание Adobe Media Server..."
    wget https://download.macromedia.com/pub/adobemediaserver/5_0_15/AdobeMediaServer5_x64.tar.gz -O AdobeMediaServer5_x64.tar.gz

    echo "Распаковка архива..."
    tar -xzvf AdobeMediaServer5_x64.tar.gz

    cd AMS_5_0_15_r5004

    echo "Копирование libasneu.so.1..."
    sudo cp libasneu.so.1 /libasneu.so.1

    echo "Создание символической ссылки для libcap.so.2..."
    sudo ln -s /lib/x86_64-linux-gnu/libcap.so.2 /lib/libcap.so.2

    echo "Установка libnspr4..."
    sudo apt update
    sudo apt install -y libnspr4

    echo "Установка Adobe Media Server..."
    sudo ./installAMS
}

# Загрузка и перемещение папки daisy
move_daisy_folder() {
    echo "Скачивание репозитория ddplusplus..."
    git clone https://github.com/123jjck/ddplusplus.git

    echo "Перемещение папки daisy..."
    sudo mv ddplusplus/daisy /opt/adobe/ams/applications/
}

# Запуск Adobe Media Server
start_adobe_media_server() {
    cd /opt/adobe/ams
    echo "Запуск adminserver..."
    sudo ./adminserver start

    echo "Запуск сервера..."
    sudo ./server start
}

# Основной процесс установки
main() {
    install_adobe_media_server
    move_daisy_folder
    start_adobe_media_server
}

# Выполнение основного процесса
main