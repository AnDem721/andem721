#` - gres
#' - apostrof / single quote / uszy  ->  'c' < "ce w uszach"
#" - cudzysłów

# CREATE - tworzenie (tabel/baz danych)
#  -> DATABASE - baza danych
#  -> TABLE    - tabela wewnątrz bazy danych

# IF NOT EXISTS - wykonaj operację po upewnieniu się, że tabela/baza nie istnieje
# USE  			- wybieramy bazę danych na której będziemy dalej pracować

CREATE DATABASE IF NOT EXISTS `codeme_class_1`;
USE `codeme_class_1`;

CREATE TABLE IF NOT EXISTS `class_participant` (
#  nazwa_kolumny    typ_danych		dodatkowe_opcje,
	`id` 			INT 			PRIMARY KEY,
    `first_name`    VARCHAR(60),
    `last_name`     VARCHAR(60),
    `age`     		INT				DEFAULT 0
);

# Czyszczenie tabeli (kompletne wymazanie rekordów)
TRUNCATE `class_participant`;

# Komenda wstaw rekord
INSERT INTO `class_participant` VALUES (1, 'Paweł', 'Recław', 20);
INSERT INTO `class_participant` values (2, 'Natalia', 'Hinca', 21);
INSERT INTO `class_participant` VALUES (3, 'Sławomir', 'Rembiesa', 31);
INSERT INTO `class_participant` VALUES (4, 'Gabriela', 'Siedlanowska', 20);
INSERT INTO `class_participant` VALUES (5, 'Kordian', 'Marczak', 18);
INSERT INTO `class_participant` VALUES (6, 'Paula', 'Halik', 28);
INSERT INTO `class_participant` VALUES (7, 'Andrzej', 'Demboowski', 37);
INSERT INTO `class_participant` VALUES (8, 'Olaf', 'Drozd', 20 );
INSERT INTO `class_participant` VALUES (9, 'Szymon', 'Klause', 35) ;
INSERT INTO `class_participant` VALUES (10, 'Grzegorz', 'Żukowski', 20);
INSERT INTO `class_participant` VALUES (11, 'Krzysztof', 'Lis', 27);
INSERT INTO `class_participant` VALUES (12, 'Jakub', 'Podolski', NULL);
INSERT INTO `class_participant` VALUES (13, 'Daria', 'Mędrek', 23);
INSERT INTO `class_participant` VALUES (14, 'Grazyna', 'Papaj', 35);
INSERT INTO `class_participant` VALUES (15, 'Ola', 'Dziuba',28);
INSERT INTO `class_participant` values (16, 'Ula', 'Baranowska', '26');

# Jeżeli kolumna nie może przyjąć wartości NULL, to zostanie tam wstawiona domyślna wartość lub 
#	jeśli domyślna wartość nie została zdefiniowana, to otrzymamy błąd.
# Jeśli nie zdefiniujemy domyślnej wartości, ale nie zabronimy wartości NULL, to domyślną wartością 
# 	będzie wartość NULL
INSERT INTO `class_participant`(`id`, `first_name`, `last_name`) VALUES (20, 'Niemowlaczek', 'Jacek');

# Alternatywna forma wstawiania [wielu] rekordów.
INSERT INTO `class_participant` VALUES 	(1, 'Paweł', 'Recław', 20), 
										(2, 'Natalia', 'Hinca', 21), 
                                        (3, 'Sławomir', 'Rembiesa', 31), 
                                        (4, 'Gabriela', 'Siedlanowska', 20), 
                                        (5, 'Kordian', 'Marczak', 18), 
                                        (6, 'Paula', 'Halik', 28), 
                                        (7, 'Andrzej', 'Demboowski', 37), 
                                        (8, 'Olaf', 'Drozd', 20 ), 
                                        (9, 'Szymon', 'Klause', 35) , 
                                        (10, 'Grzegorz', 'Żukowski', 20), 
                                        (11, 'Krzysztof', 'Lis', 27), 
                                        (12, 'Jakub', 'Podolski', NULL), 
                                        (13, 'Daria', 'Mędrek', 23), 
                                        (14, 'Grazyna', 'Papaj', 35), 
                                        (15, 'Ola', 'Dziuba', 28), 
                                        (16, 'Ula', 'Baranowska', '26');

