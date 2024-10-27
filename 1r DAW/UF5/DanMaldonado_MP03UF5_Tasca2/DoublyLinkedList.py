class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous

    def insert_head(self, data):
        # Fiquem el next-node del nou node com a head i al revés, després fiquem el nou node com a head
        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def remove(self, data):
        actual_node = self.head

        while actual_node.next is not None:
            # Si el node actual és el que volem eliminar canviem els nodes anteriors i posteriors per "eliminar" el node
            if actual_node.data == data:
                actual_node.previous.next = actual_node.next
                actual_node.next.previous = actual_node.previous
            actual_node = actual_node.next

    def in_(self, data):
        actual_node = self.head
        while actual_node is not None:
            # Retornem True si trobem el node amb la data corresponent
            if actual_node.data == data:
                return True
            actual_node = actual_node.next
        return False

    def remove_duplicates(self, data):
        actual_node = self.head
        # Mentre hi hagi elements amb la mateixa data fem el remove
        while self.in_(data):
            self.remove(data)
            actual_node = actual_node.next
        # Afegim aquesta mateixa data al final
        self.insert(data)

    def reverse(self):
        head_node = self.head
        tail_node = self.tail

        # Anem intercanviant el head_node i el tail_node fins que sigui diferent
        while head_node != tail_node and head_node.previous != tail_node:
            head_node.data, tail_node.data = tail_node.data, head_node.data
            head_node = head_node.next
            tail_node = tail_node.previous


if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
