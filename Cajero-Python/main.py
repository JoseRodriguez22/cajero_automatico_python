class Cajero:
    def __init__(cuenta):
        cuenta.continuar = True
        cuenta.monto = 1000
        cuenta.historico = "Movimientos: "
        cuenta.menu()
        cuenta.retiro()

    def verificarPIN(cuenta):
        intentos = 1
        while intentos <= 3:
            pin = int(input("Ingrese el PIN: "))
            if pin == 1235:
                break
            else:
                print("El PIN no es válido.\n")
                intentos += 1
                cuenta.continuar = False

    def retiro(cuenta):
        if cuenta.monto != 0:
            retiro = int(input("¿Cuánto dinero desea retirar? (Debe ser un numero ENTERO) "))
            cuenta.monto -= retiro
            print(f"Su nuevo saldo es: {cuenta.monto}")
            consult = f"Se retiro ${cuenta.monto}"
            cuenta.historico = cuenta.historico, consult
            print()
        else:
            print("No tiene fondos suficientes.")

    def menu(cuenta):
        cuenta.verificarPIN()
        print("Bienvenido José Alberto Rodríguez Navarro en la rama Develop\n")
        contador = 'y'
        while contador == 'y':
            print("Consultar saldo: 1\n" + "Retirar dinero: 2\n" + "Historicos de movimientos: 3\n")
            option = int(input())
            if option == 1:
                print(f"Su saldo es: ${cuenta.monto}")
                consult = f"Se consulto el saldo ${cuenta.monto}"
                cuenta.historico = cuenta.historico, consult
                print()
            elif option == 2:
                cuenta.retiro()
            elif option == 3:
                print(cuenta.historico)
                consult = "Se consulto el historial"
                cuenta.historico = cuenta.historico, consult
                print()
            else:
                print("No existe esa opción")
            print("¿Desea regresar al menu principal? (y/n)")
            contador = input()
            print()
        print("Fin del programa.")

# Se inicializa la clase Cajero con sus atributos y metodos
cajero = Cajero()