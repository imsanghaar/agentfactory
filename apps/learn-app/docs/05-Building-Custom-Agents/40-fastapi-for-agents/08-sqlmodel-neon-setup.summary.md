### Core Concept
SQLModel = Pydantic + SQLAlchemy in one—models work for both validation AND database. Neon = PostgreSQL as a service (free tier, instant setup). `table=True` makes model a database table. Session manages database operations with add/commit/refresh pattern.

### Key Mental Models
- **Dual-purpose models**: Same class validates API input AND maps to database table
- **Fast track approach**: `create_all()` creates tables—no migrations for learning phase
- **Session context**: `with Session(engine)` provides transactional scope, auto-closes
- **Dependency injection**: `session: Session = Depends(get_session)` for each request

### Critical Patterns
- Table model: `class Task(SQLModel, table=True):` with `Field(primary_key=True)`
- Engine creation: `create_engine(settings.database_url, echo=True)` for logging
- CRUD pattern: `session.add(task)`, `session.commit()`, `session.refresh(task)`
- Query: `session.exec(select(Task)).all()` for list, `session.get(Task, id)` for single
- Neon SSL: `?sslmode=require` in connection string

### AI Collaboration Keys
- Prompt 1: Filtering queries—`select(Task).where(Task.status == "pending")`
- Prompt 2: Separate request/response models—TaskCreate vs TaskRead vs Task
- Prompt 3: Connection pooling—SQLAlchemy built-in pooling behavior

### Common Mistakes
- Forgetting `table=True` (just a Pydantic model, no table created)
- Missing primary key (table creation fails)
- Not calling `session.commit()` (changes not saved, ID still None)
- Wrong connection string (missing `?sslmode=require` for Neon)

### Connections
- **Builds on**: Environment Variables (Lesson 6)
- **Leads to**: User Management & Password Hashing (Lesson 8)
