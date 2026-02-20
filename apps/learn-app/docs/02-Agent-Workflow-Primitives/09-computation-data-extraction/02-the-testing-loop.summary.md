### Core Concept

Exit code 0 means "didn't crash," not "correct answer." The only way to trust a script's output is to test it with data where you already know the right answer. This is the verification paradox: you built a tool to do work you can't easily check, so you verify with simple data you CAN check.

### Key Mental Models

- **Verification paradox**: You need the script because you can't do the math yourself, but that means you can't verify the output. The trick: test with numbers you CAN add in your head (10 + 20 + 30 = 60).
- **Zero-trust mindset**: Assume everything is broken until proven otherwise. The agent runs code — it doesn't validate business logic. You supply test data with known answers.
- **Exit code ≠ correctness**: A buggy script can silently skip data, produce wrong totals, and still exit with code 0. Logic errors don't crash — they lie.

### Critical Patterns

- Verification prompt: "Verify [tool] works correctly. Create test data with known answer [X] and check that output matches."
- Check exit codes with `echo $?` immediately after the command you care about
- Test multiple cases: integers, decimals, negatives, edge cases — different input types trigger different bugs

### Common Mistakes

- Trusting exit code 0 as proof that a script works correctly — it only proves the script didn't crash
- Testing with only one case — a single test can miss entire classes of bugs (the buggy_sum example only fails on numbers starting with 6-9)
- Running `echo $?` after an intervening command — any command between the one you're testing and `echo $?` overwrites the exit code

### Connections

- **Builds on**: sum.py from Lesson 1
- **Leads to**: Real bank data with CSV quoting traps (Lesson 3) — clean test data behaves, real data cheats
