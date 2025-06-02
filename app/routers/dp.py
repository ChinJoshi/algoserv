from fastapi import APIRouter

router = APIRouter()


@router.post("/LCS")
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    """
    intuition:

    we have two strings text1 and text2

    SRTBOT
    subproblems could be that we take suffixes, prefixes, or substrings of both of the texts and find their LCS and then use that answer for a longer suffixes,prefix, or substring of the texts
    Say we had just the last letter of text1 and text2, we could easily find the LCS by checcking if they're equal
    now say we extend text1 by 1, now just as easily, we can find the LCS by checking if this new character is equal to the character in text2
    if it is equal, we can check if the previous letter was also equal, if it was, then we just set the LCS equal to the LCS of the previous text length's LCS
    if the previous wasn't also equal, then we can add one to the previous's count
    then once we have the first char in text one LCS with the entireity of text2, we can start extending text1 and reset text2 to 1 char
    now say we have two chars in text1, we can check the first char in text1 to the first char in text2
    if they're equal, then we can say LCS[i][j] = LCS[i-1][j-1] + 1
    if they're not equal we can say LCS[i][j] = max(LCS[i-1][j], LCS[i]][j-1])

    start from text1 as one char, go over all text2, then increment text1 length

    base cases: i==len(text1) -> 0, j==len(text2) -> 0
    i==len(text1)-1 or j==len(text2)-1 -> text1[i] == text2[j] ? 1 : 0

    LCS of text1 and text2 would be LCS[0][0]
    """
    LCS = [[None for x in range(len(text2)+1)] for x in range(len(text1)+1)]
    # set base case for i==len(text1) -> 0
    for i in range(len(text2)+1):
        LCS[-1][i] = 0
    # set base case for j==len(text2) -> 0
    for i in range(len(text1)+1):
        LCS[i][-1] = 0
    
    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1):
            if text1[i]==text2[j]:
                LCS[i][j] = LCS[i+1][j+1] + 1
            else:
                LCS[i][j] = max(LCS[i+1][j], LCS[i][j+1])
    return LCS[0][0]