"""1. Cree una estructura de objetos que asemeje un Stack (Pila).
    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""

#Pilas LIFO-> Last in first out

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data
    
class EmptyStack(Exception):
    pass
        

class Stack:

    def __init__(self):
        self.head = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node)
            current_node =  current_node.next


    #Ingresar nodo al stack
    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node
        return new_node.data
        
    #remover nodo del stack

    def pop(self):
        if self.head is None:
            raise EmptyStack('The list is empty')

        removed_node = self.head
        self.head = self.head.next
        return removed_node.data

        
        
        
first_node = Node('Primero')
new_stack = Stack()
new_stack.push(first_node)
new_stack.push(Node('Segundo'))
new_stack.print_structure()
print('----POP---')
removed_value =new_stack.pop()
print(removed_value)
    










