
precio_compra = float(input("Precio de compra del producto"))
porcentaje_comision_plataforma = float(input("Porcentaje de ganancia"))
costo_envio = float (input ("costo de envio"))
unidades_vendidas_mes = float (input ("Unidades vendidas en el mes"))

comision_plataforma_efectivo = (precio_compra*porcentaje_comision_plataforma/100)
precio_venta = precio_compra + comision_plataforma_efectivo
precio_total = precio_venta + costo_envio
ganancia_mensual = unidades_vendidas_mes * comision_plataforma_efectivo

print (f"\nPrecio de compra: {precio_compra} \nPrecio venta: {precio_venta} \nCosto de envio: {costo_envio} \nPrecio a pagar: {precio_total}")
print ("-"*50)
print ("RESUMEN MENSUAL")
print (f"Porcentaje de comision: {porcentaje_comision_plataforma} \nComision esta venta: {comision_plataforma_efectivo} \nUnidades Vendidas este mes: {unidades_vendidas_mes}")
print ("-"*20)
print (f"GANANCIA ESTE MES: {ganancia_mensual}")
