### Core Concept
JWTs enable stateless authentication: user logs in once, gets signed token, includes it in subsequent requests. Token has three parts (header, payload, signature). Server validates signature to identify user—no session storage needed. OAuth2PasswordBearer integrates with Swagger UI.

### Key Mental Models
- **Signed, not encrypted**: Anyone can read JWT payload, but only server creates valid signatures
- **Stateless auth**: Token contains identity; no server-side session storage
- **Generic error messages**: "Incorrect email or password" prevents enumeration attacks
- **Form data for /token**: OAuth2 expects `username=&password=`, not JSON

### Critical Patterns
- Install: `uv add python-jose[cryptography]`
- Token creation: `jwt.encode({"sub": email, "exp": expire}, secret_key, algorithm)`
- Token decode: `jwt.decode(token, secret_key, algorithms=[algorithm])`
- OAuth2 setup: `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")`
- Protected route: `current_user: User = Depends(get_current_user)`
- Login endpoint: `/token` with `OAuth2PasswordRequestForm = Depends()`

### AI Collaboration Keys
- Prompt 1: Token expiration—refresh tokens and frontend handling
- Prompt 2: Custom claims—roles in JWT, tradeoffs of cached permissions
- Prompt 3: Testing authentication—fixtures for test users and tokens

### Common Mistakes
- Using JSON for /token (OAuth2 expects form data)
- Forgetting WWW-Authenticate header in 401 responses
- Putting sensitive data in tokens (passwords, secrets)
- Hardcoding secret key (must come from environment)

### Connections
- **Builds on**: User Management & Password Hashing (Lesson 8)
- **Leads to**: Dependency Injection (Lesson 10)
