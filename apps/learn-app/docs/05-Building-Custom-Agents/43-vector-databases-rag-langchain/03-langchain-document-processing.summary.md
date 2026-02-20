### Core Concept
Documents need chunking before embedding. RecursiveCharacterTextSplitter splits intelligently using hierarchy: paragraphs → lines → words → characters. Chunk overlap preserves boundary context. Metadata (source, page) flows through for citation and filtering.

### Key Mental Models
- **Document object**: `page_content` + `metadata` dictionary
- **Separator hierarchy**: "\n\n" → "\n" → " " → "" preserves semantic boundaries
- **Overlap prevents loss**: 20% overlap ensures boundary content appears in adjacent chunks
- **Metadata for traceability**: Source, page, position enable citations

### Critical Patterns
- Loader selection: TextLoader, PyPDFLoader, WebBaseLoader based on source type
- Splitter config: `RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)`
- Metadata inheritance: Chunks inherit parent metadata plus get `start_index`
- Processing pipeline: Load → Split → (Embed → Store in next lesson)

### AI Collaboration Keys
- Compare chunking strategies for different document types
- Debug empty loader results (encoding, path issues)
- Design chunking for API docs vs long-form content

### Common Mistakes
- Chunks too small (fragmented, context-free pieces)
- Zero overlap (boundary content lost between chunks)
- Ignoring metadata (impossible to cite sources)

### Connections
- **Builds on**: Vector Embeddings Mental Model (Lesson 2)
- **Leads to**: Qdrant Vector Store with LangChain (Lesson 4)
