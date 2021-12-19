"""
Este modulo trabaja con fetch one para traer solo de a un registro

"""
import psycopg2

conn = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
try:
    with conn:

        with conn.cursor() as curs:
            find = "SELECT producto FROM Legos WHERE iniciales IN %s"
            entrada = input('Indique las iniciales del producto: ')
            llavesPrimarias = (tuple(entrada.split(',')),)
            curs.execute(find, llavesPrimarias)
            regs = curs.fetchall()
            for registro in regs:
                print('Nombre figura: ', registro)

#e guarda error
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()