import numpy as np


class Lista:
    
    __lista = []
    __primer = 0
    __ultimo = 0
    __cantidad = 0
    
    def __init__(self,num):
        self.__lista = np.empty(int(num),dtype=int)
        self.__primer = 0
        self.__ultimo = 0
        self.__cantidad = 0
        self.__maximo = num

    def Insertar(self,elemento,posicion):
        posicion -= 1
        if(posicion < self.__maximo): #Entra en la cota
            
            if(posicion == self.__primer):
                self.__lista[self.__primer] = elemento
                self.__cantidad += 1
                self.__ultimo +=1
            else:
                if(self.__lista[self.__ultimo-1] != None):
                    self.__lista[posicion] = elemento
                    self.__ultimo +=1
                else:
                    print('El elemento no puede ser insertado en esta posicion')
        else:
            if(self.__lista[self.__ultimo-1] != None):
                self.__maximo +=1
                aux = self.__maximo
                self.__lista = np.resize(self.__lista,aux)
                self.__ultimo += 1
                self.__cantidad += 1
            
    def Mostrar(self):
        for i in range(self.__primer,self.__ultimo):
            print(self.__lista[i])
            
if __name__ == '__main__':
    ans1 = int(input('>> Ingrese longitud de la lista: '))
    Lista = Lista(ans1)
    Lista.Mostrar()

    a = True
    i=0
    elem = int(input('Ingrese elemento a insertar: '))
    pos = int(input('Ingrese POSICION: '))
    while(pos != -1):
        Lista.Insertar(elem,pos)
        Lista.Mostrar()
        elem = int(input('Ingrese elemento a insertar: '))
        pos = int(input('Ingrese POSICION: '))

            
            
                
                