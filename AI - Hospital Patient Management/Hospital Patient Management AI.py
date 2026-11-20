"""
Hospital Patient Management AI
Run: python hospital_ai.py
Requires: Python 3.8+ (no third-party packages)

This is an educational, rule-based department recommendation
prototype, not a medical diagnosis system.
"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(
    os.path.dirname(__file__), "Hospital Patient Management File.json"
)

RESULT_FILE = os.path.join(
    os.path.dirname(__file__), "Hospital Patient Management Result.json"
)


def load_departments():
    """Load hospital department information from JSON."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("departments", [])

    except FileNotFoundError:
        raise SystemExit(
            "Error: Hospital Patient Management File.json was not found. "
            "Keep it beside this Python file."
        )

    except json.JSONDecodeError:
        raise SystemExit(
            "Error: Hospital Patient Management File.json contains invalid JSON."
        )


def ask_integer(prompt, minimum=0, maximum=120):
    """Get valid integer input."""
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid whole number.")


def ask_float(prompt, minimum=0, maximum=100000000):
    """Get valid numeric input."""
    while True:
        try:
            value = float(input(prompt).strip())

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")


def get_patient_details():
    """Collect patient information."""

    print("\n=== Patient Information ===")

    name = input("Patient name: ").strip() or "Patient"

    age = ask_integer("Patient age: ", 1, 120)

    gender = input("Gender: ").strip() or "Not specified"

    print("\nEnter symptoms separated by commas.")

    print(
        "Examples: headache, dizziness, chest pain, "
        "joint pain, skin rashes"
    )

    symptoms = {
        item.strip().lower()
        for item in input("Your symptoms: ").split(",")
        if item.strip()
    }

    preferred_department = input(
        "\nPreferred department (optional: Cardiology, "
        "Neurology, Orthopedics, Dermatology, ENT): "
    ).strip().lower()

    budget = ask_float(
        "Maximum consultation budget (in INR): ",
        0,
        100000000
    )

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "symptoms": sorted(symptoms),
        "preferred_department": preferred_department,
        "annual_budget_inr": budget
    }


def score_department(patient, department):
    """
    Score departments using matching rules:

    50 points for symptom matching
    25 points for preferred department
    15 points for budget fit
    10 points for doctor availability

    This score is for department matching only,
    not for assessing medical severity.
    """

    patient_symptoms = set(patient["symptoms"])

    department_symptoms = {
        symptom.lower()
        for symptom in department.get("common_symptoms", [])
    }

    overlap = patient_symptoms.intersection(department_symptoms)

    # Symptom matching score
    symptom_score = min(50, len(overlap) * 25)

    # Preferred department matching
    preferred = patient["preferred_department"]

    department_id = department["id"].lower()
    department_name = department["name"].lower()

    preferred_match = bool(
        preferred
        and (
            preferred == department_id
            or preferred == department_name
        )
    )

    preference_score = 25 if preferred_match else 0

    # Consultation budget matching
    fee = department["consultation_fee"]
    budget = patient["annual_budget_inr"]

    if budget <= 0:
        budget_score = 0
    elif fee <= budget:
        budget_score = 15
    else:
        budget_score = max(0, 15 * budget / fee)

    # Doctor availability
    doctors = department["doctors_available"]

    availability_score = 10 if doctors > 0 else 0

    total = round(
        symptom_score
        + preference_score
        + budget_score
        + availability_score,
        1
    )

    return {
        "score": min(100, total),
        "symptom_matches": sorted(overlap),
        "preferred_department_match": preferred_match,
        "consultation_fee": fee,
        "within_budget": fee <= budget if budget > 0 else None,
        "doctors_available": doctors,
        "availability_status": (
            "Doctors available"
            if doctors > 0
            else "Availability not confirmed"
        )
    }


def recommend_departments(patient, departments):
    """Generate department recommendations."""

    results = []

    for department in departments:

        details = score_department(patient, department)

        results.append({
            "department_id": department["id"],
            "department_name": department["name"],
            "specialization": department["specialization"],
            "description": department["description"],
            "common_symptoms": department["common_symptoms"],
            "services": department["services"],
            **details
        })

    # Sort departments by matching score
    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results


def display_results(patient, recommendations):
    """Display recommendation results."""

    print(
        f"\n=== Hospital Recommendations for "
        f"{patient['name']} ==="
    )

    if not recommendations:
        print("No departments are available in the dataset.")
        return

    for index, item in enumerate(recommendations[:5], start=1):

        print(
            f"\n{index}. {item['department_name']} "
            f"({item['department_id']})"
        )

        print(f"   Match score: {item['score']}/100")

        print(f"   Specialization: {item['specialization']}")

        print(
            f"   Consultation fee: "
            f"INR {item['consultation_fee']:,.0f}"
        )

        print(
            f"   Symptom matches: "
            f"{', '.join(item['symptom_matches']) or 'None'}"
        )

        print(
            f"   Preferred department match: "
            f"{'Yes' if item['preferred_department_match'] else 'No'}"
        )

        print(
            f"   Doctors available: "
            f"{item['doctors_available']}"
        )

        print(
            f"   Within budget: "
            f"{'Yes' if item['within_budget'] else 'No'}"
        )

        print(
            f"   Services: "
            f"{', '.join(item['services'])}"
        )

        print(
            f"   Why consider it: {item['description']}"
        )

    print("\nImportant:")
    print("This recommendation is not a medical diagnosis.")
    print("Consult a qualified doctor for medical evaluation.")
    print("Verify actual doctor availability and consultation fees.")


def save_results(patient, recommendations):
    """Save recommendation results into JSON."""

    output = {
        "generated_at": datetime.now().isoformat(
            timespec="seconds"
        ),
        "patient": patient,
        "recommendations": recommendations[:5],
        "disclaimer": (
            "This is an educational department recommendation "
            "prototype, not a medical diagnosis. Consult a "
            "qualified healthcare professional. Actual doctor "
            "availability and fees must be verified with the hospital."
        )
    }

    with open(
        RESULT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"\nYour hospital report was saved to: {RESULT_FILE}"
    )


def main():

    departments = load_departments()

    patient = get_patient_details()

    recommendations = recommend_departments(
        patient,
        departments
    )

    display_results(
        patient,
        recommendations
    )

    save_results(
        patient,
        recommendations
    )


if __name__ == "__main__":
    main()