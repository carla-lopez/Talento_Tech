def agregar_producto(productos):
    while True:
        nombre = input("📝 Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            continue

        categoria = input("📁 Ingrese la categoría del producto: ").strip()
        if not categoria:
            print("❌ La categoría no puede estar vacía.")
            continue

        precio_str = input("💲 Ingrese el precio (sin centavos): ").strip()
        if not precio_str.isdigit():
            print("❌ El precio debe ser un número entero.")
            continue

        precio = int(precio_str)
        productos.append([nombre, categoria, precio])
        print(f"✅ Producto '{nombre}' agregado correctamente.\n")
        break

def mostrar_productos(productos):
    if not productos:
        print("📭 No hay productos registrados.\n")
        return

    print("\n📋 Lista de productos registrados:")
    print("────────────────────────────")
    for idx, (nombre,categoria,precio) in enumerate(productos, start=1):
        print(f"{idx:>2}. 🏷️ {nombre:<15} | 📁 {categoria:<10} | 💲${precio}")
    print("────────────────────────────\n")

def buscar_producto(productos):
    clave = input("🔍 Ingrese el nombre a buscar: ").strip().lower()
    resultados = [
        (idx + 1, producto) for idx, producto in enumerate(productos)
        if clave in producto[0].lower()
    ]

    if not resultados:
        print("🔎 No se encontraron coincidencias.\n")
        return

    print("\n📌 Resultados encontrados:")
    print("────────────────────────────")
    for idx, (nombre, categoria, precio) in [ (i, prod) for i, prod in resultados ]:
        print(f"{idx:>2}. 🏷️ {nombre:<15} | 📁 {categoria:<10} | 💲${precio}")
    print("────────────────────────────\n")

def eliminar_producto(productos):
    if not productos:
        print("🚫 No hay productos para eliminar.\n")
        return

    mostrar_productos(productos)
    opcion = input("🗑️ Ingrese el número del producto a eliminar: ").strip()
    if not opcion.isdigit():
        print("❌ Debes ingresar un número válido.\n")
        return

    idx = int(opcion) - 1
    if 0 <= idx < len(productos):
        eliminado = productos.pop(idx)
        print(f"✅ Producto '{eliminado[0]}' eliminado correctamente.\n")
    else:
        print("❌ Número fuera de rango.\n")

