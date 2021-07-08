USE `codeme_homework`;
DROP TABLE IF EXISTS `table_homework_2_students`;
CREATE TABLE IF NOT EXISTS `table_homework_2_students` (
`id_user` INT AUTO_INCREMENT PRIMARY KEY,
`pesel`  VARCHAR(11) not null CHECK (CHAR_LENGth(`pesel`) = 11),
`grades_avarage` FLOAT NOT NULL DEFAULT '0.0'); 

