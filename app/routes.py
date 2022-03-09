from app import app, tables, models
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
@app.route('/tables')
def create_tables():
    # create a table for the customers
    customer_db = models.Customer.query.all()
    table_customers = tables.Customer_table(customer_db)
    table_customers.border = True
    # create a table for the orders
    orders_db = models.Orders.query.all()
    table_orders = tables.Orders_table(orders_db)
    table_orders.border = True
    return render_template('tables.html', table1=table_customers, table2 = table_orders)