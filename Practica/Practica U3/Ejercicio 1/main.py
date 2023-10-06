from classLista import Lista
from ClassNodo import Nodo
import random



if __name__ == '__main__':
    lista = Lista()
    
    for i in range(3):
        num = random.randint(0,9)
        lista.agregarNodo(num)
        
    print("La cantidad de elementos que tiene la pila es {}".format(lista.getTope()))
    print("Los datos de la pila son: ")
    lista.recorrerPila()
    num = int(input("Ingrese el elemento a insertar en la pila: "))
    lista.agregarNodo(num)
    lista.recorrerPila()