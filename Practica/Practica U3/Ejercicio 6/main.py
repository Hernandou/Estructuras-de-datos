import random
from classCola import Cola

def llegaCliente():
    a = False
    numero = random.randint(0,2)
    if(numero == random.randint(0,2)):
        a = True
    return(a)

if __name__ == '__main__':    
    Cola = Cola()
    caja = False
    tiempo_caja = int(input('>> Ingrese el Tiempo de caja: '))
    tiempo_Atencion = 0
    contPers = 0
    timepo_simulacion = int(input('>> Ingrese el tiempo de simulacion: '))
    
    for i in range(0,timepo_simulacion):
        
       if(llegaCliente()):
           Cola.Insertar(0)
           contPers += 1
        
       elif(caja is not False):
           if(Cola.Vacia() != None):
                Cola.Suprimir()
                Cola.actualizar()
                            
           elif (tiempo_Atencion < 5):
               tiempo_Atencion += 1
               
           elif(tiempo_Atencion == 5):
               caja = False   #Falta terminar
                
    
               