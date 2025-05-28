#La CNFL necesita un programa que reciba la cantidad de Kilowatts que consume un hogar por mes.
meses_consumo = []
consumo_enero = ""
consumo_febrero = ""
consumo_marzo = ""
consumo_abril = ""
consumo_mayo = ""
consumo_junio = ""
consumo_julio = ""
consumo_agosto = ""
consumo_septiembre = ""
consumo_octubre = ""
consumo_noviembre = ""
consumo_diciembre = ""
consumo_enero = float(input("Ingrese el consumo de Enero: "))
consumo_febrero = float(input("Ingrese el consumo de Febrero: "))
consumo_marzo = float(input("Ingrese el consumo de Marzo: "))
consumo_abril = float(input("Ingrese el consumo de Abril: "))
consumo_mayo = float(input("Ingrese el consumo de Mayo: "))
consumo_junio = float(input("Ingrese el consumo de Junio: "))
consumo_julio = float(input("Ingrese el consumo de Julio: "))
consumo_agosto = float(input("Ingrese el consumo de Agosto: "))
consumo_septiembre = float(input("Ingrese el consumo de Septiembre: "))
consumo_octubre = float(input("Ingrese el consumo de Octubre: "))
consumo_noviembre = float(input("Ingrese el consumo de Noviembre: "))
consumo_diciembre = float(input("Ingrese el consumo de Diciembre: "))
meses_consumo.append(consumo_enero)
meses_consumo.append(consumo_febrero)
meses_consumo.append(consumo_marzo)
meses_consumo.append(consumo_abril)
meses_consumo.append(consumo_mayo)
meses_consumo.append(consumo_junio)
meses_consumo.append(consumo_julio)
meses_consumo.append(consumo_agosto)
meses_consumo.append(consumo_septiembre)
meses_consumo.append(consumo_octubre)
meses_consumo.append(consumo_noviembre)
meses_consumo.append(consumo_diciembre)
#print(meses)
#Si la familia consume menos de 150 kilowatts el monto por kw es de 125 colones por cada kilowatt y no paga IVA,
#si consume menos 250 kw paga 175 colones por cada kilowatt,
#si consume mas de 500 kilowatts pga a 300 colones el Kilowatt
#Se require que el programa haga lo siguiente:
#Imprimir el mes, el consumo y lo que debe pagar. Debe de desglozar el monto sin IVA, el IVA,
# el monto total
tarifa_enero = ""
monto_sin_IVA_enero = ""
monto_IVA_enero = ""
total_enero = ""
if consumo_enero < 150:
    tarifa_enero = 125
    total_enero = consumo_enero * tarifa_enero
    monto_sin_IVA_enero = total_enero
    monto_IVA_enero = 0
elif consumo_enero < 250:
    tarifa_enero = 175
    monto_sin_IVA_enero = tarifa_enero * consumo_enero
    monto_IVA_enero = monto_sin_IVA_enero * 0.13
    total_enero = monto_sin_IVA_enero + monto_IVA_enero
elif consumo_enero < 500:
    tarifa_enero = 250
    monto_sin_IVA_enero = tarifa_enero * consumo_enero
    monto_IVA_enero = monto_sin_IVA_enero * 0.13
    total_enero = monto_sin_IVA_enero + monto_IVA_enero
else:
    tarifa_enero = 300
    monto_sin_IVA_enero = tarifa_enero * consumo_enero
    monto_IVA_enero = monto_sin_IVA_enero * 0.13
    total_enero = monto_sin_IVA_enero + monto_IVA_enero
tarifa_febrero = ""
monto_sin_IVA_febrero = ""
paga_o_no_IVA_febrero = ""
monto_IVA_febrero = ""
total_febrero = ""
if consumo_febrero < 150:
    tarifa_febrero = 125
    total_febrero = consumo_febrero * tarifa_febrero
    monto_sin_IVA_febrero = total_febrero
    monto_IVA_febrero = 0
