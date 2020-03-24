print ('Bienvenido al resolvedor de problemas estoicos')
print ("Respuestas validas afirmativas: y,n,in part")
print ("el problema esta bajo tu control?")
x = input("R:")

universal_solved = ("Utilízarlo para la práctica: sabiduria, justicia,templanza y coraje.")
virtue = ("¿concierne a tu virtud?")
indiferent = ("Es indiferente para ti?")
confront = ("prefieres o no afrontarlo?")
persist = ("persista por que el conflicto puede:")
avoid = ("evitese a menos que el conflicto pueda:")

if x == "y":
    print (virtue)
    x1 = input("R:")
    if x1 == "y":
        print (universal_solved)
    else:
        print (indiferent)
        print (confront)
        x11 = input ("R:")
        if x11 == "y":
            print (persist)
            print (universal_solved)
        else:
            print (avoid)
            print (universal_solved)

elif x == "in part":
    print ("qué concierne a nuestro horizonte de decisión?")
    print ("Que es mas importante, el intento o el resultado?")
    x2 = input ("R:")
    if x2 == "intento":
        print (virtue)
        x22 = input("R:")
        if x22 == "y":
            print (universal_solved)
        else:
            print (indiferent)
            print (confront)
            x3 = input ("R:")
            if x3 == "y":
                print (persist)
                print (universal_solved)
            else:
                print (avoid)
                print (universal_solved)
    else:
        print ("no hay nada por hacer")
    
else:
    print ("no hay nada por hacer")


#El diagrama comienza por la sencilla pregunta de si el dilema existencial al que nos enfrentamos 
#está o no bajo nuestro control. Si no, no hay nada qué hacer; si en parte, hay que saber distinguir 
#qué concierne a nuestro horizonte de decisión, si el intento o el resultado; si nos involucra por completo,
#la siguiente pregunta es si la decisión involucra a la virtud; si no, es en cierta forma indiferente para
#nuestra existencia y, si acaso el único momento de dilema es si dicha decisión entra en conflicto con la sabiduría,
#la justicia, la templanza o la valentía; si es una decisión que concierne de lleno a la virtud, un estoico
#te recomendaría tomarla para ejercer estos mismos valores.

#Al final, esto último es lo más sustancioso. Ante una decisión pregúntate si tomarla requerirá de tu sabiduría,
#tu sentido de la justicia, tu templanza o tu valentía, o si una vez tomada serás más sabio, más justo, más ecuánime
#o más valiente. Si la respuesta es afirmativa, ¡toma la decisión! Probablemente después descubrirás que hacerlo valió
#la pena, que tus temores no eran tan terribles como lo supusiste y, lo más importante, que seguramente tu carácter es 
#más fuerte de lo que creías.
