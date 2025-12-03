from database import conectar_bd
from colorama import Fore, Style


def agregar_producto():
    print(f"\n{Fore.CYAN}📝 --- NUEVO PRODUCTO ---")
    
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre: break
        print(f"{Fore.RED}❌ El nombre no puede estar vacío.")
        
    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria: break
        print(f"{Fore.RED}❌ La categoría no puede estar vacía.")
        
    while True:
        precio_str = input("Ingrese el precio (sin centavos): ").strip()
        if precio_str.isdigit():
            precio = int(precio_str)
            break
        print(f"{Fore.RED}❌ El precio debe ser un número entero.")
        
    # --- SQL INSERT ---
    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO productos (nombre, categoria, precio) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, categoria, precio))
            conn.commit()
            print(f"\n{Fore.GREEN}✅ Producto '{nombre}' agregado correctamente.\n")
        except Exception as e:
            print(f"{Fore.RED}❌ Error al agregar el producto: {e}")
        finally:
            conn.close()
            
def mostrar_productos():
    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos")
            resultados = cursor.fetchall()
            
            if not resultados:
                print(f"\n{Fore.YELLOW}📭 No hay productos registrados.\n")
                return
            
            print(f"\n{Fore.CYAN}📋 --- LISTA DE PRODUCTOS REGISTRADOS ---")
            print(f"{Fore.WHITE}────────────────────────────")
            #Cabecera
            print(f"{Style.BRIGHT}{'ID':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO'}")
            print(f"{Fore.WHITE}────────────────────────────")
            
            for prod in resultados:
                # prod = (id, nombre, categoria, precio)
                id_prond, nom, cat, pre = prod
                print(f"{Fore.YELLOW}{id_prond:<5} | {Fore.WHITE}{nom:<20} | {Fore.BLUE}{cat:<15} | {Fore.GREEN}${pre}")
                
            print(f"{Fore.WHITE}────────────────────────────\n")
        except Exception as e:
            print(f"{Fore.RED}❌ Error al obtener los productos: {e}")
        finally:
            conn.close()
            
def buscar_producto():
    clave=input(f"\n{Fore.CYAN}🔍 Ingrese el nombre a buscar: ").strip()
    
    conn=conectar_bd()
    if conn:
        try:
            cursor=conn.cursor()
            #Busqueda con comododines %
            query="SELECT * FROM productos WHERE nombre LIKE %s"
            cursor.execute(query, (f"%{clave}%",))
            resultados=cursor.fetchall()
            
            if not resultados:
                print(f"\n{Fore.YELLOW}🔎 No se encontraron coincidencias para '{clave}'.\n")
            else:
                print(f"\n{Fore.GREEN}📌 --- RESULTADOS ENCONTRADOS ---")
                print(f"{Fore.WHITE}────────────────────────────")
                for prod in resultados:
                    print(f"{Fore.YELLOW}ID: {prod[0]} | {Fore.WHITE}Nombre: {prod[1]} | {Fore.BLUE}Categoría: {prod[2]} | {Fore.GREEN}Precio: ${prod[3]}")
                print(f"{Fore.WHITE}────────────────────────────\n")
        finally:
            conn.close()
            
def eliminar_producto():
    #Primero mostramos la lista para que el usuario vea los IDs
    mostrar_productos()
    
    opcion = input (f"{Fore.RED} 🗑️ Ingrese el ID del producto a eliminar: ").strip()
    
    if not opcion.isdigit():
        print(f"{Fore.RED}❌ Debes ingresar un número válido.\n")
        return
    
    id_eliminar = int(opcion)
    
    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()
            #Verificamos si el ID existe
            cursor.execute("SELECT nombre FROM productos WHERE id = %s", (id_eliminar,))
            resultado = cursor.fetchone()
            
            if not resultado:
                print(f"{Fore.RED}❌ No existe un producto con ID {id_eliminar}.\n")
            else:
                nombre_prod = resultado[0]
                cursor.execute("DELETE FROM productos WHERE id = %s", (id_eliminar,))
                conn.commit()
                print(f"\n{Fore.GREEN}✅ Producto '{nombre_prod}' (ID: {id_eliminar}) eliminado correctamente.\n")
        except Exception as e:
            print(f"{Fore.RED}❌ Error al eliminar el producto: {e}")
        finally:
            conn.close()
            
            
    


"""
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

    """