import unittest

orders = [
    {
        "Order ID": 1001,
        "Customer": "John Doe",
        "Order Details": [
            {"Item": "T-shirt", "Color": "Black", "Size": "Large", "Quantity": 2},
            {"Item": "Jeans", "Color": "Blue", "Size": "32 waist", "Quantity": 1}
        ],
        "Total Amount": 75.50,
        "Payment Method": "Credit Card"
    },
    {
        "Order ID": 1002,
        "Customer": "Jane Smith",
        "Order Details": [
            {"Item": "Laptop", "Model": "Apple MacBook Pro 13-inch", "Storage": "512GB", "Quantity": 1},
            {"Item": "Wireless Mouse", "Quantity": 1}
        ],
        "Total Amount": 2000.00,
        "Payment Method": "PayPal"
    },
    {
        "Order ID": 1003,
        "Customer": "Robert Johnson",
        "Order Details": [
            {"Item": "Books", "Category": "Fiction Novels", "Quantity": 3}
        ],
        "Total Amount": 45.00,
        "Payment Method": "Cash on Delivery"
    }
]


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

    def traverse_forward(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def traverse_backward(self):
        current = self.tail
        result = []
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


dll = DoublyLinkedList()
for order in orders:
    dll.append(order)
dll.traverse_forward()
dll.traverse_backward()


class TestingDoublyLinked(unittest.TestCase):

    def test01(self):
        dll1 = DoublyLinkedList()  # Create an instance of DoublyLinkedList
        testing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for order in testing_list:
            dll1.append(order)
        self.assertEqual(dll1.traverse_backward(), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test02(self):
        dll2 = DoublyLinkedList()  # Create an instance of DoublyLinkedList
        testing_list = [250, 300, 180]
        for order in testing_list:
            dll2.append(order)
        self.assertEqual(dll2.traverse_backward(), [180, 300, 250])

    def test03(self):
        dll3 = DoublyLinkedList()  # Create an instance of DoublyLinkedList
        testing_list = ['Luis', 'Pedro', 'Miguel']
        for order in testing_list:
            dll3.append(order)
        self.assertEqual(dll3.traverse_backward(), ['Miguel', 'Pedro', 'Luis'])

    def test04(self):
        dll4 = DoublyLinkedList()  # Create an instance of DoublyLinkedList
        testing_list = []
        for order in testing_list:
            dll4.append(order)
        self.assertEqual(dll4.traverse_backward(), [])


if __name__ == '__main__':
    unittest.main()
