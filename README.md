## Проект «API для Yatube»


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/LeschikovaTatyana/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

```
cd yatube_api
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

#### Получить Токен можно по адресу:
http://127.0.0.1:8000/api/v1/jwt/create/

Получить, создать, изменить пост:
http://127.0.0.1:8000/api/v1/posts/

Получить, создать, изменить коментарий:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Список групп:
http://127.0.0.1:8000/api/v1/groups/

Подписка на автора:
http://127.0.0.1:8000/api/v1/groups/

