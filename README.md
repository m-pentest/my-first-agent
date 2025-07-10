# Simple AI Agent (Local, Lightweight)

This is a minimal, local-first AI agent built using an open-source LLM (via Ollama) and a basic web search tool. It demonstrates the core planning–tool–response loop that underlies many agentic architectures, but without external dependencies or orchestration frameworks.

## Features

- Accepts natural language goals
- Breaks goals into subtasks using a local LLM
- Uses DuckDuckGo Search as a basic external tool
- Returns summarized answers with LLM context

## Requirements

- Python 3.8+
- Ollama installed with `mistral` or similar model
- Python packages:
  - `openai`
  - `duckduckgo-search`

## Setup

Install dependencies:

```bash
pip install openai duckduckgo-search
```

Start your local LLM model:

```bash
ollama run mistral
```

## File Structure

- `planner.py`: Handles interaction with the LLM and step planning
- `tools.py`: Provides tool functionality (DuckDuckGo search)
- `agent_runner.py`: Main execution logic and agent loop

## Run the Agent

From the terminal:

```bash
python agent_runner.py "What are the current threats in AI security?"
```

The agent will:
1. Plan the steps to answer the goal
2. Use a simple tool to gather external data
3. Generate a final answer using the LLM

## Security Considerations

This basic prototype is for educational use. It does not include safeguards against:

- Prompt injection
- Malicious tool use
- Memory-based attacks

You should treat agent input and memory as untrusted data.

## Learn More

Full walkthrough available at:  
[https://mamtaupadhyay.com/2025/07/09/llm-build-building-your-first-ai-agent/)

## License

MIT License

---

This agent is a simple starting point for more complex agentic systems. Future posts will cover adding memory, multi-step reasoning and chaining more advanced tools securely.
