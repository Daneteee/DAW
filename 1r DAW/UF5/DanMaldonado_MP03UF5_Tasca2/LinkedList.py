class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_in_place(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # Si no hi ha head el creem
        if self.head is None:
            self.head = new_node

        # Si la data és més gran que el head el fiquem com a head
        elif self.head.data > data:
            new_node.next_node = self.head
            self.head = new_node

        else:
            # Anem iterant fins trobar un node amb una data major que la data a afegir
            actual_node = self.head
            while actual_node.next_node is not None and actual_node.next_node.data < data:
                actual_node = actual_node.next_node
            new_node.next_node = actual_node.next_node
            actual_node.next_node = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    def merge(self, linked_list):
        # Si no hi ha head el creem
        if self.head is None:
            self.head = linked_list.head
        else:
            # Anem afegint cada node de la linked list a la linked list actual
            actual_node = linked_list.head
            while actual_node is not None:
                self.insert_in_place(actual_node.data)
                actual_node = actual_node.next_node

    def in_(self, data):
        actual_node = self.head
        # Iterem fins trobar un node amb la data corresponent
        while actual_node is not None:
            if actual_node.data == data:
                return True
            actual_node = actual_node.next_node
        return False

    def index(self, index):
        actual_node = self.head
        c = 0
        while actual_node is not None:
            # Retornem el node que correspon a l'index introduit
            if c == index:
                return actual_node.data
            actual_node = actual_node.next_node
            c += 1

    def find(self, data):
        actual_node = self.head
        c = 0
        while actual_node is not None:
            # Quan trobem el node retornem l'index d'aquest
            if actual_node.data == data:
                return c
            actual_node = actual_node.next_node
            c += 1

    def size_of_list(self):
        return self.num_of_nodes

    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(1)
    linked_list.insert_end(2)
    linked_list.insert_end(33)
    linked_list.insert_end(4)
    print(linked_list.find(33))
