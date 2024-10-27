class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Queue_:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # Afegeix un element a la cua
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        # Elimina el primer element
        if self.head is None:
            print("Cua buida.")
        else:
            data = self.head.data
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            else:
                self.head.previous = None

            return data

    def peek(self):
        # Retorna el valor del primer element
        if self.head is None:
            print("Cua buida.")
        else:
            return self.head.data

    def is_empty(self):
        # Comprova si la cua está buida
        return self.head is None

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data.name)
            actual_node = actual_node.next
