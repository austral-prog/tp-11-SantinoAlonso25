def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    try:
        with open(filename, 'r') as archivo:
            linea = archivo.readline().strip()
            registros = linea.split(';')

            for registro in registros:
                if registro:  # Evita procesar cadenas vacías al final
                    producto, valor = registro.split(':')
                    valor = float(valor)

                    if producto in ventas:
                        ventas[producto].append(valor)
                    else:
                        ventas[producto] = [valor]
    except FileNotFoundError:
        print(f"Error: el archivo '{filename}' no fue encontrado.")
        raise
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
        raise

    return ventas


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
