from fastapi import APIRouter

router = APIRouter()

@router.post("/graph/BFS")
def BFS():
    return "BFS test"