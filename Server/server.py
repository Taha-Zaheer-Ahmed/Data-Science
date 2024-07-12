from flask import Flask, request, jsonify
import util
import warnings

app = Flask(__name__)


@app.route("/get_location_names")
def get_location_names():

    respone = jsonify({"locations": util.get_location_names()})

    respone.headers.add("Access-Control-Allow-Origin", "*")

    return respone


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify(
        {"estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)}
    )

    return response


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    print("Starting Flask server for project...")
    util.load_saved_artifacts()
    app.run()
