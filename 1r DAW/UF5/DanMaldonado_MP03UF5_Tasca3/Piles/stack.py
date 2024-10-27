class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def push(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def size_of_list(self):
        return self.num_of_nodes

    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    def pop(self):
        head_data = self.head.data
        self.head = self.head.next_node
        self.num_of_nodes -= 1
        return head_data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.num_of_nodes == 0
