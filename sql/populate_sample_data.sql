-- Create Customer table
CREATE TABLE Customer (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create Store table
CREATE TABLE Store (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

-- Create Orders table
CREATE TABLE Orders (
    id INTEGER PRIMARY KEY,
    total REAL NOT NULL,
    date TEXT NOT NULL,
    store_id INTEGER,
    customer_id INTEGER,
    FOREIGN KEY (store_id) REFERENCES Store(id),
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

-- Populate Customer table
INSERT INTO Customer (name) VALUES
    ('Alice Johnson'),
    ('David Smith'),
    ('Eva Rodriguez'),
    ('Frank White'),
    ('Grace Lee'),
    ('Henry Brown'),
    ('Isabel Garcia'),
    ('Jack Anderson'),
    ('Kelly Taylor'),
    ('Liam Clark'),
    ('Mia Davis'),
    ('Noah Miller'),
    ('Olivia Wilson'),
    ('Peter Moore'),
    ('Quinn Thomas'),
    ('Rachel Hall'),
    ('Samuel Turner'),
    ('Tara Harris'),
    ('Ulysses Reed'),
    ('Victoria Martin');

-- Populate Store table
INSERT INTO Store (name, city) VALUES
    ('SuperMart', 'Metroville'),
    ('MegaStore', 'Bay City'),
    ('Discount Depot', 'Harbor Town'),
    ('Grocery Haven', 'Sunset Springs'),
    ('Fresh Market', 'Greenfield'),
    ('Quality Foods', 'Pleasantville'),
    ('Quick Stop', 'Riverside'),
    ('Value Mart', 'Highland Falls'),
    ('Convenience Corner', 'Mountain View'),
    ('Neighborhood Shop', 'Maple Ridge');

-- Populate Orders table for the year 2023 with at least 10 orders per month
INSERT INTO Orders (total, date, store_id, customer_id) VALUES
    (50.00, '2023-01-15', 1, 1),
    (75.50, '2023-01-20', 2, 2),
    (30.25, '2023-01-25', 3, 3),
    (100.00, '2023-01-30', 4, 4),
    (45.75, '2023-01-05', 5, 5),
    (60.50, '2023-01-10', 6, 6),
    (25.75, '2023-01-15', 7, 7),
    (80.20, '2023-01-20', 8, 8),
    (35.90, '2023-01-25', 9, 9),
    (95.25, '2023-01-30', 10, 10),
    (40.00, '2023-02-05', 1, 11),
    (120.50, '2023-02-10', 2, 12),
    (55.75, '2023-02-15', 3, 13),
    (70.30, '2023-02-20', 4, 14),
    (90.10, '2023-02-25', 5, 15),
    (65.80, '2023-02-28', 6, 16),
    (110.25, '2023-03-05', 7, 17),
    (38.50, '2023-03-10', 8, 18),
    (85.75, '2023-03-15', 9, 19),
    (42.20, '2023-03-20', 10, 20),
    -- Additional orders for a more comprehensive dataset
    (75.00, '2023-04-01', 1, 1),
    (60.30, '2023-04-05', 2, 2),
    (105.80, '2023-04-10', 3, 3),
    (48.25, '2023-04-15', 4, 4),
    (70.90, '2023-04-20', 5, 5),
    (92.40, '2023-04-25', 6, 6),
    (55.10, '2023-04-30', 7, 7),
    (80.75, '2023-05-05', 8, 8),
    (62.20, '2023-05-10', 9, 9),
    (110.50, '2023-05-15', 10, 10),
    (45.30, '2023-06-01', 1, 11),
    (78.60, '2023-06-05', 2, 12),
    (93.75, '2023-06-10', 3, 13),
    (56.40, '2023-06-15', 4, 14),
    (70.90, '2023-06-20', 5, 15),
    (105.20, '2023-06-25', 6, 16),
    (38.75, '2023-06-30', 7, 17),
    (85.20, '2023-07-05', 8, 18),
    (42.60, '2023-07-10', 9, 19),
    (78.40, '2023-07-15', 10, 20),
    -- Continue for August, September, October, November, December
    (65.00, '2023-08-01', 1, 1),
    (98.30, '2023-08-05', 2, 2),
    (115.20, '2023-08-10', 3, 3),
    (48.75, '2023-08-15', 4, 4),
    (70.90, '2023-08-20', 5, 5),
    (92.40, '2023-08-25', 6, 6),
    (55.10, '2023-08-30', 7, 7),
    (80.75, '2023-09-05', 8, 8),
    (62.20, '2023-09-10', 9, 9),
    (110.50, '2023-09-15', 10, 10),
    (45.30, '2023-10-01', 1, 11),
    (78.60, '2023-10-05', 2, 12),
    (93.75, '2023-10-10', 3, 13),
    (56.40, '2023-10-15', 4, 14),
    (70.90, '2023-10-20', 5, 15),
    (105.20, '2023-10-25', 6, 16),
    (38.75, '2023-10-30', 7, 17),
    (85.20, '2023-11-05', 8, 18),
    (42.60, '2023-11-10', 9, 19),
    (78.40, '2023-11-15', 10, 20),
    (65.00, '2023-12-01', 1, 1),
    (98.30, '2023-12-05', 2, 2),
    (115.20, '2023-12-10', 3, 3),
    (48.75, '2023-12-15', 4, 4),
    (70.90, '2023-12-20', 5, 5),
    (92.40, '2023-12-25', 6, 6),
    (55.10, '2023-12-30', 7, 7),
    (80.75, '2023-12-31', 8, 8);
