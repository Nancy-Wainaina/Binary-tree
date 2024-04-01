

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('200')
node50 = TreeNode('50')
node100 = TreeNode('100')
node30 = TreeNode('30')
node40 = TreeNode('40')
node60 = TreeNode('60')
node80 = TreeNode('80')
node55 = TreeNode('55')

root.left = node50
root.right = node100

node50.left = node30
node50.right = node40

node100.left = node60
node100.right = node80

node80.left = node55


print("root.right.left.data:", root.right.left.data)


        
       
       