from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/arithmetic-parenthesis",
    summary="Arithmetic Parenthesis Optimization",
    description="Time Complexity: O(n³). Space Complexity: O(n²). \n\nFinds the optimal way to add parentheses to an arithmetic expression to maximize its value.",
)
def arithmetic_parenthesis(operators: list[str], nums: list[int]):
    """
    intuition:

    if I have a list of operators a_i,...,a_n-1, where a_i is either + or *
    and a list of numbers v_i,...,v_n, where v_i is a positive integer
    to form an expression v_i a_i v_i+1 a_i+1 .... a_n-1 v_n
    example 7+4*3+5

    how can I add paranthesis to this expression to form the greatest possible result?
    in the example it's (7+4) * (3+5)


    we can think about the solution to this problem as a binary tree where each node is the left or right part of an operation
    well then the root of this tree would be the operation that happens in the middle of the expression
    and then all the leaf nodes are values v_n

    if we guess that middle operation, or the root of the tree, then we can find what the max value would be in that case by checking what the max value we can get from the two subtrees is, which is just a smaller version of the same problem since the subtrees are also binary trees with an operation as their root node.

    as a base case, we can start with all the trees where there is only one node, i.e., the best value we can extract from it is just the value of the root itself
    and then for all trees with two values, which would be a tree with three nodes, we can say the value will be whatever the result of the two values  with the operation that is between them applied (the operation between them would be the root node)

    and then once we get to the substrings with three values, we have to start guessing what this middle operation might be. and each one of those "guesses" results in a unique tree, where each left subtree and each right subtree would be a problem we already solved since each of those subtrees is smaller than our current tree and we have solved all smaller subtrees once we get to that point.

    so the relation there would be
    MR(i,j) is the max value we can get by paranthesizing the substring [i:j]
    MR(i,j) = max{MR(i,k) a_k-1 MR(k,j) for all i<k<=j}

    and then our answer would be MR(0,n+1)

    operators=["+","x","+"],nums=[7,4,3,5]

    """
    MR = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]

    for x in MR:
        print(x)
    print("----")
    # base cases
    # length 1
    for i in range(len(nums)):
        MR[i][i + 1] = nums[i]
    # length 2
    for i in range(len(operators)):
        if operators[i] == "+":
            MR[i][i + 2] = nums[i] + nums[i + 1]
        elif operators[i] == "x":
            MR[i][i + 2] = nums[i] * nums[i + 1]

    for x in MR:
        print(x)
    print("----")

    l = 3
    while l <= len(nums):
        print(f"l: {l}")
        i = 0
        while i + l <= len(nums):
            print(f"i: {i}")
            max_value = -1
            k = i + 1
            while k < i + l:
                print(f"k: {k}")
                if operators[k - 1] == "+":
                    value = MR[i][k] + MR[k][i + l]
                    if value > max_value:
                        max_value = value
                elif operators[k - 1] == "x":
                    value = MR[i][k] * MR[k][i + l]
                    if value > max_value:
                        max_value = value
                k += 1
            MR[i][i + l] = max_value
            i += 1
        l += 1
    return MR[0][len(nums)]
