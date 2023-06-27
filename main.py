import random

# Lista de palabras predefinidas
palabras = ['python', 'programacion', 'ahorcado', 'juego', 'variables', 'pseint', 'pseudoclases', 'tupla', 'cadenas', 'buleanos']

# Función para seleccionar una palabra aleatoria
def seleccionar_palabra():
    return random.choice(palabras)

# Función para mostrar la figura del ahorcado
def mostrar_ahorcado(intentos):
    figura = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(figura[intentos])

# Función para adivinar la palabra
def adivinar_palabra(palabra):
    palabra_adivinada = ['_'] * len(palabra)
    intentos = 0
    letras_adivinadas = []

    while True:
        mostrar_ahorcado(intentos)
        print("\nPalabra:", ' '.join(palabra_adivinada))
        letra = input("Ingresa una letra: ").lower()
        print("Letras utilizadas:", ', '.join(letras_adivinadas))

        if letra in letras_adivinadas:
            print("Ya ingresaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos += 1
            #mostrar_ahorcado(intentos)
            print("Letras utilizadas:", ', '.join(letras_adivinadas))

        if ''.join(palabra_adivinada) == palabra:
            print("\n¡Felicidades! ¡Adivinaste la palabra!")
            print("La palabra era:", palabra)
            return True

        if intentos == 6:
            print("\n¡Que pena! Perdiste!.")
            print("La palabra era:", palabra)
            return False

# Función principal
def jugar_ahorcado():
    print("Bienvenido al juego del Ahorcado!")
    puntuacion = {
        'adivinanzas_correctas': 0,
        'adivinanzas_incorrectas': 0
    }


    while True:
        palabra = seleccionar_palabra()
        print("\nNueva partida. Adivina la palabra:")
        if adivinar_palabra(palabra):
            puntuacion['adivinanzas_correctas'] += 1
        else:
            puntuacion['adivinanzas_incorrectas'] += 1

        print("\nPuntuación actual")
        print("\nAdivinanzas correctas:", puntuacion['adivinanzas_correctas'])
        print("Adivinanzas incorrectas:", puntuacion['adivinanzas_incorrectas'])

        continuar = input("\n¿Deseas jugar otra partida? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nGracias por jugar al Ahorcado! \nVuelva Prontos!")

# Iniciar el juego
jugar_ahorcado()

# Esta aplicación permite jugar al juego del "Ahorcado" en la consola. Se selecciona una palabra aleatoria de una lista predefinida y el jugador debe adivinarla ingresando letras. La figura del ahorcado se muestra progresivamente a medida que el jugador adivina letras incorrectas. El juego finaliza cuando el jugador adivina la palabra o se completa la figura del ahorcado. También se lleva un registro de la puntuación del jugador, contabilizando el número de adivinanzas correctas e incorrectas.