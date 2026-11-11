# Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos de profesional es de $300
# por cada cinco unidades y para alumnos de preparatoria es de $180 por cada cinco unidades, de acuerdo a los
# siguientes criterios:

# 1. Si el promedio es de 9.5 o más y el alumno es de preparatoria, entonces este podrá cursar 55 unidades
# y se le hará un 25% de descuento.

# 2. Si el promedio es mayor o igual a 9 pero menor que 9.5 y el alumno es de preparatoria, entonces este
# podrá cursar 50 unidades y se le hará un 10% de descuento.

# 3. Si el promedio es mayor que 7 y menor que 9 y el alumno es de preparatoria, este podrá cursar 50
# unidades y no tendrá ningún descuento.
#4
#  Si el promedio es de 7 o menor, el número de materias reprobadas es de 0 a 3 y el alumno es de
# preparatoria, entonces podrá cursar 45 unidades y no tendrá descuento.

#  Si el promedio es de 7 o menor, el número de materias reprobadas es de 4 o más y el alumno es de
# preparatoria, entonces podrá cursar 40 unidades y no tendrá ningún descuento.

#  Si el promedio es mayor o igual a 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades
# y se le hará un 20% de descuento.

#  Si el promedio es menor de 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y
# no tendrá descuento.

creditos_1 = 55
creditos_2 = 50
creditos_3 = 45
creditos_4 = 40

pago_preparatoria = 180
pago_profesional = 300

tipo_alumno = int(input("Digite el numero de acuerdo al tipo de alumno:\n1. Preparatoria\n2. Profesional\n-------\nTIPO ALUMNO: "))
promedio_alumno=float(input("Digite el promedio del alumno\n"))

if promedio_alumno > 10:
     print("Digite un valor de promedio valido")
else:
    if tipo_alumno == 1 :
        alumno= "Preparatoria"
        #1
        if promedio_alumno >= 9.5 :
            unidades = creditos_1 / 5
            pagar = unidades * pago_preparatoria
            descuento = 25
            pago_descuento = pagar-(pagar * descuento / 100)
        #2
        elif promedio_alumno >= 9 :
            unidades = creditos_2 / 5
            pagar = unidades * pago_preparatoria
            descuento = 10
            pago_descuento = pagar - (pagar * descuento / 100)
        #3
        elif promedio_alumno > 7 :
            unidades = creditos_2 / 5
            pagar = unidades * pago_preparatoria
            descuento = 0
            pago_descuento = pagar - (pagar * descuento / 100)
        #4
        elif promedio_alumno <=7 :
            numero_reprobadas = int(input("Cuantas materias reprobadas tienes?\n"))       
            if numero_reprobadas >=4:
                    unidades = creditos_4 / 5
                    pagar = unidades * pago_preparatoria
                    descuento = 0
                    pago_descuento = pagar - (pagar * descuento / 100)
            else:
                    unidades = creditos_3 / 5
                    pagar = unidades * pago_preparatoria
                    descuento = 0
                    pago_descuento = pagar - (pagar * descuento / 100)

    else:
        alumno = "Profesional"
        if promedio_alumno >= 9.5 :
            unidades = creditos_1 / 5
            pagar = unidades * pago_profesional
            descuento = 20
            pago_descuento = pagar - (pagar * descuento / 100)
        else:
            unidades = creditos_1 / 5
            pagar = unidades * pago_profesional
            descuento = 0
            pago_descuento = pagar - (pagar * descuento / 100)

    print (f"""
    Tipo de Alumno:         {alumno.upper()}
    Pagar:                  ${pagar}
    Descuento:              {descuento}%
    Pagar con descuento:    ${pago_descuento}
        """)


            
