from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def query_llm(prompt):
    response = client.chat.completions.create(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def plan_steps(goal):
    prompt = f"Break down the following goal into 2–3 clear steps: {goal}"
    return query_llm(prompt)
