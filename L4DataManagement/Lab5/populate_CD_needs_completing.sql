
-- Now proceed with your INSERT statements
INSERT ALL
    INTO artist_tbl VALUES ('A1','The Magic Hamsters')
    INTO artist_tbl VALUES ('A2','Angry Dude')
    INTO artist_tbl VALUES ('A3','Rodent String Quartet')

    INTO musician_tbl VALUES ('M1','Peter Frappocino')
    INTO musician_tbl VALUES ('M2','Regi Something')
    INTO musician_tbl VALUES ('M3','Mike Hat')
    INTO musician_tbl VALUES ('M4','Frank Spencer')

    INTO cd_tbl VALUES ('C1','title1', TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO cd_tbl VALUES ('C2','title2', TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO cd_tbl VALUES ('C3','title3', TO_DATE('12-12-2010', 'DD-MM-YYYY'))
    INTO cd_tbl VALUES ('C4','title4', TO_DATE('13-12-2010', 'DD-MM-YYYY'))

    INTO track_tbl VALUES ('t1','track1', 1, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t2','track2', 2, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t3','track3', 3, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t4','track4', 4, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t5','track5', 5, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t6','track6', 6, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t7','track7', 7, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t8','track8', 8, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t9','track9', 9, TO_DATE('10-12-2010', 'DD-MM-YYYY'))
    INTO track_tbl VALUES ('t10','track10', 10, TO_DATE('10-12-2010', 'DD-MM-YYYY'))

    INTO song_tbl VALUES ('s1','Stitle1')
    INTO song_tbl VALUES ('s2','Stitle2')
    INTO song_tbl VALUES ('s3','Stitle3')
    INTO song_tbl VALUES ('s4','Stitle4')
    INTO song_tbl VALUES ('s5','Stitle5')
    INTO song_tbl VALUES ('s6','Stitle6')
    INTO song_tbl VALUES ('s7','Stitle7')
    INTO song_tbl VALUES ('s8','Stitle8')
    INTO song_tbl VALUES ('s9','Stitle9')
    INTO song_tbl VALUES ('s10','Stitle10')
    INTO song_tbl VALUES ('s11','Stitle11')
    INTO song_tbl VALUES ('s12','Stitle12')

    INTO genre_tbl VALUES('G1','RNB', 'Rhythm and Blues - soulful')
    INTO genre_tbl VALUES('G2','Indy', 'God knows how to put that in a box')
    INTO genre_tbl VALUES('G3','Classical', 'Some stiff upper lip stuff')
SELECT * FROM dual;

-- insert links
INSERT ALL
    INTO cd_track_lnk VALUES ('C1','t1')
    INTO cd_track_lnk VALUES ('C1','t2')
    INTO cd_track_lnk VALUES ('C1','t3')
    INTO cd_track_lnk VALUES ('C1','t4')
    INTO cd_track_lnk VALUES ('C2','t3')
    INTO cd_track_lnk VALUES ('C2','t2')
    INTO cd_track_lnk VALUES ('C2','t1')

    INTO genre_track_lnk VALUES ('G1','t1')
    INTO genre_track_lnk VALUES ('G2','t2')
    INTO genre_track_lnk VALUES ('G2','t3')
    INTO genre_track_lnk VALUES ('G3','t4')
    INTO genre_track_lnk VALUES ('G3','t3')
    INTO genre_track_lnk VALUES ('G1','t2')
    INTO genre_track_lnk VALUES ('G2','t1')

    INTO song_track_lnk VALUES ('s1','t1')
    INTO song_track_lnk VALUES ('s2','t2')
    INTO song_track_lnk VALUES ('s3','t3')
    INTO song_track_lnk VALUES ('s4','t4')

    INTO musician_track_lnk VALUES ('M1','t1')
    INTO musician_track_lnk VALUES ('M2','t2')
    INTO musician_track_lnk VALUES ('M3','t3')
    INTO musician_track_lnk VALUES ('M4','t4')
    INTO musician_track_lnk VALUES ('M1','t2')
    INTO musician_track_lnk VALUES ('M2','t1')
    INTO musician_track_lnk VALUES ('M3','t1')

    INTO musician_artist_lnk VALUES ('M1','A1', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO musician_artist_lnk VALUES ('M2','A2', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO musician_artist_lnk VALUES ('M3','A3', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO musician_artist_lnk VALUES ('M4','A1', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO musician_artist_lnk VALUES ('M1','A2', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO musician_artist_lnk VALUES ('M2','A3', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))
    INTO musician_artist_lnk VALUES ('M3','A1', TO_DATE('10-12-2010', 'DD-MM-YYYY'), TO_DATE('11-12-2010', 'DD-MM-YYYY'))

    INTO musician_song_lnk VALUES ('M1','s1')
    INTO musician_song_lnk VALUES ('M2','s2')
    INTO musician_song_lnk VALUES ('M3','s3')
    INTO musician_song_lnk VALUES ('M4','s4')
    INTO musician_song_lnk VALUES ('M1','s5')
    INTO musician_song_lnk VALUES ('M2','s6')
    INTO musician_song_lnk VALUES ('M3','s7')
    INTO musician_song_lnk VALUES ('M4','s8')
SELECT * FROM dual;

COMMIT;
-- Delete all existing data from the tables in reverse order of dependencies
DELETE FROM musician_song_lnk;
DELETE FROM musician_artist_lnk;
DELETE FROM musician_track_lnk;
DELETE FROM song_track_lnk;
DELETE FROM genre_track_lnk;
DELETE FROM cd_track_lnk;
DELETE FROM artist_track_lnk;
DELETE FROM genre_tbl;
DELETE FROM musician_tbl;
DELETE FROM song_tbl;
DELETE FROM track_tbl;
DELETE FROM cd_tbl;
DELETE FROM artist_tbl;
COMMIT;



