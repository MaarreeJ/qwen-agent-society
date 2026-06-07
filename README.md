🤖 Qwen Agent Society
AI-Powered Multi-Agent Enterprise Operations Platform
Built with FastAPI, LangGraph, Agentic AI, Ollama, Qwen3, PostgreSQL, and Vector Databases.
🚀 Overview
Qwen Agent Society is an enterprise-grade multi-agent AI platform designed to automate business
operations through intelligent agent collaboration.
The platform uses a Supervisor Agent to coordinate specialized agents responsible for:
•
•
•
•
•
•
Research
Finance
Compliance
Memory Management
Validation
Workflow Orchestration
The architecture follows an Agentic AI pattern powered by LangGraph and FastAPI, enabling scalable
enterprise decision-support systems.
🎯 Problem Statement
Modern enterprises face challenges such as:
•
•
•
•
•
•
Information overload
Manual research processes
Compliance verification
Financial analysis
Knowledge management
Workflow automation
Qwen Agent Society addresses these challenges through a collaborative multi-agent framework.
🏗️ System Architecture
User
│
▼
React Frontend
│
▼
1
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
Qwen3 / Ollama
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
Semantic retrieval
RAG architecture
API-Driven Architecture
•
FastAPI backend
2
•
•
•
REST APIs
Swagger documentation
Modular architecture
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
│
├── frontend/
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
Assigns work to agents
Consolidates results
Research Agent
•
•
•
Information gathering
Knowledge extraction
Data summarization
3
Finance Agent
•
•
•
Financial analysis
Risk assessment
Business metric evaluation
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
Quality assurance
Hallucination reduction
Memory Agent
•
•
•
Long-term memory
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
Qwen3
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
4
Deployment
•
•
•
Docker
Nginx
Alibaba Cloud
🚀 Local Setup
Clone Repository
git clone https://github.com/MaarreeJ/qwen-agent-society.git
cd qwen-agent-society
Backend Setup
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Run FastAPI
uvicorn main:app --reload
Swagger
http://127.0.0.1:8000/docs
📈 Roadmap
Phase 1
•
•
•
Phase 2
•
•
•
FastAPI Backend
API Endpoints
Swagger Integration
Supervisor Agent
Research Agent
Finance Agent
5
•
Compliance Agent
Phase 3
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
React Dashboard
Phase 6
•
•
Docker Deployment
Alibaba Cloud Deployment
🧪 Current Status
Completed
•
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
Ollama Integration
Qwen3 Integration
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
6
AI Engineer | Risk Management Professional | Agentic AI Builder
GitHub: https://github.com/MaarreeJ
📜 License
MIT License
7

