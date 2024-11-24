
def create_table(conn):

    conn = conn
    cursor = conn.cursor()

    sql = ''' CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_surname VARCHAR(255) NOT NULL,
            user_age BIGINT NOT NULL,
            user_email VARCHAR(255) NOT NULL)
    '''

    cursor.execute(sql)
    conn.commit()
    return "Taula users creada correctament"
