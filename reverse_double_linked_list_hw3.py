# Reverse Double Linked List

class Node(object):
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_previous(self, previous):
        self.previous = previous

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # Метод для разворота двусвязного списка
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.previous
            current.previous = current.next
            current.next = temp
            current = current.previous
        if temp is not None:
            self.head = temp.previous

    # Метод вставки элемента в начало списка
    def add_first(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node.get_next() is not None:
            new_node.next = self.head
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node

    # Метод вставки в конец списка
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    # Показать результат работы со связным списком
    def show_list(self):
        current_node = self.head
        output = ""
        while current_node is not None:
            output += str(current_node.get_data()) + " -> "
            current_node = current_node.get_next()
        print(output)

if __name__ == "__main__":
    my_list = DoubleLinkedList()

    my_list.append(34)
    my_list.append(5)
    my_list.append(26)

    my_list.add_first(17)
    my_list.add_first(2)
    my_list.add_first(233)

    my_list.show_list()

    my_list.reverse()

    my_list.show_list()