elif consumo_febrero < 250:
    tarifa_febrero = 175
    monto_sin_IVA_febrero = tarifa_febrero * consumo_febrero
    monto_IVA_febrero = monto_sin_IVA_febrero * 0.13
    total_febrero = monto_sin_IVA_febrero + monto_IVA_febrero
elif consumo_febrero < 500:
    tarifa_febrero = 250
    monto_sin_IVA_febrero = tarifa_febrero * consumo_febrero
    monto_IVA_febrero = monto_sin_IVA_febrero * 0.13
    total_febrero = monto_sin_IVA_febrero + monto_IVA_febrero
else:
    tarifa_febrero = 300
    monto_sin_IVA_febrero = tarifa_febrero * consumo_febrero
    monto_IVA_febrero = monto_sin_IVA_febrero * 0.13
    total_febrero = monto_sin_IVA_febrero + monto_IVA_febrero
tarifa_marzo = ""
monto_sin_IVA_marzo = ""
paga_o_no_IVA_marzo = ""
monto_IVA_marzo = ""
total_marzo = ""
if consumo_marzo < 150:
    tarifa_marzo = 125
    total_marzo = consumo_marzo * tarifa_marzo
    monto_sin_IVA_marzo = total_marzo
    monto_IVA_marzo = 0
elif consumo_marzo < 250:
    tarifa_marzo = 175
    monto_sin_IVA_marzo = tarifa_marzo * consumo_marzo
    monto_IVA_marzo = monto_sin_IVA_marzo * 0.13
    total_marzo = monto_sin_IVA_marzo + monto_IVA_marzo
elif consumo_marzo < 500:
    tarifa_marzo = 250
    monto_sin_IVA_marzo = tarifa_marzo * consumo_marzo
    monto_IVA_marzo = monto_sin_IVA_marzo * 0.13
    total_marzo = monto_sin_IVA_marzo + monto_IVA_marzo
else:
    tarifa_marzo = 300
    monto_sin_IVA_marzo = tarifa_marzo * consumo_marzo
    monto_IVA_marzo = monto_sin_IVA_marzo * 0.13
    total_marzo = monto_sin_IVA_marzo + monto_IVA_marzo
tarifa_abril = ""
monto_sin_IVA_abril = ""
paga_o_no_IVA_abril = ""
monto_IVA_abril = ""
total_abril = ""
if consumo_abril < 150:
    tarifa_abril = 125
    total_abril = consumo_abril * tarifa_abril
    monto_sin_IVA_abril = total_abril
    monto_IVA_abril = 0
elif consumo_abril < 250:
    tarifa_abril = 175
    monto_sin_IVA_abril = tarifa_abril * consumo_abril
    monto_IVA_abril = monto_sin_IVA_abril * 0.13
    total_abril = monto_sin_IVA_abril + monto_IVA_abril
elif consumo_abril < 500:
    tarifa_abril = 250
    monto_sin_IVA_abril = tarifa_abril * consumo_abril
    monto_IVA_abril = monto_sin_IVA_abril * 0.13
    total_abril = monto_sin_IVA_abril + monto_IVA_abril
else:
    tarifa_abril = 300
    monto_sin_IVA_abril = tarifa_abril * consumo_abril
    monto_IVA_abril = monto_sin_IVA_abril * 0.13
    total_abril = monto_sin_IVA_abril + monto_IVA_abril
tarifa_mayo = ""
monto_sin_IVA_mayo = ""
paga_o_no_IVA_mayo = ""
monto_IVA_mayo = ""
total_mayo = ""
if consumo_mayo < 150:
    tarifa_mayo = 125
    total_mayo = consumo_mayo * tarifa_mayo
    monto_sin_IVA_mayo = total_mayo
    monto_IVA_mayo = 0
elif consumo_mayo < 250:
    tarifa_mayo = 175
    monto_sin_IVA_mayo = tarifa_mayo * consumo_mayo
    monto_IVA_mayo = monto_sin_IVA_mayo * 0.13
    total_mayo = monto_sin_IVA_mayo + monto_IVA_mayo
