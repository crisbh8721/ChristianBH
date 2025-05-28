while True:
    print("\n---MENU PRINCIPAL---")
    print("1. Saludar")
    print("2. Suma de dos números")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == '1':
        print("Hola, este es un programa de prueba")
    elif opcion == '2':
        a = float(input('Ingresa el primer número: '))
        b = float(input('Ingresa el segundo número: '))
        print(f'La suma de los dos números es {a + b}')
    elif opcion == '3':
        print('Gracias por utilizar mi software')
        break
    else:
        print("Opción inválida, INTENTE DE NUEVO")

"""
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
consumos = []
tarifas = []
montos_sin_IVA = []
montos_IVA = []
totales = []
IVA = 0.13
for i in range(len(meses)):
    consumo = float(input(f"Ingrese el consumo de {meses[i]}: "))
    consumos.append(consumo)

    if consumo < 150:
        tarifa = 125
        total = consumo * tarifa
        monto_sin_IVA = total
        monto_IVA = 0
    elif consumo < 250:
        tarifa = 175
        monto_sin_IVA = tarifa * consumo
        monto_IVA = monto_sin_IVA *IVA
        total = monto_sin_IVA + monto_IVA
    elif consumo < 500:
        tarifa = 250
        monto_sin_IVA = tarifa * consumo
        monto_IVA = monto_sin_IVA * IVA
        total = monto_sin_IVA + monto_IVA
    else:
        tarifa = 300
        monto_sin_IVA = tarifa * consumo
        monto_IVA = monto_sin_IVA * IVA
        total = monto_sin_IVA + monto_IVA

    tarifas.append(tarifa)
    montos_sin_IVA.append(monto_sin_IVA)
    montos_IVA.append(monto_IVA)
    totales.append(total)

max_consumo = max(consumos)
min_consumo = min(consumos)
indice_max = consumos.index(max_consumo)
indice_min = consumos.index(min_consumo)

mes_max = meses[indice_max]
mes_min = meses[indice_min]
monto_max = totales[indice_max]
monto_min = totales[indice_min]
print("\nResumen de consumos y costos:")
for i in range(len(meses)):
    print(f"{meses[i]}: Consumo = {consumos[i]}, "
          f"Tarifa = {tarifas[i]}, Total sin IVA = {montos_sin_IVA[i]}, "
          f"IVA = {montos_IVA[i]}, Total con IVA = {totales[i]}")

print(f"\nEl mes de mayor consumo fue {mes_max} con un consumo de {max_consumo} y un monto total de {monto_max}")
print(f"El mes de menor consumo fue {mes_min} con un consumo de {min_consumo} y un monto total de {monto_min}")"""