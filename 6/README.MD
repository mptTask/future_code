## ENPOINT в работе #6:
- **Добавить кота:** `POST /cats/` - Добавить нового кота в приют.
- **Просмотреть котов:** `GET /cats/` - Просмотреть всех котов в приюте.
- **Обновить кота:** `PUT /cats/{cat_id}/` - Обновить информацию о конкретном коте.
- **Удалить кота:** `DELETE /cats/{cat_id}/` - Удалить кота из приюта.
- **Найти кота по имени:** `GET /cats/find/?name={name}` - Найти котов по именам.

## Как запустить

1. Установите необходимые зависимости:
    ```bash
    pip install fastapi uvicorn
    ```

2. Запустите сервер FastAPI:
    ```bash
    uvicorn main:app --reload
    ```

3. Получите доступ к Swagger UI для взаимодействия с API:
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

----

## Endpoints in Action #6:
- **Add Cat:** `POST /cats/` - Add a new cat to the shelter.
- **View Cats:** `GET /cats/` - View all cats in the shelter.
- **Update Cat:** `PUT /cats/{cat_id}/` - Update information about a specific cat.
- **Delete Cat:** `DELETE /cats/{cat_id}/` - Remove a cat from the shelter.
- **Find Cat by Name:** `GET /cats/find/?name={name}` - Find cats by their names.

## How to Run

1. Install the required dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

2. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

3. Access Swagger UI to interact with the API:
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
