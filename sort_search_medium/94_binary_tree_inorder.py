class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #1 98p
        result = []
        
        def inorder_recursive(root, result):
            if root is None:
                return
            
            inorder_recursive(root.left, result)
            result.append(root.val)
            inorder_recursive(root.right, result)
            
        inorder_recursive(root, result)
        
        return result
