from ClassNodo import Nodo
class Lista:
    __cabeza : Nodo
    __tope = 0
    
    def __init__(self):
        self.__cabeza = None
            
    def agregarNodo(self,num):
        
        if(self.__cabeza == None): #Si la cabeza esta apuntando a None inserta el primer elemento al principio de la pila
            dato = Nodo(num)
            self.__cabeza = dato
            self.__tope += 1
        else:               #Si no lo inserta al final
            actual = self.__cabeza
            while (actual.getSiguiente() != None):
                actual = actual.getSiguiente()
                
            dato = Nodo(num)
            actual.setSiguiente(dato)
            self.__tope += 1
    
    def getTope(self):
        return(self.__tope)
    
    def recorrerPila(self):
        aux = self.__cabeza
        while (aux != None):
            print(aux.getDato())
            aux = aux.getSiguiente()
            