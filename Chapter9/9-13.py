def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def helper(preorder_iter):
        data = next(preorder_iter)
        if data is None:
            return None
        left_subtree = helper(preorder_iter)
        right_subtree = helper(preorder_iter)
        return BinaryTreeNode(data, left_subtree, right_subtree)

    return helper(iter(preorder))

