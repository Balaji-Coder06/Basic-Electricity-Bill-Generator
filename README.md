<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Energy Usage Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1, h2, h3 { color: #2c3e50; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Smart Energy Usage Tracker</h1>
    
<h2>Overview</h2>
<p>Managing electricity consumption efficiently can help reduce costs and promote sustainable energy use. The Smart Energy Usage Tracker is a web application built with Flask that enables users to monitor their daily electricity consumption and estimate their monthly bill. By simply entering the usage duration of household appliances, users can gain valuable insights into their energy consumption and receive practical energy-saving tips.</p>
    
<h2>Features</h2>
<p>This application allows users to log the daily usage of various household appliances, such as air conditioners, fans, televisions, and refrigerators. Using predefined power consumption rates, it calculates the total energy usage in kilowatt-hours (kWh) and provides an estimated electricity bill. Additionally, the tracker suggests personalized energy-saving strategies based on the recorded usage data, helping users make more informed decisions about their electricity consumption.</p>
    
<h2>Technologies Used</h2>
<p>The backend of the application is powered by Flask, a lightweight and efficient Python web framework. The frontend is developed using HTML, CSS, and JavaScript, ensuring an interactive and user-friendly experience. Instead of a traditional database, the application utilizes a JSON file to store appliance power consumption data, making it easy to maintain and modify.</p>
    
<h2>Installation & Setup</h2>
    <h3>Prerequisites</h3>
    <p>Before getting started, ensure that you have Python 3.x installed on your system. Additionally, install Flask by running the following command:</p>
    <pre>pip install flask</pre>
    
<h3>Steps to Install and Run</h3>
    <pre>
        git clone https://github.com/yourusername/smart-energy-tracker.git
        cd smart-energy-tracker
        pip install flask
        python app.py
    </pre>
    <p>Open a web browser and visit <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to begin tracking your energy consumption.</p>
    
<h2>Usage</h2>
    <p>Using the Smart Energy Usage Tracker is simple. Users can select an appliance from the dropdown menu and enter the number of hours they use it daily. After adding multiple appliances, they can click the "Calculate Bill" button to receive an estimate of their total energy consumption and expected electricity costs. The application also provides energy-saving tips based on recorded usage, helping users optimize their electricity consumption.</p>
    
<h2>Future Enhancements</h2>
    <p>To enhance the application's functionality, future updates may include user authentication for personalized tracking, integration with a database for storing long-term usage data, and IoT compatibility for real-time energy monitoring. Additionally, plans are in place to deploy the application on cloud platforms like Heroku or Render to make it easily accessible to users worldwide.</p>
    
<h2>License</h2>
    <p>This project is open-source and available under the MIT License. Feel free to contribute and improve its functionality.</p>
</body>
</html>
