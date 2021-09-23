def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    traversal = []
    currNode = tree
    prevNode = None

    while currNode:
        if prevNode is currNode.parent:
            if currNode.left:
                prevNode = currNode
                currNode = currNode.left
            else:
                traversal.append(currNode.data)
                prevNode = currNode
                currNode = currNode.right if currNode.right else currNode.parent
        elif prevNode is currNode.left:
            traversal.append(currNode.data)
            prevNode = currNode
            currNode = currNode.right if currNode.right else currNode.parent
        elif prevNode is currNode.right:
            prevNode = currNode
            currNode = currNode.parent
        
    return traversal

