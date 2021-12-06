--
-- File generated with SQLiteStudio v3.3.3 on ?? 12? 5 12:28:25 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Car
CREATE TABLE Car (carID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, carVIN INTEGER UNIQUE, editionCode INTEGER, carMake TEXT, carModel TEXT, manufacturerID INTEGER REFERENCES Manufacturer (manufacturerID), carPrice DOUBLE, quantityOnHand INTEGER);
INSERT INTO Car (carID, carVIN, editionCode, carMake, carModel, manufacturerID, carPrice, quantityOnHand) VALUES (1, 157944212, 2020, 'BMW', 'X6', 1, 64300.0, 5);
INSERT INTO Car (carID, carVIN, editionCode, carMake, carModel, manufacturerID, carPrice, quantityOnHand) VALUES (2, 243213442, 2020, 'BMW', 'X7', 1, 99000.0, 4);
INSERT INTO Car (carID, carVIN, editionCode, carMake, carModel, manufacturerID, carPrice, quantityOnHand) VALUES (3, 435436423, 2018, 'Mercedes-Benz', 'C-Class', 2, 30990.0, 6);
INSERT INTO Car (carID, carVIN, editionCode, carMake, carModel, manufacturerID, carPrice, quantityOnHand) VALUES (4, 121343255, 2020, 'Mercedes-Benz', 'E-Class', 2, 40990.0, 5);
INSERT INTO Car (carID, carVIN, editionCode, carMake, carModel, manufacturerID, carPrice, quantityOnHand) VALUES (5, 234127984, 2014, 'Chevrolet', 'Corvette', 3, 31998.0, 3);
INSERT INTO Car (carID, carVIN, editionCode, carMake, carModel, manufacturerID, carPrice, quantityOnHand) VALUES (6, 244355465, 2020, 'Chevrolet', 'Tahoe', 3, 64695.0, 5);

-- Table: CarSalesInvoice
CREATE TABLE CarSalesInvoice (invoiceID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, invoiceNumber INTEGER UNIQUE, orderID INTEGER REFERENCES CarSalesOrder (orderID), customerID INTEGER REFERENCES Customer (customerID), invoicePrice DOUBLE, saleTax DOUBLE, invoiceDate DATE);
INSERT INTO CarSalesInvoice (invoiceID, invoiceNumber, orderID, customerID, invoicePrice, saleTax, invoiceDate) VALUES (1, 35664353, 3, 3, 33123.0, 2133.0, '2021/5/16');
INSERT INTO CarSalesInvoice (invoiceID, invoiceNumber, orderID, customerID, invoicePrice, saleTax, invoiceDate) VALUES (2, 35664354, 3, 3, 105814.0, 6814.0, '2021/5/17');
INSERT INTO CarSalesInvoice (invoiceID, invoiceNumber, orderID, customerID, invoicePrice, saleTax, invoiceDate) VALUES (3, 14357678, 2, 2, 77066.0, 4078.0, '2021/9/12');
INSERT INTO CarSalesInvoice (invoiceID, invoiceNumber, orderID, customerID, invoicePrice, saleTax, invoiceDate) VALUES (4, 56789545, 1, 1, 67867.0, 3567.0, '2021/10/8');

-- Table: CarSalesOrder
CREATE TABLE CarSalesOrder (orderID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, orderNumber INTEGER UNIQUE, customerID INTEGER REFERENCES Customer (customerID), totalPrice DOUBLE, orderDate DATE);
INSERT INTO CarSalesOrder (orderID, orderNumber, customerID, totalPrice, orderDate) VALUES (1, 2134324, 1, 64300.0, '2021/10/7');
INSERT INTO CarSalesOrder (orderID, orderNumber, customerID, totalPrice, orderDate) VALUES (2, 1222143, 2, 72988.0, '2021/9/10');
INSERT INTO CarSalesOrder (orderID, orderNumber, customerID, totalPrice, orderDate) VALUES (3, 3567667, 3, 129990.0, '2021/5/15');

-- Table: Customer
CREATE TABLE Customer (customerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, customerName TEXT, streetAddress TEXT, city TEXT, state TEXT, zipCode INTEGER);
INSERT INTO Customer (customerID, customerName, streetAddress, city, state, zipCode) VALUES (1, 'Kiza Brown', '2133 Sun St', 'San Jose', 'CA', 95112);
INSERT INTO Customer (customerID, customerName, streetAddress, city, state, zipCode) VALUES (2, 'Jone Long', '324 6th Road', 'New York', 'NY', 10001);
INSERT INTO Customer (customerID, customerName, streetAddress, city, state, zipCode) VALUES (3, 'Rick Young', '121 Yellow St', 'Chicago', 'IL', 60001);

-- Table: Manufacturer
CREATE TABLE Manufacturer (manufacturerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, manufacturerName TEXT, streetAddress TEXT, city TEXT, state TEXT, zipCode INTEGER);
INSERT INTO Manufacturer (manufacturerID, manufacturerName, streetAddress, city, state, zipCode) VALUES (1, 'BMW Manufacturing Company', '1100 Apple road', 'Greer', 'SC', 29526);
INSERT INTO Manufacturer (manufacturerID, manufacturerName, streetAddress, city, state, zipCode) VALUES (2, 'MBUSI', '1210 Star road', 'Tuscaloosa', 'AL', 35004);
INSERT INTO Manufacturer (manufacturerID, manufacturerName, streetAddress, city, state, zipCode) VALUES (3, 'GM Mansing Grand River', '1020 Bill St', 'Lansing', 'MI', 48001);

-- Table: OrderedCar
CREATE TABLE OrderedCar (orderID INTEGER NOT NULL REFERENCES carSalesOrder (orderID), carID INTEGER NOT NULL REFERENCES Car (carID), orderedQuantity INTEGER, PRIMARY KEY (orderID, carID));
INSERT INTO OrderedCar (orderID, carID, orderedQuantity) VALUES (1, 1, 1);
INSERT INTO OrderedCar (orderID, carID, orderedQuantity) VALUES (2, 5, 1);
INSERT INTO OrderedCar (orderID, carID, orderedQuantity) VALUES (2, 4, 1);
INSERT INTO OrderedCar (orderID, carID, orderedQuantity) VALUES (3, 2, 1);
INSERT INTO OrderedCar (orderID, carID, orderedQuantity) VALUES (3, 3, 1);

-- Table: SelledCar
CREATE TABLE SelledCar (invoiceID INTEGER NOT NULL REFERENCES carSalesInvoice (invoiceID), carID INTEGER NOT NULL REFERENCES Car (carID), selledQuantity INTEGER, PRIMARY KEY (invoiceID, carID));
INSERT INTO SelledCar (invoiceID, carID, selledQuantity) VALUES (1, 3, 1);
INSERT INTO SelledCar (invoiceID, carID, selledQuantity) VALUES (2, 2, 1);
INSERT INTO SelledCar (invoiceID, carID, selledQuantity) VALUES (3, 4, 1);
INSERT INTO SelledCar (invoiceID, carID, selledQuantity) VALUES (3, 5, 1);
INSERT INTO SelledCar (invoiceID, carID, selledQuantity) VALUES (4, 1, 1);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
