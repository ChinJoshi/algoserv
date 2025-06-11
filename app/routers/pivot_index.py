from fastapi import APIRouter

router = APIRouter()

@router.post("/pivot-index", summary="Pivot Index", description="Time Complexity O(n). Space Complexity O(1). Given an array nums, calculates the leftmost pivot index. A pivot index is an index in the array where the sum of all points to the left of it and equal to the sum of all points to the right of it.")
def pivotIndex( nums: list[int]) -> int:
    """
    intuition:
    We can use a pointer and increment it along the array from left to right
    Every time we increment it we add what it was prev pointing at to the left sum and subtract what it points to now from the right sum

    Once the left and right sums are equal, we return the index
    if the index reaches the right edge of the array without a pivot, return -1

    """
    pointer = 0
    left_sum = 0
    right_sum = sum(nums[1:])
    if left_sum == right_sum:
        return 0
    pointer += 1
    
    while pointer < len(nums):
        left_sum += nums[pointer-1]
        right_sum -= nums[pointer]
        if left_sum == right_sum:
            return pointer
        pointer += 1
    
    return -1