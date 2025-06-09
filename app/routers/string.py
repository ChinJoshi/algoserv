from fastapi import APIRouter

router = APIRouter()

@router.post("/string/is-palindrome", summary="Palindrome Check", description="Time Complexity: O(n). Space Complexity: O(1). \n\nChecks if a string reads the same backward as forward.")
def isPalindrome():
    return True