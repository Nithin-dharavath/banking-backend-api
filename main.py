from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Dict, List, Annotated, Literal
from pydantic import BaseModel, Field
import json


app = FastAPI()

#data validation

class Transaction(BaseModel):

    txn_id: Annotated[str, Field(..., example="TXN1001")]
    
    type: Annotated[
        Literal["deposit", "withdraw", "transfer"],
        Field(..., example="deposit")
    ]

    amount: Annotated[
        float,
        Field(..., gt=0, example=10000)
    ]

    status: Annotated[
        Literal["success", "failed", "pending"],
        Field(..., example="success")
    ]


class Acc_Holder(BaseModel):

    id: Annotated[str, Field(..., example="ACC001")]
    name: Annotated[str, Field(..., example="Rahul Sharma")]
    city: Annotated[str, Field(..., example="Hyderabad")]
    age: Annotated[int, Field(..., gt=0, lt=120, example=32)]
    gender: Annotated[Literal["male", "female", "others"], Field(..., example="male")]
    account_type: Annotated[str, Field(..., example="savings")]
    balance: Annotated[float, Field(..., example=45000.75)]
    currency: Annotated[str, Field(..., example="INR")]
    account_status: Annotated[str, Field(..., example="active")]

    transactions: Annotated[
        List[Transaction],
        Field(..., description="transaction details")
    ]

#help functions

def load_data():
    with open ('cilent.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("cilent.json", "w") as f:
        json.dump(data, f)

#rotues

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
    raise HTTPException(status_code = 404, detail = "data not found")


@app.get("/sort")
def sort_accounts(sort_by : str = Query(..., description = "sort on bias of age, account_type or account_status"), order: str = Query("asc", description = "sort in asc or desc order")):

    valid_Fields = ["age", "account_type", "account_status"]

    if sort_by not in valid_Fields:
        raise HTTPException(status_code = 400, detail = "invalid Fields select from {valid_Fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code = 400, detail = "select asc or desc")

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=False)

    return sorted_data


@app.post("/create")
def create_new_customer(account_holder : Acc_Holder):

    data = load_data()

    if account_holder.id in data:
        raise HTTPException(status_code = 400, detail = "user already exists")

    data[account_holder.id] = account_holder.model_dump(exclude=["id"])

    save_data(data)

    return JSONResponse(status_code = 201, content = {"message" : "new customer cteated"})