from fastapi import APIRouter
from memory.memory_manager import get_memory

router = APIRouter()


@router.get("/memory")
def memory():

    return get_memory("demo_user")