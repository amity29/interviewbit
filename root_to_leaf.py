# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : A node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B, sum=0, cur=None, res=None):
        if res is None:
            res = []
        if cur is None:
            cur = []
        if not A:
            return res
        l, r, val = A.left, A.right, A.val
        sum += val
        cur.append(val)
        if l is None and r is None and sum == B:
            res.append(list(cur))
        self.pathSum(l, B, sum, cur, res)
        self.pathSum(r, B, sum, cur, res)
        cur.pop()
        sum -= val
        return res
