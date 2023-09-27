import random

def jugar():
    print ('===================================')
    print ('Bienvenido al piedra papel o tijera')
    print ('===================================')
    
    
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel y 'ti' para tijera. \n ").lower()
    computadora = random.choice(['pi','pa', 'ti'])
    
    if usuario == computadora:
        return '¡Empate!'
    
    if gano_el_jugador(usuario, computadora):
        
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def gano_el_jugador (jugador, oponente):
    
    # Retornar True si gana o gano el jugador
    # Piedra gana a tijera
    #Tijera gana a papel
    #Papel gana a tijera
    if ((jugador == 'pi' and oponente == 'ti')or
        (jugador == 'ti' and oponente == 'pa')or
        (jugador == 'pa' and oponente == 'ti')):
        return True
    else:
        return False
    
    
    
print(jugar())
    
    
    