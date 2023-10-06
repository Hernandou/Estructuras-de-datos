from classPila import Pila


if __name__ == '__main__':
    Pila1 = Pila()
    Pila2 = Pila()
    Pila3 = Pila()
    contMov = 0
    a=True
    maximo = int(input('>> Ingrese cantidad de discos: '))
    aux= maximo
    while(aux != 0):
        Pila1.Agregar(aux)
        aux -= 1
    print('PILA 1')
    Pila1.Mostrar()
    
    while(a):
        ans_od = input('  >>Ingrese Pila origen y destino (O,D): ')
        ans = ans_od.split(',')
        
        #----------------------- ORIGEN PILA 1 ----------------------
        if(int(ans[0]) == 1):
            num = Pila1.getTope()
            
            if(int(ans[1]) == 2):
                if(Pila2.Vacio() == True): #Selecciona Destino Pila 2
                    val = Pila1.Eliminar()
                    Pila2.Agregar(val)
                    contMov += 1 
                else:
                    if(num < Pila2.getTope()):
                        val = Pila1.Eliminar()
                        Pila2.Agregar(val)
                        contMov+=1
                    else:
                        print('\n¡Error - No puede apilar un disco mas grande arriba de uno mas chico\n')
            elif(int(ans[1]) == 3): #Selecciona Destino Pila 3
                if(Pila3.Vacio() == True):
                    val = Pila1.Eliminar()
                    Pila3.Agregar(val)
                    contMov += 1
                else:
                    if(num < Pila3.getTope()):
                        val = Pila1.Eliminar
                        Pila3.Agregar(val)
                        contMov+=1
                    else:
                        print('\n¡Error - No puede apilar un disco mas grande arriba de uno mas chico\n')
            #--------------------- ORIGEN PILA 2 --------------
        if(int(ans[0]) == 2): 
            num = Pila2.getTope()
            if(int(ans[1]) == 1): #Selecciona Destino Pila 1
                if(Pila1.Vacio() == True):
                    val = Pila2.Eliminar()
                    Pila1.Agregar(val)
                    contMov+=1
                else:
                    if(num < Pila1.getTope()):
                        val = Pila2.Eliminar()
                        Pila1.Agregar(val)
                        contMov+=1
                    else:
                        print('\n¡Error - No puede apilar un disco mas grande arriba de uno mas chico\n')

            elif((int(ans[1]) == 3)): #Selecciona Destino Pila 3
                if(Pila3.Vacio() == True):
                        val = Pila2.Eliminar()
                        Pila3.Agregar(val)
                        contMov += 1
                else:
                    if(num < Pila3.getTope()):
                        val = Pila2.Eliminar()
                        Pila3.Agregar(val)
                        contMov+=1
                    else:
                        print('\n¡Error! - No puede apilar un disco mas grande arriba de uno mas chico\n')
            #--------------------- ORIGEN PILA 3 --------------
        if(int(ans[0]) == 3):
            num = Pila3.getTope()
                
            if(int(ans[1]) == 1): #Selecciona destino Pila 1
                
                if(Pila1.Vacio() == True):
                    val = Pila3.Eliminar()
                    Pila1.Agregar(val)
                    contMov+=1
                else:
                    if(num < Pila1.getTope()):
                        val = Pila3.Eliminar()
                        Pila1.Agregar(val)
                        contMov+=1
                    else:
                        print('\n¡Error - No puede apilar un disco mas grande arriba de uno mas chico\n')
            
            if(int(ans[1])==2): #Selecciona destino PILA 2
                num = Pila3.getTope()
                
                if(Pila2.Vacio() == True):
                    val = Pila3.Eliminar()
                    Pila2.Agregar(val)
                    contMov+=1
                else:
                    if(num < Pila2.getTope()):
                        val = Pila3.Eliminar()
                        Pila2.Agregar(val)
                        contMov+=1
                    else:
                        print('\n¡Error! - No puede apilar un disco mas grande arriba de uno mas chico\n')
        
        print('Pila 1')
        Pila1.Mostrar()
        print('Pila 2')
        Pila2.Mostrar()
        print('Pila 3')
        Pila3.Mostrar()

        if(Pila3.getTope() == 1 and Pila3.getContador() == maximo):
            a = False
            
    print('Juego terminado - Cantidad de movimientos {}, Cantidad minima de movimientos posibles: {}'.format(contMov,(2**maximo - 1)))
                    

                            
            
                
                        
                        
                        

    
