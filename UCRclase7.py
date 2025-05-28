def menu():
    print('Tarjetero Digital')
    print('1. Ingresar un nuevo contacto')
    print('2. Modificar un contacto')
    print('3. Eliminar un contacto')
    print('4. Buscar un contacto por cedula')
    print('5. Listar todos los contactos')
    print('6. Salir')

def ingresar_contacto(contactos):
    cedula = input('Ingrese la cedula: ')
    nombre = input('Ingrese el nombre: ')
    apellidos = input('Ingrese los apellidos: ')
    email = input('Ingrese el email: ')
    telefono = input('Ingrese el telefono: ')
    contactos[cedula]={
        'Nombre': nombre,
        'Apellidos': apellidos,
        'Email': email,
        'Telefono': telefono
    }
    print('Contacto ingresado correctamente')

def modificar_contacto(contactos):
    cedula = input('Ingrese la cedula a modificar: ')
    if cedula in contactos:
        nombre = input('Ingrese el nombre: ')
        apellidos = input('Ingrese los apellidos: ')
        email = input('Ingrese el email: ')
        telefono = input('Ingrese el telefono: ')
        contactos[cedula]={
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Email': email,
            'Telefono': telefono
        }
        print('Contacto modificado correctamente')
    else:
        print('Contacto NO encontrado')

def buscar_contacto(contactos):
    cedula = input('Ingrese la cedula a buscar: ')
    if cedula in contactos:
        contacto = contacto[cedula]
        print(f'Cedula: {cedula}')
        print(f'Nombre: {contacto["Nombre"]} {contacto["Apellidos"]}')
        print(f'Correo: {contacto["Email"]}')
        print(f'Telefono: {contacto["Telefono"]}')
    else:
        print('Contacto no encontrado')

def eliminar_contacto(contactos):
    cedula = input('Ingrese la cedula a eliminar: ')
    if cedula in contactos:
        del contactos[cedula]
        print('Contacto eliminado correctamente')
    else:
        print('Contacto NO encontrado')

def listar_contactos(contactos):
    if contactos:
        for cedula, contacto in contactos.items():
            print(f'Nombre completo: {contacto["Nombre"]} {contacto["Apellidos"]}')
            print(f'Telefono: {contacto["Telefono"]}')
            print(f'Email: {contacto["Email"]}')
            print('-'*20)
    else:
        print('No hay contactos registrados')

def main():
    contactos = {}
    while True:
        menu()
        opcion = input('Seleccione una opcion: ')
        if opcion == '1':
            ingresar_contacto(contactos)
        elif opcion == '2':
            modificar_contacto(contactos)
        elif opcion == '3':
            eliminar_contacto(contactos)
        elif opcion == '4':
            buscar_contacto(contactos)
        elif opcion == '5':
            listar_contactos(contactos)
        elif opcion == '6':
            print('Saliendo del programa')
            break
        else:
            print('Seleccione una opcion valida entre 1 y 6')

main()


