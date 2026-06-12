from ollama import chat
#from pprint import pprint

messages = [
    {
        "role": "system",
        "content": "you are a cricket expert and reply should be less than 15 word"
    },
    {
        "role": "user",
        "content": "What is the best shot to play when a bouncer is coming?"
    }
]

response = chat(
    model="llama3.2:latest",
    messages=messages,
    stream=True
)
for chunk in response:
    print(chunk.message.content,end=" ",flush = True)

#print(response.message.content)
#pprint(response.model_dump())