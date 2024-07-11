# FastDale

![FastDale Logo](assets/static/favicon-32x32.png)

**FastDale** - это порт на FastAPI open-source веб-сервера DD++ для аватар-чата, частично совместимого с клиентом игры «Шарарам»

# Плюсы FD
Из плюсов можно выделить:

1. **Лёгкую установку**. Для запуска на localhost теперь не нужно искать пути распаковки, всё работает в любом месте, а также «разжёвана» инструкция по инсталляции

2. **Поддержку**. Официальный репозиторий поддерживается временами, в то время как этот будет постоянно обновляться

3. **Модифицируемость**. В нашем коде реализована возможность быстрого изменения любых конфигов в директории `/assets/preferences`, которую не предоставляют в официальном репозитории 

# Требования
Для создания сервера с Дейзи Дейлом вам нужны

1. Adobe Media Server (для: [Windows x64](https://download.macromedia.com/pub/adobemediaserver/5_0_15/AdobeMediaServer5_x64.exe), [Linux x64](https://download.macromedia.com/pub/adobemediaserver/5_0_15/AdobeMediaServer5_x64.tar.gz)) (для 32-х битных систем Windows можно попробовать использовать [эту](https://download.macromedia.com/pub/flashmediaserver/updates/3_5_4/Windows/FlashMediaServer3.5.exe) версию)

2. ЯП [Python 3.x](https://www.python.org/downloads/)

3. Веб-сервер [FastDale](https://github.com/youngive/fastdale/archive/refs/heads/master.zip)

4. Пропатченный [новый](https://shararam.ru/base.swf) / оригинальный [старый](https://web.archive.org/web/20190201092446oe_/http://sharaball.ru/base.swf?v20191116) `base.swf`

5. СУБД [MariaDB](https://mariadb.org/download/) или [MySQL](https://dev.mysql.com/downloads/mysql/) (для хранения аккаунтов)

6. Инструмент для управления базами данных (в случае с [MariaDB](https://mariadb.org/download/) идёт в комплекте [HeidiSQL](https://www.heidisql.com/download.php))


# Установка для Linux

1. **Клонируем репозиторий**:
   ```sh
   git clone https://github.com/youngive/fastdale.git
   ```
2. **Переходим в созданную директорию**:
   ```sh
   cd fastdale
   ```
3. **Запускаем скрипт предварительной установки**:
   ```sh
   chmod +x pre-install.sh
   ./pre-install.sh
   ```
   Этот скрипт подтянет необходимые программные пакеты и настроит базу данных.

4. **Устанавливаем и запускаем Adobe Media Server (AMS)**:
   ```sh
   chmod +x ams-install.sh
   ./ams-install.sh
   ```
   Примите лицензионное соглашение, введя `y`, укажите серийный номер, создайте учетную запись администратора. Из портов `[1935,80]` согласитесь только с использованием `1935`. Не устанавливайте Apache.

5. **Настраиваем AMS**:
   перейдите в [консоль управления](https://ams.felder-group.com/ams_adminConsole.htm), войдите, используя ранее созданные учетные данные администратора и выберите инстанс `daisy` в левом нижнем углу.

6. **Запускаем основной установщик**:
   ```sh
   chmod +x install.sh
   ./install.sh
   ```
   Этот скрипт установит и настроит необходимые Python-зависимости.

7. **Запускаем веб-сервер FastDale**:
   ```sh
   chmod +x start.sh
   ./start.sh
   ```

8. **Откройте браузер и наслаждайтесь игрой на** `http://localhost`.

# Дополнительные шаги для запуска FD на VDS/VPS

9. **Настройка базы данных**:
   если у вашей базы данных есть пароль (рекомендуется установить), или она расположена на удалённом сервере, обновите данные в файле `.env`.

10. **Редактирование скрипта запуска**:
    внесите изменения в `start.sh`, указав в нем флаг `--host 0.0.0.0` для открытия доступа извне

11. **Обновление конфигурации RTMP**:
    в файле `/assets/preferences/servers.json` измените значение `RTMPUrl`, заменив `localhost` на ваш IP или домен.


# Лицензия

Делайте что хотите, но на ваш страх и риск.