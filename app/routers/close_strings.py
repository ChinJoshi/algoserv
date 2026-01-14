from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/close-strings",
    summary="Close strings",
    description="""Time Complexity O(n). Space Complexity O(n). Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.""",
)
def closeStrings(self, word1: str, word2: str) -> bool:
    """
    intuition:

    okay so this does seem like an edit distance problem, but slightly simplified
    1. Given that we can swap any two characters, the order of characters does not matter, every string is really more like a set of characters
    2. Because of the "transform every existing character into another existing character" operation, we can say that as long as both strings have an equal number of unique characters and that for each unique character in one string, there is a unique character in the other string of the same amount, we can say that they are "close"

    Example:
    cabbba vs abbccc
    cabbba unique chars: (c,1) (a,2) (b,3)
    abbccc unique chars: (a,1) (b,2) (c,3)
    Since for each unique character in one string, there is a group of unique characters of the same amount in the other string, these strings are close

    Okay so it seems that "existing character" was actually only referring to existing chracters within the given string
    So what this now means is that the "counts" of unique characters still have to match across both strings, but we also need to check that if one char exists in one string, it also must exist in the other


    Overall runtime:O(n)
    """
    if len(word1) != len(word2):
        return False
    word1_dict = {}
    word2_dict = {}

    # O(n)
    for char in word1:
        if char in word1_dict:
            word1_dict[char] += 1
        else:
            word1_dict[char] = 1
    # O(n)
    for char in word2:
        if char in word2_dict:
            word2_dict[char] += 1
        else:
            word2_dict[char] = 1

    # O(n)
    if set(word1_dict.keys()) != set(word2_dict.keys()):
        return False

    # O(n)
    word2_multiset = {}
    for key in word2_dict.keys():
        if word2_dict[key] in word2_multiset:
            word2_multiset[word2_dict[key]] += 1
        else:
            word2_multiset[word2_dict[key]] = 1

    # O(n)
    for word1_unique_char in word1_dict.keys():
        if word1_dict[word1_unique_char] not in word2_multiset:
            return False
        else:
            word2_multiset[word1_dict[word1_unique_char]] -= 1
            if word2_multiset[word1_dict[word1_unique_char]] == 0:
                word2_multiset.pop(word1_dict[word1_unique_char])

    return True
