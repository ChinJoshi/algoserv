from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/container-with-most-water",
    summary="Container With Most Water",
    description="Time Complexity: O(n). Space Complexity: O(1). \n\nUses a two-pointer approach to find the container that can hold the most water.",
)
def maxArea(height: list[int]) -> int:
    """
    intuition:

    well I can easily think of a O(n^2) solution
    for each line, we can multiply the difference between it's index and greater indices by the min(height[i],height[i+x])

    something I just noticed it that we can use two pointers by the following ovservation:
    if i increases, but the height[i] does not increase, it is impossible for the height[i+x] to be a part of the max water container unless it is
    height[i]*(x) greater than height[i]

    if we assume that the second container is greater than teh first container then we can say that everytime we encounter a container, it can only be the first container if height[right]-height[left] * (x-i) > height[i] * (x-i) for all 0 < x < i

    then we can do that forwards and backwards to get our max_area
    """
    max_area = 0
    left = 0
    right = len(height) - 1
    while right - left >= 1:
        area = (right - left) * min(height[right], height[left])
        max_area = max(max_area, area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area
