from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 给定一个二叉树的根节点 root ，返回 它的 中序 遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr
    #给定一个二叉树 root ，返回其最大深度 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    # 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_invert(node: TreeNode):
            if not node:
                return
            dfs_invert(node.left)
            dfs_invert(node.right)
            node_temp = node.left
            node.left = node.right
            node.right = node_temp
        dfs_invert(root)
        return root
    # 给你一个二叉树的根节点 root ， 检查它是否轴对称
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs_symm(left_node: TreeNode, right_node: TreeNode)-> bool:
            if not left_node and not right_node:
                return True
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            return dfs_symm(left_node.left, right_node.right) and dfs_symm(left_node.right, right_node.left)
        return dfs_symm(root.left, root.right)
    #给你一棵二叉树的根节点，返回该树的直径，二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root
    #两节点之间路径的长度由它们之间边数表示
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def dfs_diam(node: TreeNode)-> int:
            if not node:
                return 0
            left = dfs_diam(node.left)
            right = dfs_diam(node.right)
            self.max_len = max(self.max_len, left + right)
            return max(left, right) + 1
        dfs_diam(root)
        return self.max_len
    # 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树
    # [1,2,3,4,5,6]
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs_bst(nums: List[int]) -> Optional[TreeNode]:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = dfs_bst(nums[:mid])
            root.right = dfs_bst(nums[mid:])
            return root
        return dfs_bst(nums)













s = Solution()
# treeNode = TreeNode(1)
# treeNode.left = TreeNode(2)
# treeNode.right = TreeNode(3)
# treeNode.left.left = TreeNode(4)
# treeNode.left.right = TreeNode(5)
# treeNode.right.left = TreeNode(4)
# treeNode.right.right = TreeNode(3)
#print(s.diameterOfBinaryTree(treeNode))
# arr = s.inorderTraversal(treeNode)
# print(arr)
arr = [-10,-3,0,5,9]
s.sortedArrayToBST(arr)