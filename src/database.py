import psycopg2


def connect():
    connection = psycopg2.connect(database='pyp',
                                  host='localhost',
                                  user='postgres',
                                  password='lolkek12')
    return connection


def close_connection(conn):
    if conn:
        conn.close()


def close_cursor(cur):
    if cur:
        cur.close()


def create_table():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS nft (mint varchar(120) primary key, name varchar(80) not null, standard varchar(50), solBalance float(25))")
        conn.commit()
    except EOFError as err:
        print("Error has occured", err)
    finally:
        close_cursor(cur)
        close_connection(conn)


def insert_value(mint, name, standard, sol_balance):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO nft (mint, name, standard, solBalance) VALUES "
                    f"('{mint}','{name}','{standard}', {sol_balance})")
        conn.commit()
    except EOFError as err:
        print("Error has occured", err)
    finally:
        close_cursor(cur)
        close_connection(conn)


def check_if_exists(mint):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(f"select exists(select * from nft where mint='{mint}')")
        conn.commit()
        return cur.fetchone()[0]
    except EOFError as err:
        print("Error has occured", err)
    finally:
        close_cursor(cur)
        close_connection(conn)


def get_value(mint):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM nft WHERE mint='{mint}'")
        conn.commit()
        return cur.fetchall()
    except EOFError as err:
        print("Error has occured", err)
    finally:
        close_cursor(cur)
        close_connection(conn)
