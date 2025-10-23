import os
import pickle

model_path = os.path.join("model", "xgb_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)