elif consumo_mayo < 500:
    tarifa_mayo = 250
    monto_sin_IVA_mayo = tarifa_mayo * consumo_mayo
    monto_IVA_mayo = monto_sin_IVA_mayo * 0.13
    total_mayo = monto_sin_IVA_mayo + monto_IVA_mayo
else:
    tarifa_mayo = 300
    monto_sin_IVA_mayo = tarifa_mayo * consumo_mayo
    monto_IVA_mayo = monto_sin_IVA_mayo * 0.13
    total_mayo = monto_sin_IVA_mayo + monto_IVA_mayo
tarifa_junio = ""
monto_sin_IVA_junio = ""
paga_o_no_IVA_junio = ""
monto_IVA_junio = ""
total_junio = ""
if consumo_junio < 150:
    tarifa_junio = 125
    total_junio = consumo_junio * tarifa_junio
    monto_sin_IVA_junio = total_junio
    monto_IVA_junio = 0
elif consumo_junio < 250:
    tarifa_junio = 175
    monto_sin_IVA_junio = tarifa_junio * consumo_junio
    monto_IVA_junio = monto_sin_IVA_junio * 0.13
    total_junio = monto_sin_IVA_junio + monto_IVA_junio
elif consumo_junio < 500:
    tarifa_junio = 250
    monto_sin_IVA_junio = tarifa_junio * consumo_junio
    monto_IVA_junio = monto_sin_IVA_junio * 0.13
    total_junio = monto_sin_IVA_junio + monto_IVA_junio
else:
    tarifa_junio = 300
    monto_sin_IVA_junio = tarifa_junio * consumo_junio
    monto_IVA_junio = monto_sin_IVA_junio * 0.13
    total_junio = monto_sin_IVA_junio + monto_IVA_junio
tarifa_julio = ""
monto_sin_IVA_julio = ""
paga_o_no_IVA_julio = ""
monto_IVA_julio = ""
total_julio = ""
if consumo_julio < 150:
    tarifa_julio = 125
    total_julio = consumo_julio * tarifa_julio
    monto_sin_IVA_julio = total_julio
    monto_IVA_julio = 0
elif consumo_julio < 250:
    tarifa_julio = 175
    monto_sin_IVA_julio = tarifa_julio * consumo_julio
    monto_IVA_julio = monto_sin_IVA_julio * 0.13
    total_junio = monto_sin_IVA_julio + monto_IVA_julio
elif consumo_julio < 500:
    tarifa_julio = 250
    monto_sin_IVA_julio = tarifa_julio * consumo_julio
    monto_IVA_julio = monto_sin_IVA_julio * 0.13
    total_junio = monto_sin_IVA_julio + monto_IVA_julio
else:
    tarifa_julio = 300
    monto_sin_IVA_julio = tarifa_julio * consumo_julio
    monto_IVA_julio = monto_sin_IVA_julio * 0.13
    total_junio = monto_sin_IVA_julio + monto_IVA_julio
tarifa_agosto = ""
monto_sin_IVA_agosto = ""
paga_o_no_IVA_agosto = ""
monto_IVA_agosto = ""
total_agosto = ""
if consumo_agosto < 150:
    tarifa_agosto = 125
    total_agosto = consumo_agosto * tarifa_agosto
    monto_sin_IVA_agosto = total_agosto
    monto_IVA_agosto = 0
elif consumo_agosto < 250:
    tarifa_agosto = 175
    monto_sin_IVA_agosto = tarifa_agosto * consumo_agosto
    monto_IVA_agosto = monto_sin_IVA_agosto * 0.13
    total_agosto = monto_sin_IVA_agosto + monto_IVA_agosto
elif consumo_abril < 500:
    tarifa_agosto = 250
    monto_sin_IVA_agosto = tarifa_agosto * consumo_agosto
    monto_IVA_agosto = monto_sin_IVA_agosto * 0.13
    total_agosto = monto_sin_IVA_agosto + monto_IVA_agosto
