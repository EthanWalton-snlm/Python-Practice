CREATE TABLE salesman (
     salesman_id INT PRIMARY KEY,
     name VARCHAR(255),
     city VARCHAR(255),
     commission DECIMAL(4, 2)
 );


 INSERT INTO salesman (salesman_id, name, city, commission) VALUES
 (5001, 'James Hoog', 'New York', 0.15),
 (5002, 'Nail Knite', 'Paris', 0.13),
 (5005, 'Pit Alex', 'London', 0.11),
 (5006, 'Mc Lyon', 'Paris', 0.14),
 (5003, 'Lauson Hen', NULL, 0.12),
 (5007, 'Paul Adam', 'Rome', 0.13);


 Select * from salesman


 CREATE TABLE orders (
     ord_no INT PRIMARY KEY,
     purch_amt DECIMAL(10, 2),
     ord_date DATE,
     customer_id INT,
     salesman_id INT
 );


 INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
 (70001, 150.5, '2012-10-05', 3005, 5002),
 (70009, 270.65, '2012-09-10', 3001, 5005),
 (70002, 65.26, '2012-10-05', 3002, 5001),
 (70004, 110.5, '2012-08-17', 3009, 5003),
 (70007, 948.5, '2012-09-10', 3005, 5002),
 (70005, 2400.6, '2012-07-27', 3007, 5001),
 (70008, 5760, '2012-09-10', 3002, 5001),
 (70010, 1983.43, '2012-10-10', 3004, 5006),
 (70003, 2480.4, '2012-10-10', 3009, 5003),
 (70012, 250.45, '2012-06-27', 3008, 5002),
 (70011, 75.29, '2012-08-17', 3003, 5007),
 (70013, 3045.6, '2012-04-25', 3002, 5001);



 Select * from salesman;
 Select * from Orders;

 -- Sub-Query
 -- 1. Write a query to display all the orders from the orders table issued by the salesman 'Paul Adam'.

 -- Step 1: Hard code the value and get final result
 Select *
 	from Orders
 	where salesman_id = 5007;

 -- Step 2: Get the Hard code value with Select
 Select salesman_id
 	from salesman
 	where name = 'Paul Adam'; -- 5007


 -- Step 3: Replace the hard coded value
 Select *
 	from Orders
 	where salesman_id = (Select salesman_id
 								from salesman
 								where name = 'Paul Adam')


 Select *
 	from Orders
 	where salesman_id = (Select salesman_id
 								from salesman
 								where name = 'Paul Adam');


 -- 2. Write a query to find all orders attributed to a salesman in Paris



 -- Step 1: Hard code the value and get final result
 Select *
 	from Orders
 	where salesman_id in (5002, 5006)

 -- Step 2: Get the Hard code value with Select
 Select salesman_id
 	from salesman
 	Where city  = 'Paris'


 -- Step 3: Replace the hard coded value

 Select *
 	from Orders
 	where salesman_id in (Select salesman_id
 							from salesman
 							Where city  = 'Paris')


 -- 3. Write a query to find the name and id of all salesmen who had more than one customer.

 -- Step 1: Hard code the value and get final result

 Select *
 	from  customer
 	Order by salesman_id;

 -- 5001, 5002

 Select *
 	from salesman
 	where salesman_id In (5001, 5002)


 -- Step 2: Get the Hard code value with Select


 Select salesman_id
 	from  customer
 	group by salesman_id
 	Having count(customer_id) > 1

 -- Step 3: Replace the hard coded value


 Select *
 	from salesman
 	where salesman_id In (
 							Select salesman_id
 								from  customer
 								group by salesman_id
 								Having count(customer_id) > 1)


 Select * from orders

 -- 4. Find all the all order where purch_amt is more than by customer_id 3005 purch_amt

 -- Anita
 -- 50
 -- 300
 -- 250

 -- Luv

 -- Step 1: Hard code the value and get final result
 Select *
 		from orders
 		where purch_amt > 948.5

 -- Step 2: Get the Hard code value with Select
 Select max(purch_amt)
 	from orders
 	Where customer_id = 3005


 -- Step 3: Replace the hard coded value

 Select *
 		from orders
 		where purch_amt > (Select max(purch_amt)
 									from orders
 									Where customer_id = 3005)

 Select *
 	from  customer

 -- All & Any -- DX

 Select purch_amt
 		from orders
 		Where customer_id = 3005

 Select *
 		from orders
 		where purch_amt > All(Select purch_amt
 										from orders
 										Where customer_id = 3005)

 -- Graham Zusi

 -- Step 2: Get the Hard code value with Select
 Select customer_id
 	from  customer
 	where cust_name = 'Graham Zusi'


 -- Step 3: Replace the hard coded value

 Select *
		from orders
 		where purch_amt > All(Select purch_amt
 										from orders
 										Where customer_id = (Select customer_id
 																from  customer
 																where cust_name = 'Graham Zusi'))

 Select *
 		from orders
 		where purch_amt > Any(Select purch_amt
 										from orders
 										Where customer_id = 3005)


 --	50
 --	200
 --	1000

 -- All - above max value - 948.5
 -- Any - above min value - 150


 -- 6.  Write a query to display only those customers whose grade are, in fact, higher than every customer in New York.

 Select *
 	from  customer


 -- 7. Write a query to find all orders with an amount smaller than any amount for a customer in London.
