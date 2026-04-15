from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)   # ✅ FIRST create app
CORS(app)               # ✅ THEN apply CORS

@app.route("/")
def home():
    return "AI SmartLab Backend Running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]
    df = pd.read_csv(file)

    numeric = df.select_dtypes(include='number')

    result = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "columns_list": df.columns.tolist(),
        "missing": df.isnull().sum().to_dict(),
        "correlation": numeric.corr().fillna(0).to_dict()
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run()
