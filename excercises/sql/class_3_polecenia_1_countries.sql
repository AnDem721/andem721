-- 1. Wyświetl strukturę tabeli employees.
select * from Employees;

-- 2. Wyświetl zawartość tabeli employees.
select * from employees;

-- 3. Wyświetl imiona, nazwiska oraz pensje pracowników.
select first_name, last_name, salary from employees;

-- 4. Wyświetl imiona, nazwiska pracowników. Nadaj aliasy „imie”, „nazwisko” odpowiednim kolumnom.
select first_name imie, last_name nazwisko from employees;
-- 5. Popraw błędy w zapytaniach:

select * from departments;
select FIRST_NAME from employees;
select hire_date as 'data zatrudnienia' from employees;
select last_name nazwisko_pracownika from employees;

-- 6. Wyświetl imiona i nazwiska pracowników w jednej kolumnie (konkatenacja).
select concat(first_name,' ', last_name) from employees;
-- 7. Wyświetl alfabetyczną listę pracowników.
select last_name, first_name from employees order by last_name asc;

-- 8. Wyświetl nazwiska pracowników w porządku malejącym.
select last_name, first_name from employees order by last_name desc;

-- 9. Wyświetl nazwiska i pensje pracowników w porządku malejącym wg pensji.
select last_name, salary from employees order by salary desc;

-- 10. Wyświetl imiona, nazwiska i pensje pracowników w porządku rosnącym wg pensji i malejącym wg nazwisk.
select first_name, last_name, salary from employees order by salary asc, last_name desc;

-- 11. Wyświetl listę nazwisk. W wyniku nie mogą pojawić się duplikaty nazwisk.
select distinct(last_name) from employees;

-- 12. Wyświetl dane pracowników o nazwisku King.
select * from employees where last_name = 'King';

-- 13. Wyświetl nazwiska pracowników, którzy zarabiają poniżej 5000.
select last_name from employees where salary <5000;

-- 14. Wyświetl imiona i nazwiska pracowników, których pensja znajduje się w przedziale [2000, 7 000].
select first_name, last_name from employees where salary between 2000 and 7000;

-- 15. Wyświetl bez duplikatów identyfikatory stanowisk z tabeli employees.
select distinct(job_id) from employees;

-- 16. Wyświetl imię, nazwisko oraz datę zatrudnienia wszystkich pracowników, których pensja nie znajduje się w przedziale [5000, 10 000]. 
-- Wyniki posortuj rosnąco wg pensji.
select first_name, last_name, hire_date from employees where salary not between 5000 and 10000;

-- 17. Wyświetl dane osób o identyfikatorach 100, 102, 105 i 107.
select * from employees where employee_id in (100, 102, 105, 107);

-- 18. Wyświetl nazwisko, pensję i premię pracowników, których nazwisko zaczyna się na literę ‘K’.
select last_name, salary, commission_pct from employees having last_name like 'k%';

-- 19. Wyświetl imiona i nazwiska pracowników, w których nazwisku występuje litera ‘i’, ‘a’ lub ‘o’.
select first_name, last_name from employees having last_name like '%i%' or '%a%' or '%o%';

-- 20. Wyświetl imiona i nazwiska pracowników zatrudnionych w oddziale o identyfikatorze 60.
select first_name, last_name from employees where DEPARTMENT_ID = 60;

-- 21. Wyświetl dane pracowników, którzy nie mają premii.
select * from employees where commission_pct is Null;

-- 22. Wyświetl imiona i nazwiska pracowników, których druga litera imienia to a-- 
select first_name, last_name from employees where substr(first_name, 2, 1) = 'a';

-- 23. Wyświetl bez duplikatów identyfikatory oddziałów z tabeli employees.
select distinct(job_id) from employees;

-- 24. Wyświetl imiona, nazwiska i pensje pracowników, którzy powyżej 10000.
select first_name, last_name, salary from employees where salary >10000;

-- 25. Wyświetl imiona, nazwiska i pensje powiększone o 20% pracowników zatrudnionych w oddziale o identyfikatorze 50.
select first_name, last_name, (salary*1.2) from employees where department_id  = 50;

-- 26. Wyświetl dane pracowników zatrudnionych w oddziale o identyfikatorze 100.
select * from employees where department_id = 100;

-- 27. Wyświetl dane oddziałów o identyfikatorze lokalizacji większym od 2000.
select * from departments where LOCATION_ID > 2000;

-- 28. Wyświetl dane lokalizacji znajdujących się w miastach, których nazwy rozpoczynają się na literę ‘S’.
select * from locations having city like 's%';

-- 29. Wyświetl bez duplikatów identyfikatory krajów z tabeli countries.
select distinct(country_id) from countries;
-- 30. Wyświetl nazwy krajów posortowane w porządku rosnącym.
select country_name from countries order by country_name asc; 

-- 31. Wyświetl nazwiska, daty zatrudnienia pracowników, pensje i pensje po podwyżce ( powiększone o 1000) nadaj kolumnom aliasy.
select last_name nazwisko, hire_date data_zatr, (salary+1000) pensja_po_podwyzce from employees;