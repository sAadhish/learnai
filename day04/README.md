# Day04 learnings
1. Created csv , json, xml files
2. xml and json format
3. json different format -> normal to complex
4. specifing role to model
5. System , user, assistant are different roles 
6. changing prompt accordingly to get more accurate answers
7. llama3.2:latest is more faster
8. How chatgpt answer for unknown data 
9. how model answer after specifing the context
10. message format

```python
from ollama import chat
from pprint import pprint

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
    messages=messages
)

print(response.message.content)
pprint(response.model_dump())
'''

