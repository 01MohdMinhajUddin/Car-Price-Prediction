# Car Price Prediction Web App

This is a Flask-based machine learning web application that predicts the selling price of a used car based on various features like brand, model, year of purchase, fuel type, and kilometers driven.

---

# Features

- Predicts car price using a pre-trained machine learning model.
- Interactive frontend using HTML, CSS (Bootstrap), and JavaScript.
- Dynamic form population based on car company and model.
- REST-style prediction via Flask.

---

# Technologies Used

- Python 3
- Flask
- HTML/CSS (Bootstrap)
- JavaScript
- scikit-learn, pandas, numpy
- Pickle (for loading the trained model)

---

# Project Structure

application.py: Main Flask application file

Cleaned_car.pickle: Trained machine learning model

Cleaned car.csv: Dataset used to populate the form

templates/index.html: HTML template for the frontend

static/css/style.css: CSS styling file

requirements.txt: List of Python dependencies

ReadME.md: Project documentation file


---

# How to Run

1. **Clone the repository**  
   bash
   git clone https://github.com/01MohdMinhajUddin/Car-Price-Prediction
   cd car-price-prediction

# Create a virtual environment and activate it
python -m venv venv
source venv/Scripts/activate      # On macs : source venv/bin/activate

# Install the dependencies

pip install -r requirements.txt

# Run the Flask application

python application.py

# Open in browser

http://127.0.0.1:5000/  in your browser to access the app.


