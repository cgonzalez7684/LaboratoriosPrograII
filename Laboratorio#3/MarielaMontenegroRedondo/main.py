ListInstrumentosMusicales = []
TipoInstrumento = input("por favor introduzca el tipo de instrumento:")
ListInstrumentosMusicales.append(TipoInstrumento)
opciones = input("¿quiere añadir otro instrumento?:")

while opciones == "Si" or opciones == "si":
    TipoInstrumento = input("por favor introduzca el tipo de instrumento:")
    ListInstrumentosMusicales.append(TipoInstrumento)
    opciones = input("¿quiere añadir otro instrumento?:")
    
    
print(f"los instrumentos musicales son: {ListInstrumentosMusicales}")