# Distractor Generation Strategies

Systematic procedures for generating plausible, educationally valuable distractors for each question type.

**Core Principle:** Every distractor should represent a real misconception or common error that domain practitioners make. Absurd options waste question real estate and damage exam reliability.

---

## Universal Distractor Quality Standards

Before generating any distractor, verify it meets these criteria:

| Criterion             | Standard                                      | Check                                             |
| --------------------- | --------------------------------------------- | ------------------------------------------------- |
| **Plausibility**      | 70-90% correct, fails on 1-2 critical details | Student familiar with domain would consider it    |
| **Functionality**     | Expected selection rate ≥5%                   | Real misconception, not obviously absurd          |
| **Distinctness**      | Each distractor wrong for different reason    | Not repeating same error 3 times                  |
| **Educational Value** | Reveals common misconception or error pattern | Helps learners understand what they misunderstood |
| **Length Parity**     | Within 0.8x-1.2x of mean option word count    | Prevents length bias (the #1 exam failure)        |
| **Specificity Match** | Same detail level as correct answer           | Prevents specificity bias                         |

---

## Question Type 1: Precision Recall (10%)

**Purpose:** Exact values, definitions, facts from source material.

**Challenge:** Distractors must be plausible alternatives without being obviously wrong.

### Distractor Strategies

#### Strategy 1A: Off-by-One / Adjacent Value

Used for: Numbers, rankings, sequences, version numbers

```
Fact from source: "The Digital FTE operates 168 hours weekly (24 × 7)"

Q: According to the document, how many hours per week does a Digital FTE operate?
**A.** 120 hours  [Off-by-1: Removes 2 days (operates 5 days only)]
**B.** 148 hours  [Off-by-1: Removes 20 hours weekly]
**C.** 168 hours  [CORRECT]
**D.** 200 hours  [Off-by-1: Assumes "always fully operational" misconception]

Strategy: All wrong answers in plausible range (120-200), correct is middle

Distractor quality:
- 120: ~8% selection (mistakes it for 5-day work week)
- 148: ~6% selection (calculation error: 24 × 6)
- 200: ~12% selection (assumes 100% utilization)
✓ All functional (≥5%)
```

#### Strategy 1B: Unit Conversion Error

Used for: Measurements, rates, conversions

```
Fact from source: "Agent Framework improves developer productivity by 45% annually"

Q: What is the stated productivity improvement rate?
**A.** 45% annually    [CORRECT]
**B.** 3.75% monthly   [Unit error: correctly divided 45/12 but converted wrong]
**C.** 45% per sprint  [Unit confusion: assumed 2-week sprint]
**D.** 540% annually   [Calculation error: 45 × 12 instead of 45% once]

Strategy: Distractors show common unit conversion mistakes

Distractor quality:
- B: ~9% selection (mathematical approach but wrong conversion)
- C: ~7% selection (reasonable misconception about time units)
- D: ~5% selection (multiplication error pattern)
✓ All functional
```

#### Strategy 1C: Related Fact Confusion

Used for: Definitions with multiple similar options

```
Fact from source: "MCP (Model Context Protocol) enables bidirectional communication
between AI and external systems"

Q: What does MCP primarily enable?
**A.** Authentication between local and cloud services  [Related but different]
**B.** Bidirectional communication between AI and external systems  [CORRECT]
**C.** Model training and fine-tuning workflows  [Related but different - that's SFT]
**D.** Version control for AI model checkpoints  [Related but different]

Strategy: All distractors are real AI concepts, just not what MCP does

Distractor quality:
- A: ~8% selection (real concept, confusion with OAuth/SSO)
- C: ~10% selection (common misconception - MCP vs. training)
- D: ~6% selection (version control is real, but not MCP)
✓ All functional
```

#### Strategy 1D: Fence-Post Error

Used for: Ranges, sequences, boundaries

```
Fact from source: "The assessment scoring scale: A+ (95-100%), A (90-94.99%), B+ (85-89.99%)"

Q: What is the score range for an "A" grade on the certification exam?
**A.** 90-95%     [Fence-post error: excludes 94.99%]
**B.** 90-94%     [Fence-post error: excludes 94.99%]
**C.** 90-94.99%  [CORRECT]
**D.** 90-100%    [Fence-post error: includes A+]

Strategy: Common boundary inclusion/exclusion errors

Distractor quality:
- A: ~7% selection (off-by-one in upper bound)
- B: ~12% selection (rounding mistake)
- D: ~8% selection (merges two adjacent grades)
✓ All functional
```

---

## Question Type 2: Conceptual Distinction (15%)

**Purpose:** Test understanding of differences between related concepts.

**Challenge:** Distractors must show plausible confusion, not just be wrong.

### Distractor Strategies

#### Strategy 2A: Surface-Level Difference (Incomplete)

Used for: Concepts with clear but incomplete distinctions

```
Concept pair: Synchronous vs. Asynchronous communication

Q: Which BEST differentiates synchronous from asynchronous communication?
**A.** Synchronous is faster; asynchronous is slower
   [Surface-level: Speed varies with conditions, not inherent]
**B.** Synchronous requires sender to wait; asynchronous doesn't
   [CORRECT: Blocking behavior is the core distinction]
**C.** Synchronous uses TCP; asynchronous uses UDP
   [Tangential: Protocol choice is independent of sync model]
**D.** Synchronous is more reliable; asynchronous loses messages
   [Partially true but orthogonal to the distinction]

Strategy: A identifies real difference (speed) but not THE distinguishing feature
         C mixes protocol with synchrony model
         D addresses reliability (not the defining distinction)

Distractor quality:
- A: ~15% selection (intuitive but not precise)
- C: ~8% selection (confuses transport layer with timing)
- D: ~7% selection (correctness ≠ distinctiveness)
✓ All functional
```

#### Strategy 2B: Reverse Confusion

Used for: Concepts often confused in opposite direction

```
Concept pair: Authentication (who are you?) vs. Authorization (what can you do?)

Q: Which BEST differentiates authentication from authorization?

**A.** Authentication is faster; authorization takes longer
   [Speed misconception: orthogonal to the distinction]
**B.** Authentication verifies identity; authorization verifies permissions
   [CORRECT: This is the core distinction]
**C.** Authentication is more important for security
   [Priority misconception: both equally critical]
**D.** Authorization is older (HTTP Basic); authentication is newer (OAuth)
   [Historical misconception: both exist in multiple forms]

Strategy: Distractors confuse the concepts without swapping them
          (unlike Strategy 2C which would get auth/authn backwards)

Distractor quality:
- A: ~6% selection (tangential performance difference)
- C: ~9% selection (security priority is orthogonal)
- D: ~7% selection (evolution of protocols, not distinction)
✓ All functional
```

#### Strategy 2C: Common Misconception

Used for: Concepts where learners typically hold wrong beliefs

```
Concept pair: REST (architectural style) vs. HTTP (protocol)

Q: Which BEST differentiates REST from HTTP?

**A.** REST is a protocol; HTTP is an implementation detail
   [REVERSED: learners often think this]
**B.** HTTP is a protocol; REST is an architectural style built on top of HTTP
   [CORRECT]
**C.** REST is only for APIs; HTTP is for web pages
   [Scope misconception: both can serve both purposes]
**D.** REST requires RESTful databases; HTTP requires RESTful servers
   [Implementation misconception: REST applies to service design, not infrastructure]

Strategy: Distractor A specifically targets the most common reversal

Distractor quality:
- A: ~18% selection (very common misconception!)
- C: ~8% selection (scope limitation error)
- D: ~6% selection (infrastructure confusion)
✓ All functional (especially A—captures common learner error)
```

---

## Question Type 3: Decision Matrix (12.5%)

**Purpose:** Test multi-criteria decision-making.

**Challenge:** Each distractor must fail on one specific constraint.

### Distractor Strategies

#### Strategy 3A: Fails on One Constraint

Used for: Scenarios with clear constraints

```
Constraints: Low cost, fast to implement (weeks, not months), scales to 1M users

Q: Given low budget, tight timeline, and need to scale to 1M users,
   which approach is MOST appropriate?

**A.** Enterprise data warehouse (Snowflake/BigQuery)
   [Fails constraint: High licensing cost ($50k+/year)]
**B.** Custom-built system from scratch in Node.js
   [Fails constraint: 4-6 months development (too slow)]
**C.** Managed streaming service (Kafka on AWS)
   [Fails constraint: Requires infrastructure learning]
**D.** Open-source streaming stack (Kafka + Flink) on existing cloud infrastructure
   [CORRECT: Open-source (low cost), proven scalable, team knows cloud ops]

Strategy: Each distractor fails exactly one constraint

Distractor quality:
- A: ~12% selection (cost consideration misses timeline)
- B: ~8% selection (custom prioritizes control, misses timeline)
- C: ~9% selection (infrastructure expertise barrier)
✓ All functional
```

#### Strategy 3B: Partial Correctness (True, but Not Best)

Used for: Scenarios where multiple options are viable

```
Constraints: Startup founder needs rapid MVP, limited DevOps knowledge

Q: For a startup MVP requiring authentication, which choice is BEST?

**A.** Firebase Authentication
   [CORRECT: Managed, <1 day integration, no ops knowledge needed]
**B.** Implement OAuth 2.0 with Keycloak
   [Viable but requires: DevOps setup (defeats "limited knowledge"), 2-3 weeks]
**C.** Use JWT tokens with custom validation
   [Viable but requires: Security knowledge (risks), 5-7 days]
**D.** Username/password with bcrypt hashing
   [Viable but requires: Implements 90% of OAuth value manually, riskier]

Strategy: All answers are viable; correct is BEST given constraints

Distractor quality:
- B: ~15% selection (solid approach, just not best for constraints)
- C: ~9% selection (reasonable but underestimates difficulty)
- D: ~6% selection (minimalist but misses modern best practice)
✓ All functional
```

#### Strategy 3C: Common Wrong Trade-Off

Used for: Scenarios where learners sacrifice wrong constraint

```
Constraints: Real-time (<100ms), reliable (99.99% uptime), budget-conscious

Q: For real-time, highly reliable system on limited budget, which approach?

**A.** Eventually consistent distributed cache (Redis cluster)
   [Wrong trade-off: Sacrifices reliability (cache loss possible)]
**B.** Strongly consistent relational DB with read replicas + monitoring
   [CORRECT: Achieves reliability + realtime + cost-effective]
**C.** In-memory database (Memcached) for speed
   [Wrong trade-off: Sacrifices reliability (no persistence)]
**D.** Single powerful database server (vertical scale)
   [Wrong trade-off: Sacrifices reliability (single point of failure)]

Strategy: Distractors represent common wrong trade-offs

Distractor quality:
- A: ~10% selection (speed tempts sacrifice of reliability)
- C: ~8% selection (classic speed-over-reliability trap)
- D: ~7% selection (vertical scaling trap for reliability)
✓ All functional
```

---

## Question Type 4: Architecture Analysis (12.5%)

**Purpose:** Test understanding of system structure and components.

**Challenge:** Distractors must be realistic roles/approaches, just not primary.

### Distractor Strategies

#### Strategy 4A: Different Component Role

Used for: Systems with multiple interacting components

```
System: Event-driven microservices with message broker

Q: In event-driven architecture, what is the PRIMARY role of the message broker?

**A.** Process and transform events into application objects
   [Role of: Event processor/stream processor, not broker]
**B.** Decouple producers from consumers using asynchronous message queues
   [CORRECT]
**C.** Store events permanently for audit and replay
   [Role of: Event store/data lake, not broker's primary role]
**D.** Validate event schemas against declared contracts
   [Role of: Schema registry, not message broker]

Strategy: Each distractor is real component responsibility

Distractor quality:
- A: ~12% selection (real function, wrong component)
- C: ~10% selection (real requirement, wrong component)
- D: ~8% selection (real concern, wrong tool)
✓ All functional
```

#### Strategy 4B: Related But Secondary Function

Used for: Components with primary and secondary roles

```
Component: Load balancer in web application

Q: What is the PRIMARY role of a load balancer?

**A.** Distribute incoming traffic across multiple servers
   [CORRECT]
**B.** Detect failing servers and route traffic away automatically
   [Secondary role: Health checking (feature, not primary purpose)]
**C.** Terminate SSL/TLS encryption
   [Possible role: SSL termination (optimization, not primary)]
**D.** Cache frequently requested content
   [Role of: Reverse proxy/cache layer, not load balancer's primary]

Strategy: All answers describe real load balancer functions

Distractor quality:
- B: ~14% selection (important secondary role, not primary)
- C: ~8% selection (useful optimization, not core purpose)
- D: ~6% selection (related concern, wrong tool)
✓ All functional
```

#### Strategy 4C: Correct Concept, Wrong Context

Used for: Cross-functional components

```
Architecture layer: API Gateway

Q: In microservices architecture, what is the PRIMARY role of the API gateway?

**A.** Aggregate responses from multiple microservices
   [Possible in some patterns, but not API gateway's primary role]
**B.** Provide a single entry point handling routing, auth, and rate limiting
   [CORRECT]
**C.** Manage service discovery and load balancing between services
   [Role of: Service mesh or orchestrator, not gateway]
**D.** Store session state for authenticated requests
   [Anti-pattern: Stateless design, not gateway's role]

Strategy: Distractors describe real architecture functions

Distractor quality:
- A: ~9% selection (aggregation is common pattern, wrong component)
- C: ~11% selection (service mesh responsibility, not gateway)
- D: ~6% selection (violates stateless principle)
✓ All functional
```

---

## Question Type 5: Economic/Quantitative (10%)

**Purpose:** Test calculation and comparative analysis.

**Challenge:** Distractors must show plausible calculation errors.

### Distractor Strategies

#### Strategy 5A: Calculation Error Pattern

Used for: Math-based questions

```
Facts: Human FTE costs $8,000/month, Digital FTE costs $2,000/month
       Organization has 50 employees

Q: What is the annual savings if 30 Human FTEs are replaced with Digital FTEs?

**A.** $180,000   [Error: 30 × 6,000 (monthly diff, not annual)]
**B.** $2,160,000 [CORRECT: 30 × $6,000/month × 12 months]
**C.** $720,000   [Error: 30 × 24,000 (double-counts, or yearly on both)]
**D.** $18,000    [Error: 30 × 600 (decimal place error)]

Strategy: Each wrong answer shows specific calculation error

Distractor quality:
- A: ~18% selection (forgets to multiply by 12)
- C: ~12% selection (wrong multiplication factor)
- D: ~5% selection (decimal place error)
✓ All functional
```

#### Strategy 5B: Partial Formula Error

Used for: Multi-step calculations

```
Facts: System A: $100k setup + $10k/month ongoing for 3 years
       System B: $500k setup, no ongoing costs for 3 years

Q: After 3 years, what is the total cost difference?

**A.** $460,000   [Error: ($100k + 10k×36) - $500k = $40k (wrong sign)]
**B.** $40,000    [Error: Only accounts for 4 months ($500k - $100k - $40k)]
**C.** $400,000   [CORRECT: System B($500k) - System A($460k) = $40k NO WAIT]
   [Let me recalculate: System A = $100k + ($10k × 36 months) = $460k]
   [System B = $500k, Difference = $500k - $460k = $40k NOT $400k]

Let me redo this more carefully:

Q: After 3 years, which has lower total cost of ownership (TCO)?
   System A: $100k setup + $5k/month maintenance
   System B: $0 setup + $20k/month + $150k at year 3

**A.** System B (TCO lower by $150k)    [Error: Ignores year-3 cost]
**B.** System A (TCO lower by $70k)     [CORRECT: A=$280k, B=$350k, diff=$70k]
**C.** System B (TCO lower by $70k)     [Error: Reversed winner]
**D.** They're equal (both $300k)       [Error: Wrong calculation entirely]

Strategy: Each error shows missed calculation step

Distractor quality:
- A: ~8% selection (misses lump-sum payment)
- C: ~10% selection (gets calculation but reverses)
- D: ~6% selection (major error, but represents "I give up" guess)
✓ All functional
```

---

## Question Type 6: Specification Design (10%)

**Purpose:** Test ability to apply frameworks and methodologies.

**Challenge:** Distractors must show reasonable but flawed framework application.

### Distractor Strategies

#### Strategy 6A: Over-Specification

Used for: Framework application scenarios

```
Framework: REST API design for resource collection

Q: When designing a REST API for listing users, which is BEST?

**A.** GET /users?page=1&limit=100&search=john&role=admin&status=active
   [Over-specification: Filters are for POST body or query normalization]
**B.** GET /users with standard pagination (limit, offset) and optional filters
   [CORRECT: Query params for filters, follows REST conventions]
**C.** POST /users with search criteria in request body
   [Wrong method: Use GET for retrieval, not POST]
**D.** GET /users/search/john?role=admin (separate search endpoint)
   [Over-engineered: Unnecessary special-case endpoint]

Strategy: Distractors show common over/under-engineering mistakes

Distractor quality:
- A: ~9% selection (follows intuition but violates REST)
- C: ~8% selection (uses wrong HTTP method)
- D: ~7% selection (works but unnecessary complexity)
✓ All functional
```

#### Strategy 6B: Under-Specification

Used for: Framework application with minimum viable implementation

```
Framework: Microservices communication pattern

Q: When services need to communicate asynchronously, what is the MINIMUM viable pattern?

**A.** Implement full event streaming (Kafka, NATS, etc.)
   [Over-specified: Overkill for simple async]
**B.** Message queue with reliable delivery + consumer acknowledgment
   [CORRECT: Minimum viable async, ensures reliability]
**C.** Simple HTTP polling between services
   [Under-specified: Wasteful, unreliable]
**D.** Shared database with polling
   [Under-specified: Creates tight coupling]

Strategy: Distractors show under/over-application of framework

Distractor quality:
- A: ~8% selection (correct direction, over-engineered)
- C: ~12% selection (seems simpler, misses reliability)
- D: ~6% selection (anti-pattern, seems simple)
✓ All functional
```

---

## Question Type 7: Critical Evaluation (12.5%)

**Purpose:** Test judgment and trade-off analysis.

**Challenge:** Distractors must represent plausible but secondary concerns.

### Distractor Strategies

#### Strategy 7A: Primary vs. Secondary Trade-Off

Used for: Architectural decisions with multiple trade-offs

```
Decision: Implement eventual consistency in financial system

Q: What is the PRIMARY trade-off of implementing eventual consistency?

**A.** Higher infrastructure costs
   [Secondary concern: Usually reduces cost]
**B.** Temporary data divergence requiring conflict resolution logic
   [CORRECT: PRIMARY trade-off - the defining characteristic]
**C.** Increased complexity of deployment
   [Secondary concern: Operational, not fundamental]
**D.** Reduced system throughput
   [Misconception: Eventual consistency improves throughput]

Strategy: Correct answer addresses CORE trade-off, not side effects

Distractor quality:
- A: ~6% selection (gets trade-off direction wrong)
- C: ~8% selection (operational concern, not fundamental)
- D: ~5% selection (fundamental misconception)
✓ All functional
```

#### Strategy 7B: Benefit Misframed as Limitation

Used for: Evaluations where learners confuse properties

```
Decision: Use denormalization in NoSQL database

Q: What is the PRIMARY limitation of data denormalization?

**A.** Query performance degrades (makes queries slower)
   [Benefit misframed: Denorm improves query speed]
**B.** Write complexity increases due to maintaining multiple copies
   [CORRECT: PRIMARY limitation - data consistency burden]
**C.** Storage requirements increase (redundant data)
   [Consequence, not primary limitation]
**D.** Development team needs SQL training
   [Orthogonal: Training is independent concern]

Strategy: Distractor A frames the benefit as limitation

Distractor quality:
- A: ~16% selection (very common confusion)
- C: ~9% selection (consequence, not primary issue)
- D: ~5% selection (personnel issue, not technical limitation)
✓ All functional (especially A—targets common misconception)
```

---

## Question Type 8: Strategic Synthesis (10%)

**Purpose:** Test integration of multiple concepts.

**Challenge:** Distractors must show partial or incomplete synthesis.

### Distractor Strategies

#### Strategy 8A: Missing One Element

Used for: Multi-component integration scenarios

```
Goal: Design system that is scalable, maintainable, AND performant

Q: To achieve scalability + maintainability + performance simultaneously,
   which combination is MOST appropriate?

**A.** Monolith with aggressive caching + CDN for performance
   [Misses: Maintains monolith (not maintainable for scale)]
**B.** Microservices + comprehensive logging + async processing
   [Missing: Doesn't address performance optimization]
**C.** Microservices + clear interfaces + async processing + strategic caching + monitoring
   [CORRECT: Addresses all three concerns]
**D.** API gateway + load balancer + database replication
   [Missing: Doesn't address maintainability (service boundaries)]

Strategy: Each distractor omits one key element

Distractor quality:
- A: ~7% selection (addresses performance but not maintainability)
- B: ~10% selection (addresses 2/3, missing performance)
- D: ~8% selection (addresses scale, missing maintainability)
✓ All functional
```

---

## Question Type 9: Research Extension (7.5%)

**Purpose:** Test extrapolation to novel scenarios.

**Challenge:** Distractors must show plausible but flawed extrapolation.

### Distractor Strategies

#### Strategy 9A: Over-Generalization

Used for: Novel scenario application of established principles

```
Principle: "Horizontal scaling (adding servers) is preferred over vertical scaling"

Q: If this principle applies to web servers, which extrapolation is MOST rigorous?

**A.** Horizontal scaling always better than vertical for ANY workload
   [Over-generalization: Doesn't apply to single-threaded workloads]
**B.** Database scaling may differ: vertical scaling acceptable for latency-sensitive operations
   [CORRECT: Qualifies principle based on specific constraints]
**C.** Horizontal scaling is required for all systems >1M users
   [Over-generalization: Netflix scaled significantly with vertical]
**D.** Vertical scaling is obsolete and should never be used
   [Extreme over-generalization: Still valid for many scenarios]

Strategy: Distractors show various over-generalizations

Distractor quality:
- A: ~9% selection (common over-generalization)
- C: ~8% selection (wrong threshold, over-applied)
- D: ~5% selection (absolutist error)
✓ All functional
```

#### Strategy 9B: Ignoring Critical Constraint

Used for: Novel scenarios with new constraints

```
Principle: "Cache frequently accessed data for performance"

Q: A healthcare system must cache patient records for speed. Which extrapolation
   considers the MOST critical new constraint (regulatory compliance)?

**A.** Cache all patient data using Redis (applies principle directly)
   [Ignores: HIPAA compliance - what data can be cached?]
**B.** Cache only aggregated statistics and metadata; never cache PII
   [CORRECT: Recognizes new constraint limits principle]
**C.** Cache with encryption to satisfy compliance
   [Partial: Addresses symptom, not root issue]
**D.** Use managed database caching with vendor compliance certification
   [Delegates: Trusts vendor, doesn't question applicability]

Strategy: Distractors show various failures to account for new constraints

Distractor quality:
- A: ~12% selection (ignores compliance entirely)
- C: ~8% selection (security theater, misses core issue)
- D: ~6% selection (abdication of responsibility)
✓ All functional
```

---

## Quality Assurance Checklist for Distractors

For EVERY question you generate, verify all distractors meet:

### Plausibility Check

- [ ] Distractor represents real misconception or error
- [ ] Domain expert would find it plausible (~5-25% of people make this error)
- [ ] Not obviously absurd or ridiculous

### Functionality Check

- [ ] Expected selection rate ≥5% (>10% is ideal)
- [ ] Distinct from other distractors (not repeating same error)
- [ ] Independent reasoning path (not dependent on other options)

### Quality Check

- [ ] All 4 options within 0.8x-1.2x of mean word count (length parity)
- [ ] Specificity level matches correct answer
- [ ] Wording clarity matches correct answer
- [ ] No trick language or gotchas

### Educational Value Check

- [ ] Reveals common misconception
- [ ] Teaches something by being wrong
- [ ] Explains why misconception is plausible
- [ ] Doesn't just confuse or frustrate

### Examples Check

- [ ] All options with same structure/format
- [ ] No "all of the above" / "none of the above"
- [ ] No hints from grammatical clues
- [ ] No clues from alphabetical patterns

---

## Common Distractor Generation Mistakes

### ❌ Mistake 1: Absurd/Silly Options

```
Q: What is 2 + 2?
**A.** 4
**B.** 3
**C.** 27    [Obviously wrong - wastes slot]
**D.** Banana  [Absurd - doesn't test knowledge]
```

**Fix:** Make C something like "5" (off-by-one error) or "22" (concatenation error)

### ❌ Mistake 2: Nonfunctional Distractors

```
Q: Which HTTP status code means "Not Found"?
**A.** 404  [Correct]
**B.** 502  [Obviously wrong - nobody picks this]
**C.** 500  [Obviously wrong - nobody picks this]
**D.** 403  [Better - authorization confusion, ~8% pick this]
```

**Fix:** Replace B and C with 405 (Method Not Allowed) and 401 (Unauthorized)

### ❌ Mistake 3: Repeating Same Error

```
Q: Best practice for cache invalidation?
**A.** Time-based expiration (TTL)  [CORRECT]
**B.** Manual invalidation on data changes  [Incomplete - doesn't mention TTL]
**C.** No invalidation needed  [Repeats: "Incomplete understanding"]
**D.** Developer disables caching  [Repeats: "No caching at all"]
```

**Fix:** Make C something like "Never cache writes, only reads" (common misconception)

### ❌ Mistake 4: Trick Wording

```
Q: Which of the following is LEAST likely to cause performance issues?
**A.** Sequential database queries
**B.** Synchronous API calls
**C.** Blocking I/O  [Trick: "LEAST likely" reverses expected answer]
**D.** Asynchronous processing
```

**Fix:** Ask positive: "Which approach is MOST likely to improve performance?"

### ❌ Mistake 5: Length Bias

```
Q: What is API rate limiting?
**A.** Prevents overload  [2 words]
**B.** Rate limiting  [2 words]
**C.** Protects the server from being overwhelmed by too many requests coming too fast  [Correct, 14 words - obviously longest!]
**D.** Denies access  [2 words]
```

**Fix:** Rewrite correct answer: "Protects server from request overload by limiting request rate"

---

## Implementation Workflow

When generating questions:

1. **Extract concept** from source material
2. **Formulate correct answer** (12-18 words, one clear idea)
3. **Count the correct answer's words** — this is your target length
4. **Identify error types** (what mistakes could learners make?)
5. **Generate 3 distractors** using strategies above, each matching the correct answer's word count (±20%)
6. **Validate all four options:**
   - Length parity: All options within 0.8x-1.2x of mean word count
   - Specificity check: Similar detail levels
   - Plausibility check: All ≥5% selection
   - Distinctness check: Each wrong for different reason

7. **Test:**
   - Have domain expert evaluate plausibility
   - Measure selection rates in actual administration
   - Flag anything <5% for revision

---

## References

- [Developing and Analyzing Distractors for Multiple-Choice Tests](https://www.researchgate.net/publication/319470426_Developing_Analyzing_and_Using_Distractors_for_Multiple-Choice_Tests_in_Education_A_Comprehensive_Review)
- [Item Analysis Impact on Difficulty and Discrimination](https://link.springer.com/article/10.1186/s12909-024-05433-y)
