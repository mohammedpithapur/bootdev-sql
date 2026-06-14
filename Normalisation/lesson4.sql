CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

create table countries(
    id INTEGER PRIMARY KEY,
    country_code text,
    name text
);

CREATE TABLE users_countries(
    country_id INTEGER,
    user_id INTEGER,
    UNIQUE (country_id, user_id),
    FOREIGN KEY (country_id) REFERENCES countries(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);