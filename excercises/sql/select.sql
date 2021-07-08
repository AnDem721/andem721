SELECT imie, nazwisko FROM klient;
SELECT * FROM klient;
SELECT * FROM klient WHERE nazwisko='kowalski';   -- case not sensitive
SELECT * FROM Klient WHERE nazwisko;
SELECT * FROM klient WHERE nazwisko<>'kowalski'; -- wszystko co nie jest kowalksim "NOT"
SELECT * FROM klient WHERE nazwisko='Kowalski' OR nazwisko="szymański"; -- jedno lub drugie 
SELECT * FROM klient WHERE nazwisko LIKE 'Kowal%' -- zaczyna sie od kowa i dalej cokolwiek (REGEXY)

