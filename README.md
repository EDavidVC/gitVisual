# Calculadora por Consola

Una calculadora simple desarrollada en Python que se ejecuta desde la terminal. Permite realizar operaciones aritméticas básicas de forma interactiva.

## Características

- Operaciones soportadas: suma (`+`), resta (`-`), multiplicación (`*`) y división (`/`).
- Validación de entradas numéricas.
- Manejo de error para división entre cero.
- Ejecución en bucle hasta que el usuario decida salir.

## Requisitos

- [Python 3](https://www.python.org/downloads/) instalado en tu sistema.

## Uso

1. Clona o descarga este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el programa:

   ```bash
   python calculadora.py
   ```

4. Ingresa la operación deseada (`+`, `-`, `*`, `/`) y los dos números cuando se te solicite.
5. Para cerrar la calculadora, escribe `salir`.

## Ejemplo

```text
=== Calculadora por consola ===
Operaciones disponibles: +, -, *, /
Escribe 'salir' para terminar.

Ingresa la operación (+, -, *, /) o 'salir': +
Ingresa el primer número: 10
Ingresa el segundo número: 5
Resultado: 10.0 + 5.0 = 15.0
```

## Estructura del proyecto

```text
.
├── calculadora.py  # Código fuente de la calculadora
└── README.md       # Documentación del proyecto
```
