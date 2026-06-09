from openai import OpenAI
import time

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def ask_qwen(prompt: str):

    try:

        print("Calling Qwen...")

        start = time.time()

        response = client.chat.completions.create(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
        )

        end = time.time()

        print(f"Qwen completed in {end-start:.2f} seconds")

        return response.choices[0].message.content

    except Exception as e:

        return f"Qwen Error: {str(e)}"