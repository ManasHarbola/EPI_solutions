def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    from collections import deque
    traversal = list()
    if tree is None:
        return traversal
    queue = deque()
    queue.append(tree)
    while queue:
        curr_level, queueSize = list(), len(queue)
        for i in range(queueSize):
            curr = queue.popleft()
            curr_level.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        traversal.append(curr_level)

    return traversal

