from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(root: Optional[TreeNode], targetSum: int):
        if root == None:
            return false
        return Solution.walker(root, 0, targetSum)

        
    def walker(start : TreeNode, path : int, targetSum: int) -> bool:
        if start == None:
            return False
        if start.left == None and start.right == None:
            if start.val + path == targetSum:
                return True
        else:
            return Solution.walker(start.left, path + start.val, targetSum) or Solution.walker(start.right,path+start.val,targetSum)
    
 
    def from_list(elements):
        root_node = TreeNode(val=elements[0])
        nodes = [root_node]
        for i, val in enumerate(elements[1:]):
            if val == "null":
                continue
            parent_node = nodes[i // 2]
            is_left = (i % 2 == 0)
            node = TreeNode(val=val)
            if is_left:
                parent_node.left = node
            else:
                parent_node.right = node
            nodes.append(node)

        return root_node

if __name__ == '__main__':
    test = Solution 
    root = test.from_list([5,4,8,11,"null",13,4,7,2,"null","null","null",1])
    print(test.hasPathSum(root, 22))