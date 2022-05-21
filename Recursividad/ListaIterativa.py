def suma(lista):
  suma = 0
  
  # Suma cada numero de la lista.
  for i in range(0, len(lista)):
    suma = suma + lista[i]
    
  # Devuelve la suma
  return suma

print(suma([6,3,4,2,10]))