else:
    tarifa_agosto = 300
    monto_sin_IVA_agosto = tarifa_agosto * consumo_agosto
    monto_IVA_agosto = monto_sin_IVA_agosto * 0.13
    total_agosto = monto_sin_IVA_agosto + monto_IVA_agosto
tarifa_septiembre = ""
monto_sin_IVA_septiembre = ""
paga_o_no_IVA_septiembre = ""
monto_IVA_septiembre = ""
total_septiembre = ""
if consumo_septiembre < 150:
    tarifa_septiembre = 125
    total_septiembre = consumo_septiembre * tarifa_septiembre
    monto_sin_IVA_septiembre = total_septiembre
    monto_IVA_septiembre = 0
elif consumo_septiembre < 250:
    tarifa_septiembre = 175
    monto_sin_IVA_septiembre = tarifa_septiembre * consumo_septiembre
    monto_IVA_septiembre = monto_sin_IVA_septiembre * 0.13
    total_septiembre = monto_sin_IVA_septiembre + monto_IVA_septiembre
elif consumo_septiembre < 500:
    tarifa_septiembre = 250
    monto_sin_IVA_septiembre = tarifa_septiembre * consumo_septiembre
    monto_IVA_septiembre = monto_sin_IVA_septiembre * 0.13
    total_septiembre = monto_sin_IVA_septiembre + monto_IVA_septiembre
else:
    tarifa_septiembre = 300
    monto_sin_IVA_septiembre = tarifa_septiembre * consumo_septiembre
    monto_IVA_septiembre = monto_sin_IVA_septiembre * 0.13
    total_septiembre = monto_sin_IVA_septiembre + monto_IVA_septiembre
tarifa_octubre = ""
monto_sin_IVA_octubre = ""
paga_o_no_IVA_octubre = ""
monto_IVA_octubre = ""
total_octubre = ""
if consumo_octubre < 150:
    tarifa_octubre = 125
    total_octubre = consumo_octubre * tarifa_octubre
    monto_sin_IVA_octubre = total_octubre
    monto_IVA_octubre = 0
elif consumo_octubre < 250:
    tarifa_octubre = 175
    monto_sin_IVA_octubre = tarifa_octubre * consumo_octubre
    monto_IVA_octubre = monto_sin_IVA_octubre * 0.13
    total_octubre = monto_sin_IVA_octubre + monto_IVA_octubre
elif consumo_octubre < 500:
    tarifa_octubre = 250
    monto_sin_IVA_octubre = tarifa_octubre * consumo_octubre
    monto_IVA_octubre = monto_sin_IVA_octubre * 0.13
    total_octubre = monto_sin_IVA_octubre + monto_IVA_octubre
else:
    tarifa_octubre = 300
    monto_sin_IVA_octubre = tarifa_octubre * consumo_octubre
    monto_IVA_octubre = monto_sin_IVA_octubre * 0.13
    total_octubre = monto_sin_IVA_octubre + monto_IVA_octubre
tarifa_noviembre = ""
monto_sin_IVA_noviembre = ""
paga_o_no_IVA_noviembre = ""
monto_IVA_noviembre = ""
total_noviembre = ""
if consumo_noviembre < 150:
    tarifa_noviembre = 125
    total_noviembre = consumo_noviembre * tarifa_noviembre
    monto_sin_IVA_noviembre = total_noviembre
    monto_IVA_noviembre = 0
elif consumo_noviembre < 250:
    tarifa_noviembre = 175
    monto_sin_IVA_noviembre = tarifa_noviembre * consumo_noviembre
    monto_IVA_noviembre = monto_sin_IVA_noviembre * 0.13
    total_noviembre = monto_sin_IVA_noviembre + monto_IVA_noviembre
