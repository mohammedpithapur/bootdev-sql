#!/usr/bin/env python3
"""
boot.dev SQL – Local Test Runner (CRUD Chapter, all 21 lessons)
Mimics boot.dev's pass/fail validation locally.

Usage:
  python3 test_runner.py              # run all tests
  python3 test_runner.py 05           # run lesson 05 only
  python3 test_runner.py 10 15        # run lessons 10 through 15
"""

import sqlite3, sys, os

GREEN  = "\033[92m"; RED    = "\033[91m"; YELLOW = "\033[93m"
CYAN   = "\033[96m"; BOLD   = "\033[1m";  RESET  = "\033[0m"

def get_fresh_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path) as f:
        conn.executescript(f.read())
    return conn

def run_sql(conn, sql):
    try:
        cur = conn.execute(sql)
        return [dict(r) for r in cur.fetchall()], None
    except Exception as e:
        return None, str(e)

def run_script(conn, sql):
    """Execute a multi-statement script (INSERT+DELETE etc), return error if any."""
    try:
        conn.executescript(sql)
        return None
    except Exception as e:
        return str(e)

def rows_match(actual, expected):
    if len(actual) != len(expected):
        return False
    return all(a == e for a, e in zip(actual, expected))

def approx_rows_match(actual, expected, tol=0.01):
    """Match rows where REAL values are compared with tolerance."""
    if len(actual) != len(expected):
        return False
    for a, e in zip(actual, expected):
        if set(a.keys()) != set(e.keys()):
            return False
        for k in e:
            av, ev = a[k], e[k]
            if isinstance(ev, float):
                if abs(float(av) - ev) > tol:
                    return False
            else:
                if av != ev:
                    return False
    return True

def print_table(rows):
    if not rows:
        print("  (no rows)"); return
    headers = list(rows[0].keys())
    widths  = {h: max(len(h), max(len(str(r.get(h,""))) for r in rows)) for h in headers}
    sep = "+" + "+".join("-"*(w+2) for w in widths.values()) + "+"
    print("  "+sep)
    print("  | "+" | ".join(h.ljust(widths[h]) for h in headers)+" |")
    print("  "+sep)
    for row in rows:
        print("  | "+" | ".join(str(row.get(h,"")).ljust(widths[h]) for h in headers)+" |")
    print("  "+sep)

# ── TEST DEFINITIONS ──────────────────────────────────────────────────────────
# Each test dict:
#   file        – student's .sql file
#   title       – shown in output
#   verify_sql  – query run AFTER the student's script to check state
#                 (omit if student query itself returns the right rows)
#   expected    – list of dicts the verify_sql must return
#   approx      – True to use float-tolerance comparison

