class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
                return None
       
        elif root.val > high:  # if the root val is greater than high then right subtree values will be even higher so we move forward with the left subtree.
            return self.trimBST(root.left,low,high)
          
        elif root.val < low:   # if the root val is less than low then left subtree values will be even lower so we move forward with the right subtree.
            return self.trimBST(root.right,low,high)
          
        else:                  # if the root val is in given range then recursively checking for left subtree and right subtree.
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
            
            return root
