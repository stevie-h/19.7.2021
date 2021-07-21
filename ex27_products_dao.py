
from ex27_product import *


def create_product_table(conn):
    conn.execute('''
        CREATE TABLE PRODUCTS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NAME TEXT NOT NULL, PRICE REAL NOT NULL,
        QUANTITY INTEGER)
        ''')


def insert_new_product(conn, e):
    conn.execute(f'''
    INSERT INTO PRODUCTS
    (NAME, PRICE, QUANTITY)
    VALUES
    ('{e.name}', {e.price}, {e.quantity})''')
    conn.commit()


def get_all_products(conn):
    result = conn.execute('SELECT * FROM PRODUCTS')
    product_list = []
    for row in result:
        e = Product(row[0], row[1], row[2], row[3])
        product_list.append(e)
    return product_list


def get_product_by_id(conn, id):
    result = conn.execute(f'SELECT * FROM PRODUCTS WHERE ID = {id}')
    for row in result:
        e = Product(row[0], row[1], row[2], row[3])
        return e
    return None


def update_product_by_id(conn, e, id):
    conn.execute(f'''UPDATE PRODUCTS SET
        NAME = '{e.name}', PRICE = {e.price}, 
        QUANTITY = {e.quantity}
        WHERE ID = {id}''')
    conn.commit()


def delete_product_by_id(conn, id):
    conn.execute(f'DELETE FROM PRODUCTS WHERE ID = {id}')
    conn.commit()

