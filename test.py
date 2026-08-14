import os
from openai import OpenAI

# Initialize client using NVIDIA's base URL
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY", "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")  # Fallback to string if env var isn't set
)

# 1. Capture user input from the console
user_prompt = input("Ask the AI something: ")

# 2. Pass user_prompt into the 'content' field
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.7,
    top_p=1,
    max_tokens=4096,
    stream=False
)

# 3. Print the output
reasoning = getattr(completion.choices[0].message, "reasoning_content", None)
if reasoning:
    print("\n--- Model Reasoning ---")
    print(reasoning)

print("\n--- Response ---")
print(completion.choices[0].message.content)
