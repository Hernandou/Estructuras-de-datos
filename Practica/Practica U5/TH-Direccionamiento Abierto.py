import numpy as np
import random
import math

class Hash:
    __tabla = []
    __size = 0
    
    def __init__(self,tam):
        self.__size = (int(tam/0.7)+tam)
        self.__tabla = np.zeros(self.__size)
        
    def hashing(self,id):
        return(round(id % self.__size))
    
    def Insertar(self,elemento):
        i = self.hashing(elemento)
        
        if(self.__tabla[i] == 0):
            self.__tabla[i] = elemento
            print('Ingresa elemento')
        else:
            ind = i
            i = self.hashing(i+1)
            
            while(self.__tabla[i] != elemento and i != ind):
                i = self.hashing(i+1)
                
            if(self.__tabla[i] == 0 and i != ind):
                self.__tabla[i] = elemento
                print('Ingresa elemento')
            else:
                print('Error la tabla esta llena')
    
    def Mostrar(self):
        j=0
        for i in range(len(self.__tabla)):
            print('{}{}'.format(j,self.__tabla[i]))
            j+=1

            
if __name__ == '__main__':
    n = 10
    TablaHash = Hash(n)
    
    for i in range(n):
        elemento = random.randint(0,n*n)
        TablaHash.Insertar(elemento)

    TablaHash.Mostrar()

        
    