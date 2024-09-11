"""3. Cree una estructura de objetos que asemeje un Binary Tree.
    1. Debe incluir un método para hacer `print` de toda la estructura.
    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""

class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def get_sorted_bin_tree(root):
    if root is None:
        return
    else:
        get_sorted_bin_tree(root.left)
        print(root.data)
        get_sorted_bin_tree(root.right)



if __name__ == '__main__':
    root = Node('b')
    root.insert('c')
    root.insert('a')

    get_sorted_bin_tree(root)
