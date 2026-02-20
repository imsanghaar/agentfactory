# Andrew Ng's Agentic AI Evaluation Methodology

## Source
Andrew Ng's Agentic AI Course - Module on Evaluations and Error Analysis

## Key Quote

> "One of the biggest predictors for whether someone is able to build agentic workflows really well is whether or not they're able to drive a really disciplined evaluation process."

## Core Philosophy

### Build First, Evaluate Second

"It's difficult to know in advance what can go wrong. Rather than trying to build evaluations in advance, I recommend you just look for the outputs and manually look for things that you wish it was doing better."

**Workflow**:
1. Build quick-and-dirty system first
2. Examine outputs manually
3. Identify unsatisfactory behaviors
4. Create targeted evals
5. Use evals to drive improvement

### Example: Competitor Mentions

"Many businesses don't want their agents to mention competitors because it creates an awkward situation. This is an example of a problem that is really hard to anticipate in advance of building the agentic workflow."

**Solution**:
- Observe pattern in outputs
- Create eval to track frequency
- For objective criteria (competitor name appears): use code
- For subjective criteria (is response helpful?): use LLM-as-judge

## The Two Types of Evaluations

### Objective vs Subjective

"One nice thing about competitor mentions is it's an objective metric—either the competitor was mentioned or not. For objective criteria, you can write code to check."

"Because LLMs output free text, there are also criteria that may be more subjective where it's harder to just write code."

### The Four Quadrants

| | Objective (Code) | Subjective (LLM Judge) |
|---|---|---|
| **Per-example ground truth** | Invoice date extraction | Gold standard talking points |
| **No per-example ground truth** | Word count limits | Rubric-based chart grading |

## Rubric-Based Grading

### Why Binary Criteria Beat 1-5 Scales

"It turns out that LLMs are actually not that good at 1-5 scale ratings. Instead of asking the LLM to grade something on a scale of 1 to 5, if you give it 5 binary criteria and have it give 5 binary scores and add them up, that tends to give more consistent results."

### Example Rubric

```
Assess the chart against this quality rubric:
1. Does the plot have a clear title? (yes/no)
2. Are the axis labels present? (yes/no)
3. Is it an appropriate chart type? (yes/no)
4. Is the data accurately represented? (yes/no)
5. Is the legend clear? (yes/no)
```

**Result**: Sum of yes answers = 0-5 score (more calibrated than direct 1-5 rating)

## Error Analysis Methodology

### The Importance of Traces

"I'll often examine the traces—the intermediate output after each step—in order to understand where it is falling short."

**Terminology**:
- **Trace**: Overall set of outputs of all intermediate steps
- **Span**: Output of a single step (from observability literature)

### Systematic Error Counting

"Rather than reading and getting an informal sense, you might build up a spreadsheet to explicitly count up where the errors are."

**Example Spreadsheet**:
| Query | Search Terms | Search Results | Best Sources | Final Output |
|-------|-------------|---------------|--------------|--------------|
| Black holes | OK | Too many blogs | Based on poor input | Missing key points |
| Seattle rent | OK | OK | Missed blog | OK |
| Fruit robots | Generic | Poor quality | Poor | Missing company |

**Result**: Count percentages:
- Search terms: 5% problems
- Search results: 45% problems ← Focus here
- Best sources: 20% problems
- Final output: 30% problems

### Prioritization

"By looking at what components are doing poorly, as well as where I have ideas for efficiently improving, that lets me prioritize what component to work on."

**Criteria**:
1. Frequency of errors
2. Feasibility of improvement
3. Impact on final output

## Component-Level Evaluations

### Why Component Evals Matter

"If the problem was web search, every time we change the web search engine we need to rerun the entire workflow—that eval is expensive. Moreover, noise introduced by randomness of other components would make it harder to see little improvements."

### Benefits

1. **Clearer signal**: Isolate specific component
2. **Faster feedback**: Don't run full workflow
3. **Less noise**: Avoid variance from other components
4. **Team efficiency**: Different teams can focus on their component

### Example: Web Search Evaluation

"Create a list of gold standard web resources. For a handful of queries, have an expert say these are the most authoritative sources. Then write code to capture how many web search outputs correspond to gold standard resources."

## Reflection with External Feedback

### Why External Feedback Matters

"Reflection with external feedback, if you can get it, is much more powerful than reflection using the LLM as the only source of feedback."

### Sources of External Feedback

1. **Code execution**: Run code, capture output/errors
2. **Pattern matching**: Search for competitor names via regex
3. **Web search**: Fact-check claims against external sources
4. **Word count**: Measure exact length vs. target

### Performance Trajectory

```
Direct generation: Performance plateaus
         +
Reflection: Bump in performance
         +
External feedback: Much higher performance
```

## Practical Tips

### Starting with Evals

"Quick and dirty evals is fine to get started. I see teams paralyzed because they think building evals is a massive multi-week effort."

**Recommendation**:
- Start with 10-20 examples
- Write code or prompt LLM-as-judge
- Get some metrics to complement human eye
- Iterate on evals as you iterate on system

### Growing Evals Over Time

"If you had 20 examples to start, you may run into places where evals fail to capture your judgment about what system is better. That's an opportunity to collect a larger eval set or change how you evaluate."

### Using Evals for Inspiration

"For applications automating tasks humans can do, look for places where performance is worse than expert human. That gives inspiration for where to focus efforts."

## The Build-Analyze Loop

"When I'm building these workflows, there are two major activities:
1. **Building**: Writing software, trying to write code to improve
2. **Analysis**: Deciding where to focus build efforts next"

**Iterative Process**:
1. Build end-to-end system
2. Examine outputs, read traces
3. Get gut sense of problems
4. Build evals (10-20 examples)
5. More refined perspective
6. Do error analysis with spreadsheet
7. Build component-level evals
8. Bounce back and forth

"Less experienced teams spend a lot of time building and probably much less time analyzing. Analysis helps you really focus where to spend your time building."

## Cost and Latency Optimization

### When to Optimize

"I'll often advise teams to focus on getting high-quality outputs and optimize cost and latency only later. Getting the output quality high is usually the hardest part."

### Benchmarking Approach

**For latency**: Time each step
```
LLM search terms: 7s
Web search: 5s
LLM select sources: 3s
Web fetch: 11s
LLM write essay: 18s
Total: 44s
```

**For cost**: Calculate per-step costs
```
Search terms tokens: $0.04
Web search API: $1.60
Source selection tokens: $0.02
Web fetch: $0.00
Essay generation: $0.12
Total: $1.78
```

**Focus**: Optimize components that dominate time/cost

---

## Key Takeaways

1. **Build first, evaluate second** - Don't theorize; build something and see what's wrong
2. **Quick-and-dirty is fine** - 10-20 examples beats paralysis
3. **Use binary criteria** - More reliable than 1-5 scales
4. **Count errors systematically** - Don't go by gut
5. **Component evals complement E2E** - Use both strategically
6. **Iterate on evals** - They improve alongside your agent
7. **Analysis time is valuable** - Less experienced teams under-invest here
