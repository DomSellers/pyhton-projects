from groq import Groq

client = Groq(api_key="")

messages = []
def ask_groq(prompt):
    messages.append({"role": "user", "content": prompt})

    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt} # edit: make the AI respond to a prompt
        ]
    )

    return response.choices[0].message.content

print(ask_groq("Ask me how I am and initate the conversation"))  #edit: edit print statement to initiate the upcoming conversation loop by asking user how they are. 

#edit: adding loop to be able to talk to the chatbot
while True:
    user_input = input("💬: ") #creating a variable to store user inputs for the prompt

    if user_input.lower() == "exit": #if statement to break loop if user types exit"
        print("Goodbye!")
        break


    reply = ask_groq(user_input)
    print("AI:", reply,"\n")
    
