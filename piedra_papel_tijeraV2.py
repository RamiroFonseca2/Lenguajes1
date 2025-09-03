# piedra_papel_tijera.py
import random
opciones = ["piedra", "papel", "tijera"]
print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")

def validarResultado(usuario,pc):
    if(usuario == "piedra" and pc == "tijera") or (usuario == "papel" and pc == "piedra") or (usuario == "tijera" and pc == "papel"):
        return True
    else:
        return False
        

ronda = 1
rondas_totales=5        #Modificacion
rondas_ganar = (rondas_totales //2) + 1 
puntos_usuario = 0
puntos_pc = 0
while (ronda <= rondas_totales):    #Modificacion
    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()
    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.")
        continue # no cuenta la ronda si la entrada es inválida
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate.")
        ronda-=1                                                        #No cuenta la ronda si es empate
    elif (validarResultado(jugada_usuario,jugada_pc)):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
        if (puntos_usuario >=rondas_ganar):
            break
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
        if(puntos_pc >=rondas_ganar):
            break
    
    ronda += 1
print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC:{puntos_pc}")
if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")