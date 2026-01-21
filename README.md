# Chatbot Project - AI Coding Agent Instructions

## Project Overview
This is a **Streamlit-based PDF chatbot** that extracts text from uploaded PDF files, processes it using LangChain, and creates a FAISS vector database for semantic search.

## Architecture & Data Flow
1. **User uploads PDF** → Streamlit sidebar file uploader
2. **Text extraction** → PyPDF2 extracts text from all pages
3. **Text chunking** → RecursiveCharacterTextSplitter splits text with:
   - Chunk size: 1000 characters
   - Overlap: 200 characters (for context preservation)
   - Separators: `["\n\n", "\n", " ", ""]` (hierarchical)
4. **Embeddings generation** → OpenAI embeddings API
5. **Vector store** → FAISS stores embeddings locally

## Key Dependencies & Versions
- **Streamlit** - Web UI framework
- **PyPDF2** - PDF text extraction
- **LangChain** - Text splitting and embeddings orchestration
- **OpenAI API** - Embedding generation (requires API key)
- **FAISS** - CPU-based vector database

## Developer Workflow

### Setup
```bash
pip install streamlit pypdf2 langchain faiss-cpu
# Set OPENAI_API_KEY environment variable
```

### Running the App
```bash
streamlit run chatboat.py
```

### Testing
- Test with sample PDFs (text-based, not scanned images)
- Verify embeddings are created without API errors
- Check chunk overlap preserves query context

## Critical Security Issue ⚠️
**DO NOT commit API keys to the repository.** The current code exposes the OpenAI API key hardcoded. Use environment variables instead:
```python
import os
OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
```

## Project Conventions
- **Single entry point** - `chatboat.py` contains entire application
- **Streamlit layout** - Sidebar for inputs, main area for outputs
- **Vector database** - FAISS used for in-memory storage (not persistent)
- **Chunking strategy** - Prioritizes paragraph breaks for semantic coherence

## Common Extension Points
1. **Add chat interface** - Chain Q&A after vector store creation (currently only shows chunks)
2. **Persist embeddings** - Save FAISS vector store to disk
3. **Handle scanned PDFs** - Integrate OCR for image-based PDFs
4. **Rate limiting** - Manage OpenAI API costs with usage tracking
5. **Multi-document support** - Store vectors from multiple PDFs in one vector store

## Project Structure
- `chatboat.py` - Main application entry point (~50 lines)
- `project.tex` - Dependency installation documentation
