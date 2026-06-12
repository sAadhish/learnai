'''def conversation(message):
    return message

def conversationfancy():
    #return "Hi i am aadhish"
    yield "I am Aadhish"
    yield "This is gud"
    yield "This is from chennai"

message_stream=conversationfancy()
print(next(message_stream))
print(next(message_stream))
print(next(message_stream))
 
conversations= [
["hi","hi"],
["how r u" ,"i am fine and what about you"],
["i am gud , bye","Bye"]
]


def displayconversation(conversations):
    for msg1,msg2 in conversations:
        print("Prabhu :" , msg1)
        print("Aadhish :" , msg2)

displayconversation(conversations)
  '''

messages=[]
message={"role":"Prabhu","content":"hi"}
messages.append(message)
message={"role":"Aadhish","content":"hi"}
messages.append(message)
message={"role":"Prabhu","content":"how are you"}
messages.append(message)
message={"role":"Aadhish","content":"doing good"}
messages.append(message)

def display_message(messages):
    for message in messages:
        print(f"{message.get('role')} : {message.get('content')}")

display_message(messages)