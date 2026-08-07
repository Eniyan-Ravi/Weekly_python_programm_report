#practice
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


class ItemRequest(BaseModel):
    id: int
    name: str
    price: int


item = []


@router.post("/", status_code=status.HTTP_201_CREATED)
def enter_item(items: ItemRequest):

    data = items.model_dump()
    item.append(data)

    return data


@router.get("/")
def get_items():
    return item


@router.get("/{item_id}")
def get_item(item_id: int):

    for existing_item in item:

        if existing_item["id"] == item_id:
            return existing_item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@router.put("/{item_id}")
def update_item(item_id: int, ite: ItemRequest):

    for index, existing_item in enumerate(item):

        if existing_item["id"] == item_id:

            item[index] = {
                "id": ite.id,
                "name": ite.name,
                "price": ite.price
            }

            return item[index]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@router.delete("/{item_id}")
def delete_item(item_id: int):

    for existing_item in item:

        if existing_item["id"] == item_id:

            item.remove(existing_item)

            return {
                "message": "Item deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )
    