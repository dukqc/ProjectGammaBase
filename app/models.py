from app import db


class Customer(db.Model):
    Customer_ID = db.Column(db.Integer, primary_key=True, unique = True)
    Customer_First_Name = db.Column(db.String(64), index=True, unique=True)
    Customer_Last_Name = db.Column(db.String(120), index=True, unique=True)
    Age = db.Column(db.Integer)
    Country = db.Column(db.String(69), index=True, unique=True)

def __repr__(self):
    return '<Customer {}>'.format(self.Customer_ID)

class Orders(db.Model):
    Order_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Date = db.Column(db.String(64), index=True, unique = True)
    Price = db.Column(db.Integer, index=True, unique = True)
    Chair = db.Column(db.Integer, index=True, unique = True)
    Stool = db.Column(db.Integer, index=True, unique = True)
    Table = db.Column(db.Integer, index=True, unique = True)
    Cabinet = db.Column(db.Integer, index=True, unique = True)
    Dresser = db.Column(db.Integer, index=True, unique = True)
    Couch = db.Column(db.Integer, index=True, unique = True)
    Bed = db.Column(db.Integer, index=True, unique = True)
    Shelf = db.Column(db.Integer, index=True, unique = True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('customer.Customer_ID'))

def __repr__(self):
    return '<Order {}>'.format(self.Order_ID)
