from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/unique-occurences",
    summary="Unique Occurences",
    description="Given an array of integers arr, returns true if the number of occurrences of each value in the array is unique or false otherwise.",
)
def uniqueOccurrences(arr: list[int]) -> bool:
    unique_occurences = {}
    for number in arr:
        if number not in unique_occurences:
            unique_occurences[number] = 0
        else:
            unique_occurences[number] += 1
    values_set = set()
    for value in unique_occurences.values():
        if value in values_set:
            return False
        else:
            values_set.add(value)
    return True
