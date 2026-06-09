from services.qwen_service import ask_qwen


def research_agent(query: str):

    print("Research agent called")

    prompt = f"""
You are a Research Agent.

Research the following topic:

{query}

Provide:
1. Background
2. Key Findings
3. Opportunities
4. Risks
"""

    return ask_qwen(prompt)

