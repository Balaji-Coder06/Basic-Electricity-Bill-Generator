from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

APPLIANCE_DATA = {
    "Fan": 0.075, "AC": 1.75, "TV": 0.15, "Fridge": 0.25, 
    "Washing Machine": 0.575, "Heater": 2.10, "Computer": 0.45
}
ELECTRICITY_RATE = 8.0

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate_usage():
    data = request.json
    total_kwh = 0

    for appliance, hours in data.items():
        if appliance in APPLIANCE_DATA:
            total_kwh += APPLIANCE_DATA[appliance] * hours

    estimated_bill = total_kwh * ELECTRICITY_RATE
    energy_tips = suggest_tips(total_kwh)

    return jsonify({"total_kwh": round(total_kwh, 2), "estimated_bill": round(estimated_bill, 2), "tips": energy_tips})

def suggest_tips(kwh):
    if kwh > 35:
        return "Your energy consumption is high! Consider using LED bulbs and energy-efficient appliances."
    elif kwh > 20:
        return "Try turning off unused appliances and unplugging devices when not needed."
    else:
        return "Good job! Your energy consumption is under control."

if __name__ == "__main__":
    app.run(debug=True)
