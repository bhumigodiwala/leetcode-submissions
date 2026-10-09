# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder -> root, left, right
        # inorder -> left, root, right

        # Approach 1: Recursive solution
        # Hints:
        # 1. 1st value of Preorder traversal is always going to be the root node
        # 2. Search the root node in inorder traversal. 
        # 3. The length of left and right subarrays in inorder traversal list 
        #    gives us no of elements in left and right subtrees and 
        #    partitioning point for the preorder traversal tree

        # Start with base case since it is a recursive algorithm
        if not preorder or not inorder:
            return None

        # Create a root node from the first element of the preorder traversal list
        root = TreeNode(preorder[0])
        # Find the partitioning index with help of index of root node in the inorder array
        mid = inorder.index(preorder[0])
        # Recursively construct left and right subtrees using the hints above
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root