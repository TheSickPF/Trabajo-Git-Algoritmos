#Horas escritas en este codigo: 1

    #Nacho te recomienda:

DS = ["Kirby: Super Star Ultra" , "Mario & Luigi: Partners in Time" , "Mario Kart DS" , "Mario Party DS" , "New Super Mario Bros." , "Phoenix Wright: Ace Attorney" , "Pokemon Black 2" , "Pokemon Pearl" , "Sonic Chronicles" , "Sonic Rush" , "Super Mario 64 DS" , "Wario Ware: Touched!" , "Yoshi's Island DS"]
cant_juegos = len(DS)
var_1 = str(input("Elige una consola! (Por el momento unicamente disponible la Nintendo DS) "))

if var_1 == "DS" or var_1 == "Nintendo DS" or var_1 == "NDS" or var_1 == "nds" or var_1 == "nintendo ds" or var_1 == "ds":
    print("¡Elige entre uno de estos tantos juegos para que el autor de este codigo te de una reseña!")
    for i in range(0, cant_juegos):
        print(DS[i])
    print(f"PD: Debes agarrar y copiar el nombre, ya que el codigo no funcionara si el nombre del juego no esta completo (-v-)")
    selector = str(input())
    if selector == "Kirby: Super Star Ultra":
        print("Kirby: Super Star Ultra es un remake del videojuego Kirby: Super Star, lanzado para la Super Nintendo. Nunca tuve la oportunidad de jugarlo legalmente, asi que me dedicaba a emularlo o simplemente jugarlo en modo descarga con un amigo, pero pese a eso, el juego es excelente. Es entretenido para pasar el rato solo, o incluso de 2 jugadores, ya que tiene posibilidad de Multijugador. 9/10 :>")
    elif selector == "Mario & Luigi: Partners in Time":
        print("Fue mi primer acercamiento con la saga, y uno de los mejores recuerdos de mi yo de 8 años, para ese momento ya existia la 3DS, pero tuve la oportunidad de jugarlo porque un amigo se habia ido de vacaciones y me dejo encargado de su consola y su R4. No tenia archivos de guardado y el juego estaba en ingles, pero eso no me impidio disfrutar de la experiencia. Pese a la historia ser un poco enredada, sigue siendo muy disfrutable en la actualidad. 8/10 (^.^)")

    elif selector == "Mario Kart DS":
        print("Uno de los mejores juegos de la consola, cualquier persona que tuviera una DS lo tenia, o lo habia jugado. La mejor experiencia single-player de un Mario Kart, la posibilidad de jugar entre 8 personas con un solo cartucho, y mi primer acercamiento a la saga. 10/10.")

    elif selector == "Mario Party DS":
        print("Uno de los mejores (si es que no el mejor) Mario Party que haya existido, lo tiene todo. Los mejores minijuegos, el mejor modo de un solo jugador, uno de los mejores multijugador, y mas encima, gracias al modo descarga de la DS se podian reunir 4 personas a jugar con un solo cartucho. 9/10 o.o")

    elif selector == "New Super Mario Bros.":
        print("Mi primer juego propio, y el que me llevo al mundo de las consolas. Ya habia tenido un acercamiento a Mario, con tan solo 2 o 3 años de edad, pero recibir este juego, junto con la consola, fue un mundo nuevo para mi. Desde entonces nunca más he vuelto a soltar las consolas y los videojuegos en general, muchas gracias Mario por todos estos años de alegria. 10/10")

    elif selector == "Phoenix Wright: Ace Attorney":
        print("")

    elif selector == "Pokemon Black 2":
        print("")

    elif selector == "Pokemon Pearl":
        print("")

    elif selector == "Sonic Chronicles":
        print("")
    
    elif selector == "Sonic Rush":
        print("")

    elif selector == "Super Mario 64 DS":
        print("")

    elif selector == "Wario Ware: Touched!":
        print("")

    elif selector == "Yoshi's Island DS":
        print("")

    else:
        print("El juego aún no esta disponible, o simplemente no existe... (En esta consola, o quizas simplemente no exista en verdad.)")
elif var_1 == "Kasane Teto" or var_1 == "Teto" or var_1 == "teto" or var_1 == "tEto" or var_1 == "TEtO" or var_1 == "TetO" or var_1 == "kasane teto":
    print("No es una consola, pero usted tiene buenos gustos. Sus taladros son bastante atractivos y me traen buenos recuerdos de una serie que vi hace algún tiempo...")

else:
    print(f"Esta consola no esta disponible por el momento, o directamente no existe...")



