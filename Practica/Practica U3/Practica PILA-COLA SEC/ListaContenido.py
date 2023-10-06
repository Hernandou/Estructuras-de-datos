import numpy as np
class Lista:
    
    __lista = []
    __primer = 0
    __ultimo = 0
    __maximo = 0
    __cantidad = 0
    def __init__(self,num):
        self.__lista = np.empty(num,dtype=int)
        self.__cantidad = 0
        self.__maximo = num
        self.__primer = 0
        self.__ultimo = 0
        
    def Insertar(self,elemento):
        
        if(self.__ultimo == self.__primer): #1ut
            self.__lista[self.__ultimo] = elemento #1ut
            self.__ultimo +=1 #2ut                                  Total Caso 1: 5ut
            self.__cantidad +=1 #2ut
        else:
            if(self.__cantidad == self.__maximo):   # 2ut
                self.__maximo+=1 #2ut
                self.__lista = np.resize(self.__lista,self.__maximo) #1ut       Caso 1: 10ut
                self.__lista[self.__ultimo] = elemento #1ut
                self.__cantidad +=1 #2ut                                
                self.__ultimo += 1 #2ut
            else:
                self.__lista[self.__ultimo] = elemento #1ut
                self.__cantidad += 1    #2ut                    
                self.__ultimo +=1   #2ut                
            
        for i in range(self.__primer,self.__ultimo):
            for j in range(self.__primer,self.__maximo-i-1):
                if(self.__lista[j] > self.__lista[j+1]):
                    aux = self.__lista[j]
                    self.__lista[j] = self.__lista[j+1]
                    self.__lista[j+1] = aux 
    
    
    def Mostrar(self):
        i= self.__primer
        while(i < self.__ultimo):
            print(self.__lista[i])
            i+=1
            
            
            
if __name__ == '__main__':
        
    long = int(input('> Ingrese longitud de la lista: '))
    Lista = Lista(long)
        
    val = int(input('> Ingrese elemento a insertar: '))
    while(val != -1):
        Lista.Insertar(val)
        Lista.Mostrar()
        val = int(input('> Ingrese elemento a insertar: '))
        
            
        
        
            
                
        
        