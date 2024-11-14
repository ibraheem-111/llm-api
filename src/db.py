import psycopg2
class DataBase:
    
    def connect(self):
        params = {
            "host": "localhost",
            "port": 5432,
            "database": "postgres",
            "user": "postgres",
            "password": "ibraheem"
        }

    # Construct connection string
        conn_string = "dbname={database} user={user} password={password} host={host} port={port}".format(**params)

    # Establish connection
        conn = psycopg2.connect(conn_string)

        return conn
    
    def close_connection(self, conn, cur):
        conn.commit()
        cur.close()
        conn.close()
        