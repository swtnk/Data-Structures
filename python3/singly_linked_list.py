class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.root = None

    def append(self, node, current_node = None):
        if self.root is None:
            self.root = node
        else:
            if current_node is None:
                current_node = self.root
            if current_node.next is None:
                current_node.next = node
            else:
                self.append(node, current_node.next)

    def get_values(self):
        current_node = self.root
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def remove_by_position(self, position):
        pass

    def remove_first_by_value(self, value):
        pass

    def remove_all_by_value(self, value):
        pass

node_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sll = SinglyLinkedList()

for node_datum in node_data:
    sll.append(Node(node_datum))

print([data for data in sll.get_values()])
