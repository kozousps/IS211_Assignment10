BEGIN TRANSACTION;
CREATE TABLE album(id INT, albumname TEXT PRIMARY KEY,
            artistname TEXT);
CREATE TABLE artist(id INT, artistname TEXT);
CREATE TABLE music(id, INT, album TEXT PRIMARY KEY, song TEXT,
            trackno INT, length INT);
COMMIT;