from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


def ask_qwen(prompt: str) -> str:

    try:

        response = client.chat.completions.create(
            model="qwen3:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Qwen Error: {str(e)}"