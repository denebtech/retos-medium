def menu():
    print("-" * 50)
    print("Calculadora de IMC (Índice de Masa Corporal)")
    
    while True:
        print("-" * 50)
        print("Sistema a emplear")
        print("1. Sistema métrico")
        print("2. Sistema inglés")
        sistema = int(input("Ingrese una de las opciones mencionadas: "))

        if sistema in [1, 2]:
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    print("-" * 50)
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))

    return sistema, peso, altura


def calculadora_metrica(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def calculadora_inglesa(peso, altura):
    imc = (peso / (altura ** 2)) * 703
    return imc


def diagnostico(imc):
    print("-" * 50)
    print(f"Tu IMC es: {imc:.2f}")
    if imc < 18.5:
        print("Categoría: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Categoría: Peso normal")
    elif 25 <= imc < 29.9:
        print("Categoría: Sobrepeso")
    else:
        print("Categoría: Obesidad")


if __name__ == "__main__":

    while True:
        sistema, peso, altura = menu()

        if sistema == 1:
            imc = calculadora_metrica(peso, altura)
            diagnostico(imc)
        if sistema == 2:
            imc = calculadora_inglesa(peso, altura)
            diagnostico(imc)

        print("-" * 50)
        continuar = input("¿Desea calcular otro IMC? (s/n): ")
        if continuar.lower() != 's':
            print("¡Gracias por usar la calculadora de IMC!")
            break
