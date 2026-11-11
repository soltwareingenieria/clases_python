# En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
# Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#  ¿Colon descubrió América?
#  ¿La independencia de México fue en el año 1810?
#  ¿The Doors fue un grupo de rock Americano?
print ("RESPONDE CORRECTAMENTE TODAS LAS PREGUNTAS PARA GANAR EL JUEGO")
pregunta_1=input("¿Colon descubrió América? si/no ").upper()
if pregunta_1=="SI" :
    print ("CORRECTO, SIGUIENTE PREGUNTA")
    pregunta_2 = input("¿La independencia de México fue en el año 1810? ").upper()

    if pregunta_2=="SI" :
        print ("CORRECTO, SIGUIENTE PREGUNTA")
        pregunta_3 = input("¿The Doors fue un grupo de rock Americano? ").upper()
        if pregunta_3 == "SI":
            print ("GANASTE EL JUEGO")
        else: 
            print ("perdiste el juego")
    else:
        print ("perdiste el juego")
else:
    print ("perdiste el juego")
