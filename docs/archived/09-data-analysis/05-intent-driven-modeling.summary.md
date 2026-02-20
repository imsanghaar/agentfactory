### Core Concept
**Intent-driven modeling** means expressing financial objectives in natural language and having Claude translate them into structured financial logic. Instead of manually building formulas, you describe "model conservative revenue scenario with 20% customer loss in Q2, 50% recovery by Q4" and Claude constructs the model with documented assumptions.

### Key Mental Models
- **Intent → Model**: Business goal expressed in words → Claude reasons through implications → Structured model with explicit assumptions
- **Assumption Documentation**: Every model is only as good as its assumptions. Claude must document every assumption explicitly so humans can validate
- **Model Refactoring**: Existing models can be improved through conversation—"add step costs when we hire in batches of 5"
- **Sensitivity Analysis**: Understanding which variables matter most by testing "what if X changes by 10%?"

### Key Facts
- **Revenue modeling patterns**: Growth rates, seasonality, customer segments, churn, expansion revenue
- **Expense modeling patterns**: Fixed costs, variable costs (tied to revenue), step costs (triggered by thresholds), headcount-driven expenses
- **Source quote** (Agentic_Financial_Planning.pdf): "Users can express objectives in natural language... Claude translates these intents into structured financial logic"

### Critical Patterns
- **Intent-driven workflow**: State business scenario → Claude reasons through financial implications → Claude documents assumptions → Claude generates model specification → Human reviews assumptions → Claude builds formulas via MCP → Human validates outputs
- Always request assumption documentation with every model
- Test models with edge cases before relying on them
- Use sensitivity analysis to identify which assumptions matter most

### Common Mistakes
- Accepting models without reviewing assumptions (garbage in, garbage out)
- Not testing edge cases (what happens if revenue goes negative?)
- Assuming Claude's model is correct without validation (always verify key calculations manually)
- Building overly complex models when simple ones suffice (complexity ≠ accuracy)

### Connections
- **Builds on**: Lesson 4 (Google Sheets MCP for formula execution), CLAUDE.md context (fiscal year, accounting policies)
- **Leads to**: AI-native accounting workflows, scenario analysis and stress testing, capstone Finance Digital FTE
