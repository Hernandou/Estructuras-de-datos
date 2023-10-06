import numpy as np

class Pila: #3 METODOS (INSERTRAR,SUPRIMIR,RECORRER)
    __tope = -1
    __pila = []
    
    def __init__(self,num=0):
        self.__pila = np.empty(num,dtype=int)
        self.__tope = -1
        self.__cant = num
    
    def Insertar(self,elemento):
        if(self.__tope < self.__cant-1):
            self.__pila[self.__tope] = elemento
            self.__tope += 1
            
    def Suprimir(self):
        if(not self.Vacia()):
            aux = self.__pila[self.__tope]
            self.__pila = np.delete(self.__pila,aux)
            self.__tope -= 1
        else:
            print('Error - Pila Vacia')
    
    def Vacia(self):
        return(self.__tope == None)
        
    def Mostrar(self):
        i = self.__tope
        while(i != -1):
            print(self.__pila[i])
            i-=1
            
            
if __name__ == '__main__':
    ans1 = int(input('>> Ingrese cantidad de elementos PILA: '))
    Pila = Pila(ans1)
    i = 0
        
    while(i<ans1):
        ans2 = int(input('>Ingrese elemento: '))
        Pila.Insertar(ans2)
        i+=1
            
    Pila.Mostrar()
    Pila.Suprimir()
    Pila.Mostrar