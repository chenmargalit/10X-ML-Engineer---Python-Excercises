from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

mdl = joblib.load('knn.joblib')


#
#
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# class Item(BaseModel):
#     item_to_predict: list


#
#
# class Items(BaseModel):
#     items_to_predict: list[list[float]]
app = FastAPI()


# GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to INT DS course"}


# POST endpoint
@app.post("/item")
def create_item(item: Item):
    return f'request received for item {item.name}'


@app.post('/return_pred/')
def return_mdl_request(item: Item):
    feature = np.array(item.item_to_predict)
    pred = mdl.predict([feature])
    res = int(pred[0])
    return res


@app.post('/return_batch_pred/')
def return_mdl_request(items: Items):
    batch = np.array(items.items_to_predict)
    preds = mdl.predict(batch)
    return preds.tolist()
