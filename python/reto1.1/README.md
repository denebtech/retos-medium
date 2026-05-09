# Python - Reto 1.1: Calculadora IMC

En nuestro primer reto vamos a crear una calculadora de IMC (índice de masa corporal), que puede ser de utilidad para tener una referencia sobre nuestra salud. Para que sea más compleja, vamos a utilizar dos variantes: el sistema métrico y el sistema inglés.

## Índice de masa corporal

De acuerdo a la definición de Wikipedia

> _El índice de masa corporal (IMC) es una razón matemática que asocia la masa (peso) y la talla (altura) de un individuo, ideada por el estadístico belga Adolphe Quetelet, por lo que también se conoce como índice de Quetelet. [Wikipedia](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal)._

De acuerdo con la información, el índice es ampliamente aceptado; sin embargo, posee limitaciones al no contemplar variables como el sexo, el porcentaje de grasa corporal o la masa muscular.
Para el cálculo del IMC tenemos las siguientes fórmulas:

- Sistema métrico: la masa (en kilogramos) dividida por la talla (en metros) al cuadrado.

    > IMC = Peso (kg) / Talla (m) ** 2

- Sistema inglés: la masa (en libras) dividida por la altura (en pulgadas) al cuadrado, multiplicado por 

    > IMC = (Peso (lb) / Talla (pulgadas) ** 2) * 703

¿Cómo debemos interpretar los resultados? De acuerdo con el valor del índice obtenido, para personas mayores desde los 20 años, tenemos las siguientes interpretaciones:

- Un IMC inferior a 18.5 se considera un peso por debajo del valor normal.
- Un IMC entre 18,5 y 24,9 se considera un peso normal.
- Un IMC entre 25 y 29,9 se considera sobrepeso.
- Un IMC de 30 o más (rojo) se considera obesidad.
