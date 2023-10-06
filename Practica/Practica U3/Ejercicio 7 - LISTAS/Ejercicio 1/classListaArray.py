import numpy as np
from classNodo import Nodo

class Lista:
    
    __lista : None
    __contador = 0
    def __init__(self,num=0):
        self.__lista = np.empty(num,dtype = Nodo)
        self.__pr = 0
        self.__ult = 0
        self.__contador = 0
        
    def AgregarElemento(self,posicion,numero):
        nuevo = Nodo(numero)
        if(posicion == 0): #Entra en 0
            print('Entra en la primera posicion')
            self.__lista[posicion] = nuevo
            self.__pr = nuevo
            self.__contador += 1
            
        elif(posicion == self.__contador): #Entra en posicion > lista
            print('Entra mayor a lista')
            self.__lista.resize(len(self.__lista)+1)
            self.__lista[posicion] = nuevo
            self.__ult = nuevo
            self.__contador += 1
            
        elif posicion < len(self.__lista): #Entra en el medio
            if((self.__lista[posicion-1] != None)):
                self.__lista[posicion] = nuevo
                print(self.__lista[posicion].getNumero())
                self.__contador += 1
                print('Elemento insertado en la posicion: ',posicion-1)
            else:
                print('Este elemento no puede ser insertado en esta posicion')
            
    def Vacio(self):
        return(self.__lista[0] == None)
    
    def Mostrar(self):
        i=0
        while(i<self.__contador):
            if(self.__lista[i] is not None):
                print(self.__lista[i].getNumero())
            else:
                print(None)
            i+=1

    def UltimoElemento(self):
        return(self.__lista[-1])
    
    def PrimerElemento(self):
        return(self.__lista[0])
    
    def Eliminar(self,posicion):
        i=0
        if(not self.Vacio()):
            self.__lista[posicion] = None
            self.__contador -=1
        else:
            print('No se puede suprimir, la lista esta vacia')
            
    def Recuperar(self,posicion):
        aux = None
        if(not self.Vacio()):
            aux = self.__lista[posicion]
        return(aux)
            
    def Siguiente(self,elemento):
        i=0
        while(self.__lista[i] != elemento):
            self.__lista[i]
            i+=1
        if(i+1 <= self.__contador):
            aux = self.__lista[i+1].getNumero()
        
        return(aux)
            
    def Anterior(self,elemento):
        i=0
        if(self.__lista[elemento-1] != None):
            while(self.__lista[i] != elemento):
                pass
            
                    
        
            
                
                
             
                
                 
            
