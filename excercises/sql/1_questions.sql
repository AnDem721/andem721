use baza

-- 1.1 Select the names of all the products in the store.
select name from Products;

-- 1.2 Select the names and the prices of all the products in the store.
select name, price from Products;

-- 1.3 Select the name of the products with a price less than or equal to $200.
select name from Products where price <= 200;

-- 1.4 Select all the products with a price between $60 and $120.
select name from Products where price between 60 and 120;

-- 1.5 Select the name and price in cents (i.e., the price must be multiplied by 100).
select name, (price*100) as cents from Products; 

-- 1.6 Compute the average price of all the products.
select avg(price) as srednia_cena from Products;

-- 1.7 Compute the average price of all products with manufacturer code equal to 2.
select avg(price) from Products where manufacturer = 2;

-- 1.8 Compute the number of products with a price larger than or equal to $180.
select count(*) from Products where price >= 180;

-- 1.9 Select the name and price of all products with a price larger than or equal to $180, and sort first by price (in descending order), 
-- and then by name (in ascending order).
select name, price from Products where price >= 180 order by price desc;

-- 1.10 Select all the data from the products, including all the data for each product's manufacturer.
select * from Products p inner join Manufacturers m on p.Manufacturer = m.Code;

-- 1.11 Select the product name, price, and manufacturer name of all the products.
select p.Name, p.Price, m.Name from Products p inner join Manufacturers m on p.Manufacturer = m.Code;


-- 1.12 Select the average price of each manufacturer's products, showing only the manufacturer's code.
select Manufacturer, avg(price) from Products group by Manufacturer;

-- 1.13 Select the average price of each manufacturer's products, showing the manufacturer's name.
select avg(p.price), m.Name from Products p join Manufacturers m on p.Manufacturer=m.Code group by m.Name;

select Manufacturer m, avg(price) from Products group by Manufacturer;

-- 1.14 Select the names of manufacturer whose products have an average price larger than or equal to $150.
select avg(p.price) as srednio, m.Name from Products p 
	join Manufacturers m on p.Manufacturer=m.Code 
        group by m.Name	having srednio >= 150;
        


-- 1.15 Select the name and price of the cheapest product.
select Name, Price from Products order by price asc limit 1;

-- 1.16 Select the name of each manufacturer along with the name and price of its most expensive product.
select m.Name, p.Name, max(p.price) from Products p right join Manufacturers m on p.Manufacturer = m.Code group by m.Name;

select max_price_mapping.name as manu_name, max_price_mapping.price, products_with_manu_name.name as product_name
from 
    (SELECT Manufacturers.Name, MAX(Price) price
     FROM Products, Manufacturers
     WHERE Manufacturer = Manufacturers.Code
     GROUP BY Manufacturers.Name)
     as max_price_mapping
   left join
     (select Products.*, Manufacturers.name manu_name
      from Products join Manufacturers
      on (Products.manufacturer = Manufacturers.code))
      as products_with_manu_name
 on
   (max_price_mapping.name = products_with_manu_name.manu_name
    and
    max_price_mapping.price = products_with_manu_name.price);

-- 1.17 Add a new product: Loudspeakers, $70, manufacturer 2.
INSERT INTO `baza`.`Products`
(`Code`,
`Name`,
`Price`,
`Manufacturer`)
VALUES
( 11, 'Loudspeakers',
'70',
2);


-- 1.18 Update the name of product 8 to "Laser Printer".
update Products
	set Name = 'Laser Printer'
		where Code = 8;

-- 1.19 Apply a 10% discount to all products.
update Products 
	set price = price * 0.9;
    

-- 1.20 Apply a 10% discount to all products with a price larger than or equal to $120.

update Products 
	set price = price * 0.9
		where price >= 120; 
