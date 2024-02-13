import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def insert_at_beginning(self, data):
        self.prepend(data)

    def insert_at_end(self, data):
        self.append(data)

    def delete_from_beginning(self):
        if self.head is None:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return True

    def delete_from_end(self):
        if self.head is None:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return True

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

dll.insert_at_beginning(0)
dll.insert_at_end(4)

dll.display()  # Output: 0 1 2 3 4

dll.delete_from_beginning()
dll.delete_from_end()

dll.display()  # Output: 1 2 3

dll.traverse_forward()  # Output: 1 2 3
dll.traverse_backward()  # Output: 3 2 1

print(dll.search(2))  # Output: True
print(dll.search(5))  # Output: False

dll.update(2, 20)
dll.display()  # Output: 1 20 3


