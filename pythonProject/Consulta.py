"""
Este modulo trabaja con fetch one para traer solo de a un registro

"""
import psycopg2
#Conexion con la base de datos
conn = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
try:
    with conn:
        #With cierra recurso de cursor, por lo que no es necesario llamar al metodo close()
        with conn.cursor() as curs:
            query = 'SELECT * FROM Legos WHERE id IN %s'
            entrada = input('Proporcina los id\'s a buscar (separado por comas): ')
            #Split separa cada uno de los valores de el input "entrada, luego lo convierte en tupla
            #Se convierte en tupla de tuplas, observe la coma al final de la sentencia
            llavesPrimarias = (tuple(entrada.split(',')),)

            curs.execute(query,llavesPrimarias)
            #fetchone regresa todos los registros
            regs = curs.fetchall()
            #Iterar cada uno de los resultados del fetch all
            for registro in regs:
                print(registro)
#e guarda error
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()