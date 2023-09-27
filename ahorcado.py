import random
import string 

from palabras import palabras 
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    #seleccionar una palabra al azar de la lista de palabras validas
    palabra = random.choice(palabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        
    return palabra.upper()
    
    

def ahorcado ():
    
    
    print ('++++++++++++++++++++++++++++++++++')
    print ('¡Bienvenido al juego del ahorcado!')
    print ('++++++++++++++++++++++++++++++++++')
    
    
    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar= set(palabra)
    letras_adivinadas= set()
    abecedario= set(string.ascii_uppercase) #no contiene la ñ
    
    vidas = 7
    
    while len (letras_por_adivinar) > 0 and vidas > 0:
        
        print (f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        #Mostrar el estado actual de la palabra
        
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostrar estado del ahorcado
        print (vidas_diccionario_visual [vidas])
        #Mostrar letras separadas por un espacio. 
        print (f"Palabra: {' '.join(palabra_lista)} ")
        
        letra_usuario = input ("Elegí una letra: ").upper()
        # Si la letra elegida por el usuario esta en el abecedario y no esta en el
        #conjunto de letras que ya se han ingresado se agrega la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #La letra estaba en la palabra?
            #Si la letra esta en la palabra remover la letra del conjunto de letras pendiente de adivinar, si no esta en la palabra quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas-1
                print(f'\nTu letra {letra_usuario} no esta en la palabra.')
        #Si la letra elegida por el usuario fue ingresada        
        elif letra_usuario in letras_adivinadas:
            print("\nYa elegiste esa letra. Por favor elige otra")
            
        else:
            print("\nEsta letra no es válida.")
            
    #Se adivinan todas las letras o se agotan las vidas
    if vidas==0:
        print(vidas_diccionario_visual [vidas])
        print(f"¡ESTAS AHORCADO! ¡PERDISTE!. Lo lamento mucho, la palabra era: {palabra}")
        
    else:
        print( f"¡HAS GANADO! ¡SOS UN CRACK! ¡ADIVINASTE LA PALABRA {palabra}!")
        
ahorcado()        
            