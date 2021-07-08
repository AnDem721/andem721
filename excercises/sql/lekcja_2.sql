
-- 1. zwracany jedna kolumne (tytul) z tabeli ksiazka.
SELECT tytul FROM CODE20_template.ksiazka;
-- 2. zwracamy dwie kolumny (tytul, autor_imie), z tabeli ksiazka
SELECT tytul, autor_imie FROM CODE20_template.ksiazka;
-- 3. zwracamy trzy kolumny (tytul, autor_imie, autor_nazwisko)  
-- z tabeli ksiazka. Wypisz tylko wiersze w ktorych min_wiek byl 
-- wiekszy od 12
SELECT tytul, autor_imie, autor_nazwisko, min_wiek  FROM CODE20_template.ksiazka WHERE min_wiek>2 ORDER BY min_wiek ASC; -- sortowanie 
SELECT * FROM ksiazka, recenzja WHERE ksiazka.ksiazka_id=recenzja.ksiazka_id;
SELECT * FROM ksiazka K, recenzja R WHERE K.ksiazka_id=R.ksiazka_id;

-- 5. Chcemy wyswietlic polecajacego i osobę która została zwerbowana 
SELECT * FROM klient K, klient P WHERE K.klient_id = P.id_polecony_przez;

SELECT imie, nazwisko FROM CODE20_template.klient UNION SELECT imie, nazwisko FROM CODE20_template.klient_archiwalny;  -- łączenie dwócj tabael, ilosc kolumn musi bc jednakowa, dane moga byc roznych typow 
SELECT imie, nazwisko FROM klient EXCEPT SELECT imie, nazwisko FROM klient_archiwalny;

SELECT DISTINCT autor_imie 	FROM ksiazka; -- wyswiatla bez duplikatów 





