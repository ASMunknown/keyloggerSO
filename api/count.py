# Función para llenar un diccionario con la frecuencia de aparición de una letra
# Clave : nombre de la letra
# Valor : El número de veces que aparece.

def count(key,usage):

    try:
        usage[key] = usage[key] + 1

    except Exception as e:
        usage[key] = 1
        
