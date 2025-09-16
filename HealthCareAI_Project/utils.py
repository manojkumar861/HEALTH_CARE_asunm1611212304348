def symptom_suggester(user_text: str) -> str:
    text = user_text.lower()
    if "fever" in text:
        return "Detected: Fever. Possible causes: viral infection, flu. Advice: rest, fluids, see doctor if high fever."
    elif "cough" in text:
        return "Detected: Cough. Possible causes: cold, allergy, bronchitis. Advice: stay hydrated, consult doctor if severe."
    else:
        return "No clear symptom detected. Try mentioning 'fever', 'cough', 'headache', etc.'"