elif consumo_noviembre < 500:
    tarifa_noviembre = 250
    monto_sin_IVA_noviembre = tarifa_noviembre * consumo_noviembre
    monto_IVA_noviembre = monto_sin_IVA_noviembre * 0.13
    total_noviembre = monto_sin_IVA_noviembre + monto_IVA_noviembre
else:
    tarifa_noviembre = 300
    monto_sin_IVA_noviembre = tarifa_noviembre * consumo_noviembre
    monto_IVA_noviembre = monto_sin_IVA_noviembre * 0.13
    total_noviembre = monto_sin_IVA_noviembre + monto_IVA_noviembre
tarifa_diciembre = ""
monto_sin_IVA_diciembre = ""
paga_o_no_IVA_diciembre = ""
monto_IVA_diciembre = ""
total_diciembre = ""
if consumo_diciembre < 150:
    tarifa_diciembre = 125
    total_diciembre = consumo_diciembre * tarifa_diciembre
    monto_sin_IVA_diciembre = total_diciembre
    monto_IVA_diciembre = 0
elif consumo_diciembre < 250:
    tarifa_diciembre = 175
    monto_sin_IVA_diciembre = tarifa_diciembre * consumo_diciembre
    monto_IVA_diciembre = monto_sin_IVA_diciembre * 0.13
    total_diciembre = monto_sin_IVA_diciembre + monto_IVA_diciembre
elif consumo_diciembre < 500:
    tarifa_diciembre = 250
    monto_sin_IVA_diciembre = tarifa_diciembre * consumo_diciembre
    monto_IVA_diciembre = monto_sin_IVA_diciembre * 0.13
    total_diciembre = monto_sin_IVA_diciembre + monto_IVA_diciembre
else:
    tarifa_diciembre = 300
    monto_sin_IVA_diciembre = tarifa_diciembre * consumo_diciembre
    monto_IVA_diciembre = monto_sin_IVA_diciembre * 0.13
    total_diciembre = monto_sin_IVA_diciembre + monto_IVA_diciembre
