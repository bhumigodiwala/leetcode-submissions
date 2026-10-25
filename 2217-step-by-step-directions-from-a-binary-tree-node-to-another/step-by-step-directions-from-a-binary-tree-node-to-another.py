# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        parent={root.val:0};edge={};stack=[root]
        while stack:
            node=stack.pop()
            for child,label in ((node.left,'L'),(node.right,'R')):
                if child:parent[child.val]=node.val;edge[child.val]=label;stack.append(child)
        ancestors={};v=startValue
        while v:ancestors[v]=len(ancestors);v=parent[v]
        down=[];v=destValue
        while v not in ancestors:down.append(edge[v]);v=parent[v]
        return 'U'*ancestors[v]+''.join(reversed(down))
