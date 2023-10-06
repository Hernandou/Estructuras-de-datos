class Nodo:
    
    __numero : int
    __modulo : int
    __siguiente : object
    
    def __init__(self,numero,modoulo):
        self.__numero = numero
        self.__siguiente = None
        self.__modulo = modoulo
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
        
    def getSiguiente(self):
        return(self.__siguiente)
    
    def setModulo(self,num):
        self.__modulo = num
    
    def getModulo(self):
        return(self.__modulo)
    
    def getDato(self):
        return(self.__numero)
