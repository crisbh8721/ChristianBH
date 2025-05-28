import random
mayusculas = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
minusculas = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
caracter_especial = ["*","&","^","%","$","#","@","!","-","+","*","/"]
password = []
password_final = ""
print("-"*50 + "\nDesea crear una contraseña?\n" + "-"*50 + "\n1) Si\n2) No\n" + "-"*50)
try:
    while True:
        selecion = int(input(": "))
        if selecion == 1 :
            while True:
                print("-" * 50)
                longitud_solicitada = int(input("Longitud deseada?(minimo 6): "))
                if longitud_solicitada < 6:
                    print("-" * 50)
                    print("Cantidad minima de characteres es 6")
                    print("-" * 50)
                else:
                    mayusculas_password = random.choice(mayusculas)
                    minusculas_password = random.choice(minusculas)
                    caracter_especial_password = random.choice(caracter_especial)
                    numeros_password = random.choice(numeros)
                    password.append(mayusculas_password)
                    password.append(minusculas_password)
                    password.append(caracter_especial_password)
                    password.append(numeros_password)
                    faltantes = int(longitud_solicitada -4)
                    for n in range(faltantes):
                        minusculas_password = random.choice(minusculas)
                        password.append(minusculas_password)
                    random.shuffle(password)
                    password_final = "".join(password)
                    print("-"*50+f"\nSu nuevo password es {password_final}\n"+"-"*50+"\nGracias por usar el generador de contraseñas\n"+"-"*50)
                    break
            break
        elif selecion == 2:
            print("-" * 50)
            print("Tenga un buen dia")
            print("-" * 50)
            break
        else:
            print("Seleccion incorrecta, trate nuevamente")
except ValueError:
    print("-" * 50)
    print("Seleccion incorrecta,Bye!!")
    print("-" * 50)


