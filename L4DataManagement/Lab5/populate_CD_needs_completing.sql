

INSERT ALL
    INTO artist_tbl Values ('A1','The Magic Hamsters')
    INTO artist_tbl Values ('A2','Angry Dude')
    INTO artist_tbl VALUES ('A3','Rodent String Quartet')

    INTO musician_tbl VALUES ('M1','Peter Frappocino')
    INTO musician_tbl VALUES ('M2','Regi Something')
    INTO musician_tbl VALUES ('M3','Mike Hat')
    INTO musician_tbl VALUES ('M4','Frank Spencer')

    INTO cd_tbl VALUES ('CD1', "title1", 20-10-2020)
    INTO cd_tbl VALUES ('CD2', "title2", 20-10-2021)
    INTO cd_tbl VALUES ('CD3', "title3", 20-10-2022)
    INTO cd_tbl VALUES ('CD4', "title4", 20-10-2023)

    INTO track_tbl VALUES ('T1', 'track1', 3.45, 20-11-2020, 1)
    INTO track_tbl VALUES ('T2', 'track2', 4.45, 20-12-2020, 1)
    INTO track_tbl VALUES ('T3', 'track3', 5.45, 20-13-2020, 2)
    INTO track_tbl VALUES ('T4', 'track4', 6.45, 20-14-2021, 2)
    INTO track_tbl VALUES ('T5', 'track5', 7.45, 20-15-2021, 1)
    INTO track_tbl VALUES ('T6', 'track6', 8.45, 20-16-2021, 3)
    INTO track_tbl VALUES ('T7', 'track7', 9.45, 20-17-2022, 3)
    INTO track_tbl VALUES ('T8', 'track8', 10.45, 20-18-2022, 4)
    INTO track_tbl VALUES ('T9', 'track9', 11.45, 20-19-2022, 4)
    INTO track_tbl VALUES ('T10', 'track10', 12.45, 20-20-2023, 1)

    INTO song_tbl VALUES ('s1', 'song1', 1)
    INTO song_tbl VALUES ('s2', 'song2', 1)
    INTO song_tbl VALUES ('s3', 'song3', 3)
    INTO song_tbl VALUES ('s4', 'song4', 2)
    INTO song_tbl VALUES ('s5', 'song5', 3)
    INTO song_tbl VALUES ('s6', 'song6', 4)
    INTO song_tbl VALUES ('s7', 'song7', 4)
    INTO song_tbl VALUES ('s8', 'song8', 1)
    INTO song_tbl VALUES ('s9', 'song9', 2)
    INTO song_tbl VALUES ('s10', 'song10', 3)

    INTO genre_tbl VALUES('G1','RNB', 'Rhythm and Blues - soulful')
    INTO genre_tbl VALUES('G2','Indy', 'God knows how to put that in a box')
    INTO genre_tbl VALUES('G3','Classical', 'Some stiff upper lip stuff')

Select * FROM Dual;

-- cleanup
DROP TABLE artist_tbl;
DROP TABLE musician_tbl;
DROP TABLE cd_tbl;
DROP TABLE track_tbl;
DROP TABLE song_tbl;
DROP TABLE genre_tbl;





