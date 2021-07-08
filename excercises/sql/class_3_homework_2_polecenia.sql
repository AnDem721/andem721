# Wypisz wszystkie ksiazki.
SELECT * FROM ksiegarnia.books;

# Wypisz wszystkie ksiazki posortowane wedlug tytulu a-z.
SELECT title, author FROM ksiegarnia.books ORDER BY title ASC;

# Wypisz wszystkie ksiazki posortowane wedlug tytulu z-a.
SELECT title, author FROM ksiegarnia.books ORDER BY title DESC;

# Wypisz wszystkie ksiazki posortowane wedlug kategorii i tytulu a-z.
SELECT * FROM ksiegarnia.books ORDER BY category, title  ASC;

# Wypisz wszystkie ksiazki opublikowane po 2012-12-31.
SELECT * FROM ksiegarnia.books WHERE published>2012-12-31;

# Wypisz wszystkie tytuly ksiazek Marcina Lisa.
SELECT title FROM ksiegarnia.books WHERE author = 'Marcin Lis';

# Wypisz wszystkie ksiazki napisane przez autora innego niz Marcin Lis w kategorii bazy danych.
SELECT * FROM ksiegarnia.books WHERE author != 'Marcin Lis' AND category='bazy danych';

# Wypisz wszystkie kategorie, w ktorych jest wiecej niz jedna ksiazka
SELECT category, COUNT(*) AS num FROM ksiegarnia.books group by category HAVING COUNT(*)>1;

# Wypisz tytuly i autorow ksiazek w cenie od 50 do 100 zlotych.
SELECT title, author, price  FROM ksiegarnia.books WHERE  price >=50 AND price <=100;
SELECT title, author, price  FROM ksiegarnia.books WHERE  price between 50 and 100;
# Wypisz wszystkie ksiazki o okreslonej dacie publikacji (nie NULL)
SELECT * FROM ksiegarnia.books WHERE published != 'NULL';

# Wypisz dane o 2, 3 i 4-tej najdrozszej ksiazce.
SELECT * FROM ksiegarnia.books ORDER BY price DESC LIMIT 5 OFFSET 1;

# Wypisz wszystkie tytuly ksiazek zaczynajace sie od tekstu "Angular".
SELECT * FROM ksiegarnia.books WHERE title LIKE 'Angular%';

# Wypisz wszystkie tytuly ksiazek o programowaniu.
SELECT * FROM ksiegarnia.books WHERE category LIKE '%programowanie%';

# Wypisz liczbę ksiazek kazdego autora posortowana wedlug liczby malejaco.
SELECT author, COUNT(*) FROM ksiegarnia.books GROUP BY author 	ORDER BY COUNT(*) DESC;

# Wypisz laczna liczbe stron wszystkich ksiazek o bazach danych.
SELECT SUM(page_count) FROM ksiegarnia.books where category='Bazy danych';
# Wypisz dane o najdrozszej ksiazce.
SELECT * FROM ksiegarnia.books ORDER BY price DESC LIMIT 1;
select * from ksiegarnia.books where price = (select max(price) from ksiegarnia.books);