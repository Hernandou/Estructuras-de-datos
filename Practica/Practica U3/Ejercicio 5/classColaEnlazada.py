from classNodo import Nodo

class Cola:
    
    __ultimo : Nodo
    __contador : int
    
    def __init__(self):
        self.__ultimo = None
        
    def Agregar(self,elemento):
        nuevo = Nodo(elemento)

        if(self.__contador == None):
            self.__ultimo = nuevo
        else:
            nuevo = nuevo.setSiguiente(self.__cabeza)
        
        
        
