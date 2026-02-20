### Core Concept
SQLModel tables require `table=True`, combine Pydantic validation with SQLAlchemy ORM, and use `sa_column=Column(JSONB)` for PostgreSQL-specific types like JSONB.

### Key Mental Models
- `table=True` creates database table; without it, just a Pydantic model
- `id: int | None` is optional because database assigns on insert
- Field constraints validate before database: `max_length`, `ge`, `le`
- Indexes speed reads, slow writes: Add to frequently-queried columns

### Critical Patterns
- JSONB columns: `Field(default_factory=list, sa_column=Column(JSONB, nullable=False, server_default="[]"))`
- Foreign keys: `Field(foreign_key="project.id", index=True)`
- Timestamps: `Field(default_factory=datetime.utcnow)`
- Composite indexes: `__table_args__ = (Index("ix_name", "col1", "col2"),)`
- GIN indexes for JSONB: `postgresql_using="gin"`

### AI Collaboration Keys
- Design models from business requirements (fields, constraints, indexes)
- Add JSONB for flexible metadata without over-normalizing
- Implement Pydantic validation for data integrity before insertion

### Common Mistakes
- Forgetting `table=True` (model won't create database table)
- Using Python list/dict without `sa_column=Column(JSONB)` for PostgreSQL
- Missing `index=True` on foreign keys (slow JOINs)
- Not using `default_factory` for mutable defaults (datetime, list, dict)

### Connections
- **Builds on**: L03 - SQLModel async engine setup
- **Leads to**: L05 - Async session management
