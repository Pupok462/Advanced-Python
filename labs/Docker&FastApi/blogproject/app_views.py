from fastapi import APIRouter

router = APIRouter(tags=["Items"], prefix="/items")


@router.get("")
def return_items():
    return [{"item_id": 1}]


@router.get("/{item_id}")
def return_index(item_id: int):
    return {"index": item_id}


@router.post("/info")
def post_data(data: dict):
    return {"data": data}
