def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    table = {data : i for i, data in enumerate(inorder)}

    def helper(preorder_i, preorder_j, inorder_i, inorder_j):
        if preorder_j <= preorder_i or inorder_j <= inorder_i:
            return None
        
        data = preorder[preorder_i]
        data_inorder_idx = table[data]
        left_inorder_j, right_inorder_i = data_inorder_idx, data_inorder_idx + 1
        left_preorder_i, left_preorder_j = preorder_i + 1, preorder_i + 1 + (data_inorder_idx - inorder_i)
        right_preorder_i, right_preorder_j = left_preorder_j, preorder_j
        return BinaryTreeNode(data, helper(left_preorder_i, left_preorder_j, inorder_i, left_inorder_j),
                            helper(right_preorder_i, right_preorder_j, right_inorder_i, inorder_j))
    
    return helper(0, len(preorder), 0, len(inorder))

