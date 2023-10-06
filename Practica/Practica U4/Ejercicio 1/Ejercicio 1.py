import math
class Nodo:

    __elemento = 0
    __izquierda = None
    __derecha = None
    
    def __init__(self,elemento):
        self.__derecha = None
        self.__izquierda = None
        self.__elemento = elemento
    
    def getElemento(self):
        return(self.__elemento)
    
    def setDerecha(self,derecha):
        self.__derecha = derecha
    
    def setIzquierda(self,izquierda):
        self.__izquierda = izquierda
        
    def getIzquierda(self):
        return(self.__izquierda)
    
    def getDerecha(self):
        return(self.__derecha)
    

class Arbol:
    
    __raiz = None
    
    def __init__(self):
        self.__raiz = None
        
    def Insertar(self,elemento,raiz=None):
        nodo = Nodo(elemento)
        
        if(self.__raiz == None):
            print('Inserta Raiz')
            self.__raiz = nodo
        else:
            if raiz==None:
                raiz = self.__raiz
                
            if(elemento > raiz.getElemento()):
                if(raiz.getDerecha() != None):
                    print('Busca derecha')
                    self.Insertar(elemento,raiz.getDerecha())
                else:
                    print('Asigna Nodo Derecha')
                    raiz.setDerecha(nodo)
                    return
            
            elif(elemento < raiz.getElemento()):
                if(raiz.getIzquierda() != None):
                    print('Busca Izquierda')
                    raiz = raiz.getIzquierda()
                    self.Insertar(elemento,raiz)
                else:
                    print('Inserta Izquierda')
                    raiz.setIzquierda(nodo)

    def Altura(self,raiz):
 
        # Caso base: el árbol vacío tiene una altura de 0
        if raiz is None:
            return(0)
        # recurre para el subárbol izquierdo y derecho y considera la profundidad máxima
        return 1 + max(self.Altura(raiz.getIzquierda()), self.Altura(raiz.getDerecha()))
        

    def getRaiz(self):
        return(self.__raiz)
    
    def Raiz(self):
        if(self.__raiz != None):
            return(self.__raiz.getElemento())
        else:
            print('No existe una raiz')
            
    def Buscar(self,elemento,raiz=None):
        
        if(self.__raiz != None):
            
            if raiz == None:
                raiz = self.__raiz
            
            if(elemento == raiz.getElemento()):
                if(elemento > raiz.getElemento()):
                    if(elemento == raiz.getElemento()):
                        self.Buscar(elemento,raiz.getDerecha())
                    else:
                        return(True)
                
                if(elemento < raiz.getElemento()):
                    if(elemento != raiz.getElemento()):
                        self.Buscar(elemento,raiz.getIzquierda())
                    else:
                        return(True)
            else:
                return(True)
            
        
    def Vacio(self):
        return(self.__raiz == None)
                

if __name__ == '__main__':
    
    arbol = Arbol()
    
    ans1 = int(input('>> Ingrese Elemento: '))
    
    while(ans1 != -1):
        arbol.Insertar(ans1)
        ans1 = int(input('>> Ingrese Elemento: '))
        
    if(arbol.Buscar(27)):
        print('Elemento encontrado')
    else:
        print('El elemento no existe')
    
    raiz = arbol.getRaiz()
    print('La altura del arbol es: ',arbol.Altura(raiz))
        
                
    
    