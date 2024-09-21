"""<aside>
**Ejercicios Extra** TEST PREGUNTAR

1. Implemente un `bubble_sort` que funcione para [Linked Lists](https://www.notion.so/Linked-Lists-7232f1d617f24040a1378b749c350540?pvs=21).
    1. La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso."""


class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data , end='->')
            current_node =  current_node.next

    def push(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = None

    def sort_list(self):
        if self.head is None:
            print('The list is empty')
        while self.head is not None:
            node_change = False
            current_node = self.head
            next_node= self.head.next
            while current_node is not None:
                print(current_node, next_node)
                if current_node.data > next_node.data:
                    current_node.data , next_node.data = next_node.data ,current_node.data
                    node_change = True
                current_node = next_node

            if not node_change:
                break



my_list = LinkedList()
my_list.push(Node(45))
my_list.push(Node(25))
my_list.push(Node(5))
my_list.push(Node(1))
my_list.push(Node(99))
my_list.print_structure()
my_list.sort_list()
my_list.print_structure()

