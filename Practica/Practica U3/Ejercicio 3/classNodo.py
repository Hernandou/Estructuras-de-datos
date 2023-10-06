class Nodo:
    
    __siguiente:object
    __numero = 0
    
    def __init__(self,numero):
        self.__siguiente = None
        self.__numero = numero
        
    def getNumero(self):
        return(self.__numero)
    def getSiguiente(self):
        return(self.__siguiente)
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    