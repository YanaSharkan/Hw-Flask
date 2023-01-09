DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  `length` INTEGER NOT NULL
);

INSERT INTO tracks(title, artist, genre, `length`)
VALUES
     ('Yellow', 'Coldplay', 'rock', 269),
     ('A sky full of stars', 'Coldplay', 'rock', 270),
     ('Hymn of the weekend', 'Coldplay', 'rock', 259),
     ('Not afraid', 'Eminem', 'rap', 247),
     ('Without me', 'Eminem', 'rap', 290),
     ('Snow on the beach', 'Taylor Swift', 'pop', 256),
     ('Who Says', 'Selena Gomez', 'pop', 196);
