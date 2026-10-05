# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1: Recursive Depth First search
        # O(n) time and O(n) space
        
        if not root:
            return 0

        ldep = self.maxDepth(root.left)
        rdep = self.maxDepth(root.right)

        maxdep = max(ldep,rdep) + 1
        return maxdep

        # Approach 2: Iterative Depth first search
        # O(n) time and O(n) space

        # if not root:
        #     return 0

        # # Give the node and depth at a time in the stack
        # stack = [[root, 1]]
        # res = 1
        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         # pop the node and add the children at the next depth
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        # return res

        
        # Approach 3: Breadth first search solution
        # O(n) time and O(n) space

        # if not root:
        #     return 0

        # level = 0

        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         # if node.left is not null
        #         if node.left:
        #             q.append(node.left)
        #         # if node.right is not null
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level