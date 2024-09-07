class Nodo:
    __derecha = None
    __izquierda = None
    __elemento = None
    
    def __init__(self,elemento):
        self.__elemento = elemento
        self.__izquierda = None
        self.__derecha = None
        
    def setIzquierda(self,izquierda):
        self.__izquierda = izquierda
    
    def setDerecha(self,siguiente):
        self.__derecha = siguiente
        
    def setElemento(self,elemento):
        self.__elemento = elemento
        
    def getDerecha(self):
        return(self.__derecha)
    
    def getIzquierda(self):
        return(self.__izquierda)
    
    def getElemento(self):
        return(self.__elemento)
    
class ArbolB:
    __raiz = None
    
    def __init__(self):
        self.__raiz = None
        
    def Insertar(self, elemento, nodo=None):
        if self.__raiz == None:
            self.__raiz = Nodo(elemento)
            print('Asigna Raiz con {}'.format(elemento))
        else:
            if nodo == None:    #si no tiene nodos y solo tiene raiz
                nodo = self.__raiz
            
            if(elemento == nodo.getElemento()):
                print('Elemento ya existente')
            else:
                if(elemento < nodo.getElemento()):
                    if(nodo.getIzquierda() != None):
                        print('Busca izquierda')
                        self.Insertar(elemento,nodo.getIzquierda())
                    else:
                        print('Inserta izquierda {}'.format(elemento))
                        nodo.setIzquierda(Nodo(elemento))

            
                else:
                    if(nodo.getDerecha() != None):
                        print('Busca Derecha')
                        self.Insertar(elemento,nodo.getDerecha())
                    else:
                        print('Inserta Derecha {}'.format(elemento))
                        nodo.setDerecha(Nodo(elemento))
        
    def PreOrden(self, nodo=None):
        if nodo is None:
            nodo = self.__raiz

        if nodo is not None:
            print(nodo.getElemento())
            if(nodo.getIzquierda() != None):
                self.PreOrden(nodo.getIzquierda())
            
            if(nodo.getDerecha() != None):
                self.PreOrden(nodo.getDerecha())
        
    def InOrden(self,nodo=None):
        if(nodo == None):
            nodo = self.__raiz
        
        if(nodo != None):
            if(nodo.getIzquierda() != None):
                self.InOrden(nodo.getIzquierda())
                
            print(nodo.getElemento())
            if(nodo.getDerecha() != None):
                self.InOrden(nodo.getDerecha())
            
    def PostOrden(self,nodo = None):
        if(nodo == None):
            nodo = self.__raiz
        
        if(nodo != None):
            if(nodo.getIzquierda() != None):
                self.PostOrden(nodo.getIzquierda())
            
            if(nodo.getDerecha() != None):
                self.PostOrden(nodo.getDerecha())
            
            print(nodo.getElemento())
            
    def Buscar(self,elemento,nodo=None):
        if(nodo == None):
            nodo = self.__raiz
        else:
            if(nodo.getElemento() == elemento):
                return(elemento)
            else:
                pass
        
    def Frontera(self,nodo=None):
        if(nodo == None):
            nodo = self.__raiz
        
        if(nodo.getDerecha() != None and nodo.getIzquierda() != None):
            self.Frontera(nodo.getIzquierda())
            self.Frontera(nodo.getDerecha())
            
        else:
            print(nodo.getElemento())

    def Mostrar(self,nodo=None):
        if(nodo == None):
            nodo = self.__raiz
        else:
            print(nodo.getElemento())
            self.Mostrar(nodo.getIzquierda())
            self.Mostrar(nodo.getDerecha()) 
            
    def Altura(self,raiz):
 
        # Caso base: el árbol vacío tiene una altura de 0
        if raiz is None:
            return(1)
        # recurre para el subárbol izquierdo y derecho y considera la profundidad máxima
        return 1 + max(self.Altura(raiz.getIzquierda()), self.Altura(raiz.getDerecha()))

    def Hoja(self,elemento,nodo=None): #Queda Terminar
        if(nodo == None):
            nodo = self.__raiz
        else:
            if(nodo.getElemento() == elemento):
                if(nodo.getIzquierda() == None and nodo.getDerecha() == None):
                    return(True)
                else:
                    pass
                    
                                   
    def getRaiz(self):
        return(self.__raiz)
    
    

                
            
        
        
            

if __name__ == '__main__':
    arbolB = ArbolB()
    arbolB.Insertar(10)
    arbolB.Insertar(5)
    arbolB.Insertar(15)
    arbolB.Insertar(3)
    arbolB.Insertar(7)
    arbolB.Insertar(20)


    arbolB.Mostrar(arbolB.getRaiz())
    print('La altura del arbol es:',arbolB.Altura(arbolB.getRaiz()))
    print('PreOrden')
    arbolB.PreOrden()
    print('InOrden')
    arbolB.InOrden()
    print('PostOrden')
    arbolB.PostOrden()
    print('Frontera')
    arbolB.Frontera()