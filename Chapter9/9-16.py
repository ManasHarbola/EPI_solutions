def construct_right_sibling(tree: BinaryTreeNode) -> None:
    '''
    from collections import deque
    if tree is None:
        return
    queue = deque()
    queue.append(tree)
    while queue:
        size = len(queue)
        while size:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if size > 1:
                node.next = queue[0]
            size -= 1
    '''
    def helper(node):
        while node and node.left:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            node = node.next
    while tree and tree.left:
        helper(tree)
        tree = tree.left

