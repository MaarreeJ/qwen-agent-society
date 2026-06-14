from graph.workflow import run_graph


def run_workflow(
    query,
    context=""
):

    print("Running LangGraph Workflow")

    return run_graph(
        query=query,
        context=context
    )