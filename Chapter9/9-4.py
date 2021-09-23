def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = 0
        while node is not None:
            depth, node = depth + 1, node.parent
        return depth
    n0_depth, n1_depth = get_depth(node0), get_depth(node1)
    if n1_depth > n0_depth:
        node0, node1 = node1, node0
    for i in range(abs(n0_depth - n1_depth)):
        node0 = node0.parent
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0

