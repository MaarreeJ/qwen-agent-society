
from memory.memory_manager import save_memory
from typing import TypedDict

from langgraph.graph import StateGraph

from agents.research import research_agent
from agents.finance import finance_agent
from agents.compliance import compliance_agent
from agents.validator import validator_agent


class AgentState(TypedDict):
    query: str
    research: str
    finance: dict
    compliance: dict
    validation: dict


# ----------------------
# Nodes
# ----------------------

def research_node(state):

    print("Research Node")

    state["research"] = research_agent(
        state["query"]
    )

    save_memory(
        "demo_user",
        "last_research",
        state["research"]
    )

    print("Memory Saved")

    return state


def finance_node(state):

    print("Finance Node")

    state["finance"] = finance_agent(
        state["research"]
    )

    return state


def compliance_node(state):

    print("Compliance Node")

    state["compliance"] = compliance_agent(
        state["research"]
    )

    return state


def validator_node(state):

    print("Validator Node")

    state["validation"] = validator_agent(
        state["research"],
        state["finance"],
        state["compliance"]
    )

    return state


# ----------------------
# Graph
# ----------------------

builder = StateGraph(AgentState)

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "finance",
    finance_node
)

builder.add_node(
    "compliance",
    compliance_node
)

builder.add_node(
    "validator",
    validator_node
)

builder.set_entry_point("research")

builder.add_edge(
    "research",
    "finance"
)

builder.add_edge(
    "finance",
    "compliance"
)

builder.add_edge(
    "compliance",
    "validator"
)

graph = builder.compile()


def run_graph(query):

    state = {
        "query": query,
        "research": "",
        "finance": {},
        "compliance": {},
        "validation": {}
    }

    return graph.invoke(state)