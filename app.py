from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained machine learning model
model = joblib.load("crop_model.pkl")


# =========================================================
# CROP INFORMATION - ENGLISH
# =========================================================

crop_info_en = {
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


# =========================================================
# CROP INFORMATION - HINDI
# =========================================================

crop_info_hi = {
    "rice": "चावल की फसल के लिए सामान्यतः गर्म मौसम और पर्याप्त पानी की आवश्यकता होती है।",
    "maize": "मक्का गर्म परिस्थितियों और उचित मिट्टी की नमी में अच्छी तरह उगता है।",
    "chickpea": "चना सामान्यतः ठंडी और अपेक्षाकृत शुष्क परिस्थितियों के लिए उपयुक्त होता है।",
    "kidneybeans": "राजमा के लिए मध्यम तापमान और उचित मिट्टी की नमी आवश्यक होती है।",
    "pigeonpeas": "अरहर गर्म मौसम की फसल है और अपेक्षाकृत सूखी परिस्थितियों को सहन कर सकती है।",
    "mothbeans": "मोठ एक सूखा-सहिष्णु फसल है जो गर्म और शुष्क परिस्थितियों में उगाई जा सकती है।",
    "mungbean": "मूंग कम अवधि की फसल है जो गर्म परिस्थितियों में अच्छी तरह उगती है।",
    "blackgram": "उड़द सामान्यतः गर्म और नम परिस्थितियों में अच्छी तरह उगती है।",
    "lentil": "मसूर सामान्यतः ठंडी परिस्थितियों और मध्यम नमी में उगाई जाती है।",
    "pomegranate": "अनार गर्म और अपेक्षाकृत शुष्क जलवायु को पसंद करता है।",
    "banana": "केले के लिए गर्म तापमान, पर्याप्त नमी और उपजाऊ मिट्टी की आवश्यकता होती है।",
    "mango": "आम गर्म जलवायु में अच्छी तरह उगता है और उचित मिट्टी की स्थिति आवश्यक होती है।",
    "grapes": "अंगूर के लिए गर्म जलवायु और अच्छी जल निकासी वाली मिट्टी उपयुक्त होती है।",
    "watermelon": "तरबूज गर्म परिस्थितियों और पर्याप्त मिट्टी की नमी को पसंद करता है।",
    "muskmelon": "खरबूजा गर्म परिस्थितियों और उचित नमी में अच्छी तरह उगता है।",
    "apple": "सेब की फसल के लिए सामान्यतः ठंडी जलवायु की आवश्यकता होती है।",
    "orange": "संतरा गर्म उपोष्णकटिबंधीय परिस्थितियों और उचित मिट्टी की नमी में अच्छी तरह उगता है।",
    "papaya": "पपीता गर्म तापमान और अच्छी जल निकासी वाली उपजाऊ मिट्टी को पसंद करता है।",
    "coconut": "नारियल के लिए गर्म और नम जलवायु तथा पर्याप्त पानी की आवश्यकता होती है।",
    "cotton": "कपास गर्म परिस्थितियों और उचित मिट्टी की नमी को पसंद करता है।",
    "jute": "जूट के लिए गर्म और नम परिस्थितियों तथा पर्याप्त वर्षा की आवश्यकता होती है।",
    "coffee": "कॉफी गर्म और नम परिस्थितियों तथा उचित वर्षा में अच्छी तरह उगती है।"
}


# =========================================================
# FERTILIZER GUIDANCE - ENGLISH
# =========================================================

fertilizer_info_en = {
    "rice": "Balanced NPK fertilizer is generally used for rice. Nitrogen is particularly important.",
    "maize": "Maize generally requires good nitrogen availability along with balanced NPK nutrients.",
    "chickpea": "Chickpea generally benefits from adequate phosphorus and potassium.",
    "kidneybeans": "Kidney beans generally benefit from balanced nutrients, especially phosphorus.",
    "pigeonpeas": "Pigeon pea generally benefits from adequate phosphorus and potassium.",
    "mothbeans": "Moth bean benefits from balanced fertilizer and proper soil nutrient management.",
    "mungbean": "Mung bean generally benefits from adequate phosphorus and potassium.",
    "blackgram": "Black gram benefits from balanced NPK and suitable phosphorus management.",
    "lentil": "Lentil generally benefits from adequate phosphorus and potassium.",
    "pomegranate": "Pomegranate can benefit from balanced NPK and organic manure.",
    "banana": "Banana generally requires good nitrogen and potassium availability.",
    "mango": "Mango can benefit from balanced NPK and organic manure.",
    "grapes": "Grapes require balanced nitrogen, phosphorus and potassium management.",
    "watermelon": "Watermelon benefits from balanced NPK with suitable potassium management.",
    "muskmelon": "Muskmelon benefits from balanced nutrients and adequate potassium.",
    "apple": "Apple generally benefits from balanced NPK and organic manure.",
    "orange": "Orange can benefit from balanced NPK and organic manure.",
    "papaya": "Papaya benefits from balanced nutrients including nitrogen and potassium.",
    "coconut": "Coconut requires balanced nutrient management including nitrogen and potassium.",
    "cotton": "Cotton benefits from balanced nitrogen, phosphorus and potassium.",
    "jute": "Jute generally requires good nitrogen availability with balanced NPK management.",
    "coffee": "Coffee benefits from balanced nitrogen, phosphorus and potassium management."
}


# =========================================================
# FERTILIZER GUIDANCE - HINDI
# =========================================================

fertilizer_info_hi = {
    "rice": "चावल में सामान्यतः संतुलित NPK fertilizer का उपयोग किया जाता है। Nitrogen विशेष रूप से महत्वपूर्ण है।",
    "maize": "मक्का में सामान्यतः Nitrogen की अच्छी उपलब्धता और संतुलित NPK nutrients आवश्यक होते हैं।",
    "chickpea": "चना में पर्याप्त Phosphorus और Potassium उपयोगी होते हैं।",
    "kidneybeans": "राजमा में balanced nutrients, विशेष रूप से Phosphorus, उपयोगी होता है।",
    "pigeonpeas": "अरहर में पर्याप्त Phosphorus और Potassium उपयोगी होते हैं।",
    "mothbeans": "मोठ में balanced fertilizer और उचित soil nutrient management उपयोगी है।",
    "mungbean": "मूंग में पर्याप्त Phosphorus और Potassium उपयोगी होते हैं।",
    "blackgram": "उड़द में balanced NPK और उचित Phosphorus management उपयोगी है।",
    "lentil": "मसूर में पर्याप्त Phosphorus और Potassium उपयोगी होते हैं।",
    "pomegranate": "अनार में balanced NPK और organic manure उपयोगी हो सकते हैं।",
    "banana": "केले में Nitrogen और Potassium की अच्छी उपलब्धता सामान्यतः आवश्यक होती है।",
    "mango": "आम में balanced NPK और organic manure उपयोगी हो सकते हैं।",
    "grapes": "अंगूर में Nitrogen, Phosphorus और Potassium का balanced management आवश्यक है।",
    "watermelon": "तरबूज में balanced NPK और उचित Potassium management उपयोगी है।",
    "muskmelon": "खरबूजे में balanced nutrients और पर्याप्त Potassium उपयोगी होता है।",
    "apple": "सेब में balanced NPK और organic manure उपयोगी हो सकते हैं।",
    "orange": "संतरे में balanced NPK और organic manure उपयोगी हो सकते हैं।",
    "papaya": "पपीते में Nitrogen और Potassium सहित balanced nutrients महत्वपूर्ण हैं।",
    "coconut": "नारियल में Nitrogen और Potassium सहित balanced nutrient management आवश्यक है।",
    "cotton": "कपास में Nitrogen, Phosphorus और Potassium की balanced supply महत्वपूर्ण है।",
    "jute": "जूट में Nitrogen की अच्छी उपलब्धता और balanced NPK management उपयोगी है।",
    "coffee": "कॉफी में Nitrogen, Phosphorus और Potassium सहित balanced nutrient management आवश्यक है।"
}


# =========================================================
# CROP NAMES - HINDI
# =========================================================

crop_names_hi = {
    "rice": "चावल",
    "maize": "मक्का",
    "chickpea": "चना",
    "kidneybeans": "राजमा",
    "pigeonpeas": "अरहर",
    "mothbeans": "मोठ",
    "mungbean": "मूंग",
    "blackgram": "उड़द",
    "lentil": "मसूर",
    "pomegranate": "अनार",
    "banana": "केला",
    "mango": "आम",
    "grapes": "अंगूर",
    "watermelon": "तरबूज",
    "muskmelon": "खरबूजा",
    "apple": "सेब",
    "orange": "संतरा",
    "papaya": "पपीता",
    "coconut": "नारियल",
    "cotton": "कपास",
    "jute": "जूट",
    "coffee": "कॉफी"
}


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get selected language
        language = request.form.get("language", "en")

        # Get input values
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])


        # -------------------------------------------------
        # INPUT VALIDATION
        # -------------------------------------------------

        if N < 0 or P < 0 or K < 0:

            error = (
                "N, P and K values cannot be negative."
                if language == "en"
                else "N, P और K की value negative नहीं हो सकती।"
            )

            return render_template(
                "index.html",
                error=error,
                language=language
            )


        if humidity < 0 or humidity > 100:

            error = (
                "Humidity must be between 0 and 100%."
                if language == "en"
                else "Humidity 0 से 100% के बीच होनी चाहिए।"
            )

            return render_template(
                "index.html",
                error=error,
                language=language
            )


        if ph < 0 or ph > 14:

            error = (
                "pH value must be between 0 and 14."
                if language == "en"
                else "pH की value 0 से 14 के बीच होनी चाहिए।"
            )

            return render_template(
                "index.html",
                error=error,
                language=language
            )


        if temperature < -50 or temperature > 70:

            error = (
                "Temperature must be between -50°C and 70°C."
                if language == "en"
                else "Temperature -50°C से 70°C के बीच होनी चाहिए।"
            )

            return render_template(
                "index.html",
                error=error,
                language=language
            )


        if rainfall < 0:

            error = (
                "Rainfall cannot be negative."
                if language == "en"
                else "Rainfall negative नहीं हो सकती।"
            )

            return render_template(
                "index.html",
                error=error,
                language=language
            )


        # -------------------------------------------------
        # PREPARE INPUT DATA
        # -------------------------------------------------

        input_data = [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]]


        # -------------------------------------------------
        # MODEL PREDICTION
        # -------------------------------------------------

        prediction = model.predict(input_data)[0]


        # -------------------------------------------------
        # CONFIDENCE
        # -------------------------------------------------

        probabilities = model.predict_proba(input_data)[0]

        confidence = round(
            max(probabilities) * 100,
            2
        )


        # -------------------------------------------------
        # LANGUAGE SELECTION
        # -------------------------------------------------

        if language == "hi":

            crop_name = crop_names_hi.get(
                prediction,
                prediction
            )

            information = crop_info_hi.get(
                prediction,
                "कोई अतिरिक्त जानकारी उपलब्ध नहीं है।"
            )

            fertilizer = fertilizer_info_hi.get(
                prediction,
                "उर्वरक की जानकारी उपलब्ध नहीं है।"
            )

        else:

            crop_name = prediction

            information = crop_info_en.get(
                prediction,
                "No additional information available."
            )

            fertilizer = fertilizer_info_en.get(
                prediction,
                "No fertilizer information available."
            )


        # -------------------------------------------------
        # SEND RESULT TO HTML
        # -------------------------------------------------

        return render_template(
            "index.html",
            prediction=crop_name,
            confidence=confidence,
            information=information,
            fertilizer=fertilizer,
            language=language
        )


    except ValueError:

        language = request.form.get(
            "language",
            "en"
        )

        error = (
            "Please enter valid numbers in all fields."
            if language == "en"
            else "कृपया सभी fields में valid numbers डालें।"
        )

        return render_template(
            "index.html",
            error=error,
            language=language
        )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )