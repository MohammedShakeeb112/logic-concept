# binary search tree has max of 2 childnode
# in bst all leftside node should less than root node & rightside node will be greater than root node
# duplicate values are not allowed
#          15   --> rootNOde
#        /    \
#       /      \
#     12       27  --> childNode
#     / \      / \ 
#    /   \    /   \
#   7    14  20   88   --> 7,14,88 are leafNode &  --> 20 is childNode
#             \
#              \
#              23    --> leafNOde

# search in bst O(logn)
# no. of nodes = 8
# search reduces by half 
# 8 --> 4 --> 2 --> 1

# insertion in bst O(logn)
# insert 13
#          15               if 13 < 15 --> insert at leftside  
#        /    \
#       /      \
#     12       27           if 13 > 12 --> insert at righttside              
#     / \      / \ 
#    /   \    /   \
#   7    14  20   88        if 13 < 14 --> insert at leftside
#       /     \
#      /       \
#     13       23    

#search operation can be done by 2 ways 
# 1. breadth first search
# 2. depth first search : In-order Traversal, Pre-order Traversal, Posrt-order Traversal

# DFS depth first search :
#          15                 In-order Traversal: [7,12,14,15,20,23,27,88]  left,node,right,root,left,node,right
#        /    \               leftLeafNode,parentLeftLeafNodeRoot,rightLeafNode,rootNode
#       /      \
#     12       27             Pre-order Traversal: [15,12,7,14,27,20,23,88]  root,left,right          
#     / \      / \            rootNode,leftNode,leftLeafNode,rightLeafNode,rightNode,leftLeafNode
#    /   \    /   \
#   7    14  20   88          Posrt-order Traversal: [7,14,12,23,20,88,27,15]
#             \
#              \
#              23    

class BinarySearchTree:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def add_child(self, data):
        #check data already exists or not in root
        if self.root == data: return
        #check data is less than root add data to left tree
        if self.root > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        #check data is greather than root add data to right tree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        el = []
        #visit left tree
        if self.left:
            el += self.left.in_order_traversal()
        #visit baseNode/parentNode
        el.append(self.root)
        #visit right tree
        if self.right:
            el += self.right.in_order_traversal()
        return el

    def pre_order_traversal(self):
        el = []
        #visit baseNode/parentNode
        el.append(self.root)
        #visit left tree
        if self.left:
            el += self.left.pre_order_traversal()
        #visit right tree
        if self.right:
            el += self.right.pre_order_traversal()
        return el

    def post_order_traversal(self):
        el = []
        #visit left tree
        if self.left:
            el += self.left.post_order_traversal()
        #visit right tree
        if self.right:
            el += self.right.post_order_traversal()
        #visit baseNode/parentNode
        el.append(self.root)
        return el

    def search(self, val): #O(logn)
        #val exists in root 
        if self.root == val:
            return True
        #check val might be on left subtree
        if self.root > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        #check val might be on right subtree
        if self.root < val:
            if self.right:
                return self.right.search(val)
            else:
                return False
# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
    def find_min(self):
        if self.left is None:
            return self.root
        return self.left.find_min()
            
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.root

    def calculate_sum(self):
        #method1
        # total = self.in_order_traversal()
        # return sum(total)        
        #method2
        # left_sum = 0
        # right_sum = 0
        # if self.left:
        #     left_sum += self.left.calculate_sum()
        # if self.right:
        #     right_sum += self.right.calculate_sum()
        # return self.root + left_sum + right_sum
        #method3
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.root + left_sum + right_sum

def build_tree(el):
    root = BinarySearchTree(el[0])
    for i in range(1, len(el)):
        root.add_child(el[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    iot = numbers_tree.in_order_traversal()
    pot = numbers_tree.pre_order_traversal()
    pst = numbers_tree.post_order_traversal()
    print(iot)
    print(pot)
    print(pst)
    print(numbers_tree.search(5))
    countries = ['India', 'Pakistan', 'Aghanistan', 'Egypt', 'China', 'Saudi Arabia']
    countries_tree = build_tree(countries)
    print(countries_tree.in_order_traversal())
    print(countries_tree.pre_order_traversal())
    print(countries_tree.post_order_traversal())
    print(countries_tree.search('France'))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    