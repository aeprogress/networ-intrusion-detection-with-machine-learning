import json
from fastapi import Depends, FastAPI
from classifier.model import Model, get_model
import json
app = FastAPI()


@app.post("/predict")
async def predict(data: list, model: Model = Depends(get_model)):
    results = model.predict(data=data)
    return {results}
