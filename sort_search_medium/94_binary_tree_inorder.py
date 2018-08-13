class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        """
        #1 54p
        result = []
        
        def inorder_recursive(root, result):
            if root is None:
                return
            
            inorder_recursive(root.left, result)
            result.append(root.val)
            inorder_recursive(root.right, result)
            
        inorder_recursive(root, result)
        
        return result
        """
        
        #2 75p
        # Iterative
        stack = []
        result = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
                
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
                
        return result
