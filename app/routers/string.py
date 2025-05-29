from fastapi import APIRouter

router = APIRouter()

@router.post("/string/is-palindrome")
def isPalindrome():
    return True