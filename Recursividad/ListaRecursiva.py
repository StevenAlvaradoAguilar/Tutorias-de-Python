def suma(lista):
  
  if len(lista) == 1:   # Caso base
    return lista[0]
  else:
    return lista[0] + suma(lista[1:]) # La función se llama a si misma (Recursión)
                                      # lista[1:] devuelve la lista sin su primer elemento
                                      
print(suma([6,3,4,2,10]))