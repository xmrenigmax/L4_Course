
-- Data Creation
CREATE TABLE ARTIST (
    ARTIST_ID INT PRIMARY KEY,
    ARTIST_NAME VARCHAR(50) NOT NULL,
    ARTIST_TYPE VARCHAR(50) CHECK (ARTIST_TYPE IN ('group', 'solo')) NOT NULL
);

CREATE TABLE CD (
    CD_ID INT PRIMARY KEY,
    CD_TITLE VARCHAR(50) NOT NULL,
    CD_RELEASE_DATE DATE NOT NULL,
    FOREIGN KEY (ARTIST_ID) REFERENCES ARTIST(ARTIST_ID)
)

CREATE TABLE TRACK (
    TRACK_ID INT PRIMARY KEY,
    TRACK_TITLE VARCHAR(50) NOT NULL,
    TRACK_DURATION TIME NOT NULL,
    FOREIGN KEY (CD_ID) REFERENCES CD(CD_ID)
)

-- query : 
/* list all artists */
SELECT * FROM ARTIST;

/* List all CDS by artist */
SELECT CD_TITLE FROM CD 
JOIN ARTIST ON CD.ARTIST_ID = ARTIST.ARTIST_ID
WHERE ARTIST.ARTIST_NAME = 'artist_name';

/* list all tracks by artist */
SELECT TRACK_TITLE, TRACK_DURATION FROM TRACK
JOIN CD ON TRACK.CD_ID = CD.CD_ID
JOIN ARTIST ON CD.ARTIST_ID = ARTIST.ARTIST_ID
WHERE ARTIST.ARTIST_NAME = 'artist_name';

/* list all tracks on cd */
SELECT TRACK_TITLE, TRACK_DURATION FROM TRACK
JOIN CD ON TRACK.CD_ID = CD.CD_ID
WHERE CD.CD_TITLE = 'cd_title';

/* List of all CDS in Order of release date */
SELECT CD_TITLE FROM CD
ORDER BY CD_RELEASE_DATE;

/* List of group members in database in alphabetical order */
SELECT ARTIST_NAME FROM ARTIST
WHERE ARTIST_TYPE = 'group'
ORDER BY ARTIST_NAME ASC;