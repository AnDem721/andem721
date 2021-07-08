
CREATE DATABASE IF NOT EXISTS `codeme_homework`;
USE `codeme_homework`;
CREATE TABLE IF NOT EXISTS `table_homework_companies` (
	`id_user`				INT AUTO_INCREMENT	PRIMARY KEY,
    `first_name`			VARCHAR(100),
    `last_name`				VARCHAR(100),
    `established_date`		DATE 	DEFAULT DATE(NOW()),
    `address`				CHAR(100) 	DEFAULT 'NONE',
    `company_name`			CHAR(100),
    `tax_id_no`				INT 	DEFAULT 0 
    );
 TRUNCATE `table_homework_companies`;   
 INSERT INTO `table_homework_companies` (first_name, last_name, established_date, address, company_name, tax_id_no) VALUES
 ('Andrzej', 'Dembowski', '2021-01-01', 'to jest adres', 'Super Firma', '626525263');
 INSERT INTO `table_homework_companies` (first_name, last_name, address, company_name) VALUES
 ('Michał', 'Michalski', 'to tez jest adres', 'Jeszcze lepsza firma');
 
 