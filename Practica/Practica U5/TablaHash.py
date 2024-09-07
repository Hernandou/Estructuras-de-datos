import numpy as np
import random
import math

class Hash:
    __tabla = []
    __size = 0
    
    def __init__(self,tam):
        self.__size = self.PerroPrimo(round(tam/0.7))
        print(self.__size)
        self.__tabla = np.zeros(self.__size)
        
    def hashing(self,id):
        return(id % self.__size)
    
    def PerroPrimo(self,n):
        aux = round(n**(1/2))
        i = 2 #Primer Primo
        
        while(i <= aux):
            if(n % i) == 0:
                break
            else:
                i += 1
                
        if(i < aux):
            return self.PerroPrimo(n+1)
        else:
            return n

        
    
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

        
    