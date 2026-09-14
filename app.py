from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("crop_model.pkl")


crop_info = {
    "rice": "Rice generally requires warm conditions and adequate water availability.",
    "maize": "Maize grows well in warm conditions with suitable soil moisture.",
    "chickpea": "Chickpea is generally suitable for relatively dry and cool growing conditions.",
    "kidneybeans": "Kidney beans require moderate temperature and suitable soil moisture.",
    "pigeonpeas": "Pigeon pea is a warm-season crop and can tolerate relatively dry conditions.",
    "mothbeans": "Moth bean is a drought-tolerant crop suitable for warm and dry conditions.",
    "mungbean": "Mung bean is a short-duration crop that grows well in warm conditions.",
    "blackgram": "Black gram generally grows well in warm and humid conditions.",
    "lentil": "Lentil is generally grown in cooler conditions with moderate moisture.",
    "pomegranate": "Pomegranate prefers warm and relatively dry climatic conditions.",
    "banana": "Banana requires warm temperatures, good moisture and fertile soil.",
    "mango": "Mango grows well in warm climates and requires suitable soil conditions.",
    "grapes": "Grapes generally require a warm climate and well-drained soil.",
    "watermelon": "Watermelon prefers warm conditions and adequate soil moisture.",
    "muskmelon": "Muskmelon grows well in warm conditions with suitable moisture.",
    "apple": "Apple generally requires cooler climatic conditions.",
    "orange": "Orange grows well in warm subtropical conditions with suitable soil moisture.",
    "papaya": "Papaya prefers warm temperatures and well-drained fertile soil.",
    "coconut": "Coconut generally requires a warm, humid climate and good water availability.",
    "cotton": "Cotton prefers warm conditions with suitable soil moisture.",
    "jute": "Jute generally requires warm and humid conditions with adequate rainfall.",
    "coffee": "Coffee generally grows well in warm, humid conditions with suitable rainfall."
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    input_data = [[
        N, P, K, temperature, humidity, ph, rainfall
    ]]

    # Prediction
    prediction = model.predict(input_data)[0]

    # Prediction probability
    probabilities = model.predict_proba(input_data)[0]
    confidence = round(max(probabilities) * 100, 2)

    information = crop_info.get(
        prediction,
        "No additional information available."
    )

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        information=information
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)