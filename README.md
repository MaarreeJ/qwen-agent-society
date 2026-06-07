<div align="center">
🤖 Qwen Agent Society
AI-Powered Multi-Agent Enterprise Operations Platform
Built with FastAPI, LangGraph, Agentic AI, React, PostgreSQL, and Vector Databases.
Python
FastAPI
LangGraph
React
License
</div>
🚀 Overview
Qwen Agent Society is an enterprise-grade multi-agent AI platform designed to automate business
operations through intelligent agent collaboration.
The platform uses a Supervisor Agent to coordinate specialized agents responsible for research,
finance, compliance, memory management, validation, and workflow orchestration.
The architecture follows an Agentic AI pattern powered by LangGraph and FastAPI, enabling scalable
enterprise decision-support systems.
🎯 Problem Statement
Modern enterprises face challenges in:
•
•
•
•
Information overload
Manual research processes
Compliance verification
Financial analysis
1
•
•
Knowledge management
Workflow automation
Qwen Agent Society addresses these challenges by orchestrating multiple AI agents that collaborate to
solve complex business tasks.
🏗️ System Architecture
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
│
▼
├── Research Agent
├── Finance Agent
├── Compliance Agent
├── Memory Agent
└── Validator Agent
LangGraph Workflow Engine
│
▼
LLM Provider
(OpenAI / Groq / Qwen / Ollama)
│
▼
Response Generation
✨ Features
Multi-Agent System
•
•
•
•
•
•
Supervisor Agent
Research Agent
Finance Agent
Compliance Agent
Validator Agent
Memory Agent
2
Enterprise Workflow Automation
•
•
•
•
•
Task decomposition
Agent routing
Decision support
Automated validation
Workflow orchestration
Knowledge Management
•
•
•
•
Long-term memory
Vector search
Retrieval-Augmented Generation (RAG)
Semantic search
API-Driven Architecture
•
•
•
•
FastAPI backend
REST APIs
Swagger documentation
Modular architecture
Frontend
•
•
•
•
React
Vite
TypeScript
Tailwind CSS
📂 Project Structure
qwen-agent-society/
│
├── backend/
│ ├── agents/
│ ├── api/
│ ├── config/
│ ├── database/
│ ├── graph/
│ ├── memory/
│ ├── models/
│ ├── schemas/
│ ├── services/
│ ├── tests/
│ ├── tools/
│ ├── main.py
│ └── requirements.txt
3
│
│
├── frontend/
│ ├── src/
│ ├── package.json
│ ├── vite.config.ts
│ └── tailwind.config.js
├── docs/
├── deployment/
├── demo/
├── README.md
└── LICENSE
🧠 Agent Responsibilities
Supervisor Agent
•
•
Receives user requests
Breaks tasks into subtasks
•
•
Assigns work to specialized agents
Consolidates responses
Research Agent
•
•
•
Information gathering
Knowledge extraction
Data summarization
Finance Agent
•
•
•
Financial analysis
Risk assessment
Business metrics evaluation
Compliance Agent
•
•
•
Policy verification
Regulatory checks
Governance validation
Validator Agent
•
•
•
Response verification
Output quality assurance
Hallucination reduction
4
Memory Agent
•
•
•
Long-term memory management
Retrieval operations
Context preservation
⚙️ Technology Stack
Backend
•
•
•
•
•
Python
FastAPI
LangGraph
LangChain
Pydantic
AI Models
•
•
•
•
OpenAI
Groq
Qwen
Ollama
Databases
•
•
PostgreSQL
Qdrant
Frontend
•
•
•
•
React
TypeScript
Vite
Tailwind CSS
Deployment
•
•
•
Docker
Nginx
Alibaba Cloud
5
🚀 Local Setup
Clone Repository
git clone https://github.com/MaarreeJ/qwen-agent-society.git
cd qwen-agent-society
Backend Setup
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Create .env
OPENAI_API_KEY=your_key_here
Start FastAPI
uvicorn main:app --reload
API Documentation
http://127.0.0.1:8000/docs
Frontend Setup
cd frontend
npm install
npm run dev
6
📈 Roadmap
Phase 1
•
•
•
FastAPI Backend
API Endpoints
Swagger Integration
Phase 2
•
•
•
•
Phase 3
Multi-Agent Framework
Supervisor Agent
Research Agent
Finance Agent
•
•
•
LangGraph Integration
Agent Routing
State Management
Phase 4
•
•
•
Memory Layer
PostgreSQL
Qdrant
Phase 5
•
•
React Dashboard
Enterprise UI
Phase 6
•
•
Docker Deployment
Cloud Hosting
🧪 Current Status
Completed
•
•
•
•
•
•
Project Structure
FastAPI Backend
Swagger Documentation
GitHub Integration
Supervisor Agent
OpenAI Service Layer
7
In Progress
•
•
•
LangGraph Workflow
Agent Collaboration
Memory Layer
Planned
•
•
•
Full RAG Integration
Human-in-the-Loop Approval
Enterprise Dashboard
👨‍💻 Author
Marree Jachaak
AI Engineer | Risk Management Professional | Agentic AI Builder
GitHub: https://github.com/MaarreeJ
📜 License
MIT License
