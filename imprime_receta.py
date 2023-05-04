def imprimir_contenido_archivo(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    except IOError:
        print(f"Error al leer el archivo '{archivo}'.")

archivo_recetas = "recetas.md"
imprimir_contenido_archivo(archivo_recetas)
