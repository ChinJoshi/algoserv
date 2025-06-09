from fastapi import APIRouter

router = APIRouter()

@router.post("/string-compression", summary="String Compression", description="Time Complexity: O(n). Space Complexity: O(1). \n\nCompresses a string by replacing consecutive repeated characters with the character followed by the count of repetitions.")
def compress(chars: list[str]) -> int:
    """
    intuition:
    seems like a pretty fit problem for a two pointer approach


    we'll have one pointer that points to where we're gonna write to (the cursor)
    another pointer will be the one scanning the array, and will count consecutive chars

    """
    left = 0
    right = 1
    prev_right_val = chars[left]
    counter = 1
    while right < len(chars):
        if chars[right] != prev_right_val:
            chars[left] = prev_right_val
            left += 1
            if counter > 1:
                for char in str(counter):
                    chars[left] = char
                    left += 1
            counter = 0
        prev_right_val = chars[right]
        right += 1
        counter += 1
        # print(f'left: {left}')
        # print(f'right: {right}')
        # print(f'counter: {counter}')
        # print(f'prev_right_val: {prev_right_val}')
        # print(f'chars: {chars[:left]}')
        # print("################################")
    chars[left] = chars[-1]
    if counter > 1:
        for char in str(counter):
            chars[left+1] = char
            left += 1
        # chars[left+1] = str(counter)
        # left += 1
    return left+1