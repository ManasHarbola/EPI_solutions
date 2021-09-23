def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def is_balanced_helper(currNode):
        #base case: null node: is balanced and bf is 0
        if currNode is None:
            return (True, 0)

        left_result = is_balanced_helper(currNode.left)
        if not left_result[0]:
            return (False, 0)
        right_result = is_balanced_helper(currNode.right)
        if not right_result[0]:
            return (False, 0)
        
        bf = left_result[1] - right_result[1]
        return (abs(bf) < 2, max(left_result[1], right_result[1]) + 1)
    
    return is_balanced_helper(tree)[0]

