from classNodo import Nodo

class Pila:
    
    __tope  : object
    
    def __init__(self):
        self.__tope = None
        self.__contador = 0
        
    def Agregar(self,num):
        nuevo = Nodo(num)
        nuevo.setSiguiente(self.__tope)
        self.__tope = nuevo
        self.__contador+=1
    
    def Eliminar(self):
        if(self.Vacio() != True):
            aux = self.__tope
            auxnum = self.__tope.getNumero()
            self.__tope = self.__tope.getSiguiente()
            del(aux)
            self.__contador -=1
        return(auxnum)
    
    def getTope(self):
        a : int
        a=0
        if(self.__tope != None):
            a = self.__tope.getNumero()
        return(a)
    
    def getContador(self):
        return(self.__contador)
            
    def Mostrar(self):
        aux = self.__tope
        if(self.__tope != None):
            while(self.__tope.getSiguiente() != None):
                print('|{}|\t'.format(self.__tope.getNumero()))
                self.__tope = self.__tope.getSiguiente()
            print('|{}|\t'.format(self.__tope.getNumero()))
            self.__tope = aux
            
        
    def Vacio(self):
        return(self.__contador == 0)
    
            
            

            

        
        
            
            
        