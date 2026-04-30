# RAG, Agentic AI, and Multi-Agent Systems

## Table of Contents
1. [Retrieval-Augmented Generation](#retrieval-augmented-generation)
2. [Agent Architectures](#agent-architectures)
3. [Tool Use and Function Calling](#tool-use-and-function-calling)
4. [Multi-Agent Systems](#multi-agent-systems)
5. [Evaluation and Benchmarks](#evaluation-and-benchmarks)

---

## Retrieval-Augmented Generation

### Core Idea
Augment LLM with external knowledge at inference time:
1. **Retrieve** relevant documents from a knowledge base
2. **Augment** the prompt with retrieved context
3. **Generate** response grounded in retrieved information

### RAG Pipeline
```
Query → Embedding Model → Vector Search → Top-K Documents → [Query + Context] → LLM → Response
```

### Embedding and Retrieval
- **Dense retrieval:** Encode query and docs with embedding model (e.g., BGE, E5, GTE). Cosine similarity search.
- **Sparse retrieval:** BM25, TF-IDF. Keyword-based. Good for exact match.
- **Hybrid:** Combine dense + sparse scores (Reciprocal Rank Fusion).

### Vector Databases
| Database | Type | Key Feature |
|----------|------|------------|
| FAISS | Library | Facebook. GPU-accelerated. HNSW + IVF indexes. |
| Chroma | Embedded | Simple Python API. Good for prototyping. |
| Pinecone | Cloud | Managed service. Metadata filtering. |
| Weaviate | Self-hosted/cloud | GraphQL API. Hybrid search built-in. |
| Qdrant | Self-hosted/cloud | Rust-based. Filtering + payload support. |
| pgvector | PostgreSQL extension | SQL-native vector search. |

### Chunking Strategies
- **Fixed-size:** Split by token count (e.g., 512 tokens). Simple but breaks semantic units.
- **Recursive character:** Split by paragraph → sentence → word. LangChain default.
- **Semantic:** Group sentences by embedding similarity.
- **Document-structure-aware:** Split by headings, sections. Best for technical docs.

### Advanced RAG Patterns
- **Query rewriting:** Rephrase query for better retrieval (HyDE: generate hypothetical answer, use it as query)
- **Multi-query:** Generate multiple query variants, retrieve for each, merge results
- **Self-RAG:** LLM decides whether to retrieve, critiques relevance of retrieved docs
- **Corrective RAG (CRAG):** If retrieved docs are irrelevant, fall back to web search
- **GraphRAG:** Build knowledge graph from corpus, traverse graph for multi-hop retrieval
- **Agentic RAG:** Agent decides when/what to retrieve iteratively during reasoning

### RAG Evaluation Metrics
- **Retrieval:** Recall@K, MRR (Mean Reciprocal Rank), NDCG
- **Generation faithfulness:** Does answer match retrieved context? (RAGAS, TruLens)
- **Answer relevance:** Does answer address the question?
- **Context relevance:** Are retrieved documents relevant to the query?

---

## Agent Architectures

### ReAct (Reason + Act)
Interleave reasoning and actions:
```
Thought: I need to find the population of Tokyo.
Action: search("Tokyo population 2024")
Observation: Tokyo has ~14 million people in the city proper.
Thought: I now have the answer.
Action: finish("Tokyo has approximately 14 million people")
```

### Planning Strategies
- **Chain-of-Thought (CoT):** Think step by step before answering
- **Tree of Thought (ToT):** Explore multiple reasoning paths, evaluate, backtrack
- **Plan-and-Execute:** Generate full plan upfront, execute steps, replan if needed
- **Reflexion:** After failure, generate verbal self-reflection, use in next attempt
- **LATS (Language Agent Tree Search):** MCTS-style search over action space

### Memory Systems
- **Short-term:** Conversation context window (limited by context length)
- **Long-term:** Vector database of past interactions/knowledge
- **Working memory:** Scratchpad for intermediate reasoning results
- **Episodic memory:** Summaries of past task completions (Reflexion, Voyager)

### Agent Frameworks
| Framework | Key Feature | Best For |
|-----------|------------|----------|
| LangChain | Most popular, extensive integrations | RAG, chains, general agents |
| LangGraph | Graph-based workflows, state machines | Complex multi-step agents |
| CrewAI | Role-based multi-agent collaboration | Team simulation |
| AutoGen | Microsoft. Conversational multi-agent | Research, coding agents |
| Semantic Kernel | Microsoft. Enterprise .NET/Python | Enterprise integration |
| Haystack | Pipeline-based, modular | Production RAG systems |
| OpenAI Agents SDK | Built-in tool use, handoffs | OpenAI ecosystem |

---

## Tool Use and Function Calling

### Function Calling Pattern
LLM outputs structured tool calls instead of text:
```json
{
  "tool": "calculate",
  "arguments": {"expression": "sqrt(144) + 3^2"}
}
```

System executes tool, returns result, LLM continues generation.

### Common Tool Categories
- **Information retrieval:** Web search, database queries, API calls
- **Computation:** Calculator, code interpreter, symbolic math
- **File operations:** Read/write files, parse documents
- **Communication:** Send email, post message
- **Environment interaction:** Browser automation, terminal commands

### Model Context Protocol (MCP)
Anthropic's open standard for LLM-tool integration:
- Standardized JSON-RPC protocol between LLM and tool servers
- Server exposes: tools (functions), resources (data), prompts (templates)
- Transport: stdio, SSE, HTTP
- Enables universal tool interoperability across LLM providers

### Code Agents
Agents that write and execute code as their primary action:
- **Code interpreter:** Execute Python/JS in sandbox (ChatGPT, Claude)
- **Claude Code:** Terminal-based agentic coding (read/write files, run commands)
- **Devin / SWE-Agent:** Autonomous software engineering agents
- **Key pattern:** Plan → Write code → Execute → Observe output → Fix errors → Iterate

---

## Multi-Agent Systems

### Communication Patterns
- **Sequential:** Agent A → Agent B → Agent C (pipeline)
- **Hierarchical:** Manager agent delegates to specialist agents
- **Debate:** Multiple agents argue, judge selects best response
- **Collaborative:** Agents share workspace, build on each other's work
- **Competitive:** Agents try different approaches, best wins (ensemble)

### Orchestration Patterns
```
                 ┌─ Research Agent
User → Router → ├─ Coding Agent    → Aggregator → User
                 └─ Analysis Agent
```

- **Router:** Classifies query, sends to appropriate specialist
- **Supervisor:** Monitors agent progress, intervenes if stuck
- **Aggregator:** Combines outputs from multiple agents

### State Management
Multi-agent systems need shared state:
- **Shared memory:** All agents read/write common knowledge base
- **Message passing:** Agents communicate via structured messages
- **Blackboard:** Shared workspace where agents post partial solutions
- **Graph state:** LangGraph models agent state as a typed graph

### Guardrails and Safety
- **Input validation:** Schema enforcement on tool calls
- **Output filtering:** Block harmful/off-topic responses
- **Budget limits:** Max tokens, max tool calls, max time per task
- **Human-in-the-loop:** Require approval for high-stakes actions
- **Sandboxing:** Execute code in containers with no network/filesystem access

---

## Evaluation and Benchmarks

### Agent Benchmarks
| Benchmark | Evaluates | Key Metric |
|-----------|----------|------------|
| SWE-bench | Software engineering (fix real GitHub issues) | % resolved |
| WebArena | Web browsing task completion | Success rate |
| GAIA | General AI assistants (multi-tool) | Accuracy |
| AgentBench | Multi-environment agent tasks | Score |
| HumanEval | Code generation | pass@k |
| MATH / GSM8K | Mathematical reasoning | Accuracy |
| MMLU | Knowledge across 57 subjects | Accuracy |
| REAL | Browser automation (research, coding) | % accuracy |

### RAG Benchmarks
- **BEIR:** Information retrieval benchmark (18 datasets)
- **MTEB:** Massive Text Embedding Benchmark (embedding quality)
- **RAGAS:** Framework for evaluating RAG pipelines (faithfulness, relevance)
- **RGB:** Benchmark specifically for RAG systems
