CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country_code TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

create TABLE devices (
    id INTEGER PRIMARY KEY,
    mac_address text,
    type text,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) 
    REFERENCES users(id)
);