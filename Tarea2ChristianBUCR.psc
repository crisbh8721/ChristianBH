Algoritmo AñoBisiesto
    Definir año Como Entero
    Definir condicion Como Cadena
    Escribir "Ingrese un año: "
    Leer año
    Si año MOD 4 = 0 Entonces
        Si año MOD 100 = 0 Entonces
            Si año MOD 400 = 0 Entonces
                condicion <- "Es bisiesto"
            Sino
                condicion <- "No es bisiesto"
            Fin Si
        Sino
            condicion <- "Es bisiesto"
        Fin Si
    Sino
        condicion <- "No es bisiesto"
    Fin Si
    Escribir condicion
FinAlgoritmo