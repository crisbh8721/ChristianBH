capital_inicial = int(input("Ingrese el capital inicial: "))
tasa_de_interes_anual = int(input("Ingrese la tasa de interes anual : "))
numero_de_años= int(input("Ingrese numero de años: "))
interes_simple = (capital_inicial * tasa_de_interes_anual * numero_de_años)
print(interes_simple)

candidad_de_timpo_en_segundos = int(input("Ingrese una candidad de timpo en segundos : "))
equivalente_en_horas = (candidad_de_timpo_en_segundos / 3600)
equivalente_en_minutos = candidad_de_timpo_en_segundos / 60
equivalente_en_segundos = candidad_de_timpo_en_segundos
print(f"{equivalente_en_horas:.2f}")
print(equivalente_en_minutos)
print(equivalente_en_segundos)