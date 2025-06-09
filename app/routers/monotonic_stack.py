from fastapi import APIRouter
from collections import deque

router = APIRouter()

@router.post("/daily-temperatures", summary="Daily Temperatures", description="Time Complexity: O(n). Space Complexity: O(n). \n\nUses a monotonic stack to find the number of days until a warmer temperature for each day.")
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    intuition:

    so the first simple thought I have at a solution would be to take an O(N^2) approach
    for each element in the array, we can serach all proceeding elements until we find a greater element

    I think we may be able to do something a bit better than that
    Say we put all of the elements into a stack where the first day is on the top of the stack
    then we can pop off the stack
    check the top of the stack
    if it's greater than what I just popped, answer is 1
    else, increment the answer by 1

    Say we have one stack
    We push each element one by one
    When an element that is being pushed on the stack is greater than the current top of the stack, we pop the top element off and take the difference of their indexes until we reach a point where the element being added is no longer greater than the top of the stack
    the difference between the indexes is the number of days you would have to wait
    Since each element is pushed on the stack once O(N) and popped off the stack once O(N), the running time is O(N) + O(N) = O(N)
    """
    output = [0 for x in range(len(temperatures))]
    stack = deque()
    for index, temperature in enumerate(temperatures):
        while len(stack) >= 1 and temperature > stack[-1][0]:
            output[stack[-1][1]] = index - stack[-1][1]
            stack.pop()
        stack.append([temperature,index])
    return output