USE tasks;
-- CREATING A TABLE
create table sales(sale_date date,product_id int,total_revenue float);
insert into sales values("2025-09-11",1,123742.98);
select *from sales;
insert into sales values('2025-10-15',2,121331.1212);
insert into sales values('2025-09-02', 2, 95000.75),('2025-09-03', 1, 123742.98),('2025-09-04', 3, 87000.00),('2025-09-05', 2, 66000.25),('2025-09-06', 4, 143000.90),('2025-09-07', 3, 78000.40),('2025-09-08', 5, 99000.60),('2025-09-09', 1, 110500.10),('2025-09-10', 2, 102300.80);
-- What is the total revenue for all sales?
select sum(total_revenue) from sales;
-- What is the average revenue per sale?
select avg(total_revenue) from sales;
-- What is the maximum and minimum revenue for a single sale?
select min(total_revenue),max(total_revenue) from sales;
-- How many sales were made for each product ID?
select product_id,count(*) from sales group by product_id