import numpy as np
class Secuencial:
    
    __cantidad : int
    __ind : int
    __list : None
    
    def __init__(self,maxim = 0):
        self.__list = np.empty(int(maxim),dtype=int)
        self.__cantidad = maxim
        self.__ind = 0
        
    def Insertar(self, elem):
        if(self.__cantidad == self.__ind):
            self.__list.resize(1)
            self.__list[self.__ind] = elem
            self.__ind += 1
        else:
            self.__list[self.__ind] = elem
            self.__ind+=1
            
    
    def Vacio(self):
        return(self.__cantidad == self.__ind)
    
    def Eliminar(self):
        if(len(self.__list) != 0):
            self.__list[self.__ind-1] = 0
            self.__ind -= 1
                
    def mostrar(self):
       for i in range(len(self.__list)):
           print(self.__list[i])