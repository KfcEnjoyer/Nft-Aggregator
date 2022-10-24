import psycopg2


def connect():
    connection = psycopg2.connect(database='DBname',
                                  host='localhost',
                                  user='postgres',
                                  password='DBpassword')
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
            "CREATE TABLE IF NOT EXISTS nft (mint varchar(120) primary key, nft json)")
        conn.commit()
    except EOFError as err:
        print("Error has occured", err)
    finally:
        close_cursor(cur)
        close_connection(conn)


def insert_value(mint, nft):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO nft (mint, nft) VALUES "
                    f"('{mint}','{nft}')")
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
        cur.execute(f"SELECT mint, nft->>'name', nft->>'standard', nft->'metaplex'->'owners'"
                    f" FROM nft WHERE mint='{mint}'")
        conn.commit()
        return cur.fetchall()
    except EOFError as err:
        print("Error has occured", err)
    finally:
        close_cursor(cur)
        close_connection(conn)
