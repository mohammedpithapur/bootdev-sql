# boot.dev SQL – CRUD Chapter (Local Setup)

All 21 lessons from the boot.dev CRUD chapter, with a local test runner
that gives you pass/fail feedback just like boot.dev does.

---

## Folder structure

```
bootdev-sql/
├── schema.sql          ← CashPal DB (reloaded fresh for every test)
├── test_runner.py      ← Test runner — don't edit this
├── README.md
└── crud/
    ├── 01_what_is_crud.sql
    ├── 02_insert_record.sql
    ├── 03_http_crud_lifecycle.sql
    ├── 04_manual_entry.sql
    ├── 05_count.sql
    ├── 06_select_where.sql
    ├── 07_select_multiple_where.sql
    ├── 08_update_record.sql
    ├── 09_update_multiple_fields.sql
    ├── 10_delete_record.sql
    ├── 11_delete_multiple.sql
    ├── 12_select_distinct.sql
    ├── 13_select_count_where.sql
    ├── 14_insert_no_id.sql
    ├── 15_sql_injection_safe.sql
    ├── 16_update_with_expression.sql
    ├── 17_select_limit.sql
    ├── 18_select_order_by.sql
    ├── 19_select_order_limit.sql
    ├── 20_update_where_comparison.sql
    └── 21_delete_where_comparison.sql
```

---

## Running tests

```bash
python3 test_runner.py           # all 21 lessons
python3 test_runner.py 05        # just lesson 05
python3 test_runner.py 10 15     # lessons 10 through 15
```

Output per lesson:
- **SKIP** — file is still empty, write your SQL and re-run
- **PASS** — correct! shows the result table
- **FAIL** — wrong, shows Expected vs Got so you can debug

Each test runs on a **fresh copy** of the database, so UPDATE/DELETE
exercises don't affect each other.

---

## The CashPal schema

### users
| id | name    | age | country_code | balance | is_admin |
|----|---------|-----|--------------|---------|----------|
| 1  | Alice   | 30  | US           | 1000.0  | 1        |
| 2  | Bob     | 25  | US           |  500.0  | 0        |
| 3  | Charlie | 35  | UK           |  750.0  | 0        |
| 4  | Diana   | 28  | IN           |  200.0  | 0        |
| 5  | Eve     | 22  | US           | 1500.0  | 0        |

### transactions
| id | sender_id | receiver_id | amount | note              |
|----|-----------|-------------|--------|-------------------|
| 1  | 1         | 2           |  50.00 | lunch             |
| 2  | 3         | 1           | 100.00 | rent share        |
| 3  | 2         | 3           |  25.00 | coffee            |
| 4  | 5         | 4           | 300.00 | freelance payment |
| 5  | 1         | 5           |  75.00 | birthday gift     |

---

## Quick SQL reference card

```sql
-- INSERT
INSERT INTO users (name, age, country_code, balance)
VALUES ('Frank', 29, 'US', 300.00);

-- SELECT
SELECT * FROM users;
SELECT name, balance FROM users;
SELECT count(*) FROM users;
SELECT DISTINCT country_code FROM users;

-- WHERE
SELECT * FROM users WHERE country_code = 'US';
SELECT * FROM users WHERE balance > 500 AND age < 30;

-- ORDER BY + LIMIT
SELECT name, balance FROM users ORDER BY balance DESC;
SELECT name, balance FROM users ORDER BY balance DESC LIMIT 3;

-- UPDATE  ← ALWAYS use WHERE or you'll update every row!
UPDATE users SET balance = 999.99 WHERE name = 'Bob';
UPDATE users SET balance = 999.99, country_code = 'UK' WHERE name = 'Bob';
UPDATE users SET balance = balance * 1.10;   -- expression

-- DELETE  ← ALWAYS use WHERE or you'll delete every row!
DELETE FROM users WHERE name = 'Diana';
DELETE FROM transactions WHERE amount < 30;
```

---

## No installs needed

Uses Python's built-in `sqlite3` module. Just Python 3 required.
