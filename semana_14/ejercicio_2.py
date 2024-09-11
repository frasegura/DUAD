"""2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class EmptyQueue(Exception):
    pass

    
class DoubleEndedQueue():
    def __init__(self) -> None:
        self.head = None

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node =  current_node.next

    def push_left(self , left_node):
        left_node.next = self.head
        self.head = left_node

    def push_right(self,right_node):
        if self.head is None:
            self.head = right_node
            return
        actual_node = self.head

        while actual_node is not None:
            if actual_node.next is None:
                actual_node.next = right_node
                break   
            actual_node = actual_node.next

    def pop_left(self):
        if self.head is None:
            raise EmptyQueue('The list is empty')  
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            return deleted_value
            
        deleted_value = self.head    
        self.head = self.head.next
        return deleted_value.data


    def pop_right(self):
        if self.head is None:
            raise EmptyQueue('The list is empty')
        
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            return deleted_value
        
        current_value = self.head
        
        while current_value.next.next is not None:
            current_value = current_value.next
        deleted_value = current_value.next.data
        current_value.next = None
        return deleted_value
            

new_queue = DoubleEndedQueue()
#Push methods:
new_queue.push_right(Node('Tercero'))
new_queue.push_right(Node('Cuarto'))
new_queue.push_left(Node('Segundo'))
new_queue.push_left(Node('Primero'))

#pop methods:
print (f'Left deleted value : {new_queue.pop_left()}')
print (f'right deleted value : {new_queue.pop_right()}')
print('Resulting list : ')
new_queue.print_structure()

