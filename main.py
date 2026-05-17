from fastapi import FastAPI, Path
import json

app = FastAPI()

#help functions

def load_data():
    with open ('cilent.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return {"message" : "banking Transcation API"}

@app.get("/about")
def about():
    return {"message" : "project is about to develop a backend fastapi of banking transcation"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/cilent/{account_id}")
def view_account(account_id : str = Path(..., description = "id of the cilent account", example = "ACC001")):
    data = load_data()

    if account_id in data:
        return data[account_id]
    return {"error" : "account_not_found"}


