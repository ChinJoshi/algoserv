from fastapi import APIRouter

router = APIRouter()

@router.post("/find-peak-element", summary="Find Peak Element", description="""Time complexity: O(logn). Space Complexity: O(1). A peak element is an element that is strictly greater than its neighbors. If the array contains multiple peaks, the index to any one of the peaks will be returned. \nYou may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.""")
def findPeakElement(nums: list[int]) -> int:
    """
    intuition:
    interesting to me that it has to be done in log time
    obviously, this could be easily done in linear time

    a log time requirements automatically makes me thing of some kind of binary search
    it's a bit confuing to try and figure out the relation
    say for example we did a binary search style algo
    with a l and r pointer we'd look at the middle, but then how do we know which way to go
    Okay so I had to look up the solution, it is a bit unintuitive

    The essence of the logic is that, we can be sure that there is a solution on a side greater than the element we are looking at currently

    This is because a side which is greater than the element we are looking at can be one of two types of series:
    - It can be either monotonically increasing in the direction away from the current element or it can not be

    - If it is monotonically increasing, then we can be sure there is a peak element on that side since the edge element would be a peak element (since nums[-1] and nums[n] are -infinity)
    - If it is not monotonically increasing, then we can say that at some point there will be a dip in the series which implies that adjacent to the dip there will be a peak

    If both the left and right of an element are greater than the current element, it doesn't matter which one we choose to go towards, since we can say that there is a peak element on both sides

    """
    left = 0
    right = len(nums)-1
    while right != left:
        middle = int((right-left)/2) + left
        if nums[middle +1] > nums[middle]:
            left = middle+1
        elif nums[middle-1] > nums[middle]:
            right = middle
        else:
            return middle
    return right