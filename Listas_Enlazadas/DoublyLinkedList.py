# Paso 6: creación de una lista de enlace doble / Step 6: create a double linked list
# Clase de nodO de lista extendida / extended list node class

class ListNode:
    def __init__(self, data):
        "constructor class to initiate this object"

        # Almacenamiento de datos
        # store data
        self.data = data
        
        # Referencia al almacenamiento (siguiente elemento)
        # store reference (next item)
        self.next = None

        # Referencia al almacenamiento (anterior elemento)
        # store reference (previous item)
        self.previous = None
        return

    def has_value(self, value):
        "Metodo para comparar el valor con los datos del nodo"
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
        

# una clase de lista de enlace doble / a double linked list class

class DoubleLinkedList:
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return

    def list_length(self):
        "returns the number of list items"
        
        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count = count + 1
            
            # jump to the linked node
            current_node = current_node.next
        
        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next
        
        return

    def unordered_search (self, value):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        # define list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        
        return results
    
    # Agregar nodos en una lista de doble enlace / add nodes to a double linked list   
    def add_list_item(self, item):
        "añadir un elemento al final de la lista"
        "add an item at the end of the list"

        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        
        return 
    
    # Eliminar un elemento de una lista de doble enlace / remove an item from a double linked list
    def remove_list_item_by_id(self, item_id):
        "elimina el elemento de la lista con la identificación del elemento"
        "remove the list item with the item id"
        
        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                # we don't have to look any further
                return
 
            # needed for the next iteration
            current_node = next_node
            current_id = current_id + 1
                
        return
    
# crear tres nodos individuales
# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
node4 = ListNode(15)

track = DoubleLinkedList()
print("track length: %i" % track.list_length())

for current_node in [node1, node2, node3, node4]:
    track.add_list_item(current_node)
    print("track length: %i" % track.list_length())
    track.output_list()

results = track.unordered_search(15)
print(results)

track.remove_list_item_by_id(4)
track.output_list()    
    