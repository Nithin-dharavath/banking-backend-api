from fastapi import FastAPI, Path, HTTPException, Query
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
def view_account(account_id : str = Path(..., description = "id of the cilent account", examples = "ACC001")):
    data = load_data()

    if account_id in data:
        return data[account_id]
    raise HTTPException(status_code = 404, description = "data not found")


@app.get("/sort")
def sort_accounts(sort_by : str = Query(..., description = "sort on bias of age, account_type or account_status"), order: str = Query("asc", description = "sort in asc or desc order")):

    valid_fields = ["age", "account_type", "account_status"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, description = "invalid fields select from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code = 400, description = "select asc or desc")

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=False)

    return sorted_data
