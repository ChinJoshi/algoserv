from fastapi import APIRouter

router = APIRouter()

@router.post("/is-palindrome", summary="Palindrome Check", description="Time Complexity: O(n). Space Complexity: O(1). \n\nChecks if a string reads the same backward as forward.")
def isPalindrome(word: str):
    reversed_word = reversed(word)
    for idx,letter in enumerate(reversed_word):
        if letter != word[idx]:
            return False
    return True
    