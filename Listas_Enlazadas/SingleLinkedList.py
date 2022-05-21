from ListNode import ListNode
# Paso 2: creación de una clase para una lista unificada / Step 2: create a class for a unified list
# None en python significa que no hay nada / None in python means nothing

class SingleLinkedList:
    def __init__(self):
        "constructor para iniciar este objeto"
        "constructor to initiate this object"
        self.head = None
        self.tail = None
        return

    # Paso 3: Agregar nodos a la lista / Step 3: Add nodes to the list

    def add_list_item(self, item):
            "añadir un elemento al final de la lista"
            "add an item at the end of the list"
            
            if not isinstance(item, ListNode):
                item = ListNode(item)

            if self.head is None:
                self.head = item
            else:
                self.tail.next = item

            self.tail = item
                
            return

    # El método list_length(). El método cuenta los nodos y devuelve la longitud de la lista.
    # The list_length() method. The method counts the nodes and returns the length of the list.

    def list_length(self):
            "devuelve el número de elementos de la lista"
            "returns the number of list items"
            
            count = 0
            current_node = self.head
            
            while current_node is not None:
                # aumenta el contador en uno
                # increase counter by one 
                count = count + 1
                
                # salta al nodo vinculado
                # jump to the linked node
                current_node = current_node.next
                
            return count
        
    # El método output_list() genera los valores del node utilizando la propiedad del node data.
    # The output_list() method generates the values of the node using the node data property.   
        
    def output_list(self):
            "genera la lista (el valor del nodo, en realidad)"
            "outputs the list (the value of the node, actually)"
            
            current_node = self.head
            
            while current_node is not None:
                print(current_node.data)
                
                # salta al nodo vinculado
                # jump to the linked node
                current_node = current_node.next
                
            return   
    
    # Paso 4: búsqueda en la lista / Step 4: search in the list   
    # búsqueda desordenada / unsorted search
    def unordered_search (self, value):
            "search the linked list for the node that has this value"
            
            # definir el nodo actual
            # define current_node
            current_node = self.head
            
            # definir la posición del nodo
            # define position
            node_id = 1
            
            # definir lista de resultados
            # define list of results
            results = []
            
            while current_node is not None:
                if current_node.has_value(value):
                    results.append(node_id)
                  
                # salta al nodo vinculado  
                # jump to the linked node
                current_node = current_node.next
                node_id = node_id + 1
            
            return results 
    
    # Paso 5: eliminar un artículo de la lista / Step 5: remove an item from the list
    
    def remove_list_item_by_id(self, item_id):
        "elimina un elemento de la lista por su id"
        "remove the list item with the item id"
        
        current_id = 1
        current_node = self.head
        previous_node = None
        
        while current_node is not None:
            if current_id == item_id:
                # si este es el primer nodo (cabeza)
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # no tenemos que buscar más
                    # we don't have to look any further
                    return
            
            # necesario para la próxima iteración
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        
        return
    
# Creación de nodos y salida de lista / Creating nodes and outputting list

# crear cuatro nodos individuales
# create four single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
item3 = "Berlin"
node4 = ListNode(15)

track = SingleLinkedList()
print("track length: %i" % track.list_length())

for current_item in [node1, node2, item3, node4]:
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()   
 

    
    
    
    
    
    
    
    
    
    
    