-- 6. Wypisz książki o rodzaju "Bajki"
SELECT tytul FROM ksiazka WHERE rodzaj='Bajki';
-- 7. Wypisz książki o rodzaju "Bajki" autora "Brzechwa"
SELECT tytul FROM ksiazka WHERE rodzaj='Bajki' AND autor_nazwisko='Brzechwa';
-- 8. Wypisz klientów o nazwisku rozpoczynającym się na literę "K"
SELECT * FROM klient WHERE nazwisko LIKE 'K%';
-- 9. Wypisz klientów o nazwisku kończącym się na literą "a"
SELECT * FROM klient WHERE nazwisko LIKE '%a';
-- 8. Wypisz klientów o nazwisku rozpoczynającym się na literą "S" którzy urodzili się po 1960 roku.
SELECT * FROM klient WHERE nazwisko LIKE 'S%' AND rok_urodzenia > 1960;
-- 11. Znaleźć wszystkie książki których autor miał na imie 'Władysław'
SELECT * FROM ksiazka WHERE autor_imie='Władysław';
-- 12. Znaleźć książki gdzie imie autora zaczyna się od J
SELECT * FROM ksiazka WHERE autor_imie LIKE'J%';
-- 13. Wyświetlić wszystkie ksiazki gdzie typy inne niż 'Bajki'
SELECT * FROM ksiazka WHERE rodzaj !='Bajki';
-- 14. Wyświetlić książki posortowane według min_wiek od największej do najmniejszej
SELECT * FROM ksiazka ORDER BY min_wiek ASC;
-- 15. Wyswietlić w jednej tabeli imiona uzytkownikow i imiona autorow ksiazek 