class Nodo:
    
    __numero = 0
    __siguiente : None
    
    def __init__(self,num):
        self.__numero = num

    
    def getNumero(self):
        return(self.__numero)
