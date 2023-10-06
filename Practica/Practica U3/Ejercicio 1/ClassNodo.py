class Nodo:
    
    __datos = 0
    __siguiente : object
    
    def __init__(self,dato):
        self.__datos = dato
        self.__siguiente = None
    
    def setSiguiente(self,sig):
        self.__siguiente = sig
        
    def getSiguiente(self):
        return(self.__siguiente)

    def getDato(self):
        return(self.__datos)