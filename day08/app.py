import chromadb
from pprint import pprint

client=chromadb.PersistentClient("./chroma_db")
collection=client.get_or_create_collection("documents_notes")

'''
collection.add(
    documents=[
        # Cricket
        "Sachin Tendulkar is one of the greatest cricketers in history.",
        "Virat Kohli has scored many centuries for India.",
        "MS Dhoni is known for his calm captaincy and finishing abilities.",

        # Football
        "Lionel Messi won multiple Ballon d'Or awards.",
        "Cristiano Ronaldo is one of the highest goal scorers in football.",
        "Kylian Mbappe is a French football superstar.",

        # Technology
        "Python is a popular programming language for AI and data science.",
        "Java is widely used in enterprise software development.",
        "Docker helps developers package applications into containers.",
        "Kubernetes is used to orchestrate containerized applications.",

        # AI
        "Machine learning enables computers to learn from data.",
        "Deep learning uses neural networks with many layers.",
        "Large language models can generate human-like text.",
        "Vector databases store embeddings for semantic search.",

        # Movies
        "Interstellar is a science fiction movie directed by Christopher Nolan.",
        "The Dark Knight features Batman and the Joker.",
        "Avatar became one of the highest grossing films ever.",

        # Space
        "NASA launched the James Webb Space Telescope.",
        "Mars is often called the Red Planet.",
        "The Moon is Earth's natural satellite.",

        # Animals
        "Tigers are powerful big cats found in Asia.",
        "Elephants are the largest land animals.",
        "Dolphins are intelligent marine mammals.",

        # Food
        "Pizza is one of the most popular foods worldwide.",
        "Biryani is a famous rice dish from the Indian subcontinent.",
        "Mango is known as the king of fruits.",

        # Business
        "Apple develops the iPhone and Mac computers.",
        "Google operates the world's largest search engine.",
        "Microsoft created the Windows operating system."
    ],
    ids=[str(i) for i in range(1, 30)]
)
'''
#pprint(collection.count())

data=collection.get(include=["documents","embeddings"])
for i in range(len(data["ids"])):
    print("\nID:", data["ids"][i])
    print("Embedding Size:", len(data["embeddings"][i]))
    print("Embedding : ",data["embeddings"][i])

result=collection.query(query_texts="top football players",n_results=3)
pprint(result)