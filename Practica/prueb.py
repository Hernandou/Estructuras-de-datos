import numpy as np
class GrafoDir:
    __matriz= None
    __cantidad = 0
    __nodos = None
    __caminos = None
    
    def __init__(self,nodos,arcos):
        self.__cantidad = len(nodos)
        self.__nodos = nodos
        self.__matriz = np.zeros((self.__cantidad,self.__cantidad),dtype=int)
        
        for tupla in arcos:
            nodo1 = self.__nodos.index(tupla[0])
            nodo2 = self.__nodos.index(tupla[1])
            
            self.__matriz[nodo1][nodo2] = 1
            
    def setCamino(self,cam):
        self.__caminos = cam

    def Camino(self,nodo1,nodo2,visitados=[]):
        fila = self.__nodos.index(nodo1)
        if(nodo1 not in visitados):
            visitados.append(nodo1)
        
        if(nodo1 == nodo2):
            return 
        else:
            for i in range(self.__cantidad):
                if(self.__matriz[fila][i] == 1):
                    self.setCamino(visitados)
                    self.Camino(self.__nodos[i],nodo2,visitados)
        return visitados
            


if __name__ == '__main__':
    nodos = ['a','b','c','d','e']
    arcos = [('b','d'),('d','a'),('a','c')]
    
    grafo = GrafoDir(nodos,arcos)
    print(grafo.Camino('b','c'))
    