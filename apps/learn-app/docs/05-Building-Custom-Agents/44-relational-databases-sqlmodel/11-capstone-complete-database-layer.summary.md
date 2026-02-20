### Core Concept
Integrate all database patterns (engine, sessions, models, CRUD, relationships, transactions, migrations) into a production-ready Task API database layer that your `relational-db-agent` skill can generate.

### Key Mental Models
- Database layer is the foundation: All agent persistence flows through it
- Pattern integration: Each component connects to others
- Skill validation: Can your skill generate complete, correct code?
- Multi-tenancy for SaaS: Row-level (tenant_id), schema-per-tenant, or database-per-tenant

### Critical Patterns
- Project structure: database.py, models/, services/, routers/, alembic/
- Worker model: Multiple relationships to Task (assigned_tasks, created_tasks)
- Task model: Self-referential (parent/subtasks), multiple FKs to Worker
- Service layer: CRUD with selectinload, transactions, IntegrityError handling
- Multi-tenancy: `tenant_id` on every table, filter in every query

### AI Collaboration Keys
- Generate complete Task model with all relationships and JSONB
- Generate TaskService with transactions and eager loading
- Review implementation for missing awaits, N+1, transaction safety

### Common Mistakes
- Missing checklist items: pool_pre_ping, expire_on_commit, unique().all()
- Multi-tenancy gaps: Queries without tenant_id filter leak data
- Testing only with small data: Profile with realistic volumes
- Skipping Alembic model imports: Migrations won't detect new tables

### Connections
- **Builds on**: All previous lessons (L00-L10)
- **Leads to**: Chapter 45 - Agent Memory Systems
