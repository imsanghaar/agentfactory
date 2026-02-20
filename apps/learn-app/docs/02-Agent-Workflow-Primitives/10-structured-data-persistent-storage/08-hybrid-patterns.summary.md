### Core Concept
True hybrid verification uses two independent code paths (SQL + raw CSV) to check the same answer. False hybrid reruns the same query twice.

### Continuity Bridge
From reliable cloud connection (L6) to deciding when SQL-only is enough and when independent verification is worth the cost.

### Key Mental Models
- False hybrid: same query twice confirms determinism, not correctness.
- True hybrid: SQL path vs CSV parser = different failure modes.
- Scope parity: both paths must answer the same question over the same data.
- Low-stakes = SQL-only; financial/audit outputs = hybrid + release gate.

### Critical Patterns
- SQL total vs raw CSV recompute with decimal-safe arithmetic.
- Mismatch policy: verified = release, mismatch = block and investigate.
- Independence checklist: data source differs, parsing path differs, scope matches.
- Tolerance threshold explicit for financial data ($0.01).

### Common Mistake
Calling mismatched-scope comparisons "verification" and publishing anyway. Also: running same SQL twice and calling it independent verification.
