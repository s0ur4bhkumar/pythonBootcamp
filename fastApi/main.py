import asyncio
from enum import Enum
from typing import Annotated, Dict, List

from fastapi import FastAPI, Query
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


# root
@app.get("/")
async def root():
    return {"message": "hello world"}


# path params
# @app.get("/items/{item_id}")
# def get_name(item_id: int):
#     return {"item_id": item_id}


# fixed values
@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
    if model_name == "alexnet":
        return {"model_name": model_name, "message": "deep learning for the win"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "leCNN all the images"}
    return {"model_name": model_name, "message": "have some residuals"}


# file path
@app.get("/file/{file_path:path}")
def get_path(file_path: str):
    return file_path


# querry parameteres
fake_items_db: List[Dict[str, str]] = [
    {"item_name": "foo"},
    {"item_name": "bar"},
    {"item_name": "baz"},
]


# @app.get("/items/")
# def get_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# Request Body


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# @app.post("/items/")
# def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# annotations


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query(max_length=4)] = None):
    results: dict[str, list[dict[str, str]] | str | list[str]] = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]
    }
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":

    async def task1():
        print("Task 1 started")
        await asyncio.sleep(3)
        print("Task 1 finished")

    async def task2():
        print("Task 2 started")
        await asyncio.sleep(1)
        print("Task 2 finished")

    async def main():
        await asyncio.gather(task1(), task2())  # Runs both tasks together

    asyncio.run(main())
