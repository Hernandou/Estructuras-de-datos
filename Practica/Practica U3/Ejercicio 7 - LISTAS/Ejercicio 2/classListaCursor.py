import numpy as np
from classNodo import Nodo

class Lista:
    
    __lista = []
    __disponible = 0
    __cabeza = -1
    
    def __init__(self,dim):
        self.__lista = np.empty(dim,dtype=Nodo)
        nodo = Nodo(0)
        for i in range(0,dim-1):
            self.__lista[i] = nodo
            self.__lista[i].setSiguiente(i+1)
        self.__lista[dim-1]=nodo
        self.__lista[dim-1].setSiguiente(-1)
            
        
    def Agregar(self,numero):
        nuevo = Nodo(numero)
        
        if(self.__disponible != -1):
            if(self.__cabeza == -1):
                self.__lista[self.__disponible] = nuevo
                nuevo.getSiguiente(self.__cabeza)
                self.__cabeza = nuevo
                 
    
    def Mostrar(self):
        pass
    
        
        