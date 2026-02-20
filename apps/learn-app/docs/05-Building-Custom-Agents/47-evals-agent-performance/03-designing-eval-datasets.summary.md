### Core Concept
10-20 thoughtful test cases beat 1000 random ones because the purpose of evaluation is improvement, not scoring. Twenty cases that reveal WHY things fail enable faster improvement than a thousand cases that only report WHAT percentage passes.

### Key Mental Models
- Quality over quantity: Andrew Ng's directive to start with 10-20 cases
- Three-category framework: Typical (10), Edge (5), Error (5) with different pass rate expectations
- Real data over synthetic: Production logs, support tickets, and user feedback capture how users actually behave
- Dataset growth: Add cases when production failures reveal gaps, not based on arbitrary coverage targets

### Critical Patterns
- Typical cases (90%+ expected pass rate): Common use cases representing 80% of real usage
- Edge cases (70-80% acceptable pass rate): Unusual but valid, tests judgment calls
- Error cases (should fail gracefully): Requests outside capabilities, malformed inputs, impossible requests
- Eval case structure: `id`, `category`, `input`, `expected_behavior`, `rationale`
- The rationale field is essential - captures why each case exists and what it tests

### AI Collaboration Keys
- Use AI to extract eval cases from user feedback and complaints
- Generate edge case variants from typical cases systematically
- Have AI audit your dataset for balance, coverage, diversity, and real vs synthetic mix

### Common Mistakes
- All synthetic data (misses real user messiness - typos, abbreviations, assumed context)
- Only happy path cases (tells nothing about robustness)
- No rationale field (cases become mysterious artifacts that cannot be maintained)
- Waiting for "complete" coverage (paralysis - start with 20, grow organically)

### Connections
- **Builds on**: Lesson 02 (Understanding which quadrant needs ground truth)
- **Leads to**: Lesson 04 (Building Graders with Binary Criteria)
