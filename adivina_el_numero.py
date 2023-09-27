import random

def adivina_el_numero (x):
    print('========================================')
    print('Bienvenido al juego de adivina el numero')
    print('========================================')
    print('Tu objetivo es adivinar un numero generado por la computadora.')
    
    numero_aleatorio = random.randint(1,x) #numero aleatorio entre 1 y x
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        #el usuario ingresa un numero
        prediccion = int(input(f'Adivina un numero entre 1 y {x}: '))
        
        if prediccion < numero_aleatorio:
            print('El numero ingresado es menor al numero que debe adivinar')
        elif prediccion > numero_aleatorio:
            print('El numero ingresado es mayor al numero que debe adivinar')
            
            
            
    print(f'¡Felicitaciones! ¡Usted ha adivinado el número {numero_aleatorio} correctamente!')
    
adivina_el_numero(100)
