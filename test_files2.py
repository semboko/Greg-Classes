import json
import pickle


users = {
    "fake1": "password1",
    "fake2": "password2",
}

chats = {
    frozenset(["fake1", "fake2"]): [
        {"author": "fake1", "message": "asdfasdfasdf"},
        {"author": "fake1", "message": "asdfasdfasdf"},
        {"author": "fake1", "message": "asdfasdfasdf"},
    ]
}

data = open("data.txt", "wb")
data.write(pickle.dumps(chats))
data.close()


data = open("data.txt", "rb")
chats = pickle.loads(data.read())
print(chats)
data.close()