print("============================== Enero ==============================")
print(f"El consumo para el mes de enero es de {consumo_enero} kilowatts")
print(f"La Tarifa para el mes de enero es de {tarifa_enero} colones")
print(f"El monto sin IVA para enero es {monto_sin_IVA_enero} colones")
print(f"El Monto de IVA para enero es {monto_IVA_enero} colones")
print(f"El monto total para enero es {total_enero} colones")
print("=====================================================================")
print("============================== Febrero ==============================")
print(f"El consumo para el mes de Febrero es de {consumo_febrero} kilowatts")
print(f"La Tarifa para el mes de Febrero es de {tarifa_febrero} colones")
print(f"El monto sin IVA para Febrero es {monto_sin_IVA_febrero} colones")
print(f"El Monto de IVA para Febrero es {monto_IVA_febrero} colones")
print(f"El monto total para Febrero es {total_febrero} colones")
print("=====================================================================")
print("============================== Marzo ==============================")
print(f"El consumo para el mes de Marzo es de {consumo_marzo} kilowatts")
print(f"La Tarifa para el mes de Marzo es de {tarifa_marzo} colones")
print(f"El monto sin IVA para Marzo es {monto_sin_IVA_marzo} colones")
print(f"El Monto de IVA para Marzo es {monto_IVA_marzo} colones")
print(f"El monto total para Marzo es {total_marzo} colones")
print("=====================================================================")
print("============================== Abril ==============================")
print(f"El consumo para el mes de Abril es de {consumo_abril} kilowatts")
print(f"La Tarifa para el mes de Abril es de {tarifa_abril} colones")
print(f"El monto sin IVA para Abril es {monto_sin_IVA_abril} colones")
print(f"El Monto de IVA para Abril es {monto_IVA_abril} colones")
print(f"El monto total para Abril es {total_abril} colones")
print("=====================================================================")
print("============================== Mayo ==============================")
print(f"El consumo para el mes de Mayo es de {consumo_mayo} kilowatts")
print(f"La Tarifa para el mes de Mayo es de {tarifa_mayo} colones")
print(f"El monto sin IVA para Mayo es {monto_sin_IVA_mayo} colones")
print(f"El Monto de IVA para Mayo es {monto_IVA_mayo} colones")
print(f"El monto total para Mayo es {total_mayo} colones")
print("=====================================================================")
print("============================== Junio ==============================")
print(f"El consumo para el mes de Junio es de {consumo_junio} kilowatts")
print(f"La Tarifa para el mes de Junio es de {tarifa_junio} colones")
print(f"El monto sin IVA para Junio es {monto_sin_IVA_junio} colones")
print(f"El Monto de IVA para Junio es {monto_IVA_junio} colones")
print(f"El monto total para Junio es {total_junio} colones")
print("=====================================================================")
print("============================== Julio ==============================")
print(f"El consumo para el mes de Julio es de {consumo_julio} kilowatts")
print(f"La Tarifa para el mes de Julio es de {tarifa_julio} colones")
print(f"El monto sin IVA para Julio es {monto_sin_IVA_julio} colones")
print(f"El Monto de IVA para Julio es {monto_IVA_julio} colones")
print(f"El monto total para Julio es {total_julio} colones")
print("=====================================================================")
print("============================== Agosto ==============================")
print(f"El consumo para el mes de Agosto es de {consumo_agosto} kilowatts")
print(f"La Tarifa para el mes de Agosto es de {tarifa_agosto} colones")
print(f"El monto sin IVA para Agosto es {monto_sin_IVA_agosto} colones")
print(f"El Monto de IVA para Agosto es {monto_IVA_agosto} colones")
print(f"El monto total para Agosto es {total_agosto} colones")
print("=====================================================================")
print("============================== Septiembre ==============================")
print(f"El consumo para el mes de Septiembre es de {consumo_septiembre} kilowatts")
print(f"La Tarifa para el mes de Septiembre es de {tarifa_septiembre} colones")
print(f"El monto sin IVA para Septiembre es {monto_sin_IVA_septiembre} colones")
print(f"El Monto de IVA para Septiembre es {monto_IVA_septiembre} colones")
print(f"El monto total para Septiembre es {total_septiembre} colones")
print("=====================================================================")
print("============================== Octubre ==============================")
print(f"El consumo para el mes de Octubre es de {consumo_octubre} kilowatts")
print(f"La Tarifa para el mes de Octubre es de {tarifa_octubre} colones")
print(f"El monto sin IVA para Octubre es {monto_sin_IVA_octubre} colones")
print(f"El Monto de IVA para Octubre es {monto_IVA_octubre} colones")
print(f"El monto total para Octubre es {total_octubre} colones")
print("=====================================================================")
print("============================== Noviembre ==============================")
print(f"El consumo para el mes de Noviembre es de {consumo_noviembre} kilowatts")
print(f"La Tarifa para el mes de Noviembre es de {tarifa_noviembre} colones")
print(f"El monto sin IVA para Noviembre es {monto_sin_IVA_noviembre} colones")
print(f"El Monto de IVA para Noviembre es {monto_IVA_noviembre} colones")
print(f"El monto total para Noviembre es {total_noviembre} colones")
print("=====================================================================")
print("============================== Diciembre ==============================")
print(f"El consumo para el mes de Diciembre es de {consumo_diciembre} kilowatts")
print(f"La Tarifa para el mes de Diciembre es de {tarifa_diciembre} colones")
print(f"El monto sin IVA para Diciembre es {monto_sin_IVA_diciembre} colones")
print(f"El Monto de IVA para Diciembre es {monto_IVA_diciembre} colones")
print(f"El monto total para Diciembre es {total_diciembre} colones")
print("=====================================================================")
#Determine e imprima cual fue el mes de mayor y menor consumo
mes_de_mayor_consumo = max(meses_consumo)
indice_mes_de_mayor_consumo = meses_consumo.index(mes_de_mayor_consumo)
mes_de_menor_consumo = min(meses_consumo)
indice_mes_de_menor_consumo =  meses_consumo.index(mes_de_menor_consumo)
mes_mayor_reporte = ""
monto_mayor_reporte = ""
if indice_mes_de_mayor_consumo == 0:
    mes_mayor_reporte = "Enero"
    monto_mayor_reporte = total_enero