TESTS = [
  {
    "num": "01", "title": "Read all users (SELECT *)",
    "file": "crud/01_what_is_crud.sql",
    "expected": [
      {"id":1,"name":"Alice",  "age":30,"country_code":"US","balance":1000.0,"is_admin":1},
      {"id":2,"name":"Bob",    "age":25,"country_code":"US","balance": 500.0,"is_admin":0},
      {"id":3,"name":"Charlie","age":35,"country_code":"UK","balance": 750.0,"is_admin":0},
      {"id":4,"name":"Diana",  "age":28,"country_code":"IN","balance": 200.0,"is_admin":0},
      {"id":5,"name":"Eve",    "age":22,"country_code":"US","balance":1500.0,"is_admin":0},
    ],
  },
  {
    "num": "02", "title": "INSERT a user (John, age 30, US)",
    "file": "crud/02_insert_record.sql",
    "verify_sql": "SELECT name, age, country_code FROM users WHERE name='John'",
    "expected": [{"name":"John","age":30,"country_code":"US"}],
  },
  {
    "num": "03", "title": "INSERT a transaction (amount=99.99, note='test payment')",
    "file": "crud/03_http_crud_lifecycle.sql",
    "verify_sql": "SELECT amount, note FROM transactions WHERE note='test payment'",
    "expected": [{"amount":99.99,"note":"test payment"}],
    "approx": True,
  },
  {
    "num": "04", "title": "INSERT two users (Grace and Hank)",
    "file": "crud/04_manual_entry.sql",
    "verify_sql": "SELECT name, age FROM users WHERE name IN ('Grace','Hank') ORDER BY name",
    "expected": [{"name":"Grace","age":28},{"name":"Hank","age":35}],
  },
  {
    "num": "05", "title": "COUNT all users",
    "file": "crud/05_count.sql",
    "expected": [{"count(*)":5}],
  },
  {
    "num": "06", "title": "SELECT name & country_code WHERE country_code='US'",
    "file": "crud/06_select_where.sql",
    "expected": [
      {"name":"Alice",  "country_code":"US"},
      {"name":"Bob",    "country_code":"US"},
      {"name":"Eve",    "country_code":"US"},
    ],
  },
  {
    "num": "07", "title": "SELECT name & age WHERE country='US' AND age > 25",
    "file": "crud/07_select_multiple_where.sql",
    "expected": [
      {"name":"Alice","age":30},
    ],
  },
  {
    "num": "08", "title": "UPDATE Alice's balance to 2000.00",
    "file": "crud/08_update_record.sql",
    "verify_sql": "SELECT name, balance FROM users WHERE name='Alice'",
    "expected": [{"name":"Alice","balance":2000.0}],
    "approx": True,
  },
  {
    "num": "09", "title": "UPDATE Bob: balance=999.99, country_code='UK'",
    "file": "crud/09_update_multiple_fields.sql",
    "verify_sql": "SELECT name, balance, country_code FROM users WHERE name='Bob'",
    "expected": [{"name":"Bob","balance":999.99,"country_code":"UK"}],
    "approx": True,
  },
  {
    "num": "10", "title": "DELETE user named Diana",
    "file": "crud/10_delete_record.sql",
    "verify_sql": "SELECT * FROM users WHERE name='Diana'",
    "expected": [],
  },
  {
    "num": "11", "title": "DELETE all transactions with amount < 30",
    "file": "crud/11_delete_multiple.sql",
    "verify_sql": "SELECT * FROM transactions WHERE amount < 30",
    "expected": [],
  },
  {
    "num": "12", "title": "SELECT DISTINCT country_codes",
    "file": "crud/12_select_distinct.sql",
    "expected": [{"country_code":"US"},{"country_code":"UK"},{"country_code":"IN"}],
  },
  {
    "num": "13", "title": "COUNT users with balance > 400",
    "file": "crud/13_select_count_where.sql",
    "expected": [{"count(*)":4}],
  },
  {
    "num": "14", "title": "INSERT user without specifying id (Ivan)",
    "file": "crud/14_insert_no_id.sql",
    "verify_sql": "SELECT name, age, country_code FROM users WHERE name='Ivan'",
    "expected": [{"name":"Ivan","age":22,"country_code":"IN"}],
  },
  {
    "num": "15", "title": "INSERT user with apostrophe in name (O'Brien)",
    "file": "crud/15_sql_injection_safe.sql",
    "verify_sql": "SELECT name, age FROM users WHERE age=40",
    "expected": [{"name":"O'Brien","age":40}],
  },
  {
    "num": "16", "title": "UPDATE all balances by +10% (multiply by 1.10)",
    "file": "crud/16_update_with_expression.sql",
    "verify_sql": "SELECT name, balance FROM users ORDER BY id",
    "expected": [
      {"name":"Alice",   "balance":1100.0},
      {"name":"Bob",     "balance": 550.0},
      {"name":"Charlie", "balance": 825.0},
      {"name":"Diana",   "balance": 220.0},
      {"name":"Eve",     "balance":1650.0},
    ],
    "approx": True,
  },
  {
    "num": "17", "title": "SELECT first 3 users (LIMIT 3)",
    "file": "crud/17_select_limit.sql",
    "expected": [
      {"id":1,"name":"Alice",  "age":30,"country_code":"US","balance":1000.0,"is_admin":1},
      {"id":2,"name":"Bob",    "age":25,"country_code":"US","balance": 500.0,"is_admin":0},
      {"id":3,"name":"Charlie","age":35,"country_code":"UK","balance": 750.0,"is_admin":0},
    ],
  },
  {
    "num": "18", "title": "SELECT name & balance ORDER BY balance DESC",
    "file": "crud/18_select_order_by.sql",
    "expected": [
      {"name":"Eve",    "balance":1500.0},
      {"name":"Alice",  "balance":1000.0},
      {"name":"Charlie","balance": 750.0},
      {"name":"Bob",    "balance": 500.0},
      {"name":"Diana",  "balance": 200.0},
    ],
  },
  {
    "num": "19", "title": "TOP 2 richest users (ORDER BY balance DESC LIMIT 2)",
    "file": "crud/19_select_order_limit.sql",
    "expected": [
      {"name":"Eve",  "balance":1500.0},
      {"name":"Alice","balance":1000.0},
    ],
  },
  {
    "num": "20", "title": "UPDATE is_admin=1 WHERE balance >= 750",
    "file": "crud/20_update_where_comparison.sql",
    "verify_sql": "SELECT name FROM users WHERE is_admin=0 AND balance >= 750",
    "expected": [],  # no such users should remain
  },
  {
    "num": "21", "title": "INSERT broke user then DELETE WHERE balance=0",
    "file": "crud/21_delete_where_comparison.sql",
    "verify_sql": "SELECT * FROM users WHERE balance=0",
    "expected": [],
  },
]


