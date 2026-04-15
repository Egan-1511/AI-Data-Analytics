from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI SmartLab Backend Running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        df = pd.read_csv(file)

        numeric = df.select_dtypes(include='number')

        result = {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "columns_list": df.columns.tolist(),
            "missing": df.isnull().sum().to_dict(),
            "correlation": numeric.corr().fillna(0).to_dict()
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
