# Day03 Learning

1.git account creation
2. ssh key creation
3. git clone
4. git private and public key
5. git add .
6. git commit
7. git push
8. use ollama model
9. getting response for the message 
10. import pprint 

```python
from ollama import chat
from pprint import pprint

messages = [
    {
        "role": "user",
        "content": "What is AI?"
    }
]

response = chat(
    model="llama3.1",
    messages=messages
)

print(response.message.content)
pprint(response.model_dump())
'''