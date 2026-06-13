# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

This is a Python learning project focused on AI agents, deep learning architectures, and algorithm practice. The codebase is organized into chapters that progressively demonstrate AI concepts.

## Environment Setup

- Python 3.13 virtual environment located at `.venv/`
- Activate environment: `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
- Key dependencies: `openai`, `tavily-python`, `requests`, `torch`, `python-dotenv`

## Running Code

Execute individual Python files directly:
```bash
python chapter1/agent01.py
python chapter3/transformer_demo.py
python chapter4/llm_client.py
python algorithm/day01.py
```

## API Configuration

The LLM client requires environment variables. Create a `.env` file with:
```
LLM_MODEL_ID=<model_name>
LLM_API_KEY=<api_key>
LLM_BASE_URL=<api_endpoint>
LLM_HTTP_TIMEOUT=<timeout_seconds>
```

For `react_demo.py`, also configure `TAVILY_API_KEY` for the search tool.

## Code Architecture

### Chapter Structure

- **chapter1**: Basic LLM client wrapper (`HelloAgentsLLM`) with streaming response support. Demonstrates OpenAI-compatible API integration.
- **chapter3**: Transformer architecture demo with encoder/decoder layers. Contains placeholder modules (PositionalEncoding, MultiHeadAttention, PositionWiseFeedForward) that are stubs for future implementation.
- **chapter4**: ReAct agent implementation with tool calling pattern. Shows a Thought-Action-Observation loop with two tools (`get_weather`, `get_attraction`). Uses regex parsing to extract actions from LLM output.

### Algorithm Module

`algorithm/day01.py` contains LeetCode solutions within a `Solution` class. Each problem typically includes multiple implementations (e.g., `twoSum` and `twoSum1`) showing different approaches - often brute force followed by optimized solutions.

### ReAct Agent Pattern

The `react_demo.py` implements the ReAct (Reasoning + Acting) pattern:
1. LLM receives prompt with available tools and output format requirements
2. LLM outputs `Thought: ... Action: ...` pairs
3. System parses action, executes tool if needed, or returns final answer
4. Observation is appended to prompt history for next iteration

## 
1. 该项目用于学习agent相关知识
2. 用户具有五年后端java开发经验，现在在学习agent，需要帮助用户理解agent工程化并助力于用户快速理解并学习agent
3. 用户对于python只熟悉基础语法，涉及到python的高级特性及实际开发中常用的技能及语法也帮助用户顺带学习
4. 用户学习目的是为了面试并理解agent工程化及原理