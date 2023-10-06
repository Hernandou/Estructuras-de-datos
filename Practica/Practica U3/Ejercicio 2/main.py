from classPila import Pila
import math



if __name__ == '__main__':
    
    Pila = Pila()
    
    numero = int(input('>> Ingresar numero decimal: '))
    resp = numero
    mod = 0
    a = True
    
    while(a):
        if(numero != 1):
            mod = numero % 2
            math.trunc(mod)
            Pila.Agregar(numero,mod)
            numero = math.trunc(numero/2)
            
        else:
            Pila.Agregar(1,1)
            a = False
    
    print('         El numero {} (decimal) = {} (Binario)'.format(resp,Pila.recorrerModulo()))
    #Falta ver como mostrar la pila de forma inversa
    

        
    

        




