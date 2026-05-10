def menu():
    print("-" * 50)
    print("Contador de vocales y consonantes")

    while True:
        print("-" * 50)
        texto = input("Ingrese un texto: ")

        if texto:
            break
        else:
            print("El texto no puede estar vacío. Intente nuevamente.")
    
    return texto


def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador_vocales = sum(1 for letra in texto if letra in vocales)
    return contador_vocales


def contar_consonantes(texto):
    vocales = "aeiouAEIOU"
    contador_consonantes = sum(1 for letra in texto if letra.isalpha() and letra not in vocales)
    return contador_consonantes


def contador_palabras(texto):
    palabras = [palabra for palabra in texto.split(" ") if palabra.isalpha()]
    return len(palabras)


if __name__ == "__main__":
    while True:
        texto = menu()
        vocales = contar_vocales(texto)
        consonantes = contar_consonantes(texto)
        palabras = contador_palabras(texto)

        print("-" * 50)
        print(f"Texto ingresado: {texto}")
        print(f"Número de vocales: {vocales}")
        print(f"Número de consonantes: {consonantes}")
        print(f"Número de palabras: {palabras}")

        print("-" * 50)
        continuar = input("¿Desea ingresar otro texto? (s/n): ")
        if continuar.lower() != 's':
            break
