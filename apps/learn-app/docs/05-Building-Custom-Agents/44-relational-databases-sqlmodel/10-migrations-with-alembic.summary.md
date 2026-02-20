### Core Concept
Initialize Alembic with `-t async` for async migrations, import ALL models in env.py for autogenerate detection, and always backup before running migrations in production.

### Key Mental Models
- Migrations are versioned schema scripts: Apply/rollback changes safely
- Model imports are CRITICAL: Alembic only sees imported models in metadata
- Autogenerate compares: SQLModel.metadata vs current database schema
- Backup before migrate: Untested backup is not a backup

### Critical Patterns
- Initialize: `alembic init -t async alembic`
- env.py: Import all models, set `target_metadata = SQLModel.metadata`
- Generate: `alembic revision --autogenerate -m "Add tasks table"`
- Apply: `alembic upgrade head`
- Data migration: Add column nullable, update rows, alter to non-nullable
- Backup: `pg_dump -F c -f backup.dump` before any migration

### AI Collaboration Keys
- Walk through new table workflow: imports, generate, review, apply
- Design safe column renames that preserve data and support rollback
- Plan production deployment: backup, test on copy, migrate, verify

### Common Mistakes
- Forgetting to import models in env.py (autogenerate misses changes)
- Not setting `target_metadata = SQLModel.metadata`
- Running migrations without backup (data loss on failure)
- Missing `PYTHONPATH=.` causing import errors

### Connections
- **Builds on**: L09 - Transactions and error handling
- **Leads to**: L11 - Capstone: Complete database layer
