# Data structures exercise: General Tree
#     Below is the management hierarchy of a company.
# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,
# Here is how your main function should will look like,
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy
from PIL import Image
hr1 = Image.open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/hr1.png')
hr1nd = Image.open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/hr1nd.png')
hr2 = Image.open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/hr2.png')
hr2nd = Image.open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/hr2nd.png')
# hr1.show()
# hr1nd.show()
# hr2.show()
# hr2nd.show()

class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def company_infrastructure():
    #rootNode
    root = Tree('Nilupul  (CEO)')
    #rootChildNode
    cto = Tree('Chinmay   (CTO)')
    hr = Tree('Gels    (HR Head)')
    #ctoChildNode
    in_hd = Tree('Vishwa    (Infrastructure Head)')
    ah = Tree('Aamir   (Application Head)')
    #hrChildNode
    hr.add_child(Tree('Peter    (Recruitment manager)'))
    hr.add_child(Tree('Waqas   (Policy Manage)'))
    #in_hdChildNode
    in_hd.add_child(Tree('Dhaval   (Cloud Manager)'))
    in_hd.add_child(Tree('Abhijit   (App Manager)'))

    #adding all to rootNode
    cto.add_child(in_hd)
    cto.add_child(ah)
    root.add_child(cto)
    root.add_child(hr)

    root.print_tree()

def position():
    #rootNode
    root = Tree('CEO')
    #rootChildNode
    cto = Tree('CTO')
    hr = Tree('HR Head')
    #ctoChildNode
    in_hd = Tree('Infrastructure Head')
    ah = Tree('Application Head')
    #hrChildNode
    hr.add_child(Tree('Recruitment manager'))
    hr.add_child(Tree('Policy Manage'))
    #in_hdChildNode
    in_hd.add_child(Tree('Cloud Manager'))
    in_hd.add_child(Tree('App Manager'))

    #adding all to rootNode
    cto.add_child(in_hd)
    cto.add_child(ah)
    root.add_child(cto)
    root.add_child(hr)

    root.print_tree()

def name():
    #rootNode
    root = Tree('Nilupul')
    #rootChildNode
    cto = Tree('Chinmay')
    hr = Tree('Gels')
    #ctoChildNode
    in_hd = Tree('Vishwa')
    ah = Tree('Aamir')
    #hrChildNode
    hr.add_child(Tree('Peter'))
    hr.add_child(Tree('Waqas'))
    #in_hdChildNode
    in_hd.add_child(Tree('Dhaval'))
    in_hd.add_child(Tree('Abhijit'))

    #adding all to rootNode
    cto.add_child(in_hd)
    cto.add_child(ah)
    root.add_child(cto)
    root.add_child(hr)

    root.print_tree()

# if __name__ == '__main__':
    # root = company_infrastructure()
    # root = position()
    # root = name()


# efficient ways 
class Tree_Node:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self, criteria):
        if criteria == 'both':
            result = self.name + '(' + self.designation + ')'
        elif criteria == 'name':
            result = self.name
        else:
            result = self.designation
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + result)
        for child in self.children:
            child.print_tree(criteria)

def company_infrastructure():
    #rootNode
    ceo = Tree_Node('Nilupul','CEO')
    #rootChildNode
    cto = Tree_Node('Chinmay','CTO')
    hr = Tree_Node('Gels', 'HR Head')
    #ctoChildNode
    in_hd = Tree_Node('Vishwa','Infrastructure Head')
    ah = Tree_Node('Aamir', 'Application Head')
    #hrChildNode
    hr.add_child(Tree_Node('Peter', 'Recruitment manager'))
    hr.add_child(Tree_Node('Waqas', 'Policy Manage'))
    #in_hdChildNode
    in_hd.add_child(Tree_Node('Dhaval','Cloud Manager'))
    in_hd.add_child(Tree_Node('Abhijit', 'App Manager'))

    #adding all to rootNode
    cto.add_child(in_hd)
    cto.add_child(ah)
    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo
# if __name__ == '__main__':
    # root_node = company_infrastructure()
    # root_node.print_tree('both')
    # root_node.print_tree('name')
    # root_node.print_tree('designation')


class Tree_node:
    def __init__(self, country):
        self.country = country
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() > level: return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.country)
        # print(self.children)
        if self.children:
            for child in self.children:
                child.print_tree(level)
    
def country():
    #rootNode
    world = Tree_node('Global')
    #childNode
    india = Tree_node('India')
    usa = Tree_node('USA')
    #indiaChildNode
    gujarat = Tree_node('Gujarat')
    karnataka = Tree_node('Karnataka')
    #gujaratChildNode
    ahm = Tree_node('Ahmedabad')
    bar = Tree_node('Baroda')
    #karnatakaChildNode
    blr = Tree_node('Bangalore')
    msr = Tree_node('Mysore')
    #usaChildNode
    njs = Tree_node('New Jersey')
    cal = Tree_node('California')
    #njsChildNode
    pn = Tree_node('Princeton')
    tn = Tree_node('Trenton')
    #calChildNode
    sf = Tree_node('San Francisco')
    mv = Tree_node('Mountain View')
    pa = Tree_node('Palo Alto')

    gujarat.add_child(ahm)
    gujarat.add_child(bar)
    karnataka.add_child(blr)
    karnataka.add_child(msr)
    njs.add_child(pn)
    njs.add_child(tn)
    cal.add_child(sf)
    cal.add_child(mv)
    cal.add_child(pa)
    india.add_child(gujarat)
    india.add_child(karnataka)
    usa.add_child(njs)
    usa.add_child(cal)
    world.add_child(india)
    world.add_child(usa)

    return world

if __name__ == '__main__':
    root = country()
    # root.print_tree(1)
    # root.print_tree(2)
    root.print_tree(2)





