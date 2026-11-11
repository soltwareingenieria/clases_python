#Una persona tiene tres suscripciones (por ejemplo, música, video y almacenamiento). El programa pide el precio mensual de cada una y calcula el gasto mensual total, el gasto anual y cuánto representa cada una del total, en porcentaje.
#Un pintor cotiza un trabajo. El programa pide el largo, ancho y alto de la habitación, y el rendimiento de la pintura (m2 por galón) y su precio. Calcula el área de las cuatro paredes, los galones necesarios y el costo total.



alto_pared = float(input("Digita el alto de la pared"))
medida_ancho_habitacion= float(input("Digita el ancho de la habitacion"))
medida_largo_habitacion = float(input("Digita el largo de la habitacion"))


rendimiento_pintura_tipo_1 = 20
rendimiento_pintura_tipo_2 = 25
rendimiento_pintura_tipo_3 = 20

precio_tipo1 = 151000
precio_tipo2 = 63900
precio_tipo3 = 38400

pared_larga = (alto_pared * medida_largo_habitacion)*2
pared_corta = (alto_pared * medida_ancho_habitacion)*2

total_metros_pared = (pared_corta+pared_larga)

cantidad_galones_pintura_tipo1 = total_metros_pared/rendimiento_pintura_tipo_1
cantidad_galones_pintura_tipo2 = total_metros_pared/rendimiento_pintura_tipo_2
cantidad_galones_pintura_tipo3 = total_metros_pared/rendimiento_pintura_tipo_3

costo_pintura_tipo1 = cantidad_galones_pintura_tipo1*precio_tipo1
costo_pintura_tipo2 = cantidad_galones_pintura_tipo2*precio_tipo2
costo_pintura_tipo3 = cantidad_galones_pintura_tipo3*precio_tipo3

print(f"CANTIDAD DE PINTURA A UTILIZAR \nSEGUN EL RENDIMIENTO DEL TIPO DE PINTURA \nGALONES")
print("-"*50)
print(f"Tipo 1: {cantidad_galones_pintura_tipo1} \nTipo2: {cantidad_galones_pintura_tipo2} \nTipo3: {cantidad_galones_pintura_tipo3} \n")
print("COSTO DE PINTURA A UTILIZAR")
print("-"*50)
print(f"Tipo 1: {costo_pintura_tipo1} \nTipo2: {costo_pintura_tipo2} \nTipo3: {costo_pintura_tipo3} \n")
