🤖 Qwen Agent Society
AI-Powered Multi-Agent Enterprise Operations Platform

Built with FastAPI, LangGraph, Agentic AI, Ollama, Qwen3, PostgreSQL, and Vector Databases.

🚀 Overview

Qwen Agent Society is an enterprise-grade multi-agent AI platform designed to automate business operations through intelligent agent collaboration.

Core Agents
Supervisor Agent
Research Agent
Finance Agent
Compliance Agent
Memory Agent
Validator Agent
🏗️ Architecture
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
Supervisor Agent
 │
 ├── Research Agent
 ├── Finance Agent
 ├── Compliance Agent
 ├── Memory Agent
 └── Validator Agent
 │
 ▼
LangGraph Workflow
 │
 ▼
Qwen3 via Ollama
 │
 ▼
Response
✨ Features
Multi-Agent Collaboration
Task decomposition
Agent routing
Validation pipeline
Memory management
Enterprise Workflows
Research automation
Compliance checking
Financial analysis
Knowledge retrieval
🛠️ Technology Stack
Backend
Python
FastAPI
LangGraph
LangChain
AI
Qwen3
Ollama
Database
PostgreSQL
Qdrant
Frontend
React
TypeScript
Tailwind CSS
🚀 Run Locally
git clone https://github.com/MaarreeJ/qwen-agent-society.git

cd qwen-agent-society/backend

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
📚 API Docs
http://127.0.0.1:8000/docs
📈 Roadmap

FastAPI Backend

Supervisor Agent

Ollama Integration

Qwen3 Integration

LangGraph Workflow

Memory Layer

RAG Integration

Alibaba Cloud Deployment

👨‍💻 Author

Marree Jachaak

AI Engineer | Risk Management Professional | Agentic AI Builder

GitHub: https://github.com/MaarreeJ

📜 License

MIT License