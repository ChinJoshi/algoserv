from fastapi import APIRouter

router = APIRouter()


@router.post("max-vowels",summary="max vowels",description="Time Complexity: O(n). Space Complexity: O(1). \n\nGiven some substring length k and lowercase string s, determines the number of vowels in the k-length substring of s which contains the most vowels")
def maxVowels(s: str, k: int) -> int:
    """
    intuition:

    I think this is pretty straightforward using a sliding window where we have a left and right pointer

    we'll iterate over the inital window to get teh number fo vowels
    for each slide of the window:
    check the left pointer to see if the value left behind was vowel, if so subtract one from vowel count
    check the right pointer to see if the value being included is now a vowel, if so add to the vowel count
    """
    # vowel set
    vowel_set = set(['a','e','i','o','u'])
    # iterate over the first window
    left = 0
    right = k-1
    vowel_count = 0

    for char in s[:k]:
        if char in vowel_set:
            vowel_count += 1
    max_vowel_count = vowel_count

    while right < len(s)-1:
        if s[left] in vowel_set:
            vowel_count-=1
        left+= 1
        right += 1
        if s[right] in vowel_set:
            vowel_count += 1
        max_vowel_count = max(max_vowel_count,vowel_count)
    return max_vowel_count

