class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(node, result):
            if node:
                # Traverse left subtree
                helper(node.left, result)
                # Visit root
                result.append(node.val)
                # Traverse right subtree
                helper(node.right, result)
        
        result = []
        helper(root, result)
        return result
