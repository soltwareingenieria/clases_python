#Escribe un programa que pida la edad (entero). Si la persona es menor de 18 años, debe mostrar Eres menor de edad y no pedir nada más. Si tiene 18 años o más, debe pedir el dinero que tiene (entero) para pagar una compra de 20000 pesos: si tiene 20000 o más, debe mostrar Compra realizada; si tiene menos, debe mostrar Dinero insuficiente.

edad=float(input("Digita tu edad "))
if edad<18:
    print ("Debes se mayor de 18 años para realizar esta compra")
else:
    dinero=float(input("Deposita tu dinero "))
    if dinero >= 20000:
        print ("Compra exitosa")
    else:
        faltante=20000-dinero
        print (f"Te faltan ${faltante:,.0f} para completar tu compra")
