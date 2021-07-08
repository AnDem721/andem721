USE biblioteka;
-- Wyświetlić (kolumny id, login i hasło) wszystkie rekordy z tabeli admin, bibliotekarz i czytelnik.
SELECT id_admin, login, haslo FROM biblioteka.admin UNION SELECT id_bibliotekarz, login, haslo FROM biblioteka.bibliotekarz UNION SELECT id_czytelnik, login, haslo FROM biblioteka.czytelnik;

#2 Liczba książek wydanych na autora
-- Napisać zapytanie, które wyświetli liczbę wydanych książek poszczególnego 
-- autora, np. Michael Feathers, 1; Robert C. Martin 2; itd.
SELECT autor, COUNT(*) FROM biblioteka.ksiazka GROUP BY autor;

#3 Rozwinięcie zadania #2
-- Napisać zapytanie, które wyświetli liczbę wydanych ksiązek poszczególnego 
-- autora, który wydał co najmniej 2 książki
SELECT autor, COUNT(*) as ilosc FROM biblioteka.ksiazka GROUP BY autor HAVING ilosc >= 2;

#4 Różnica pomiędzy datami
-- Napisać zapytanie, które wyświetli liczbę dni do odbioru od zamówienia
SELECT data_zamowienia, data_odbioru, DATEDIFF (data_odbioru, data_zamowienia) as dni FROM biblioteka.zamowienie; 
#5 Różnica pomiędzy datami - cd
-- Napisać zapytanie, które wyświetli liczbę dni od odbioru od teraz... jeżeli 
-- pozycja nie zostałą zwrócona.
SELECT DATEDIFF (NOW(), data_odbioru) as trzymane FROM biblioteka.zamowienie WHERE data_zwrotu is NULL and data_odbioru is not null;
#6 Wyświeltić wszystkie kategorie po przecinku
SELECT group_concat(nazwa) AS kategorie  FROM biblioteka.kategoria;
#7 Wyświetlić wszystkie kategorie po średnika
-- zlicz ile jest książek danej kategorii i wyswietl w formacie nazwa kategorii - ilosc ksiazek tej kategorii
SELECT COUNT(cat.id_kategoria), cat.nazwa 
	FROM ksiazka k, kategoria cat 
		where k.id_kategoria =cat.id_kategoria 
			group by cat.id_kategoria;
-- wyswietl jakie ksiazki wypozyczył czytelnik który ma w imieniu leżące koło siebie litery pi albo na końcu imienia litery yk
select * from zamowienie z inner join (select id_ksiazka, tytul from ksiazka) as k on z.id_ksiazka = k.id_ksiazka
	inner join (select id_czytelnik, imie, nazwisko from czytelnik) as czyt on z.id_czytelnik = czyt.id_czytelnik
		where data_odbioru != 'Null'
			and czyt.imie like '%pi%' or czyt.nazwisko like '%yk';
				
			
	

-- wyswietl ile książek mają czytelnicy z imieniem Piotr i nazwiskiem klimek
--  select (select id_czytelnik from czytelnik where imie = 'Piotr') czytelnik, data_zwrotu, count(*) ilosc_ksiazek from zamowienie 
-- 	where data_zwrotu is null group by czytelnik;
--     
 select id_czytelnik, data_zwrotu, count(*) ilosc_ksiazek from zamowienie 
	where id_czytelnik in (select id_czytelnik from czytelnik where imie = 'Piotr' and nazwisko='KLimek')
		and data_zwrotu is null group by id_czytelnik;

-- wyswietl jakie ksiazki sa nie wypozyczone, posortuj je alfabetycznie po tytule ksiazki a nastepnie po opisie
select id_ksiazka, autor, tytul from ksiazka where id_ksiazka in (select id_ksiazka from zamowienie z where data_odbioru is null or (data_zwrotu-data_odbioru) is not null);

-- wyswietl ile jest wypozyczonych ksiazek
select count(*) from zamowienie z where data_odbioru is not null and data_zwrotu is null
-- wyswietl wypozyczone kategorie ksiazek przy czym wyswietl te ktorych jest wiecej niz 3 posortuj je malejąco
-- wyswietl ludzi którzy wypozyczyli ksiazki z kategorii programowanie, Poradniki, Webmasterstwo oraz maja wypozyczone liczbą różną od 1 ksiązek
-- wyswietl ludzi którzy wypozyczyli ksiazki z kategorii która w nazwie posiada ciąg 'GRAM' oraz nie oddali ksiazek do wypozyczalni oraz odebrali je po 2014-08-03
-- wyswietl unikalnych czytelników którzy zamówili ksiązkę pomiędzy 2014-08-01 oraz katergoria ksiązki to Programowanie a teraźniejszą datą ogranicz ich liczbe do 4

