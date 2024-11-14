from flask import Flask, request
from db import DataBase

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/order")
def getorder():
    db = DataBase()
    # data = request.json
    filter = request.args.get('filter')
    value = request.args.get('value')

# # Establish connection
    conn = db.connect()

    cur = conn.cursor()

    cur.execute(f"select * from orders where {filter}='{value}'")

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
    db.close_connection(conn, cur)
    
    return {"order":order_dict}, 200

@app.route("/customer")
def get_customer():
    # filter = request.args.get('filter')
    value = request.args.get('customer_id')

    db = DataBase()
    conn = db.connect()

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
    db.close_connection(conn, cur)
    
    return {"customer":customer_dict}, 200

@app.route("/product")
def get_product():
    # filter = request.args.get('filter')
    value = request.args.get('product_id')
    db = DataBase()
    conn = db.connect()
    conn = db.connect()

    cur = conn.cursor()

    cur.execute(f"select * from products where product_id={value}")

    product = cur.fetchone()
    
    product_dict = {
            "product_id":product[0],
            "product_name":product[1],
            "price":product[2], 
            "stock":product[3], 
            "category":product[4]
            }

    print(product)
    print(product_dict)
    db.close_connection(conn, cur)
    
    return {"product":product_dict}, 200

@app.route("/run_query")
def run_query():
    try:
        value = request.args.get('query')
        db = DataBase()
        conn = db.connect()
        conn = db.connect()

        cur = conn.cursor()

        cur.execute(query)
        
        result = cur.fetchone()

        return {"result":result}, 200
    except Exception as e:
        print(e)
        return {"error": "something went wrong"},500

