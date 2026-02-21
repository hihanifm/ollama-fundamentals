from ollama._client import Client

_client = Client()
print(_client.list())

res = _client.chat(
    # model="llama3.2",
    messages=[
        {"role": "user", "content": "why is the sky blue?"},
    ],
)
print(res["message"]["content"])