def run_test(test, verbose=True):
    conn = get_fresh_db()
    qfile = os.path.join(os.path.dirname(__file__), test["file"])

    if not os.path.exists(qfile):
        if verbose:
            print(f"  {YELLOW}SKIP{RESET}  [{test['num']}] {test['title']}")
            print(f"         → missing file: {test['file']}\n")
        return None

    with open(qfile) as f:
        student_sql = f.read().strip()

    # strip comment-only lines to detect empty files
    code_lines = [l for l in student_sql.splitlines()
                  if l.strip() and not l.strip().startswith("--")]
    if not code_lines:
        if verbose:
            print(f"  {YELLOW}SKIP{RESET}  [{test['num']}] {test['title']}  (file is empty)\n")
        return None

    # Run student SQL (may be SELECT or multi-statement script)
    err = run_script(conn, student_sql)
    if err:
        if verbose:
            print(f"  {RED}FAIL{RESET}  [{test['num']}] {test['title']}")
            print(f"         {RED}SQL error:{RESET} {err}\n")
        return False

    verify = test.get("verify_sql") or student_sql
    actual, err2 = run_sql(conn, verify)
    if err2:
        if verbose:
            print(f"  {RED}FAIL{RESET}  [{test['num']}] {test['title']}")
            print(f"         {RED}Verify error:{RESET} {err2}\n")
        return False

    expected = test["expected"]
    use_approx = test.get("approx", False)
    ok = approx_rows_match(actual, expected) if use_approx else rows_match(actual, expected)

    if ok:
        if verbose:
            print(f"  {GREEN}PASS{RESET}  [{test['num']}] {test['title']}")
            if actual:
                print_table(actual)
            print()
        return True
    else:
        if verbose:
            print(f"  {RED}FAIL{RESET}  [{test['num']}] {test['title']}")
            print(f"  {CYAN}Expected:{RESET}")
            print_table(expected)
            print(f"  {CYAN}Got:{RESET}")
            print_table(actual)
            print()
        return False


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        tests = [t for t in TESTS if t["num"] == args[0].zfill(2) or t["file"].startswith(f"crud/{args[0]}")]
    elif len(args) == 2:
        start, end = int(args[0]), int(args[1])
        tests = [t for t in TESTS if start <= int(t["num"]) <= end]
    else:
        tests = TESTS

    if not tests:
        print(f"No tests matched. Use a lesson number like: python3 test_runner.py 05")
        sys.exit(1)

    print(f"\n{BOLD}boot.dev SQL – CRUD Chapter ({len(tests)} lessons){RESET}")
    print("=" * 50)

    passed = skipped = failed = 0
    for t in tests:
        r = run_test(t)
        if r is True:   passed  += 1
        elif r is False: failed += 1
        else:            skipped+= 1

    print("=" * 50)
    print(f"{GREEN}{passed} passed{RESET}  {YELLOW}{skipped} skipped{RESET}  {RED}{failed} failed{RESET}\n")
    if skipped:
        print(f"{YELLOW}Tip:{RESET} Write your SQL in the empty files, then re-run.\n")
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
