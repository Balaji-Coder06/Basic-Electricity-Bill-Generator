from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Sample power consumption data (in kWh per hour)
APPLIANCE_DATA = {
    "fan": 0.075, "ac": 1.5, "tv": 0.1, "fridge": 0.2, 
    "washing machine": 0.5, "heater": 2.0, "computer": 0.3
}

# Electricity rate per kWh (Example: ₹5 per unit)
ELECTRICITY_RATE = 5.0

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
    if kwh > 50:
        return "Your energy consumption is high! Consider using LED bulbs and energy-efficient appliances."
    elif kwh > 20:
        return "Try turning off unused appliances and unplugging devices when not needed."
    else:
        return "Good job! Your energy consumption is under control."

if __name__ == "__main__":
    app.run(debug=True)
