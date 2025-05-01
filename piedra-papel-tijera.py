nombre1 = input("Como se llamara el jugador 1")
nombre2 = input("Como se llamara el jugador 2")



jugador1 = input("Hola Jugador 1 ! que eliges piedra, papel o tijera?" )
jugador2 = input("Hola Jugador 2 ! que eliges piedra, papel o tijera?" )

condicion1 = jugador1 == "Piedra" and jugador2 == "tijera" 
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 =  jugador1 == "Tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
      print("ha ganado el jugador", nombre1)
else:
    print("ha ganado el jugador", nombre2)