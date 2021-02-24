# Пульт охраны банка
<img src="https://dvmn.org/media/lessons/Django_1-st_LVl_003.png" alt="security" width="150"/>

Репозиторий с сайтом для урока «Пишем пульт охранника банка» курса [dvmn.org](https://dvmn.org/modules/)

Это внутренний репозиторий для сотрудника банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны можно подлючить к удалённой базе данных. Сайт выводит список сотрудников банка с активными картами доступа и список тех, кто сейчас находится в хранилище с указанием времени пребывания.

Также сайт позволяет посмотреть историю посещений хранилища для любого выбранного сотрудника. Для каждого посещения выводится дата, время и продолжительность пребывания в хранилище.

Если сотрудник находится в хранилище более часа, система отмечает данный визит как подозрительный.

## Установка и запуск сайта
Скачайте код:
```
git clone https://github.com/vitaliy-pavlenko/django-orm-watching-storage.git
```
Перейдите в каталог проекта:
```
cd django-orm-watching-storage
```
Установите зависимости в виртуальное окружение:
```
pip install -r requirements.txt
```
Создайте .env файл с конфигурацией
```
DB_SETTINGS=postgres://USER:PASSWORD@HOST:PORT/NAME
```
Запустите сайт:
```
python manage.py runserver 8000
```
Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Дополнительные настройки в .env
```
SECRET_KEY=YOUR_KEY
DEBUG=true
ALLOWED_HOSTS=host1,host2
```
