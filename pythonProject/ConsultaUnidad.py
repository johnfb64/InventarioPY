"""
Este modulo trabaja con fetch one para traer solo de a un registro

"""
class ConsultaUnidad:

    import psycopg2

    conn = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
    try:
        with conn:

            with conn.cursor() as curs:
                qProducto = "SELECT * FROM Legos WHERE iniciales = %s"
                print('#####################################################')
                entrada = input('Indique las iniciales del producto: ')
                curs.execute(qProducto, (entrada,))
                regs = curs.fetchone()
                print(f'Nombre de figura: ', regs[3])
                print(f'Franquicia: ', regs[1])
                print(f'Codigo: ', regs[2])
                print(f'Cantidad: ', regs[4])
                print(f'Ubicación: ', regs[6])
                print(f'Precio: ', regs[5])

                print('#####################################################')

    #e guarda error
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conn.close()

