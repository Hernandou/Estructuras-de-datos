from classNodo import Nodo
class Lista:
   
   __ultimo : int
   __cabeza : object
   
   def __init__(self):
       self.__cabeza = None
       self.__ultimo = 0
    
   def Insertar(self,elem,posicion):
        nuevo = Nodo(elem)
         
        if(posicion >= 0 and posicion <= self.__ultimo+1):
            aux = self.__cabeza
            i =  1
            while(aux.getSiguiente() != None and i<= posicion-1):
               aux = aux.setSiguiente()
               i+=1
            
            nuevo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nuevo)
                
                
           
                
                
                
                        
                        
                        
                
                
                
                
        