class Elemento:
    __numero : int
    __siguiente : None
    
    def __init__(self,elemento):
        self.__siguiente = None
        self.__numero = elemento
        
    def setSiguiente(self,obj):
        self.__siguiente = obj
        
    def setNumero(self,numero):
        self.__numero = numero
    
    def getNumero(self):
        return(self.__numero)
        
    def getSiguiente(self):
        return(self.__siguiente)