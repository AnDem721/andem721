
-- 4.1 Select the title of all movies.
select title from Movies;
-- 4.2 Show all the distinct ratings in the database.

select distinct(rating) from Movies having rating is not Null;
-- 4.3  Show all unrated movies.
select title from Movies where Rating is Null;
-- 4.4 Select all movie theaters that are not currently showing a movie.
select Name from MovieTheaters where Movie is not Null;
-- 4.5 Select all data from all movie theaters 
    -- and, additionally, the data from the movie that is being shown in the theater (if one is being shown).
    select * from MovieTheaters mt inner join Movies m on mt.Movie = m.Code; 
-- 4.6 Select all data from all movies and, if that movie is being shown in a theater, show the data from the theater.
select * from Movies m left join (select * from MovieTheaters where Movie is not Null) as p on m.Code = p.Movie;
-- 4.7 Show the titles of movies not currently being shown in any theaters.
select Title from Movies m where m.Code not in (select Movie from MovieTheaters where Movie is not Null);
-- 4.8 Add the unrated movie "One, Two, Three".
INSERT INTO `baza`.`Movies`
(`Code`,
`Title`,
`Rating`)
VALUES
(9,
'One, two, three',
Null);


-- 4.9 Set the rating of all unrated movies to "G".
UPDATE `baza`.`Movies`
SET
Rating = 'G'
WHERE Rating is Null;


-- 4.10 Remove movie theaters projecting movies rated "NC-17".
DELETE FROM `baza`.`MovieTheaters`
WHERE Movie in (select Code from Movies where Rating like 'NC-17');


