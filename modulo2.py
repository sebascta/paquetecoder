# Base de datos de usuarios registrados
base_datos = {}

def leerdata(base_datos):
    for usuario, contraseña in base_datos.items():
        print(f'Usuario: {usuario}, Contraseña: {contraseña}')

#registrar un nuevo usuario
nuevo_usuario = input('Nombre de usuario: ')
nueva_contraseña = input('Ingrese una contraseña: ')
base_datos[nuevo_usuario] = nueva_contraseña
print('Usuario registrado exitosamente.')

leerdata(base_datos)

#inicio de sesion
usuario = input('Ingrese su usuario: ')

if usuario in base_datos:
    print('Usuario registrado.')

    contraseña = input('Ingresa tu contraseña: ')

    if base_datos[usuario] == contraseña:
        print('Contraseña Correcta. Puede Continuar..')
    else:
        print('Contraseña incorrecta...Intente Nuevamente.  ')
else:
    print('Usuario no registrado.  ')

leerdata(base_datos)