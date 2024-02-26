from sqlite3                 import connect
from pydantic                import BaseModel
from typing                  import List, Optional
from fastapi                 import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app     = FastAPI()
conn    = connect('./db/store.db')
cursor  = conn.cursor()

# Настройки CORS, необходимы для разрешения конфликтов при запуске на одном хосте
app.add_middleware(
    CORSMiddleware,
    allow_origins     =["http://0.0.0.0:8000",],
    allow_credentials =True,
    allow_methods     =["*"],
    allow_headers     =["*"],
)


class Item(BaseModel):
    name       : str
    price      : float
    description: Optional[str] = None


# Info ->

@app.get("/items/", response_model=List[Item])
async def read_items() -> list:
    """
    Получение списка всех товаров
    :return: list: Список товаров
    """
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    return [{"id": item[0], "name": item[1], "description": item[2], "price": item[3]} for item in items]


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int) -> dict:
    """
    Получение информации о товаре по ID
    :param item_id: int: ID товара
    :return:       dict: Товар
    """
    cursor.execute("SELECT * FROM items WHERE id=?", (item_id,))
    item = cursor.fetchone()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"id": item[0], "name": item[1], "description": item[2], "price": item[3]}


# Create ->

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> dict:
    """
    Создание товара
    :param item: Item: Товар
    :return:     dict: Новый товар
    """
    cursor.execute('INSERT INTO items (name, description, price) VALUES (?, ?, ?)',
                   (item.name, item.description, item.price))
    item_id = cursor.lastrowid
    conn.commit()

    return {"id": item_id, **item.dict()}


# Update ->

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item) -> dict:
    """
    Изменение информации о товаре по ID
    :param item_id: int: ID товара
    :param item:   Item: Товар
    :return:       dict: Обновленный товар
    """
    cursor.execute("UPDATE items SET name=?, description=?, price=? WHERE id=?",
                   (item.name, item.description, item.price, item_id))
    conn.commit()

    return {"id": item_id, **item.dict()}


# Delete ->

@app.delete("/items/")
async def delete_all_items() -> dict:
    """
    Удаление всех товаров
    :return: dict: Сообщение об успешном удалении
    """
    cursor.execute("DELETE FROM items")
    conn.commit()

    return {"message": "All items deleted successfully"}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int) -> dict:
    """
    Удаление товара по ID
    :param item_id: int: ID товара
    :return:       dict: Сообщение об успешном удалении
    """
    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()

    return {"message": "Item deleted successfully"}
