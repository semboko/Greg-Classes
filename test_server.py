from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from uvicorn import run
from secrets import token_hex
from datetime import datetime
from contextlib import asynccontextmanager
from os import listdir
import pickle

users = {}
tokens = {}
favorites = {}
chats = {}


def init_file(filename: str) -> None:
    if filename not in listdir("data"):
        try:
            file = open("data/" + filename, "wb")
            file.write(pickle.dumps({}))
        finally:
            file.close()


def load_file(filename: str) -> dict:
    try:
        file = open("./data/" + filename, "rb")
        data = pickle.loads(file.read())
    finally:
        file.close()
    return data


def save_file(filename: str, obj: dict) -> None:
    try:
        file = open("./data/" + filename, "wb")
        file.write(pickle.dumps(obj))
    finally:
        file.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # On StartUp
    init_file("users.bin")
    init_file("tokens.bin")
    init_file("favorites.bin")
    init_file("chats.bin")

    global users, tokens, favorites, chats
    users = load_file("users.bin")
    tokens = load_file("tokens.bin")
    favorites = load_file("favorites.bin")
    chats = load_file("chats.bin")

    yield

    # On ShudDown
    save_file("users.bin", users)
    save_file("tokens.bin", tokens)
    save_file("favorites.bin", favorites)
    save_file("chats.bin", chats)


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")


# Dependency 1
def get_user(token: str) -> str:
    if token not in tokens:
        raise HTTPException(status_code=400)
    return tokens[token]


@app.get("/user/signup")
def signup(username: str, password: str) -> str:
    if username in users:
        raise HTTPException(status_code=400)
    users[username] = password
    favorites[username] = []
    return "OK"


@app.get("/user/signin")
def signin(username: str, password: str) -> str:
    if username not in users:
        raise HTTPException(status_code=400)
    saved_password = users[username]
    if password != saved_password:
        raise HTTPException(status_code=400)
    token = token_hex(16)
    tokens[token] = username
    return token


@app.get("/user/search")
def search(prefix: str, username: str = Depends(get_user)):
    if len(prefix) < 3:
        return []

    result = []
    for username in users.keys():
        if prefix in username:
            result.append(username)

    return result


@app.get("/favorite/add")
def add_to_favorites(favorite_name: str, username: str = Depends(get_user)):
    favorites[username].append(favorite_name)
    pair = frozenset((username, favorite_name))
    chats[pair] = []


@app.get("/favorite/list")
def get_list_of_favorites(username: str = Depends(get_user)):
    friends = favorites[username]
    result = []
    for f in friends:
        result.append(
            {
                "imgLink": "https://i.pravatar.cc/100?id=2",
                "time": "5:11PM",
                "username": f,
                "lastMsg": "This is the last message",
                "counter": "1",
            }
        )
    return result


@app.get("/chat")
def get_messages(favorite_name: str, username: str = Depends(get_user)):
    pair = frozenset((username, favorite_name))
    return {
        "username": favorite_name,
        "lastVisit": "1727227400",
        "messages": chats[pair],
    }


@app.get("/chat/send")
def send_message(
    favorite_name: str, message_body: str, username: str = Depends(get_user)
):
    pair = frozenset((username, favorite_name))
    chats[pair].append(
        {
            "text": message_body,
            "time": int(datetime.now().timestamp()),
            "author": username,
        }
    )


run(app)
