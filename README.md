# Agentic

A modular Python agent framework for LLM tool use and orchestration.

## Features
- Modular code: prompt formatting, LLM calls, parsing, tool logic, and orchestration are separated
- Easily extendable with new tools
- Uses Ollama and the phi3 model for LLM calls

## Usage
1. Install [Ollama](https://ollama.com/) and ensure the `phi3` model is available.
2. Run the agent:
   ```bash
   python run_agent.py
   ```
3. Enter your prompt and interact with the agent.

## Project Structure
- `agent.py` — Orchestrates the agent loop
- `call_llm.py` — Handles LLM calls
- `prompt_building.py` — Formats prompts for the LLM
- `parsing.py` — Parses LLM responses
- `tool_call.py` — Implements and dispatches tool calls
- `run_agent.py` — Entry point for running the agent

## License
MIT
