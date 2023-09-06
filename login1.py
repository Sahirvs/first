# logica de inicio de sesion
def login(usuario, password):
    # decicion si existe o no existe el usuario 
    if usuario == "fernanda" and password == "10122005123":
        print("ingresaste correctamente ")
        print("ahora si puedes jugar al cachipum")
    else:
        print("datos incorrectos para el inicio de sesion")

# bloque de pruebas
if __name__ == "__main__":
# declarando variables para los parametros 
    user = input("ingrese su usuario: ")
    pass1 = input("ingrese su contraseña: ") 
    # invocando a la funcion }
    login(user, pass1)