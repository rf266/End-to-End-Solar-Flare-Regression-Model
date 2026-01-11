from fastapi import FastAPI
import uvicorn
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel): 
    activity: int
    evol: int
    prev24: int
    hist: int
    complex: int
    area: int
    area_largest: int 
    zurich_b: bool
    zurich_c: bool
    zurich_d: bool
    zurich_e: bool
    zurich_f: bool
    zurich_h: bool
    spot_size_a :bool
    spot_size_h:bool
    spot_size_k :bool
    spot_size_r :bool
    spot_size_s :bool
    spot_size_x :bool   
    spot_dist_c :bool
    spot_dist_i : bool
    spot_dist_o :bool
    spot_dist_x :bool

@app.post("/predict")
def predict(data:Input):
    model = joblib.load("ridge_regression_solar.pkl")
    newdf = pd.DataFrame(data) 
    prediction = model.predict(newdf)
    return prediction[0] 