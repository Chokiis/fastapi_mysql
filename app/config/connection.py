import mysql.connector
import os
import time

# Intenta conectarse a MySQL con un retardo para esperar que la base de datos inicie
class dbConnection():
    max_attempts = 30
    for attempt in range(max_attempts):
        try:
            db = mysql.connector.connect(
                host=os.environ["MYSQL_HOST"],
                user=os.environ["MYSQL_USER"],
                password=os.environ["MYSQL_PASSWORD"],
                database=os.environ["MYSQL_DB"]
            )
            cursor = db.cursor()
            break  # Si se conecta con éxito, salir del bucle
        except mysql.connector.Error as err:
            if attempt < max_attempts - 1:
                print(f"Error al conectar a la base de datos. Intento {attempt + 1}/{max_attempts}. Retrying...")
                time.sleep(5)  # Espera 2 segundos antes de intentar nuevamente
            else:
                raise  # Si no se puede conectar después de varios intentos, levantar la excepción