# 🌤️ Daily AI Weather Predictor
**Course: CSA2001 – Fundamentals of AI and ML    Student:Abhinav Singh Registration Number: 25BAI10303**
> **A Lightweight, Zero-Dependency Weather Forecasting Tool built in Python.**

## 🚀 Overview
The **Daily AI Weather Predictor** is a desktop application designed to track and forecast local weather conditions. It allows users to log daily Temperature, Humidity, and AQI (Air Quality Index) data, then uses a custom-built machine learning algorithm to predict tomorrow's values.

This project was developed as a challenge to implement **Machine Learning from scratch** using only the Python Standard Library. 

### 💎 Key Highlights
* **Zero External Dependencies:** No `pip install` required. No Scikit-Learn, No Pandas, No NumPy.
* **Homemade AI Engine:** Features a manual implementation of Simple Linear Regression.
* **Persistent Weather Memory:** Uses a local JSON-based "AI Memory" system to store historical weather logs.
* **Native GUI:** A clean, dark-themed user interface built with `Tkinter`.

---

## 🧠 How the AI Works (The Math)
At the heart of the application is the `predict_next` method, which implements **Simple Linear Regression**. 

The model assumes a linear relationship between time ($x$) and the weather value ($y$), represented by the equation:

$$y = mx + b$$

Where:
* **$y$**: The predicted weather value for tomorrow.
* **$x$**: The time step (index of the day).
* **$m$ (Slope)**: The rate of change, calculated using the Least Squares method:
    $$m = \frac{n\sum(xy) - \sum x \sum y}{n\sum(x^2) - (\sum x)^2}$$
* **$b$ (Intercept)**: The value at $x=0$, calculated as:
    $$b = \frac{\sum y - m\sum x}{n}$$

The algorithm analyzes your historical input and calculates the line of best fit to project the most likely weather for the following day.

---

## 🛠️ Features
- **Weather Logging:** Easily input daily metrics (Temp, Humidity, AQI).
- **Trend Analysis:** Automated insights (e.g., "The weather is warming up").
- **Error Handling:** Robust validation to ensure only numerical data is processed.
- **Dark Mode UI:** Modern, high-contrast interface for better readability.

---

## 📦 Installation & Usage
Since this project uses only standard libraries, setup is instant.

1.  **Clone the repository or copy the code:**
    ```bash
    git clone [https://github.com/abhinav191220/weather-predictor.git](https://github.com/abhinav191220/weather-predictor.git)
    cd weather-predictor
    ```
2.  **Run the application:**
    ```bash
    python weather_predictor.py
    ```
3.  **Operation:**
    * Enter the current Weather stats (Temp, Humidity, AQI).
    * Click **Save & Predict**.
    * **Do the step twice.**
    * The AI will update its memory and display the prediction for the next day in the blue display box.
---

## 📁 Project Structure
* `weather_predictor.py`: Contains the `AIPredictorApp` class, UI logic, and Regression math.
* `weather_memory.json`: (Generated automatically) Stores your historical weather data logs.

## 🤝 Technical Requirements
* **Python 3.12.8**
* **Modules:** `tkinter`, `json`, `os` (All included in standard Python installation).

---

*Developed with a focus on algorithmic transparency and lightweight software design.*
