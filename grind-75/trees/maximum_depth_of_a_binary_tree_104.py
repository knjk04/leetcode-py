# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth2(self, root: Optional[TreeNode], max_depth) -> int:
        if not root:
            return max_depth

        return max(1 + self.maxDepth2(root.left, max_depth),
                   1 + self.maxDepth2(root.right, max_depth))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth2(root.left, 1), self.maxDepth2(root.right, 1))
