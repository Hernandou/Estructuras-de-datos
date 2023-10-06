class Nodo:
    
    __ocurrencias = None
    __letra = ''
    __siguiente = None
    __derecha = None
    __izquierda = None
    __altura = 0    
    def __init__(self,ocurrencia,letra):
        self.__ocurrencias = ocurrencia
        self.__letra = letra
        self.__siguiente = None
        self.__derecha = None
        self.__izquierda = None
        self.__altura = 0
        
    def getDerecha(self):
        return(self.__derecha)
    
    def getIzquierda(self):
        return(self.__izquierda)
    
    def getLetra(self):
        return(self.__letra)        
    
    def getOcurrencias(self):
        return(self.__ocurrencias)
    
    def getSiguiente(self):
        return(self.__siguiente)
    
    def setDerecha(self,derecha):
        self.__derecha = derecha
        
    def setLetra(self,letra):
        self.__letra = letra
        
    def setIzquierda(self,izquierda):
        self.__izquierda = izquierda
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

        
class Arbol:
    
    __raiz = None
    
    def __init__(self):
        self.__raiz = None
        
    def Insertar(self,elemento,letra,nodo=None):
        if(nodo == None):
            nodo = Nodo(elemento,letra)
        else:
            elemento = nodo.getOcurrencias()
            letra = nodo.getLetra()
            
        if((self.__raiz is None) or (elemento <= self.__raiz.getOcurrencias())):
            print('Inserta {} con ocurrencia: {}'.format(letra,elemento))
            nodo.setSiguiente(self.__raiz)
            self.__raiz = nodo
            
        else:
                aux = self.__raiz.getSiguiente()
                anterior = self.__raiz
                
                while(aux is not None and elemento > aux.getOcurrencias()):
                    anterior = aux
                    aux = aux.getSiguiente()

                print('Inserta {} con ocurrencia: {}'.format(letra,elemento))
                nodo.setSiguiente(aux)
                anterior.setSiguiente(nodo)
     
    def OrganizarNodos(self,raiz = None):
        if(raiz == None):
            return
        else:
            anterior = raiz
            raiz = anterior.getSiguiente()
            
            if(anterior != None and raiz != None):
                if(anterior.getOcurrencias() <= raiz.getOcurrencias()):
                    nodo = Nodo(anterior.getOcurrencias()+raiz.getOcurrencias(),anterior.getLetra()+raiz.getLetra())
                    nodo.setDerecha(raiz)
                    nodo.setIzquierda(anterior)
                    cabeza = raiz.getSiguiente()
                    self.setRaiz(cabeza)
                    self.Insertar(0,'',nodo)
                    self.OrganizarNodos(cabeza)
                else:
                    nodo = Nodo(anterior.getOcurrencias()+raiz.getOcurrencias(),anterior.getLetra()+raiz.getLetra())
                    nodo.setIzquierda(raiz)
                    nodo.setDerecha(anterior)
                    cabeza = raiz.getSiguiente()
                    self.setRaiz(cabeza)
                    self.Insertar(0,'',nodo)
                    self.OrganizarNodos(cabeza)
                    
        return
                
    def MostrarLista(self):
        aux = self.__raiz
        i = 0
        while(aux != None):
            print('Nodo {}\n Letra: {} Ocurrencia: {}'.format(i,aux.getLetra(),aux.getOcurrencias()))
            aux = aux.getSiguiente()
            i+=1
    
    def MostrarArbol(self,raiz=__raiz):
        print(raiz)
        
            
    def Altura(self,raiz):
        if(raiz.getDerecha() == None and raiz.getIzquierda() == None): #Es una hoja
            return 0
        else:
            izquierda=0
            derecha=0
            
            if(raiz.getIzquierda() != None):
                derecha = self.Altura(raiz.getIzquierda())
            
            if(raiz.getDerecha() != None):
                izquierda = self.Altura(raiz.getDerecha())
            return 1 + max(izquierda,derecha)
            
    def inOrden(self,raiz=None):
        if(raiz == None):
            return
        else:
            if(raiz.getIzquierda() != None):
                pass

    def getRaiz(self):
        return(self.__raiz)
    
    def setRaiz(self,raiz):
        self.__raiz = raiz
        
      
if __name__ == '__main__':
    Arbolito = Arbol()
    ListaCaract = []
    cont = 0
    with open('/Users/hernan/Desktop/UNSJ/Segundo Año/Estructuras de datos/Practica/Practica U4/Ejercicio 1/Ejercicio 2.py/Lorem Ipsum.txt', mode ='r') as archivo:
        palabra = archivo.readline()           
    
    for j in range(len(palabra)):
        if(palabra[j] not in ListaCaract):
            ListaCaract.append(palabra[j])
    print('Caracteres detectados: ',ListaCaract) 
    
    for i in ListaCaract:
        cont = 0
        for j in palabra:
            if(i == j):
                cont+=1
        Arbolito.Insertar(cont,i)

    Arbolito.MostrarLista()
    raiz = Arbolito.getRaiz()
    Arbolito.OrganizarNodos(raiz)
    raiz = Arbolito.getRaiz()
    print('Cabeza : ',raiz.getLetra())
    print('----------')
    Arbolito.MostrarLista()
    print('Altura: ',Arbolito.Altura(raiz))
    #print(Arbolito.MostrarArbol())