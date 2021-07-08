use mydb;
INSERT INTO `status_konta`
(`idstatus_konta`,`status`) VALUES (null, 'AKTYWNE'), (NULL, 'NIEAKTYWNE'), (NULL, 'ZABLOKOWANE');

INSERT INTO `status_wpisu` (`idstatus_wpisu`,`status`) VALUES (NULL, 'ORYGINALNY'), (NULL, 'EDYTOWANY');

INSERT INTO `typ_konta` (`idtyp_konta`,`typ`) VALUES (NULL,'PUBLICZNE'), (NULL,'PRYWATNE');

INSERT INTO `typ_wpisu` (`idtyp_wpisu`,`typ_wpisu`) VALUES (NULL,'WPIS'), (NULL,'KOMENTARZ'), (NULL,'UDOSTEPNIONY_WPIS');

INSERT INTO `user`
(`iduser`,`login`,`password`,`nazwa`,`opis`,`data_zalozenia`,`typ_konta_idtyp_konta`,`status_konta_idstatus_konta`)
VALUES
(null,'andem','12345','@andem','To jest mój opis', now(), 1,1),
(null,'TomaszD','duda123','@tod','to jest bardziej rozbudowany opis', now(), 2,1),
(null,'Marcin','marcin123','@marc','to jest bardziej rozbudowany opis', now(), 2,1),
(null,'Anna','&*^@#%#','@ana','to jest opis Anny', now(), 1,1),
(null,'Barbara','barbaraaaa','@brb','brak opisu', now(), 2,3);

-- uzytkownik sledzi innego 
INSERT INTO `microblog`.`śledzenie`
(`idśledzenie`,`data_utworzenia`,`id_obserwujacego`,`id_obserwowanego`)
VALUES
(null,now(),1,3), (null,now(),1,2), (null,now(),2,3), (null,now(),2,1);

