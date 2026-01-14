from collections import deque

from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/reorder-routes-to-make-all-paths-lead-to-the-city-zero",
    summary="Reorder Routes to Make All Paths Lead to the City Zero",
    description="""There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

The task consists of reorienting some roads such that each city can visit the city 0. Returns the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.""",
)
def minReorder(n: int, connections: list[list[int]]) -> int:
    """
    intuition:
    Okay, so instincitvely the way I view thiw problem is to say that we should view the cities as all in a line.
    Somewhere across this line is the city 0.
    All cities to the left of 0 should have roads which point to the right and all cities to the right should have roads that point left.

    So the way I can view this problem is to say, first we should find 0 and it's neighbors.
    We can start by treating all roads as traversible in both directions and do a dfs.
    For each node we encounter we can mark the road we took there as one that needs to be flipped if it is inbound to the node, since we know that as we travel in the direction away from node 0, all roads should point toward it


    Now consider the case, that our graph forms a circle. This actually wouldn't be possible, since we have n nodes, but only n-1 roads. We need not worry about this case.

    I think it'll be easiest to solve this problem if we have an adjacency list first
    So we can create that with a dict
    Also put the connections list into a set so we can easily check if a node is inbound or outbound
    then once we have the adjacency list:
    start at node 0:
    go depth first and incremenet when we find roads in the wrong direction

    Time complexity: O(n)
    Space Complexity: O(n)
    """
    # O(n)
    connections_set = set((connection[0], connection[1]) for connection in connections)

    # O(n)
    adjacency_list = {}
    for connection in connections:
        if connection[0] not in adjacency_list:
            adjacency_list[connection[0]] = set([connection[1]])
        else:
            adjacency_list[connection[0]].add(connection[1])
        if connection[1] not in adjacency_list:
            adjacency_list[connection[1]] = set([connection[0]])
        else:
            adjacency_list[connection[1]].add(connection[0])

    flip_count = 0
    # O(n)
    nodes = deque(zip(adjacency_list[0], (0 for x in range(len(adjacency_list[0])))))

    # O(n)
    while len(nodes) > 0:
        node, prev_node = nodes.pop()
        if (node, prev_node) not in connections_set:
            flip_count += 1
        adjacency_list[node].remove(prev_node)
        for new_node in adjacency_list[node]:
            nodes.append((new_node, node))
    return flip_count
