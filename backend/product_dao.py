from sql_connection import get_sql_connection


# extracting product details from database
def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM "
             "products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
    return response


# inserting new product record in the database
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = "insert into products (name, uom_id, price_per_unit) values (%s, %s, %s)"
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


# deleting a specific product from database
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("delete from products where product_id = " + str(product_id))
    cursor.execute(query)
    connection.commit()


# updating product price
def update_product_price(connection, product_id, new_price):
    cursor = connection.cursor()
    query = "UPDATE products SET price_per_unit = %s WHERE product_id = %s"
    cursor.execute(query, (new_price, product_id))
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 13))
