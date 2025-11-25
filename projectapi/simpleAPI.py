from groq import Groq

client = Groq(api_key="")


def ask_groq(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Hello! Who are you?"}
        ]
    )

    return response.choices[0].message.content

print(ask_groq("Hello! Who are you?"))
