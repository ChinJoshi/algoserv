from fastapi import APIRouter

router = APIRouter()

@router.post("/single-number", summary="Single Number", description="Given a non-empty array of integers nums, every element appears twice except for one. This endpoint retuns that single one.")
def singleNumber(nums: list[int]) -> int:
    """
    intuition:
    a naive approach could be to iterate over the entire array for every element in the array, checking to see if it has a repeat
    That would be O(n^2) runtime so it isn't the ultimate solution

    Another naive solution could be to hold an dictionary with keys from -3*10^4 to 3*10^4 and for each have the value be the number of occurences, then check if any have 1 occurence
    That would be O(N) tc and O(1) space complexity, though the space used is large

    I looked at the hint and it told me to think about the XOR operator's properties. XOR is 1 exclusively when one of the operands is 1. 

    Okay so I looked up the solution to the problem and it makes a lot of sense to me now. 
    Basically, since we know that there will always be 2 of each number that is not the single number, we know that when we XOR together every number that is not the single number, we will get 0. So now we have this 0 from XORing all the doubled values, when we XOR that with the single value, we'll then get the single value itself. So this means that if we just XOR all values in the list, the result will be the single value.

    Another way to think of this would be to say that we know when you XOR an even number of 1s together you get a 0, and with an odd number of 1s you get a 0. We know that in each columnn of the XOR, the columns with an odd number of 1's are the columns where the single value is 1. Thus the resultant will be equivelant to the single value.
    """
    result = 0
    for num in nums:
        result ^= num
    return result