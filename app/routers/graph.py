from fastapi import APIRouter

router = APIRouter()

@router.post("/graph/BFS", summary="Breadth-First Search", description="Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges. Space Complexity: O(V). \n\nImplements breadth-first search traversal for graphs.")
def BFS():
    return "BFS test"