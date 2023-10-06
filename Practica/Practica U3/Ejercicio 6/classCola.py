from classElemento import Elemento
 
class Cola:
    
    __cabeza : int
    __tope : int
    
    def __init__(self):
        self.__cabeza = None
        self.__tope = None
    
    def Insertar(self,elemento):
        obj = Elemento(elemento)
        
        if(self.__cabeza == None):
            self.__cabeza = obj
            self.__tope = obj
        else:
            self.__tope.setSiguiente(obj)
            self.__tope = obj
    
    def Suprimir(self):
        aux = self.__cabeza
        self.__cabeza.setSiguiente(self.__cabeza.getSiguiente())
        del(aux)
        
    def Vacia(self):
        return(self.__cabeza == None)
    
    def actualizar(self):
        aux = self.__cabeza
        while(aux != None):
            aux.__setNumero(aux.__getNumero()+1)
            aux.__getSiguiente(3)
