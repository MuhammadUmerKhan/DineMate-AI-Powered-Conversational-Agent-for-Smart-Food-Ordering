-- ✅ Create the menu table to store food items and their prices
-- CREATE TABLE menu (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each menu item
--     name TEXT UNIQUE NOT NULL,             -- Item name (must be unique)
--     price REAL NOT NULL                    -- Price of the item (decimal values)
-- );

-- -- ✅ Insert menu items into the menu table
-- INSERT INTO menu (name, price) VALUES
-- ('Cheese Burger', 5.99),
-- ('Chicken Burger', 6.99),
-- ('Veggie Burger', 5.49),
-- ('Pepperoni Pizza', 12.99),
-- ('Margherita Pizza', 11.49),
-- ('BBQ Chicken Pizza', 13.99),
-- ('Grilled Chicken Sandwich', 7.99),
-- ('Club Sandwich', 6.99),
-- ('Spaghetti Carbonara', 9.99),
-- ('Fettuccine Alfredo', 10.49),
-- ('Tandoori Chicken', 11.99),
-- ('Butter Chicken', 12.49),
-- ('Beef Steak', 15.99),
-- ('Chicken Biryani', 8.99),
-- ('Mutton Biryani', 10.99),
-- ('Prawn Curry', 13.49),
-- ('Fish and Chips', 9.49),
-- ('French Fries', 3.99),
-- ('Garlic Bread', 4.49),
-- ('Chocolate Brownie', 5.49),
-- ('Vanilla Ice Cream', 3.99),
-- ('Strawberry Shake', 4.99),
-- ('Mango Smoothie', 5.49),
-- ('Coca-Cola', 2.49),
-- ('Pepsi', 2.49),
-- ('Fresh Orange Juice', 4.99);

-- --------------------------------------------------------

-- ✅ Create the orders table to store customer orders
-- DROP TABLE orders;
-- CREATE TABLE orders (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Unique order ID
--     items TEXT NOT NULL,                    -- Ordered items in JSON format (e.g., {"burger": 2})
--     total_price REAL NOT NULL,               -- Total price
--     status TEXT CHECK(status IN ('Pending', 'In Process', 'Completed', 'Canceled', 'Preparing', 'Ready')) DEFAULT 'Pending',  -- Status with default
--     date TEXT DEFAULT (DATE('now')),         -- Order placement date
--     time TEXT DEFAULT (TIME('now'))          -- Order placement time
-- );
-- ✅ Insert sample orders
-- INSERT INTO orders (items, total_price, status) VALUES
-- ('{"Cheese Burger": 2, "French Fries": 1, "Coca-Cola": 1}', 17.46, 'Pending'),
-- ('{"Pepperoni Pizza": 1, "Garlic Bread": 1, "Pepsi": 1}', 19.97, 'In Process'),
-- ('{"Chicken Biryani": 2, "Mango Smoothie": 1}', 23.47, 'Completed'),
-- ('{"Club Sandwich": 1, "Strawberry Shake": 1}', 11.98, 'Pending'),
-- ('{"Beef Steak": 1, "Fresh Orange Juice": 1}', 20.98, 'In Process');

-- ✅ Create staff table
-- CREATE TABLE staff (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     username TEXT UNIQUE NOT NULL,
--     password_hash TEXT NOT NULL,
--     role TEXT CHECK(role IN ('admin', 'kitchen_staff', 'customer_support')) NOT NULL,
--     is_staff BOOLEAN DEFAULT TRUE
-- );

-- ✅ Create customers table
-- CREATE TABLE customers (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     username TEXT UNIQUE NOT NULL,
--     password_hash TEXT NOT NULL,
--     email TEXT UNIQUE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- SELECT * FROM staff;
-- SELECT * FROM customers;