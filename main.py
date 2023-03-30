import openai
import os

# Set up the OpenAI API
openai.api_key = "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"


def chat_with_gpt(prompt):
  # Set up the API call parameters
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"{prompt}\n\n- ChatGPT:",
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
  )

  # Extract and return the response
  response = completions.choices[0].text.strip()
  return response


if __name__ == "__main__":
  print("Welcome to the ChatGPT conversation! (Type 'exit' to quit)")

  while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
      break

    response = chat_with_gpt(user_input)
    print(f"ChatGPT: {response}")
