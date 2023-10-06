import numpy as np
import random
from classListaArray import Lista

if __name__ == '__main__':
    num = int(input('Ingrese longitud de la lista: '))
    Lista = Lista(num)
    a = True
    i=0
    
    while(a):
        num2 = int(input('Ingrese posicion a insertar: '))
        val = int(input('Ingrese valor a insertar: '))
        Lista.AgregarElemento(num2,val)
        i+=1
        if(i>num):
            ans = input('¿Desea seguir cargando datos? Y/N: ')
            if(ans=='N' or ans == 'n'):
                a = False
                
    Lista.Mostrar()
    ans = int(input('Ingrese posicion del elemento a suprimir: '))
    Lista.Eliminar(ans)
    Lista.Mostrar()
    
    