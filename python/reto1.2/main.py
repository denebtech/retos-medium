def menu():
    print("Conversor de escalas de temperatura")
    print("-" * 50)

    while True:
        print("Seleccione la escala de temperatura que desea convertir:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        try:
            escala = int(input("Ingrese una de las opciones mencionadas: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

        if escala not in [1, 2, 3]:
            print("Opción no válida. Intente nuevamente.")
            continue

        while True:
            try:
                temperatura = float(input("Ingrese la temperatura a convertir: "))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                continue
            break

        return escala, temperatura


def convertir_celsius(temperatura):
    fahrenheit = (temperatura * 9/5) + 32
    kelvin = temperatura + 273.15
    return fahrenheit, kelvin


def convertir_fahrenheit(temperatura):
    celsius = (temperatura - 32) * 5/9
    kelvin = ((temperatura - 32) * 5/9) + 273.15
    return celsius, kelvin


def convertir_kelvin(temperatura):
    celsius = temperatura - 273.15
    fahrenheit = ((temperatura - 273.15) * 9/5) + 32
    return celsius, fahrenheit


if __name__ == "__main__":
    
    while True:
        escala, temperatura = menu()

        if escala == 1:
            fahrenheit, kelvin = convertir_celsius(temperatura)
            print(f"{temperatura:.2f}°C es igual a {fahrenheit:.2f}°F y {kelvin:.2f}K")
        elif escala == 2:
            celsius, kelvin = convertir_fahrenheit(temperatura)
            print(f"{temperatura:.2f}°F es igual a {celsius:.2f}°C y {kelvin:.2f}K")
        elif escala == 3:
            celsius, fahrenheit = convertir_kelvin(temperatura)
            print(f"{temperatura:.2f}K es igual a {celsius:.2f}°C y {fahrenheit:.2f}°F")
        
        print("-" * 50)
        continuar = input("¿Desea realizar otra conversión? (s/n): ")
        if continuar.lower() != 's':
            print("¡Gracias por usar el conversor de escalas de temperatura!")
            break
