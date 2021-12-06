import mysql.connector as mysql
def insert(carVIN, editionCode,carMake,carModel,manufacturerID,carPrice,quantityOnHand):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("INSERT INTO Car VALUES (NULL,%s, %s, %s, %s, %s,%s,%s)",(carVIN, editionCode,carMake,carModel,manufacturerID,carPrice,quantityOnHand))
    conn.commit()
    conn.close()
def view():
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Car")
    rows = cur.fetchall()
    conn.close()
    return rows
def search(carVIN="", editionCode="",carMake="",carModel="",manufacturerID="",carPrice="",quantityOnHand=""):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Car WHERE carVIN =%s OR editionCode=%s OR carMake=%s OR carModel=%s OR manufacturerID=%s OR carPrice=%s OR quantityOnHand=%s",(carVIN, editionCode,carMake,carModel,manufacturerID,carPrice,quantityOnHand))
    rows = cur.fetchall()
    conn.commit()
    return rows
def delete(carID):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("DELETE FROM Car WHERE carID=%s",(carID,))
    conn.commit()
    conn.close()
def update(carID,carVIN, editionCode,carMake,carModel,manufacturerID,carPrice,quantityOnHand):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("UPDATE Car SET carVIN =%s , editionCode=%s , carMake=%s , carModel=%s , manufacturerID=%s , carPrice=%s , quantityOnHand=%s WHERE carID=%s",(carVIN, editionCode,carMake,carModel,manufacturerID,carPrice,quantityOnHand,carID))
    conn.commit()
    conn.close()
def view2():
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT Car.carVIN,editionCode,carMake,carModel,carPrice FROM Car INNER JOIN SelledCar on SelledCar.carID = Car.carID INNER JOIN CarSalesInvoice on CarSalesInvoice.invoiceID = SelledCar.invoiceID")
    rows = cur.fetchall()
    conn.close()
    return rows
def insert2(customerName, streetAddress,city,state,zipCode):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("INSERT INTO Customer VALUES (NULL,%s, %s, %s, %s, %s)",(customerName, streetAddress,city,state,zipCode))
    conn.commit()
    conn.close()
def view3():
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Customer")
    rows = cur.fetchall()
    conn.close()
    return rows
def search2(customerName, streetAddress,city,state,zipCode):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Customer WHERE customerName =%s OR streetAddress=%s OR city=%s OR state=%s OR zipCode=%s",(customerName, streetAddress,city,state,zipCode))
    rows = cur.fetchall()
    conn.commit()
    return rows
def delete2(customerID):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("DELETE FROM Customer WHERE customerID=%s",(customerID,))
    conn.commit()
    conn.close()
def update2(customerID,customerName, streetAddress,city,state,zipCode):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("UPDATE Customer SET customerName =%s , streetAddress=%s , city=%s , state=%s , zipCode=%s WHERE customerID=%s",(customerName, streetAddress,city,state,zipCode,customerID))
    conn.commit()
    conn.close()
def insert3(orderNumber, customerID,totalPrice,orderDate):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("INSERT INTO carsalesorder VALUES (NULL,%s, %s, %s, %s)",(orderNumber, customerID,totalPrice,orderDate))
    conn.commit()
    conn.close()
def view4():
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM CarSalesOrder")
    rows = cur.fetchall()
    conn.close()
    return rows
def search3(orderNumber, customerID,totalPrice,orderDate):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM carsalesorder WHERE orderNumber =%s OR customerID=%s OR totalPrice=%s OR orderDate=%s",(orderNumber, customerID,totalPrice,orderDate))
    rows = cur.fetchall()
    conn.commit()
    return rows
def delete3(orderID):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("DELETE FROM carsalesorder WHERE orderID=%s",(orderID,))
    conn.commit()
    conn.close()
def update3(orderID,orderNumber, customerID,totalPrice,orderDate):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("UPDATE carsalesorder SET orderNumber =%s ,  customerID=%s , totalPrice=%s , orderDate=%s WHERE orderID=%s",(orderNumber, customerID,totalPrice,orderDate,orderID))
    conn.commit()
    conn.close()
def insert4(manufacturerName, streetAddress,city,state,zipCode):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("INSERT INTO manufacturer VALUES (NULL,%s, %s, %s, %s, %s)",(manufacturerName, streetAddress,city,state,zipCode))
    conn.commit()
    conn.close()
def view5():
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM manufacturer")
    rows = cur.fetchall()
    conn.close()
    return rows
def search4(manufacturerName, streetAddress,city,state,zipCode):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("SELECT * FROM manufacturer WHERE manufacturerName =%s OR streetAddress=%s OR city=%s OR state=%s OR zipCode=%s",(manufacturerName, streetAddress,city,state,zipCode))
    rows = cur.fetchall()
    conn.commit()
    return rows
def delete4(manufacturerID):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("DELETE FROM manufacturer WHERE manufacturerID=%s",(manufacturerID,))
    conn.commit()
    conn.close()
def update4(manufacturerID,manufacturerName, streetAddress,city,state,zipCode):
    conn=mysql.connect(host="localhost",database="cardealer",user="python-user",password="password")
    cur=conn.cursor()
    cur.execute("UPDATE manufacturer SET manufacturerName =%s , streetAddress=%s , city=%s , state=%s , zipCode=%s WHERE customerID=%s",(manufacturerName, streetAddress,city,state,zipCode,manufacturerID))
    conn.commit()
    conn.close()    