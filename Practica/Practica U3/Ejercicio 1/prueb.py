from classSecuencial import Secuencial

if __name__ == '__main__':

    maxim = int(input('>> Ingrese dimension de la pila: '))
    Lista = Secuencial(maxim)
    
    #for i in range(0,maxim):
    #    Lista.Insertar(i)
               
    print(Lista.mostrar())
    Lista.Eliminar()
    print(Lista.mostrar())
    print('¿La lista esta vacia? : {}'.format(Lista.Vacio()))