# delete a node from bst
        #       17
        #    /     \
        #   4       20
        #  / \     /  \  
        # 1   9   18  23
        #               \
        #               34
class BinarySearchTree:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.root == data: return
        if self.root > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        if self.root < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.root == val:
            return True
        if self.root > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if self.root < val:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        el = []
        if self.left:
            el += self.left.in_order_traversal()
        el.append(self.root)
        if self.right:
            el += self.right.in_order_traversal()
        return el

    def pre_order_traversal(self):
        el = [self.root]
        if self.left:
            el += self.left.pre_order_traversal()
        if self.right:
            el += self.right.pre_order_traversal()
        return el

    def post_order_traversal(self):
        el = []
        if self.left:
            el += self.left.post_order_traversal()
        if self.right:
            el += self.right.post_order_traversal()
        el.append(self.root)
        return el

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.root

    def find_max(self):
        if self.right is None:
            return self.root
        return self.right.find_max()

    def delete(self, val):
        if self.root > val:
            if self.left:
                self.left = self.left.delete(val)
        elif self.root < val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None: return None
            elif self.left is None: return self.right
            elif self.right is None: return self.left
            #get min_val from right subtree
            # min_val = self.right.find_min()
            # self.root = min_val
            # self.right = self.right.delete(min_val)
            #get max_val form left subtree
            max_val = self.left.find_max()
            self.root = max_val
            self.left = self.left.delete(max_val)
        return self

def build_tree(el):
    root = BinarySearchTree(el[0])
    print('Building Tree',el)
    for i in range(1, len(el)):
        root.add_child(el[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 9, 20, 18, 23, 34]
    # numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.pre_order_traversal())
    # print(numbers_tree.post_order_traversal())
    # print(numbers_tree.search(5))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(18)
    print(numbers_tree.in_order_traversal())
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(17)
    print(numbers_tree.in_order_traversal())
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(1)
    print(numbers_tree.in_order_traversal())