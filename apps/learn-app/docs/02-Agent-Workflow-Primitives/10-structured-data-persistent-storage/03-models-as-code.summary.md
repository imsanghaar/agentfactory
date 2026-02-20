### Core Concept
SQLAlchemy models define schema contracts in Python -- types, constraints, and relationships that the database enforces automatically.

### Continuity Bridge
From proving persistence (L1) to defining what shape the persisted data must take.

### Key Mental Models
- `Numeric(10, 2)` for money -- float stores 0.1 + 0.2 as 0.30000000000000004.
- Foreign keys make impossible states impossible.
- nullable=False and unique=True encode business assumptions the database enforces.

### Critical Patterns
- User, Category, Expense three-table ER model with FK constraints.
- SQLite FK pragma listener for local development parity with PostgreSQL.
- One canonical runnable model file with explicit imports.

### Common Mistake
Using Float for financial values. Also: skipping nullable/unique constraints and discovering corrupt data weeks later.