elif indice_mes_de_mayor_consumo == 1:
    mes_mayor_reporte = "Febrero"
    monto_mayor_reporte = total_febrero
elif indice_mes_de_mayor_consumo == 2:
    mes_mayor_reporte = "Marzo"
    monto_mayor_reporte = total_marzo
elif indice_mes_de_mayor_consumo == 3:
    mes_mayor_reporte = "Abril"
    monto_mayor_reporte = total_abril
elif indice_mes_de_mayor_consumo == 4:
    mes_mayor_reporte = "Mayo"
    monto_mayor_reporte = total_mayo
elif indice_mes_de_mayor_consumo == 5:
    mes_mayor_reporte = "Junio"
    monto_mayor_reporte = total_junio
elif indice_mes_de_mayor_consumo == 6:
    mes_mayor_reporte = "Julio"
    monto_mayor_reporte = total_julio
elif indice_mes_de_mayor_consumo == 7:
    mes_mayor_reporte = "Agosto"
    monto_mayor_reporte = total_agosto
elif indice_mes_de_mayor_consumo == 8:
    mes_mayor_reporte = "Septiembre"
    monto_mayor_reporte = total_septiembre
elif indice_mes_de_mayor_consumo == 9:
    mes_mayor_reporte = "Octubre"
    monto_mayor_reporte = total_octubre
elif indice_mes_de_mayor_consumo == 10:
    mes_mayor_reporte = "Noviembre"
    monto_mayor_reporte = total_noviembre
else:
    mes_menor_reporte = "Diciembre"
    monto_mayor_reporte = total_diciembre
mes_menor_reporte = ""
monto_menor_reporte = ""
if indice_mes_de_menor_consumo == 0:
    mes_menor_reporte = "Enero"
    monto_menor_reporte = total_enero
elif indice_mes_de_menor_consumo  == 1:
    mes_menor_reporte = "Febrero"
    monto_menor_reporte = total_febrero
elif indice_mes_de_menor_consumo  == 2:
    mes_menor_reporte = "Marzo"
    monto_menor_reporte = total_marzo
elif indice_mes_de_menor_consumo  == 3:
    mes_menor_reporte = "Abril"
    monto_menor_reporte = total_abril
elif indice_mes_de_menor_consumo  == 4:
    mes_menor_reporte = "Mayo"
    monto_menor_reporte = total_mayo
elif indice_mes_de_menor_consumo  == 5:
    mes_menor_reporte = "Junio"
    monto_menor_reporte = total_junio
elif indice_mes_de_menor_consumo == 6:
    mes_menor_reporte = "Julio"
    monto_menor_reporte = total_julio
elif indice_mes_de_menor_consumo == 7:
    mes_menor_reporte = "Agosto"
    monto_menor_reporte = total_agosto
elif indice_mes_de_menor_consumo == 8:
    mes_menor_reporte = "Septiembre"
    monto_menor_reporte = total_septiembre
elif indice_mes_de_menor_consumo == 9:
    mes_menor_reporte = "Octubre"
    monto_menor_reporte = total_octubre
elif indice_mes_de_menor_consumo == 10:
    mes_menor_reporte = "Noviembre"
    monto_menor_reporte = total_noviembre
else:
    mes_menor_reporte = "Diciembre"
    monto_menor_reporte = total_diciembre
print(f"El mes de mayor consumo es {mes_mayor_reporte} con {mes_de_mayor_consumo} kilowatts, Factura {monto_mayor_reporte} colones")
print(f"El mes de menor consumo es {mes_menor_reporte} con {mes_de_menor_consumo} kilowatts, Factura {monto_menor_reporte} colones")
print("=====================================================================")

