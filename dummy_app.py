import requests
root = "http://127.0.0.1:8000/"

test_dict = {
    "item_id": 5,
    "q": "test"
}
params={"q": "test"}
path = f"items/{test_dict['item_id']}"

req = requests.get(url=f"{root}{path}", params=params)
data = req.json()

print(data)
print(type(data))
##### Rebuilding Quizzer main interface in dummy_app: