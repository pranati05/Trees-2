# Time Complexity : O(N2)
# Space Complexity : O(N2)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Recursive Approach. Since postorder traversal is left, right, root, every recursion we get the last element from postorder
# Then get the index of root from inorder so everything before the index is left subtree and everything after the index is right subtree


class Solution:
    def buildTree(self, inorder:List[int], postorder: List[int]) -> TreeNode | None:
        if not inorder:
            return None
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        return root