### Core Concept
Never store passwords—store hashes. Argon2 is the gold standard (memory-hard, GPU-resistant, configurable difficulty). pwdlib provides `hash_password()` and `verify_password()`. User model has `hashed_password` field (explicit naming), signup endpoint prevents duplicate emails.

### Key Mental Models
- **Hash vs plaintext**: If database leaks, hashes are useless strings requiring expensive cracking
- **Separate models**: `User` (database with hashed_password) vs `UserCreate` (request with password)
- **Never return hashes**: Response includes `id` and `email` only, not password data
- **Enumeration prevention**: Duplicate check with generic error message

### Critical Patterns
- Install: `uv add pwdlib[argon2]`
- Hash creation: `password_hash = PasswordHash((Argon2Hasher(),))`
- Hash/verify: `hash_password(password)` and `verify_password(plain, hashed)`
- User model: `hashed_password: str` field, `email: str = Field(unique=True, index=True)`
- Signup: Check existing email, create user with hashed password, return safe fields only

### AI Collaboration Keys
- Prompt 1: Password strength validation—Pydantic model vs security module tradeoffs
- Prompt 2: Email validation—Pydantic `EmailStr` vs external verification
- Prompt 3: Password reset flow—token generation, expiration, usage

### Common Mistakes
- Storing plaintext passwords (catastrophic security failure)
- Returning hash in response (information leakage)
- Using MD5/SHA for passwords (not password hashing algorithms)
- Naming field `password` instead of `hashed_password` (confusing)

### Connections
- **Builds on**: SQLModel + Neon Setup (Lesson 7)
- **Leads to**: JWT Authentication (Lesson 9)
