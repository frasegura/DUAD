"""<aside>
**Ejercicios Extra** TEST PREGUNTAR

1. Implemente un `bubble_sort` que funcione para [Linked Lists](https://www.notion.so/Linked-Lists-7232f1d617f24040a1378b749c350540?pvs=21).
    1. La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso."""


class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class EmptyList(Exception):
    pass

class LinkedList:
    def __init__(self):
        self.head = None


    def print_structure(self):
        current_node = self.head
        while current_node is not None:           
            print(current_node.data,end = '->')
            current_node =  current_node.next
        print('None')

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
            raise EmptyList('The list is empty!')

        while self.head is not None:
            node_change = False
            current_node = self.head
            print('Empieza de nuevo :  ',current_node.data)
            #self.print_structure()
            while current_node.next is not None:   
                next_node = current_node.next
                if current_node.data > next_node.data:
                    current_node.data , next_node.data = next_node.data ,current_node.data
                    node_change = True
                current_node = next_node
                print('nodo actual :', current_node.data)
                self.print_structure()
            if not node_change:
                return

my_list = LinkedList()
my_list.push(Node(25))
my_list.push(Node(5))
my_list.push(Node(1))
my_list.push(Node(99))
my_list.push(Node(20))
my_list.push(Node(89))
my_list.push(Node(59))
my_list.push(Node(100))
print('Lista Original')
my_list.print_structure()
print('-----')
my_list.sort_list()
print('Lista ordenada:')
my_list.print_structure()

