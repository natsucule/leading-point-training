# Task — Investigate Failed Orders

## Objective
You are given:

1. A Linux server folder containing logs
2. A PostgreSQL database containing users and orders

Your goal is to investigate failed orders and generate a summary report.

---

# Part 1 — Linux Task

You have a log file located at:

```bash
/var/log/salespoint/app.log
```

Sample log lines:

```text
2026-05-12 09:10:11 INFO Order created order_id=1001 user_id=42
2026-05-12 09:10:15 ERROR Payment failed order_id=1001
2026-05-12 09:11:01 INFO Order created order_id=1002 user_id=55
2026-05-12 09:11:05 ERROR Timeout while contacting payment gateway order_id=1002
2026-05-12 09:12:10 INFO Order created order_id=1003 user_id=42
```

## Requirements

Using Linux commands only:

1. Extract all ERROR lines into:
```bash
errors.log
```

2. Count total ERROR lines

3. Find all unique `order_id` values that had errors

4. Save the unique failed order IDs into:
```bash
failed_orders.txt
```

---

# Part 2 — SQL Task

## Database Setup

Run the following SQL script:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_orders_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
);

INSERT INTO users (id, name)
VALUES
    (42, 'Ahmad'),
    (55, 'Sarah');

INSERT INTO orders (id, user_id, amount, status)
VALUES
    (1001, 42, 50.00, 'failed'),
    (1002, 55, 120.00, 'failed'),
    (1003, 42, 75.00, 'success');
```

---

# SQL Requirements

Write SQL queries for:

## 1. Show all failed orders

Expected columns:
- order_id
- user_name
- amount

---

## 2. Count failed orders per user

Expected output:
| user_name | failed_orders |

---

## 3. Find total failed amount per user

Expected output:
| user_name | total_failed_amount |

---

# Bonus Task

Combine both Linux + SQL:

- Extract failed order IDs from logs
- Query only those orders from the database

---

# Deliverables

Submit:

- Linux commands used
- SQL queries
- Screenshots/output
- Git repository link

---

# Evaluation Criteria

You will be evaluated on:

- Linux command usage
- SQL query correctness
- Problem-solving approach
- Clean organization
- Ability to explain your solution
