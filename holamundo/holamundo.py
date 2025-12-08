import random

def jugar ():
    opciones = ["piedra", "papel","tijera"]

    print("elige una opcion:")
    print("1. piedra")
    print("2. papel")
    print("3. tijera")

    eleccion_jugador=int(input("Introduce un numero (1-3):"))
    jugador=opciones [eleccion_jugador-1]

    maquina = random.choice(opciones)

    print(f"\\Tu elegiste: {jugador}")
    print(f"\\La maquina: {maquina}")

    match (jugador, maquina):
        case(x,y) if x==y: 
            print ("Empate")
        case ("piedra", "tijera"):
            print ("Ganaste")
        case ("tijera", "papel"):
            print ("Ganaste")
        case ("papel", "piedra"):
            print ("Ganaste")
        case _:
            print("Perdiste")
    
if __name__ == "__main__":
         jugar()