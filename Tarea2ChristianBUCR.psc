Algoritmo A�oBisiesto
    Definir a�o Como Entero
    Definir condicion Como Cadena
    Escribir "Ingrese un a�o: "
    Leer a�o
    Si a�o MOD 4 = 0 Entonces
        Si a�o MOD 100 = 0 Entonces
            Si a�o MOD 400 = 0 Entonces
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