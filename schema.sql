-- CashPal Database Schema (matches boot.dev column names exactly)

CREATE TABLE IF NOT EXISTS users (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL,
    age          INTEGER,
    country_code TEXT    DEFAULT 'US',
    balance      REAL    DEFAULT 0.0,
    is_admin     INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id   INTEGER NOT NULL,
    receiver_id INTEGER NOT NULL,
    amount      REAL    NOT NULL,
    note        TEXT,
    FOREIGN KEY(sender_id)   REFERENCES users(id),
    FOREIGN KEY(receiver_id) REFERENCES users(id)
);

-- Seed data
INSERT INTO users (name, age, country_code, balance, is_admin) VALUES
    ('Alice',   30, 'US', 1000.00, 1),
    ('Bob',     25, 'US',  500.00, 0),
    ('Charlie', 35, 'UK',  750.00, 0),
    ('Diana',   28, 'IN',  200.00, 0),
    ('Eve',     22, 'US', 1500.00, 0);

INSERT INTO transactions (sender_id, receiver_id, amount, note) VALUES
    (1, 2,  50.00, 'lunch'),
    (3, 1, 100.00, 'rent share'),
    (2, 3,  25.00, 'coffee'),
    (5, 4, 300.00, 'freelance payment'),
    (1, 5,  75.00, 'birthday gift');
