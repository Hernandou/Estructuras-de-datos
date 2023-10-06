from classNodo import Nodo
class Pila:
    
    __tope : Nodo
    __cabeza : Nodo
    
    def __init__(self):
        self.__cabeza = None
        
    def AgregarNumero(self,numero):
        obj = Nodo(int(numero))
        
        if(self.__cabeza == None):
            self.__cabeza = obj
            self.__tope = obj
        else:
            self.__tope.setSiguiente(obj)
            self.__tope = obj            
            
    def resultado(self):
        aux = self.__cabeza
        acum = 1
        while(aux != None and aux.getNumero() != 0):
            acum = acum * aux.getNumero()
            aux = aux.getSiguiente()
        
        return(acum)
            