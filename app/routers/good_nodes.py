from fastapi import APIRouter
from collections import deque

router = APIRouter()

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_tree(arr):
    def helper(i):
        if i >= len(arr) or arr[i] is None:
            return None
        node = TreeNode(arr[i])
        node.left = helper(2*i + 1)
        node.right = helper(2*i + 2)
        return node
    
    return helper(0)

@router.post("/good-nodes", summary="Count Good Nodes in Binary Tree", description="Time Complexity O(V). Space Complexity O(V). Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Returns the number of good nodes in the binary tree. Binary tree should be input in array form.")
def goodNodes(root: list[int]) -> int:
    """
    intuition:
    this is a fun one!

    Okay so we need to check for each node in the path, if all the nodes leading to it from the root are less than it's value
    Naively, we could simply hold the set of elements along the path for a node while performing a bfs or a dfs
    That would end up with a time complexity along the lines of O(V * (V+E)) since at each node, we'd have to potentially check the value of all other nodes, since they could be along the path.
    More easily, we could just hold the largest value that we have encountered thus far and compare it to the current value, marking a node good if it is larger than the largest value we have encountered
    I think a BFS would be simpler to use here, but really we could use dfs to, it doesn't matter

    Something like

    # second value is largest value encountered thus far
    good = 0
    queue = [(root,-inf)]
    while queue not empty:
        node,value = queue.popleft()
        if node.value > value:
            good += 1
        if node.left:
            queue.append(node.left,max(node.value,value))
        if node.right:
            queue.append(node.right,max(node.value,value))
    """
    root_node = array_to_tree(root)
    
    good = 0
    queue = deque([(root_node, -(10**4))])
    while len(queue) > 0:
        node, val = queue.popleft()
        if node.val >= val:
            good += 1
        if node.left:
            queue.append((node.left, max(node.val, val)))
        if node.right:
            queue.append((node.right, max(node.val, val)))
    return good