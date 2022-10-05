from operator import le
from re import S
from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            newRoot = TreeNode(val=val, left = root)
            root = newRoot #!!!!!
            return True            
        else:
            return Solution.walker(root,1,val,depth)

    def walker(start : TreeNode, level, val, depth) -> bool:
        if start != None:
            if level == depth-1:
                newLeft = TreeNode(val = val,left = start.left)
                newRight = TreeNode(val=val, right = start.right)
                start.left = newLeft
                start.right = newRight
                return True
            elif level < depth-1:
                return Solution.walker(start.left,level+1, val,depth) & Solution.walker(start.right,level+1, val, depth)
        else:
            return True
    
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
    root = test.from_list([4,2,6,3,1,5])
    root2 = test.from_list([4,2,"null",3,1])
    print(test.addOneRow(root, 1, 2))
    print(test.addOneRow(root2, 1, 3))