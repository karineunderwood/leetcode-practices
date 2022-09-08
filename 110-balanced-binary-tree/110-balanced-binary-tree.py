# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         if root  == none, then the tree is balanced - return True
#         do it on the recursive way, not checking from the root, but from the leaf node

        def dfs_recursion(root):
            if root is None:
                return [True, 0]
            
            left = dfs_recursion(root.left)
            right = dfs_recursion(root.right)
            
            balanced_tree = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced_tree, 1 + max(left[1], right[1])]
            
        return dfs_recursion(root)[0]
                                                         
        