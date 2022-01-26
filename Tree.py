#general tree consist of rootNode, childNode, leafNode ==> general tree can have mutiple node leaf
class Tree:
    def __init__(self, data):
        self.data = data #name of rootNode/childNode/leafNode
        self.children = [] #children of rootNode is childNode, children of childNode is leafNode
        self.parent = None #parent of leafNode is childNode,and parent of childNode is rootNode 

    #adding childNode
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    #print the hirerachy of tree ==> rootNode --> childNode --> leafNode
    def print_tree(self):
        # print(self.data)
        spaces = ' ' * self.get_spaces()*4
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                # print('   |__'+child.data)
                child.print_tree()

    def get_spaces(self):
        spaces = 0
        p = self.parent
        while p:
            spaces += 1
            p = p.parent
        return spaces

def build_product():
    #root node
    root = Tree('Electronics')
    #childnode
    laptop = Tree('Laptop')
    mobile = Tree('Mobile')
    tv = Tree('Television')
    #leafnode
    #laptop's childNode
    laptop.add_child(Tree('Dell'))
    laptop.add_child(Tree('HP'))
    laptop.add_child(Tree('Mac'))
    #mobile's childNode
    mobile.add_child(Tree('Apple'))
    mobile.add_child(Tree('Nokia'))
    mobile.add_child(Tree('Blackberry'))
    #tv's childNode
    tv.add_child(Tree('Samsung'))
    tv.add_child(Tree('Toshiba'))
    tv.add_child(Tree('Micromax'))
    
    #adding childNode to rootNode
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    root = build_product()




    