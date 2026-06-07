from services.qwen_service import ask_qwen


def supervisor_agent(user_query: str):

    prompt = f"""
You are the Supervisor Agent in a multi-agent system.

Analyze the user request.

Create:

1. Research Tasks
2. Finance Tasks
3. Compliance Tasks

User Request:
{user_query}

Return:

- Summary
- Task Breakdown
- Recommended Agent Workflow
"""

    return ask_qwen(prompt)