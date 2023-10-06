from classPila import Pila


if __name__ == '__main__':
    
    Pila = Pila()
    print('--------- Calculadora Factorial ---------')
    numero = int(input('>> Ingrese Numero: '))
    Pila.AgregarNumero(numero)
    a = True
    
    while(a):
        if(numero != 0):
            numero -= 1
            Pila.AgregarNumero(numero)
        else: 
            a = False
            
    print('El factorial de {} es: {}'.format(numero,Pila.resultado()))
    
    