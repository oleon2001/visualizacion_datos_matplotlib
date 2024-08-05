def longitud_texto(texto):
    """
    Devuelve la longitud del texto ingresado.
    """
    try:
        return len(texto)
    except TypeError:
        print("Error: Debe ingresar un texto.")
        return None

texto = input("Ingrese el texto correspondiente: ")
longitud = longitud_texto(texto)

if longitud is not None:
    print(f"La longitud del texto es: {longitud}")