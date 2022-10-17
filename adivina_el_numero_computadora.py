import random

def adivina_el_numero_computadora(x):
    
    print("""============================""")
    print("""   ¡Bienvenido/a al juego! """)
    print("""============================""")
    print(f'Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo')
    
    
    limite_inferior = 1 # intervalo [1, x]
    limite_superior = x
    
    respuesta = ''
    
    while respuesta != 'c':
        # Generar prediccion 
        
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # también podría ser el límite superior
            
        # Obtener respuesta del usuario
        
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
    
        if respuesta == 'a':
            limite_superior = prediccion - 1
        elif respuesta == 'b':
            limite_inferior = prediccion + 1
          
        # Intervalo inicial : [1, 10]
        # prediccion: 6
        # respuesta: b
        # intervalo: [7, 10]
        
        
    print(f'¡ Siiiii! La comutadora adivinó tu número correctamente: {prediccion}')  
        
   
adivina_el_numero_computadora(10)
    