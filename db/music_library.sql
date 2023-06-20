DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
 

CREATE TABLE albums (
    id SERIAL PRIMARY KEY, 
    title VARCHAR(255),
    genre VARCHAR(255),
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
    album_id INT NOT NULL REFERENCES albums(id)
);
