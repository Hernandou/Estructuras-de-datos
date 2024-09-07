def Merge(arr):
    if(len(arr) == 1):
        return arr
    else:
        mitad = len(arr) // 2
        mitad_Izquierda = arr[:mitad]
        mitad_Derecha = arr[mitad:]
        
        mitad_Izquierda = Merge(mitad_Izquierda)
        mitad_Derecha = Merge(mitad_Derecha)
        
    return MergeSort(mitad_Izquierda,mitad_Derecha)
    
def MergeSort(Mitad_Izquierda,Mitad_Derecha):
    i=j=0
    arregloResultado = []
    
    while(i < len(Mitad_Izquierda) and j < len(Mitad_Derecha)):
        if(Mitad_Izquierda[i] < Mitad_Derecha[j]):
            arregloResultado.append(Mitad_Izquierda[i])
            i+=1
        else:
            arregloResultado.append(Mitad_Derecha[j])
            j+=1
        
    while(i < len(Mitad_Izquierda)):
        arregloResultado.append(Mitad_Izquierda[i])
        i+=1

    while(j < len(Mitad_Derecha)):
        arregloResultado.append(Mitad_Derecha[j])

        j+=1
    
    del Mitad_Derecha
    del Mitad_Izquierda
    
    return(arregloResultado)  
            

if __name__ == '__main__':

    arreglo = [8,2,5,32,24,60,1,4]    

    print('Arreglo Ordenado {}'.format(Merge(arreglo)))