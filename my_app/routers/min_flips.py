from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/min-flips",
    summary="Minimum Flips",
    description="Minimum Flips to Make a OR b Equal to c",
)
def minFlips(a: int, b: int, c: int) -> int:
    # O(log(max(a,b,c)))
    a = list(bin(a))[2:]
    b = list(bin(b))[2:]
    c = list(bin(c))[2:]

    # # O(log(max(a,b,c)))
    max_len = max([len(a), len(b), len(c)])
    for bit_string in [a, b, c]:
        bit_string.reverse()
        for i in range(max_len):
            if i > len(bit_string) - 1:
                bit_string.append("0")
        bit_string.reverse()
        print(bit_string)

    # O(log(max(a,b,c)))
    flip_counter = 0
    for i in range(max_len):
        if c[i] == "1":
            if a[i] != "1" and b[i] != "1":
                flip_counter += 1
        else:
            if a[i] != "0":
                flip_counter += 1
            if b[i] != "0":
                flip_counter += 1
    return flip_counter
