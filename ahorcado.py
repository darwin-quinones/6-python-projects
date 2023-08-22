from operator import le
import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(lista_palabras):
    # Seleccionar una palabra al azar de la lista de palabras validas
    palabra = random.choice(lista_palabras)
    
    # elegir palabras son - y espacios
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)

    return palabra.upper()


def ahorcado():
    
    
    print("""============================""")
    print("""   ¡Bienvenido/a al juego del Ahorcado! """)
    print("""============================""")
    
    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) 
    # conjunto set
    # 'pythoon' = {'p', 'y', 't', 'h', 'o', 'n'}
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # letras adivinadas 
        # ' '.join({'A', 'B', 'C'}) -> 'A B C'
        
        print(f'Te quedan {vidas} vidas y has usado estás letras: {" ".join(letras_adivinadas)}')
        
        # Estado actual de la palabra (list comprehension) H-LA, S-MA-A
        # 
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # mostrar las letras separadas por un espacio
        print(f'Palabra: {" ".join(palabra_lista)}')
        
        letra_usuario = input('Escoge una letra: ').upper()
        
        # si la letra escogida por el usuario está en el abecedario 
        # y no está en el conjunto de letras que ya se han ingresado,  
        # se añade la letra al conjunto de letras ingresadas.
        
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            # si la letra está en la palabra, quitar la letra del conjento 
            # de letras pendientes por adivinar.
            # si no está en la palabra, quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                # vidad = vidad -1
                vidas -= 1
                print(f'\n Tu letra {letra_usuario} no está en la palabra')
                
        # si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            
            print('\n Ya escogiste esa letra. Por favor escoge otra')
        else:
            print('Esta letra no es válida.')
            
    # El juego llega aqui cuando se adivinan todas las 
    # letras de la palabra o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f'¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era : {palabra}')
        
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')
        
ahorcado()