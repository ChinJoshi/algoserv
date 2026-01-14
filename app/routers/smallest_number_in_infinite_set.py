import heapq

from fastapi import APIRouter

router = APIRouter()


class SmallestInfiniteSet:
    """
    intuition:
    obviously we can't store an infinte set, but we can easily store the smallest value remaining in an infinite of positive numbers
    and we can handle popSmallest() quite simply with this scheme, simply return and increment our smallest value var.
    when. we introduce addBack(), which adds a positive number back to the set if it's not already in it, we'd have to keep track of a little bit more
    we'd need to keep track of the set of values lesser than when the infinite set becomes unbroken, the smallest value in this set, and the point at which the set becomes unbroken

    we'd need the smallest in order to popSmallest()
    we'd need the point at which the set becomes unbroken in order to evaluate if the number being added back is in the infinite set
    we'd need the set of values lesser than the point of unbrokenness to determine whether the addBack() value is contained in the infinite set

    for the set, we can use the set type
    for storing the smallest value in the set we can use a minheap
    keep track of the smallest value in the set
    the set/heap will contain values in the set, and the above greatest value in the heap will be unborken infinite positive values

    heap build is O(n) time

    if we use the meme from the contraints that 1 <= num <= 1000 and that At most 1000 calls will be made in total to popSmallest and addBack:
        then we can just use a set and for pop smallest we seasch for and take out the smallest value
        for add back we can just add to the set

    add a min heap for popSmallest

    okay so in the end all we needed:
    a minheap to quickly find the smallest value in the set
    a set to hold values we know are in the infinite set
    a starting_size value to initialize the heap and set with

    we use the starting_size to also tell us what the largest value in the set and heap is at all times
    that makes it very easy to reject addBack calls and also to let us know what to push into the set/heap when it is emptied by many calls to popSmallest. This is since we know the value at starting_size was the greatest value in the set/heap and since we reject any pushes to the set that are greater than starting_size, we maintain this property for the entireiety of the program.


    """

    def __init__(self):
        # starting size can be any positive integer technically
        starting_size = 1
        self.infinite_min_heap = [x for x in range(1, starting_size + 1)]
        heapq.heapify(self.infinite_min_heap)
        self.infinite_set = set(self.infinite_min_heap)
        self.next_value = starting_size + 1

    def popSmallest(self) -> int:
        min_val = heapq.heappop(self.infinite_min_heap)
        self.infinite_set.remove(min_val)
        if len(self.infinite_set) == 0:
            self.infinite_set.add(self.next_value)
            heapq.heappush(self.infinite_min_heap, self.next_value)
            self.next_value += 1
        return min_val

    def addBack(self, num: int) -> None:
        if num not in self.infinite_set and num < self.next_value:
            self.infinite_set.add(num)
            heapq.heappush(self.infinite_min_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


"""
example call would look like:
function_calls: ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
operands: [[], [2], [], [], [], [1], [], [], []]
"""


@router.post(
    "/smallest-infinite-number-in-set",
    summary="Smallest Number in Infinite Set",
    description="Time Complexity: O(log n) per operation. Space Complexity: O(n). \n\nImplements a data structure that keeps track of the smallest number in an infinite set with add and pop operations.",
)
def smallestIniniteSet(
    function_calls: list[str], operands: list[int]
) -> list[int | None]:
    obj = None
    ret_val = []
    for index, function_call in enumerate(function_calls):
        if function_call == "SmallestInfiniteSet":
            obj = SmallestInfiniteSet()
        if function_call == "popSmallest":
            ret_val.append(obj.popSmallest())
        elif function_call == "addBack":
            ret_val.append(None)
            obj.addBack(operands[index])
