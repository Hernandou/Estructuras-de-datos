from classNodo import Nodo
class Pila:
    
    __cabeza : None
    __tope = 0
    
    def __init__(self):
        self.__cabeza = None

    def Agregar(self,numero,modulo):
        
        if(self.__cabeza == None): #Ingresamos el elemento al principio de la pila si es None la cabeza
            obj = Nodo(numero,modulo)
            self.__cabeza = obj
            
        else: #Busca el ultimo elemento de la pila y lo inserta al final
            actual = self.__cabeza
            while(actual.getSiguiente() != None):
                actual = actual.getSiguiente()
                
            obj = Nodo(numero,modulo)
            actual.setSiguiente(obj)
                
    def recorrerModulo(self):
        aux = self.__cabeza
        cadena = ''
        
        while(aux != None):
            cadena += str(aux.getModulo())
            aux = aux.getSiguiente()
        
        return(cadena)  
                