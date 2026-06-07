# qwen-agent-society
Enterprise AI Agent Society leveraging Agentic AI, LangGraph, FastAPI, and multi-agent orchestration to automate research, financial analysis, compliance checks, and business decision-making.
🤖 Qwen Agent Society
AI-Powered Multi-Agent Enterprise Operations Platform
🚀 Overview

Qwen Agent Society is an enterprise-grade AI platform that orchestrates multiple intelligent agents to automate business operations, research workflows, financial analysis, compliance validation, and decision support.

The platform leverages Agentic AI principles and LangGraph orchestration to coordinate specialized AI agents working together as a collaborative enterprise workforce.

🏗️ Architecture
User
 │
 ▼
Frontend (React)
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
 ├── Validator Agent
 └── Memory Agent
 │
 ▼
LangGraph Workflow Engine
 │
 ▼
LLM Provider (Qwen/OpenAI/Groq/Ollama)
🎯 Key Features

✅ Multi-Agent Orchestration

✅ Supervisor Agent Routing

✅ Research Agent

✅ Finance Agent

✅ Compliance Agent

✅ Validation Agent

✅ Memory Management

✅ LangGraph Workflow Engine

✅ FastAPI REST APIs

✅ React Frontend

✅ Enterprise Decision Support

✅ Extensible LLM Integration

🛠️ Technology Stack
Backend
Python
FastAPI
LangGraph
LangChain
Pydantic
AI Models
Qwen
OpenAI
Groq
Ollama
Databases
PostgreSQL
Qdrant Vector Database
Frontend
React
TypeScript
Vite
Deployment
Docker
Alibaba Cloud
Nginx
📂 Project Structure
qwen-agent-society/
├── backend/
├── frontend/
├── docs/
├── deployment/
├── README.md
└── LICENSE
⚡ Quick Start
Backend
cd backend
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
API Documentation
http://127.0.0.1:8000/docs
📈 Current Development Roadmap
Phase 1
FastAPI Backend
Supervisor Agent
LLM Integration
Phase 2
Research Agent
Finance Agent
Compliance Agent
Phase 3
LangGraph Workflow Engine
Phase 4
Memory Layer
PostgreSQL
Qdrant
Phase 5
React Frontend
Phase 6
Docker Deployment
Cloud Hosting
👨‍💻 Author

Marree Jachaak

AI Engineer | Risk Management Professional | Agentic AI Builder

📜 License

MIT License
