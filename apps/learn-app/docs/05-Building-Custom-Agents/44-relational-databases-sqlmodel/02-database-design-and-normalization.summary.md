### Core Concept
Database design starts with entity identification, relationship mapping, and normalization (1NF, 2NF, 3NF) to prevent data anomalies - then strategically denormalize for agent performance.

### Key Mental Models
- Entities are "things" (nouns): Task, Project, Worker
- Attributes describe entities: Ask "does this describe THIS entity?"
- Relationships connect entities: 1:N, N:1, M:N with foreign keys
- Normalization prevents anomalies: Update, insert, delete problems

### Critical Patterns
- 1NF: Atomic values, no repeating groups (JSONB acceptable for simple lists)
- 2NF: Non-key columns depend on ENTIRE primary key
- 3NF: No non-key column depends on another non-key column
- Acceptable denormalization: Audit logs (snapshots), read-heavy counters, JSONB metadata
- Mermaid ERD syntax: `PROJECT ||--o{ TASK : contains`

### AI Collaboration Keys
- Extract entities from business requirements before designing tables
- Apply the 3NF test: "Does this value change when something OTHER than the PK changes?"
- Evaluate denormalization trade-offs based on read/write ratios

### Common Mistakes
- Storing derived data in wrong table (project_name in task)
- Normalizing data that needs historical accuracy (audit logs)
- Creating tables for every possible metadata field instead of using JSONB

### Connections
- **Builds on**: L01 - Why agents need structured data
- **Leads to**: L03 - SQLModel async engine setup
