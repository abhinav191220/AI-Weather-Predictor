# 🌤️ AI Weather Predictor
**|| CSA 2001 : Fundamentals in AI and ML  ||  Name :- Abhinav Singh  ||  Reg. No. :- 25BAI10303 ||**
> **A Lightweight, Zero-Dependency Atmospheric Forecasting Suite built in Python.**

## 🚀 Project Overview
The **AI Weather Predictor** is a precision desktop utility engineered to synthesize and forecast localized weather trends. By ingesting daily metrics—Temperature, Humidity, Wind Speed, Precipitation, and AQI—the system employs a **deterministic mathematical engine** to project atmospheric states for the subsequent 24-hour cycle.

This project serves as a technical demonstration of **Machine Learning from first principles**, implemented entirely within the Python Standard Library to ensure maximum portability and performance.

### 💎 Engineering Highlights
* **Zero-Dependency Architecture:** Operational without `pip` installations. No Scikit-Learn, Pandas, or NumPy—just pure algorithmic Python.
* **Linear Extrapolation Engine:** Features a manual implementation of **Least Squares Regression** to derive the "Line of Best Fit" for atmospheric variables.
* **Stateful Memory System:** Utilizes an atomic JSON serialization layer to maintain historical data integrity across application restarts.
* **High-Contrast HUD:** A sophisticated, "Neon-Obsidian" Graphical User Interface (GUI) built using the `Tkinter` framework for professional data visualization.

---

## 🧠 Algorithmic Logic (The Mathematics)
The system’s predictive intelligence is powered by the `predict_next` method. It models the relationship between time ($x$) and the observed metric ($y$) using a **Simple Linear Regression** model:

$$y = mx + b$$

**Variables & Derivations:**
* **$y$**: The predicted value for the next chronological index ($n+1$).
* **$x$**: The independent time-step variable.
* **$m$ (Slope)**: The velocity of change, derived via the **Least Squares** method:
    $$m = \frac{n\sum(xy) - \sum x \sum y}{n\sum(x^2) - (\sum x)^2}$$
* **$b$ (y-Intercept)**: The baseline value, calculated as:
    $$b = \frac{\sum y - m\sum x}{n}$$

By processing the historical "memory" of the station, the algorithm minimizes the sum of squared residuals to project the most statistically probable outcome for Tomorrow.

---

## 🛠️ System Features
* **Multivariate Ingest:** Synchronized tracking of 5 distinct weather vectors (Thermal, Kinetic, Volumetric, etc.).
* **Automated Analytics:** Instant trend insights (e.g., "System detects a Cooling Trend").
* **Data Validation Layer:** Robust error-trapping to prevent system crashes from non-numeric or corrupted inputs.
* **Pro-Terminal UI:** A monospaced display box designed to mimic professional meteorological workstations.

---

## 📦 Deployment & Usage
Since the project relies exclusively on the standard library, deployment is instantaneous.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/abhinav191220/weather-predictor.git](https://github.com/abhinav191220/weather-predictor.git)
    cd weather-predictor
    ```
2.  **Initialize the Station:**
    ```bash
    python weather_predictor.py
    ```
3.  **Operation Protocols:**
    * Input the current metrics for **Yesterday** and **Today**.
    * Click **Execute Prediction**.
    * *Note: The AI requires a minimum of **two data points** to establish a valid mathematical trajectory.*
    * The prediction will populate the terminal HUD with the forecast and smart analytics for Tomorrow.

---

## 📁 Project Structure
* `weather_predictor.py`: Core logic, `ProPredictorApp` class, and the Regression engine.
* `weather_memory.json`: The local data layer storing station identity and historical logs.

## 🤝 Technical Specifications
* **Runtime:** Python 3.10+
* **Standard Modules:** `tkinter`, `json`, `os`, `math`
* **GUI Resolution:** Optimized for 550x920 High-DPI displays.

---
*Developed with a focus on algorithmic transparency and lightweight software engineering.*dxc
