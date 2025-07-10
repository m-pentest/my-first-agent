from planner import plan_steps, query_llm
from tools import search_tool

def run_agent(goal):
    print("Planning steps...")
    steps = plan_steps(goal)
    print("\nPlanned Steps:\n", steps)

    print("\nRunning tool on step 1...")
    result = search_tool(goal)
    print("\nTool Result:\n", result)

    print("\nSummarizing response...")
    summary_prompt = f"Using this result, summarize a final answer to: {goal}\n\n{result}"
    final_answer = query_llm(summary_prompt)
    print("\nFinal Answer:\n", final_answer)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        user_goal = " ".join(sys.argv[1:])
    else:
        user_goal = input("Enter a goal for the agent: ")
    run_agent(user_goal)
