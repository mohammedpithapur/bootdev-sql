CREATE TABLE banks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  routing_number INTEGER,
  is_admin BOOLEAN
);

CREATE table users_banks(
    user_id INTEGER,
    bank_id INTEGER,
    UNIQUE (user_id, bank_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (bank_id) REFERENCES banks(id),
)