from fastapi import APIRouter
from collections import deque
router = APIRouter()


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_tree(arr):
    # Helper function to construct the tree
    def helper(i):
        if i >= len(arr) or arr[i] is None:
            return None
        node = TreeNode(arr[i])
        node.left = helper(2*i + 1)
        node.right = helper(2*i + 2)
        return node
    
    return helper(0)


@router.post("/leaf-similar-trees", summary="Leaf Similar Trees", description="Time Complexity O(V+E). Space Complexity O(V). Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence. Two binary trees are considered leaf-similar if their leaf value sequence is the same. \n\n binary trees should be input in array form")
def leafSimilar(root1: list[int], root2: list[int]) -> bool:
    root1 = array_to_tree(root1)
    root2 = array_to_tree(root2)

    def dfs_get_leaves(root):
        # DFS, for dfs we would want to use a stack so that the most recently discovered nodes get traveled to next (LIFO)
        stack = deque()
        tree_leaves = []
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            if node.left is None and node.right is None:
                tree_leaves.append(node.val)
        # print(tree_leaves)
        return tree_leaves
    
    tree1_leaves = dfs_get_leaves(root1)
    tree2_leaves = dfs_get_leaves(root2)

    return tree1_leaves == tree2_leaves