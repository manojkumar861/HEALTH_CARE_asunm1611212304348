# ai_client.py
# Handles AI logic: Symptom Checker, Chatbot, BMI, Calorie Calculator

def predict_disease(symptoms):
    """Simple rule-based symptom checker"""
    symptoms = symptoms.lower()

    if "fever" in symptoms and "cough" in symptoms:
        return "You may have Flu. Please rest and drink fluids."
    elif "headache" in symptoms and "nausea" in symptoms:
        return "You may have Migraine. Consider consulting a neurologist."
    elif "chest pain" in symptoms:
        return "Chest pain is serious. Please consult a doctor immediately!"
    else:
        return "No clear prediction. Please describe your symptoms more clearly."


def calculate_bmi(weight, height):
    """Calculate BMI and return category"""
    try:
        weight = float(weight)
        height = float(height) / 100  # convert cm → meters
        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return f"Your BMI is {bmi:.2f}, which is considered {category}."
    except:
        return "Format: bmi weight height (e.g., bmi 70 175)"


def calculate_calories(weight, height, age, gender, activity):
    """Calculate daily calorie needs using Mifflin-St Jeor Equation"""
    try:
        weight = float(weight)
        height = float(height)
        age = int(age)

        if gender.lower() == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:  # female
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        activity_factors = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very active": 1.9
        }

        factor = activity_factors.get(activity.lower(), 1.2)
        calories = bmr * factor

        return f"Your estimated daily calorie need is {calories:.0f} kcal ({activity} lifestyle)."
    except:
        return "Format: calories weight height age gender activity (e.g., calories 70 175 25 male moderate)"


def chatbot_response(user_input):
    """Chatbot with Symptom Checker, BMI, and Calorie Calculator"""
    user_input = user_input.lower().strip()

    responses = {
        "hello": "Hi! How can I assist you with your health today?",
        "hi": "Hello! Tell me your symptoms or questions.",
        "bye": "Take care! Stay healthy.",
        "help": "You can:\n- Describe symptoms (e.g., 'I have fever and cough')\n- Calculate BMI (bmi weight height)\n- Calculate Calories (calories weight height age gender activity)"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    # BMI
    if user_input.startswith("bmi"):
        try:
            _, weight, height = user_input.split()
            return calculate_bmi(weight, height)
        except:
            return "Format: bmi weight height (e.g., bmi 70 175)"

    # Calories
    if user_input.startswith("calories"):
        try:
            _, weight, height, age, gender, activity = user_input.split()
            return calculate_calories(weight, height, age, gender, activity)
        except:
            return "Format: calories weight height age gender activity (e.g., calories 70 175 25 male moderate)"

    # Else → symptom checker
    return predict_disease(user_input)
