# #Diccionarios
# # mi_diccionario = {'nombre': 'Luis Fernando', 'apellido':'Corrales', 'edad':48}
# # print(mi_diccionario)
estudiantes = {
    'ana':{'edad':20,'carrera': 'Ingenieria','promedio': 8.7},
    'luis':{'edad':22,'carrera': 'Medicina','promedio': 9.1},
    'carla':{'edad':23,'carrera': 'Derecho','promedio': 8.3},
}
nombre = 'ana'
#
# if nombre in estudiantes:
#     print(f"{nombre}, {estudiantes[nombre]}")
# else:
#     print("Estudiante no encontrado")
#
# info = estudiantes.get('luis', "Estudiante no encontrado")
# print(info)
# print(estudiantes.keys())
# print(estudiantes.values())
# # print(estudiantes.items())
#
# estudiantes['ana'].update({'promedio': 10.0})
# estudiantes.update({
#     'mario':{'edad':20,'carrera':'Arquitectura','promedio':'8.5'},
#     'christian':{'edad':37,'carrera':'Arquitectura','promedio':'9.5'}
# })
#
# eliminado = estudiantes.pop('ana','No existe')
#
# #mostrar a todos los estudiantes con prometio mayor a 8.5
for nombre, datos in estudiantes.items():
    if datos['promedio'] > 8.5:
        print(f'{nombre.title()} tiene un promedio de {datos['promedio']}')