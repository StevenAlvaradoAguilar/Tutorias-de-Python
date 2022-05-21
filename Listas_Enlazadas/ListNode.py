# Paso 1: Nodo como estructura de datos / Step 1: Node as data structure
class ListNode:
    """
    Debemos de saber que el constructor en python siempre va ser __init__ y este siempre va estar debajo
    de la clase. Siempre tendrá un self como argumento para que sepa que es una instancia de la clase.
    """
    """ 
    We must know that the constructor in python will always be __init__ and this will always be below the class. 
    It will always have a self as an argument so it knows that it is an instance of the class.
    """
    def __init__(self, data):
        "constructor para iniciar este objeto"
        "constructor to initiate this object"
        
        # Almacenamiento de datos / store data
        self.data = data
        
        # Referencia al almacenamiento (siguiente elemento) / store reference (next item)
        self.next = None
        return
    
    def has_value(self, value):
        "método para comparar el valor con los datos del nodo"
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

# Creación de instancias de nodes / creating nodes instances
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
# Impresión de datos / printing data
print(node1.data)
print(node2.data)
print(node3.data)






