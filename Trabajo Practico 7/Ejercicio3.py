# Lista de diccionarios con información de libros
libros = [
    {
        'titulo': 'Libro A',
        'autor': 'Autor X',
        'año_publicacion': 2005
    },
    {
        'titulo': 'Libro B',
        'autor': 'Autor Y',
        'año_publicacion': 2010
    },
    {
        'titulo': 'Libro C',
        'autor': 'Autor Z',
        'año_publicacion': 2000
    }
]

# Función para ordenar la lista de libros por un campo específico
def ordenar_libros(libros, campo):
    return sorted(libros, key=lambda libro: libro[campo])

# Solicitar al usuario el campo por el que desea ordenar (autor o año_publicacion)
campo_ordenamiento = input("¿Por cuál campo desea ordenar los libros (autor/año_publicacion)? ").lower()

# Verificar el campo ingresado
if campo_ordenamiento in ['autor', 'año_publicacion']:
    # Ordenar la lista de libros por el campo especificado
    libros_ordenados = ordenar_libros(libros, campo_ordenamiento)
    
    # Mostrar la lista de libros ordenada
    print("Lista de libros ordenada por", campo_ordenamiento)
    for libro in libros_ordenados:
        print(libro)
else:
    print("Campo no válido. Por favor, ingrese 'autor' o 'año_publicacion'.")
