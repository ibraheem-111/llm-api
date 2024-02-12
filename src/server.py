from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/order")
def getorder():
    # data = request.json
    filter = request.args.get('filter')
    value = request.args.get('value')
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

    cur = conn.cursor()

    cur.execute(f"select * from orders where {filter}={value}")

    order = cur.fetchone()
    
    order_dict = {
            "customer_id":order[0],
            "product_id":order[1],
            "order_id":order[2], 
            "quantity":order[3],
            "time":order[4],
            "status":order[5]
            }

    print(order)
    print(order_dict)
    conn.commit()
    cur.close()
    conn.close()
    
    return {"order":order_dict}, 200

@app.route("customer")
def get_customer():
    # filter = request.args.get('filter')
    value = request.args.get('customer_id')
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

    cur = conn.cursor()

    cur.execute(f"select * from customers where customer_id={value}")

    customer = cur.fetchone()
    
    customer_dict = {
            "customer_id":customer[0],
            "name":customer[1],
            "phone":customer[2], 
            "address":customer[3]
            }

    print(customer)
    print(customer_dict)
    conn.commit()
    cur.close()
    conn.close()
    
    return {"order":customer_dict}, 200

@app.route("product")
def get_product():
    # filter = request.args.get('filter')
    value = request.args.get('product_id')
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

    cur = conn.cursor()

    cur.execute(f"select * from products where product_id={value}")

    product = cur.fetchone()
    
    product_dict = {
            "customer_id":product[0],
            "name":product[1],
            "phone":product[2], 
            "address":product[3]
            }

    print(product)
    print(product_dict)
    conn.commit()
    cur.close()
    conn.close()
    
    return {"order":product_dict}, 200