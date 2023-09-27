import random


def adivina_el_numero_pc (x):
    print('==========================')
    print('¡Bienvenido al nuevo juego!')
    print('==========================')
    print(f'Selecciona un número entre 1 y {x} para que la compu intente adivinarlo.')
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ''
    
    while respuesta != 'c':
        #Generar prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint (limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
        #Obtener respuesta del usuario    
        respuesta = input(f'Mi prediccion es: {prediccion}. Si el número que tienes en mente es más bajo que mi predicción ingresa (A). Si el número que tienes en mente es mas alto que mi predicción, ingresa (B). Si es el correcto, ingresa (C): ').lower()
        
        if respuesta == 'a':
            limite_superior = prediccion -1 
        elif respuesta == 'b':
            limite_inferior = prediccion + 1
        
    print (f'¡He adivinado tu número correctamente! El número era {prediccion}. ¡Muchas gracias por jugar!')
    


adivina_el_numero_pc(18)
