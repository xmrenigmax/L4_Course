CREATE TABLE artist_tbl
(
artist_id VARCHAR2(10),
artist_name VARCHAR2(100),
PRIMARY KEY(artist_id)
);

CREATE TABLE cd_tbl
(
cd_id VARCHAR2(10),
cd_title VARCHAR2(100),
cd_release_date DATE,
PRIMARY KEY(cd_id)
);

CREATE TABLE track_tbl
(
track_id VARCHAR2(10),
track_title VARCHAR2(100),
track_length NUMERIC,
track_release_date DATE,
PRIMARY KEY(track_id)
);

CREATE TABLE song_tbl
(
song_id VARCHAR2(10),
song_title VARCHAR2(100),
PRIMARY KEY(song_id)
);

CREATE TABLE musician_tbl
(
musician_id VARCHAR2(10),
musician_name VARCHAR2(100),
PRIMARY KEY(musician_id)
);

CREATE TABLE genre_tbl
(
genre_id VARCHAR2(10),
genre_name VARCHAR2(100),
genre_description VARCHAR(500),
PRIMARY KEY(genre_id)
);

CREATE TABLE artist_track_lnk
(
fk_artist_id VARCHAR2(10),
fk_track_id VARCHAR2(10),
PRIMARY KEY (fk_artist_id, fk_track_id),
FOREIGN KEY (fk_artist_id) REFERENCES artist_tbl(artist_id),
FOREIGN KEY (fk_track_id) REFERENCES track_tbl(track_id)
);

CREATE TABLE cd_track_lnk
(
fk_cd_id VARCHAR2(10),
fk_track_id VARCHAR2(10),
PRIMARY KEY (fk_cd_id, fk_track_id),
FOREIGN KEY (fk_cd_id) REFERENCES cd_tbl(cd_id),
FOREIGN KEY (fk_track_id) REFERENCES track_tbl(track_id)
);

CREATE TABLE genre_track_lnk
(
fk_genre_id VARCHAR2(10),
fk_track_id VARCHAR2(10),
PRIMARY KEY (fk_track_id, fk_genre_id),
FOREIGN KEY (fk_genre_id) REFERENCES genre_tbl(genre_id),
FOREIGN KEY (fk_track_id) REFERENCES track_tbl(track_id)
);

CREATE TABLE song_track_lnk
(
fk_song_id VARCHAR2(10),
fk_track_id VARCHAR2(10),
PRIMARY KEY (fk_song_id, fk_track_id),
FOREIGN KEY (fk_song_id) REFERENCES song_tbl(song_id),
FOREIGN KEY (fk_track_id) REFERENCES track_tbl(track_id)
);

CREATE TABLE musician_track_lnk
(
fk_musician_id VARCHAR2(10),
fk_track_id VARCHAR2(10),
PRIMARY KEY (fk_musician_id, fk_track_id),
FOREIGN KEY (fk_musician_id) REFERENCES musician_tbl(musician_id),
FOREIGN KEY (fk_track_id) REFERENCES track_tbl(track_id)
);

CREATE TABLE musician_artist_lnk
(
fk_musician_id VARCHAR2(10),
fk_artist_id VARCHAR2(10),
musician_joined DATE, 			
musician_left DATE,
PRIMARY KEY (fk_musician_id,fk_artist_id,musician_joined),
FOREIGN KEY (fk_musician_id) REFERENCES musician_tbl(musician_id),
FOREIGN KEY (fk_artist_id) REFERENCES artist_tbl(artist_id)
);

CREATE TABLE musician_song_lnk
(
fk_musician_id VARCHAR2(10),
fk_song_id VARCHAR2(10),
PRIMARY KEY (fk_musician_id, fk_song_id),
FOREIGN KEY (fk_musician_id) REFERENCES musician_tbl(musician_id),
FOREIGN KEY (fk_song_id) REFERENCES song_tbl(song_id)
);

commit;

-- cleanup




