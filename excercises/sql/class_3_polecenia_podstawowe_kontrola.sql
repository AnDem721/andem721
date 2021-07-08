USE kontrola;
-- Podstawowe zapytania
-- 1) Wyświetlenie wszystkich strażników z tym, że zamiast kolumna 'imie' chciałbym żeby była kolumna imie_strażnika
select id, imie as imie_straznika, nazwisko, stopien, data_zatrudnienia, pensja, skladka_na_ubezpieczenie from straznik;

-- 2) Wyświetlić strażników którzy mają pensje (bez uwzględniania składni na ubezpieczenia) większe niż 1500zł
select * from straznik where pensja > 1500;
 
-- 3) Wyświetlić strażników z pensją większą od 1500zł ale mniejszą niż 2500zł
select * from straznik where pensja between 1500 and 2500;

-- 4) Wyświetlić strażników ale bez strażników o nazwisku Nowak i Kowalczyk
select * from straznik where nazwisko != 'Nowak' and nazwisko != 'Koowalczyk';
 
-- 5) Wyświetlić strażników ale bez strażników o id 1,6,5 (z użyciem IN)
select * from straznik where id not in (1,5,6);

-- 6) Wyświetlić strazników i pensje które są większe od 1500 ale po odjęciu "skladka_na_ubezpieczenie"
select * from straznik where (pensja - skladka_na_ubezpieczenie)>1500;

-- 7) Wyświetlić pasażerów posortowanych po nazwisku i imieniu
select * from pasazer order by nazwisko, imie desc;
 
-- 8) Wyświetlić strażników którzy mają nazwisko rozpoczynające się od "Kowal"
select * from straznik where nazwisko like 'Kowal%';

-- 9) Wyświetlić strażników o nazwisku Nowak i którzy zostali zatrudnieni w tym roku (funkcja year)
select * from straznik where nazwisko = 'Nowak' and year(data_zatrudnienia)=year(now());

-- 10) Wyświetlić nazwisko+pensje strażników pomniejszone skladka_na_ubezpieczenie, kolumna ma się nazywać pensja_do_wyplaty
select nazwisko, (pensja-skladka_na_ubezpieczenie) as pensja_do_wyplaty from straznik; 

-- 11) Wyświetlić wszystkich strażników aktualnych i archiwalnych (kontrola.straznik_archiwum) w jednej tabeli
select * from straznik union select * from straznik_archiwum;

-- 12) Wyświetlić strażnika który nie ma ustawionego pola skladka_na_ubezpieczenie (jest to NULL)
select * from straznik having skladka_na_ubezpieczenie = 'Null'; 
-- Używanie agregatów - Proszę 
-- ---------------------------
-- 1) Napisać zapytania które poda sumę  pensji (pola pensja) dla wszystkich strażników
select sum(pensja) from straznik;
-- 2) Podać średnią pensję strażników 
select avg(pensja) from straznik;
-- 3) Wyświetlić największą pensje
select id from straznik order by pensja;
-- 
-- 4) Podac liczbę  pasażerów w systemie
select count(*) from pasazer;
-- 5) Podać liczbę strażników ale tych którzy mają uzupełnione pole skladka_na_ubezpieczenie
select count(*) from straznik where skladka_na_ubezpieczenie != "null";

-- Zapytania z JOIN
-- -------------------
-- 1) Wyświetlić wszystkie kontrole przeprowadzone na  lotnisku Gdańsk
select * from kontrola k inner join numer_stanowiska ns on k.id_numer_stanowiska = ns.id where ns.nazwa_portu ='Gdańsk';
---
select * from kontrola k where k.id_numer_stanowiska in (select id from numer_stanowiska where nazwa_portu = 'Gdańsk'); -- druga wersja 

-- 2) Wyświetlić wszystkie kontrole przeprowadzone dla lotnisku Gdańsk przez strażnika/ów który ma nazwisko 'Nowak'
select * from kontrola k 
	inner join straznik s on k.id_straznik = s.id
	inner join numer_stanowiska ns on k.id_numer_stanowiska = ns.id
		where s.nazwisko = 'Nowak'
			and ns.nazwa_portu = 'gdańsk';
---
select * from kontrola k 
	where k.id_straznik in (select id from straznik where nazwisko = 'Nowak') 
		and k.id_numer_stanowiska in (select id from numer_stanowiska 
			where nazwa_portu = 'Gdańsk');
