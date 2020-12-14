class Node:
    '''
    Nodes are the user defined data type that contain data and address to the other nodes.
    This node has been defined to be used in any binary tree.

    It has three attributes:
    1. data: to hold user data.
    2. left: to hold the address of node to the left of it as a left child.
    3. right: to hold the address of node to the right of it as a right child.
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    '''
    Trees are the data structure which helps in organising data in hierarchical format.
    They consists of one or more Nodes (another user defined data type that contains data and
    address to other nodes).
    If every node of a tree is having at most two children (i.e.: left and right) are
    called as Binary Tree.
    Node parent to the all other nodes but has no parent is called as Root node.

    Binary Trees if formed in such a fashion that data of child are organised left or
    right of the parent on the basis of some comparision (e.g.: for numerical data node
    with data less than the data of parent node are set to the left of parent else right
    of the parent) are called Binary Search Tree (BST).
    Searching for element in BST has less time complexity that randomly distributes
    nodes in the tree as while searching through tree we can neglect traversing some
    sections of the whole tree.

    Attributes of a tree is Node.
    '''
    def __init__(self, duplicate = False):
        self.root = None
        self.count_node = 0
        self.duplicate = duplicate

    def append(self, node, current = None):
        if self.root is None:
            self.root = node
        else:
            if current is None:
                current = self.root
            if current.data > node.data:
                if current.left is None:
                    current.left = node
                    self.count_node += 1
                else:
                    self.append(node, current.left)
            else:
                if not self.duplicate:
                    if current.data == node.data:
                        print('Node with same value already exists.')
                        return False
                if current.right is None:
                    current.right = node
                    self.count_node += 1
                else:
                    self.append(node, current.right)
            current = None
        return True

    def get_in_order(self, node):
        if node is None:
            return True
        yield from self.get_in_order(node.left)
        yield node.data
        yield from self.get_in_order(node.right)

    def get_pre_order(self, node):
        if node is None:
            return True
        yield node.data
        yield from self.get_pre_order(node.left)
        yield from self.get_pre_order(node.right)

    def get_post_order(self, node):
        if node is None:
            return True
        yield from self.get_post_order(node.left)
        yield from self.get_post_order(node.right)
        yield node.data


node_data = [500, 250, 750, 200, 300, 700, 800]

bst = BinarySearchTree()

for node_datum in node_data:
    bst.append(Node(node_datum))

print([x for x in bst.get_in_order(bst.root)])
print([x for x in bst.get_pre_order(bst.root)])
print([x for x in bst.get_post_order(bst.root)])