print("-----------GERENCIA DE COMPAÑIA AUTOMOTRIZ------------")

impuesto = 0.0
total = 0.0
categoria1 = 0.0
categoria2 = 0.0
categoria3 = 0.0
contAuto=0
numAuto=int(input("Ingrese el número de automóviles: "))

while numAuto>0:
	print()
	print("Ingresa una de las siguientes claves para los vehículos: 1, 2 o 3")
	clave = int(input(f"Ingresa la clave del vehículo {contAuto+1}: "))
	if clave<4 and clave>0:
		if clave==1:
			precio = float(input("Ingresa el precio del vehículo: $ "))
			impuesto = precio*.10
			categoria1 = categoria1+impuesto
		elif clave==2:
			precio = float(input("Ingresa el precio del vehículo: $ "))
			impuesto = precio*.07
			categoria2 = categoria2+impuesto
		else:
			precio = float(input("Ingresa el precio del vehículo: $ "))
			impuesto = precio*.05
			categoria3 = categoria3+impuesto
		total = total+impuesto
		print(f"El impuesto a pagar por este vehículo es: $ {round(impuesto,2)} ")
		contAuto+=1
		numAuto = numAuto-1
	else:
		print("La clave ingresada no existe")
print(f"El impuesto a pagar por la categoría 1 es: $ {round(categoria1,2)}")
print(f"El impuesto a pagar por la categoría 2 es: $ {round(categoria2,2)}")
print(f"El impuesto a pagar por la categoría 3 es: $ {round(categoria3,2)}")
print()
print(f"El impuesto total a pagar por todos los vehículos es: $ {round(total,2)}")


