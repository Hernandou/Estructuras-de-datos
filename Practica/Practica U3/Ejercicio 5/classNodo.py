
class Nodo:
    __numero : int
    __siguiente : object
    
    def __init__(self,numero):
        self.__siguiente = None
        self.__numero = numero
        
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
        
    def getSiguiente(self):
        return(self.__siguiente)
    
    def getNumero(self):
        return(self.__numero)
        