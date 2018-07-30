class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #1 70p
        # Recursive
        
        return self.dfs(root, 0)
        
        
    def dfs(self, node, result):
        
        if not node:
            return result
        
        return max(self.dfs(node.left, result + 1), self.dfs(node.right, result + 1))
    
        """
        #2 70p
        # Recursive    
        
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        """
        
        """
        #3
        # DFS
        if not root:
            return 0
        nodes = [root]
        ans = 0
        while nodes:
            temp = []
            ans += 1
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                nodes = temp
            else:
                nodes = []
        return ans
        """
