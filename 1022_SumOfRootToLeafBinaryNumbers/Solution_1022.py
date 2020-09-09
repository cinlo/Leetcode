# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        self.sum = 0

        def dfs(node):
            pre_node = stack.pop()
            stack.append(pre_node)
            print("this is pre_node", pre_node.val)
            print("this is cur_node", node.val)
            node.val = pre_node.val * 2 + node.val
            if node.left is None and node.right is None:
                self.sum += node.val
            if node.left is not None:
                stack.append(node)
                dfs(node.left)
            if node.right is not None:
                stack.append(node)
                dfs(node.right)

        if root.left is None and root.right is None:
            return root.val
        if root.left is not None:
            stack = [root]
            dfs(root.left)
        if root.right is not None:
            stack = [root]
            dfs(root.right)
        return self.sum
