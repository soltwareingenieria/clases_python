#Escribe un programa que decida si se aprueba un crédito. Primero pide la edad (entero). Si es menor de 18, debe mostrar No cumples la edad mínima. Si tiene 18 años o más, debe preguntar si tiene empleo (si o no). Si no tiene empleo, debe mostrar Necesitas un empleo para solicitar el crédito. Si tiene empleo, debe pedir los ingresos mensuales en pesos (entero): con 2000000 o más debe mostrar Crédito aprobado; con menos, debe mostrar Ingresos insuficientes.

edad=float(input("Digita la edad\n"))
if edad>=18:
    empleo=input("En este momento tienes un empleo? si/no\n").upper()
    if empleo =="SI":
        ingresos = float(input("Cual es tu ingreso mensual?\n"))
        if ingresos >= 2000000 :
            print ("Credito Aprobado")
        else:
            print ("Ingresos insuficiente para tu credito")
    else:
        print ("En este momento no podemos gestionar tu credito")
else:
    print ("Eres menor de edad, no se puede gestionar un credito ")
