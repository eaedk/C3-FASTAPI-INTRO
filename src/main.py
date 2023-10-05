from typing import Union
import pandas as pd
import numpy as np
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/maths/") # {val_01}/{val_02}/{operator}
def calculator(val_01: float, val_02: float, operator):
    """API's endpoint to do simple math operations 
    """

    operator = operator.lower().strip() # operator cleaning
    op = ""
    if operator.lower().strip() == "add":
        result = val_01 + val_02
        op = "+"
    elif operator == "sub":
        result = val_01 - val_02
        op = "-"
    elif operator == "":
        pass
    elif operator == "":
        pass
    
    return {"value_A": val_01, "value_b": val_02,
            "string": f"{val_01} {op} {val_02} = {result}" ,  
            "result":result}

# Predict endpoint
@app.get("/inference")
def predict(age, gender, height, ):
    """
    """

    # Prepare the features and structure them like in the notebook
    df = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "height of father": [height], 
    })

    print(f"\n\n[Info] The initial and raw df: \n{df.to_markdown()}\n\n")

    # Features preprocessing and creation

    # df_scaled = scaler.transform(df[numerical_features])
    # df_encoded = encoder.transform(df[categorical_features])
    # df_cleaned = pd.concat([df_scaled ,df_encoded], axis=1)

    # Prediction
    # raw_prediction = model.predict(df_cleaned)

    # Format the prediction to send the API's Response
    output = {
        "features" : {
                    "age": age,
                    "gender": gender,
                    "height of father": height, 
                    },
        "df": df, # Pandas is now automatically converted, no more error 
        # "array": np.array([1, 2, 3]), # Numpy arrays raise an error
        "array": np.array([1, 2, 3]).tolist(),
    }
    return output

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)