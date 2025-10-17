UPDATE drivers SET current_truck_id = 1 WHERE driver_id = 1;
UPDATE drivers SET current_truck_id = 2 WHERE driver_id = 2;
UPDATE drivers SET current_truck_id = 3 WHERE driver_id = 3;
UPDATE drivers SET current_truck_id = 4 WHERE driver_id = 4;
UPDATE drivers SET current_truck_id = 5 WHERE driver_id = 5;
UPDATE drivers SET current_truck_id = 6 WHERE driver_id = 6;
UPDATE drivers SET current_truck_id = 8 WHERE driver_id = 7;
UPDATE drivers SET current_truck_id = 9 WHERE driver_id = 8;
UPDATE drivers SET current_truck_id = 10 WHERE driver_id = 9;
UPDATE drivers SET current_truck_id = 11 WHERE driver_id = 10;

-- Insert sample loads
INSERT INTO loads (
    driver_id, truck_id, cargo_type, cargo_description, cargo_quantity, weight_lbs,
    pickup_location, destination, load_status, scheduled_departure_time, priority_level,
    temperature_control, hazmat, rate_amount, customer_name
) VALUES
-- LOADED Loads
(1, 1, 'Electronics', 'Laptops and monitors for retail stores', '20 pallets', 35000.00,
 'Amazon Warehouse, 1234 Logistics Dr, Chicago, IL 60601',
 'Best Buy Distribution Center, 5678 Commerce St, Dallas, TX 75201',
 'LOADED', NOW() + INTERVAL '2 hours', 'HIGH', FALSE, FALSE, 2500.00, 'Best Buy'),

(2, 2, 'Produce', 'Fresh vegetables and fruits', '15 tons', 30000.00,
 'Farm Fresh Foods, 9876 Rural Rd, Salinas, CA 93901',
 'Whole Foods Market, 3456 Market St, San Francisco, CA 94102',
 'LOADED', NOW() + INTERVAL '3 hours', 'URGENT', TRUE, FALSE, 3200.00, 'Whole Foods'),

(3, 3, 'Construction Materials', 'Steel beams and metal sheets', '25 tons', 50000.00,
 'Steel Mill, 5432 Industrial Blvd, Pittsburgh, PA 15201',
 'Construction Site, 7890 Building Ave, New York, NY 10001',
 'LOADED', NOW() + INTERVAL '4 hours', 'NORMAL', FALSE, FALSE, 4500.00, 'ABC Construction'),

(5, 5, 'Pharmaceuticals', 'Medical supplies and medications', '10 pallets', 15000.00,
 'Pharma Warehouse, 2468 Medical Dr, Boston, MA 02101',
 'Hospital Supply Center, 1357 Health St, Miami, FL 33101',
 'LOADED', NOW() + INTERVAL '1 hour', 'URGENT', TRUE, FALSE, 5000.00, 'MedSupply Inc'),

-- NOT LOADED Loads (Various delay reasons)
(4, 4, 'Auto Parts', 'Car engines and transmissions', '18 pallets', 28000.00,
 'Auto Parts Depot, 1111 Motor Ave, Detroit, MI 48201',
 'Car Dealer Network, 2222 Vehicle Rd, Cleveland, OH 44101',
 'LOADING', NOW() + INTERVAL '5 hours', 'NORMAL', FALSE, FALSE, 3800.00, 'Auto Network USA'),

(6, 6, 'Furniture', 'Office desks and chairs', '30 pallets', 42000.00,
 'Furniture Factory, 3333 Oak St, Grand Rapids, MI 49501',
 'Office Depot DC, 4444 Supply Way, Indianapolis, IN 46201',
 'ASSIGNED', NOW() + INTERVAL '6 hours', 'NORMAL', FALSE, FALSE, 2800.00, 'Office Depot'),

(7, 8, 'Food Products', 'Canned goods and packaged foods', '22 pallets', 32000.00,
 'Food Processing Plant, 5555 Factory Ln, Minneapolis, MN 55401',
 'Grocery Chain DC, 6666 Distribution Dr, Milwaukee, WI 53201',
 'ASSIGNED', NOW() + INTERVAL '7 hours', 'NORMAL', FALSE, FALSE, 2200.00, 'SuperMart'),

(8, 9, 'Textiles', 'Clothing and fabrics', '25 pallets', 18000.00,
 'Textile Mill, 7777 Cotton Rd, Charlotte, NC 28201',
 'Fashion Retailer DC, 8888 Style Blvd, Atlanta, GA 30301',
 'ASSIGNED', NOW() + INTERVAL '8 hours', 'LOW', FALSE, FALSE, 1900.00, 'Fashion First'),

(9, 10, 'Chemicals', 'Industrial cleaning supplies', '12 tons', 24000.00,
 'Chemical Plant, 9999 Science Dr, Houston, TX 77001',
 'Industrial Supplier, 1010 Factory St, New Orleans, LA 70112',
 'LOADING', NOW() + INTERVAL '5 hours', 'NORMAL', FALSE, TRUE, 3500.00, 'CleanCo Industries'),

(10, 11, 'Consumer Goods', 'Household items and appliances', '28 pallets', 38000.00,
 'Import Warehouse, 1212 Shipping Way, Los Angeles, CA 90001',
 'Retail Chain DC, 1313 Store Rd, Phoenix, AZ 85001',
 'ASSIGNED', NOW() + INTERVAL '9 hours', 'NORMAL', FALSE, FALSE, 3100.00, 'HomeGoods Plus');