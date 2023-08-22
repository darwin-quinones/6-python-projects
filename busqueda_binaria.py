
# algoritmo de busqueda ingenua: 
# buscar elemento por elemento(secuencia) luego busqueda binaria

import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        # range(len(lista)) -> 0, 1, 2, 3, ... len(lista) - 1
        
        if lista[i] == objetivo:
            return i
    return -1

# argumento
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8] 

#print(busqueda_ingenua(mi_lista, 10)) # parametros

# algotimo de busqueda binaria: es mucho más rapido

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # inicio lista
    if limite_superior is None:
        limite_superior = len(lista) - 1 # fin lista
        
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior) // 2 # dividir y retorna entero
    
    # [1, 3, 5, 10, 12]
    #  0  1  2  3  4 indices
    # punto_medio = (0 + 4) // 2 = 4 // 2 = 2
    
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)
    
    
    
    
if __name__ == '__main__':
    # mi_lista = [1, 3, 5, 10, 12]
    # print(busqueda_binaria(mi_lista, 129))
    
    # crear unalista ordenada con 10000 numeros aleatorios
    tamaño = 10000
    conjunto_inicial = set()
    
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        
    lista_ordenada = sorted(list(conjunto_inicial)) # lista ordenada
    
    # medir el tiempo de busqueda inguenua
    inicio = time.time()  
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f'Tiempo de búsqueda ingenua: {fin - inicio} segundos')
    
    # medir el tiempo de busqueda binaria 
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f'Tiempo de búsqueda binaria : {fin - inicio} segundos')