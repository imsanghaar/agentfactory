# Fast Clone Guide

This repository contains a large history (~420MB when cloned fully). Use one of these methods for faster clones:

## Option 1: Shallow Clone (Fastest - Recommended)

```bash
git clone --depth 1 https://github.com/panaversity/agentfactory.git
```

**Pros:**
- Smallest download (~50MB)
- Fast clone (~30 seconds)
- Good for: CI/CD, one-time builds

**Cons:**
- Only gets latest commit
- Can't access full history

---

## Option 2: Partial Clone with Sparse Checkout (Recommended for Development)

```bash
git clone --filter=blob:none --sparse https://github.com/panaversity/agentfactory.git
cd agentfactory
git sparse-checkout init --cone
git sparse-checkout set apps/learn-app docs apps/sso
```

**Pros:**
- Download only what you need (~100-150MB)
- Can still access full commit history
- Can expand to other directories later

**Cons:**
- Slightly more setup

**Expand later:**
```bash
git sparse-checkout add libs
```

---

## Option 3: Full Clone (Not Recommended)

```bash
git clone https://github.com/panaversity/agentfactory.git
```

**Download size:** 420MB+
**Time:** 5-10 minutes

---

## CI/CD Configuration

All GitHub Actions workflows now use `filter: blob:none` for fast clones (~50MB instead of 420MB).

If you have custom CI, add to your checkout step:

```yaml
- uses: actions/checkout@v4
  with:
    filter: blob:none
```

---

## Why So Large?

The repository contains ~400MB of presentation slides (PDFs) in its git history. These methods exclude or minimize downloading them.
