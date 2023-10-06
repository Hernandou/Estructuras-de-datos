import numpy as np
class Cola:
    
    __cola = []
    __ultimo = 0
    __primer = 0
    __cantidad = 0
    __max = 0
    
    def __init__(self,num=0):
        self.__cola = np.empty(num,dtype=int)
        self.__ultimo = 0
        self.__primer = 0
        self.__max = num
        self.__cantidad = 0
        
    def Insertar(self,elemento):
        if(self.__cantidad < self.__max):
            self.__cola[self.__ultimo] = elemento
            self.__ultimo += 1 % self.__max #Calculo raro
            self.__cantidad+=1
                
    def Vacio(self):
        return(self.__cola[self.__primer] == None)
    
    def Suprimir(self):
        
        if(self.Vacio() != None):
            aux = self.__cola[self.__primer]
            self.__cola = np.delete(self.__cola,self.__primer)
            self.__primer +=1 
            return(aux)   
        else:
            print('Error Cola vacia')
            
    def Mostrar(self):
        j = self.__primer
        a = True
        while(a):
            if(j < self.__max):
                print('Elemento ',j)
                print(self.__cola[j])
                j+=1
            else:
                a = False
            
        

if __name__ == '__main__':    
    ans1 = int(input(' >> Ingrese longitud de la cola: '))
    Cola = Cola(ans1)

    i=0
    while(i < ans1):
        ans2 = int(input(' >> Ingrese elemento a insertar: '))
        Cola.Insertar(ans2)
        i+=1
    
    Cola.Mostrar()
    Cola.Suprimir()
    print('------')
    Cola.Mostrar()
