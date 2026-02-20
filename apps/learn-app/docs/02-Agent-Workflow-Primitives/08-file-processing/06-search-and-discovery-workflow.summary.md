### Core Concept

Descriptive search means describing what you're looking for, not where you think it is. You know the content or purpose. Let the agent find the location. This "invisible skill" — describing what you need in progressively specific terms — transfers to databases, research, and any domain where you search large collections.

### Key Mental Models

- **What over where**: Describe characteristics (PDF about taxes from 2023), not locations (maybe in Downloads). You remember what things are, not where you put them.
- **Conversational refinement**: Start broad ("tax document from 2023"). See candidates. Narrow down ("from Chase, not Fidelity"). Each refinement gives the agent better search criteria.
- **Pattern-based discovery**: Once you find one example, ask the agent to find all similar files. One found document unlocks everything related.
- **Metadata to content progression**: Lesson 1 searched metadata (counts, sizes). Lesson 3 organized by extension (surface attributes). This lesson searches inside files (deep attributes). Each level reaches information the previous couldn't.

### Critical Patterns

- **"Find files that match [description] from [time period]"**: The agent searches multiple locations using `find` and `grep` based on your description.
- **"It was specifically from [source/context]"**: Narrows results when initial search returns too many candidates.
- **"Find all similar files to this one"**: Triggers pattern-based discovery after finding a good example.
- **Searching inside files**: When filenames are useless (`document.pdf`, `file(1).pdf`), the agent uses `pdftotext` and `grep` to search content. This is the jump from metadata-based to content-based search.
- **"Save the full list to search-results.txt and just show me the first 10"**: Protects your session from result floods while creating a persistent record.
- **Principle 1 (Bash is the Key)**: The agent combines `find`, `grep`, `pdftotext`, `xargs`, and pipes to search by name, content, and metadata.

### Common Mistakes

- Searching only one folder at a time: The agent can search multiple locations simultaneously.
- Relying on exact filenames: You rarely remember precise names. Describe content instead.
- Not refining through conversation: First search often returns many candidates. Narrow down iteratively.
- Stopping at filename search: When filenames are generic, content search (`pdftotext`, `grep`) finds what metadata cannot.

### Connections

- **Builds on**: Lessons 1-5 (all previous workflows including error recovery), Principle 1 (Bash) from Part 1
- **Leads to**: Capstone toolkit (Lesson 7) where search patterns become reusable prompts
