# 🛒 Sistema de Gestión Básica de Productos

 Este proyecto es una aplicación de consola escrita en Python que permite gestionar productos de forma sencilla. Ideal para paracticar estructuras de datos, bucles, condicionales y validaciones.

## 📦 Funcionalidades:

- **Agregar producto** : Ingresar nombre,categoria y precio (sin centavos.).
- **Mostrar productos**: Visualizar todos los productos registrados, numerados (ID) y ordenados.
- **Buscar producto**: Buscar por nomer y mostrar coincidencias.
- **Eliminar producto**: Eliminar un producto por su numero ID de la lista.
- **Salir**: Finaliza el programa.

## 🎨 Estética en consola

Este sistema utiliza **emojis Unicode** para mejorar la experiencia visual en consola. Los íconos se agregan directamente en el código como parte de los mensajes, sin necesidad de instalar librerías externas.

Ejemplos:

- `✅` para confirmar acciones exitosas.
- `❌` para indicar errores o entradas inválidas.
-  `🛒`, `📦`, `🔍`, `🗑️` para representar funciones del sistema.

> ⚠️ Los emojis se muestran correctamente en la mayoría de terminales modernas. Si tu consola no los soporta, podés reemplazarlos por texto plano o símbolos ASCII.

También podés integrar colores en consola usando la librería [`colorama`](https://pypi.org/project/colorama/):

```bash
pip install colorama

```

## 🧠 Tecnologías utilizadas

- Python 3.x
- Visual Studio Coder 
- (Opcional) colorama para colores en consola 

## 🗂️ Estructura del proyecto

```python
Talento_Tech/Python/pre-entrega
│
├── main.py               # Punto de entrada: menú principal y flujo general
├── producto.py           # Funciones para agregar, mostrar, buscar y eliminar productos
├── utils.py              # Validaciones y funciones auxiliares (opcional)
├── README.md             # Documentación del proyecto
└── data/                 # Carpeta para persistencia futura (CSV, JSON, etc.)
    └── productos.json    # Archivo de ejemplo para guardar productos (opcional)
```


## Cómo ejecutar

1. Cloná o descargá el repositorio.
2. Abrí el proyecto en Visual Studio Code.
3. Ejecutá 'main.py' desde la terminal o el entorno de desarrollo.

```bash

python main.py

```
👩‍💻 Autora

 Carla - Estudiante en la carrera tecnico superior en programacion en la UTN. Apasionada por la administracion de sistemas, scripting y visualizacion tecnica. Este proyecto forma parte de mi preparacion sumando mas conocimientos a mi carrera para un mejor dominio del mismo. 


