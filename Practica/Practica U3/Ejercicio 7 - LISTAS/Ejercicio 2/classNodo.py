class Nodo:
    
    __elemento : int
    __siguiente = 0
    
    def __init__(self,elemento):
        self.__siguiente = -1
        self.__elemento = elemento
        
    def setSiguiente(self,num):
        self.__siguiente = num
        
    def setElemento(self,elemento):
        self.__elemento = elemento
        
    def getSiguiente(self):
        return(self.__siguiente)
    
    def getElemento(self):
        return(self.__elemento)