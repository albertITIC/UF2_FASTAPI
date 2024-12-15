# Fitxer que ens serveix per connectar-nos a la base de dades
import mysql.connector
import psycopg2


def db_conn():
    try:
        conn = psycopg2.connect(
            dbname = "postgres",
            user = "user_postgres",          
            password = "pass_postgres",    
            host = "localhost",
            port = "5432"
            # collation = "utf8mb4_general_ci"
        )
        
           
        # return mysql.connector.connect(
        #     host = host,
        #     port = port,
        #     user = user,
        #     password = password,
        #     database = dbname,
        #     collation = collation
        # ) 
            
    except Exception as e:
            return {"status": -1, "message": f"Error de connexió:{e}" }
        
    return conn