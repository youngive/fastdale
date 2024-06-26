# FastDale

![FastDale Logo](assets/static/favicon-32x32.png)

**FastDale** - это порт на FastAPI open-source веб-сервера DD++ для аватар-чата, частично совместимого с клиентом игры «Шарарам»

# Плюсы FastDale
Из плюсов можно выделить:

1. **Лёгкую установку**. Для запуска на localhost теперь не нужно искать пути распаковки, всё работает в любом месте, а также «разжёвана» инструкция по инсталляции

2. **Поддержку**. Официальный репозиторий поддерживается временами, в то время как этот будет постоянно обновляться

3. **Модифицируемость**. В нашем коде реализована возможность быстрого изменения любых конфигов в директории `/assets/preferences`, которую не предоставляют в официальном репозитории 

# Требования
Для создания сервера с Дейзи Дейлом вам нужны

1. Adobe Media Server (для: [Windows x64](https://download.macromedia.com/pub/adobemediaserver/5_0_15/AdobeMediaServer5_x64.exe), [Linux x64](https://download.macromedia.com/pub/adobemediaserver/5_0_15/AdobeMediaServer5_x64.tar.gz)) (для 32-х битных систем Windows можно попробовать использовать [эту](https://download.macromedia.com/pub/flashmediaserver/updates/3_5_4/Windows/FlashMediaServer3.5.exe) версию), apache **не** ставим и **убираем** использовние порта 80)

2. Последняя версия [Python](https://www.python.org/downloads/)

3. [FastDale](https://github.com/youngive/fastdale/releases)

4. Патч клиента Шарарама `base.swf`

5. [MariaDB](https://mariadb.org/download/) или [MySQL](https://dev.mysql.com/downloads/mysql/) (для хранения аккаунтов)

6. [HeidiSQL](https://www.heidisql.com/download.php) (в случае с [MariaDB](https://mariadb.org/download/) идёт в комплекте)

# Установка (Windows)

1. Первым делом необходимо перенести папку [daisy](https://github.com/123jjck/ddplusplus/tree/master/daisy) из репозитория DD++ в папку `applications` в корне Adobe Media Server.
2. В HeidiSQL создаём базу данных под названием `daisy` с кодировкой `utf8mb4_general_ci` и импортируем туда [dump.sql](https://raw.githubusercontent.com/123jjck/ddplusplus/master/dump.sql)
3. Запускаем Adobe Media Server и Adobe Media Administration Server
4. Клонируем / распаковываем репозиторий в удобное для вас место
5. Переходим в созданную директорию
6. Заливаем пропатченный `base.swf` на веб-сервер в папку `/assets/static`
7. Открываем `install.bat` для установки зависимостей
8. Открываем `start.bat` для запуска FastDale
9. Теперь вы можете зайти на `localhost` и наслаждаться игрой

# Дополнительные шаги для запуска сервера на VDS/VPS
10. Если на вашей базе данных стоит пароль, либо она расположена на удалённом сервере - меняем данные от базы данных в файле `.env`
11. Укажите в «батнике» `start.bat` флаг `--host 0.0.0.0` для открытия доступа извне

# Лицензия

Делайте что хотите, но на ваш страх и риск.