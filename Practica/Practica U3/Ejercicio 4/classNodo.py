class Nodo:
    
    __numero = 0
    __siguiente : None
    
    def __init__(self,num):
        self.__numero = num
        self.__siguiente = None
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
        
    def getSiguiente(self):
        return(self.__siguiente)
    
    def getNumero(self):
        return(self.__numero)
    