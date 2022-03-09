from flask_table import Table, Col

class Customer_table(Table):
    Customer_ID = Col('Customer_ID')
    Customer_First_Name = Col('Customer_First_Name')
    Customer_Last_Name = Col('Customer_Last_Name')
    Age = Col('Age')
    Country = Col('Country')



class Orders_table(Table):
    Order_ID = Col('Order_ID')
    Date = Col('Date')
    Price = Col('Price')
    Chair = Col('Chair')
    Stool = Col('Stool')
    Table = Col('Table')
    Cabinet = Col('Cabinet')
    Dresser = Col('Dresser')
    Couch = Col('Couch')
    Bed = Col('Bed')
    Shelf = Col('Shelf')