-- 3) Wyświetlić strażników i przeprowadzone przez nich kontrole jeśli strażnik nie ma kontroli to wyświetlamy informację o strażniku a w części kontrolu wyświetlamy nulle 
select * from straznik s left join kontrola k on s.id = k.id_straznik;

-- 4) Wyświetlić wszystkie lotniska odwiedzone przez pasażera imie="Jan"  AND nazwisko="Brzechwa"
select distinct(nazwa_portu) from numer_stanowiska ns
	inner join kontrola k on ns.id = k.id_numer_stanowiska
		inner join pasazer as p on p.id = k.id_pasazer
			where p.imie = 'Jan'
				and p.nazwisko = 'Brzechwa';
	
-- PODZAPYTANIA
-- 1) Wyświetlić wszystkie kontrole przeprowadzone dla lotniksa Gdańsk przez strażnika który ma największe zarobki
select * from kontrola as k 
	where k.id_numer_stanowiska in (select id from numer_stanowiska where nazwa_portu='Gdańsk')
		and k.id_straznik in (select pensja from straznik order by pensja desc limit 1);
        
select * from kontrola as k
	inner join straznik s on k.id_straznik=s.id
		where k.id_numer_stanowiska in (select id from numer_stanowiska where nazwa_portu='Gdańsk') order by s.pensja desc limit 1;

-- 2) Wyświetlić z użyciem podzapytania wszystkiich pasażerów skontrolowanych przez strażnika o nazwisku "Nowak"
select * from pasazer p  
	inner join (select * from kontrola k where k.id_straznik in (select id from straznik where nazwisko = 'Nowak')) as kontrole 
		on p.id = kontrole.id_pasazer;
-- 3) Wyświetlić strażników a w ostatniej kolumnie kwotę najwyższej pensji strażnika
select nazwisko, (select max(pensja) from straznik) from straznik; 
	

-- 4) Wyświetlić strażników a w ostatniej kolumnie informację o ile mniej/więcej zarabia dany strażnik od średniej  
select nazwisko, ((select avg(pensja) from straznik)-pensja) as odchylenie from straznik;

-- Zlozone
-- 1) Wyświetlić pasażera który  nigdy nie był kontrolowany. 
select * from pasazer p
	where p.id not in (select id_pasazer from kontrola);
	
-- 2) Znaleźć pasażera który odwiedził największą ilość lotnisk (użyć LIMIT), wyświetlić jaką liczbę lotnisk odwiedzili.
select id_pasazer, count(*) from kontrola group by id_pasazer desc limit 1;
-- 3) Znaleźć 2 strażników którzy skontrolowali największą ilość klientów.
select * from straznik swhere; 
    
-- 4) Znaleźć lotnisko przez które poleciała najmniejsza ilość pasażerów (użyć wszystkich danych).
-- !!!!!!
select ns.nazwa_portu, count(*) as liczba_kontroli from kontrola k
	join numer_stanowiska ns on ns.id=k.id_numer_stanowiska
		where wynik_kontroli=true
			group by ns.nazwa_portu order by liczba_kontroli asc limit 1;
            
-- 5) Znaleźć miesiac (w przeciagu całego okresu)  w którym był największy ruch na wszystkich lotniskach / wybranym lotnisku. Użyć
-- 	date_trunc('month', timestamp '2001-02-16 20:38:40')
select date_format(czas_kontroli, '%Y-%m') as 'date', count(*)
	from kontrola 
		group by date_format(czas_kontroli, '%Y-%m')
        order by count(*) desc limit 2;

-- 6) Wyświetlić  ilość pasażerów w kolejnych latach dla każdego lotniska  (lotnisko sortujemy według nazwy rosnąco a póxniej według roku)
--   Lotnisko ABC   2000   300
--   Lotnisko ABC   2001   400
--   Lotnisko BCD   2000   333
--   Lotnisko CDE   2000   323
--   Lotnisko CDE   2001   332



-- MODYFIKACJA DANYCH
-- 1) Umieścić wiersz z swoimi danymi w tablicy pasażera i dodać kontrole na lotnisku Gdańsk przez strażnika id=1 w dniu dzisiejszym
-- 2) Zmienić nazwisko strażników z 'Nowak' na 'Nowakowski' przy okazji zwiększając im pensje o 10%
-- 3) Skasować wiersz  z swoim wpisem w tablicy pasażer.
-- 4) Skasoważ strażnika który skontrolował największa liczbę pasażerów.
-- 
-- 