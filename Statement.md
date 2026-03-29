# 📑 PROJECT SPECIFICATION: WEATHER AI PREDICTOR

---

## 1. PROBLEM DEFINITION

In the modern landscape of software development, predicting complex local weather trends typically requires heavy Machine Learning libraries or constant internet connectivity. 

This project addresses the need for a **lightweight, offline tool** that can:
* Learn from user-provided data across five key metrics: **Temperature, Humidity, Wind Speed, Precipitation, and AQI**.
* Recognize atmospheric shifts and velocity changes over time.
* Provide accurate forecasts without the overhead of external dependencies.

---

## 2. PROJECT OBJECTIVE

The primary goal is to engineer a **Standalone Weather Assistant** featuring:
* **Multivariate Tracking:** A dedicated interface for monitoring City-Specific data.
* **Predictive Modeling:** A manual Linear Regression engine ($y=mx+b$) to simulate AI forecasting for each variable.
* **Persistent Memory:** A local JSON Data Layer to ensure the "AI" retains historical records across restarts.
* **Modern UX:** A high-contrast Graphical User Interface (GUI) optimized for rapid data entry.

---

## 3. TECHNICAL CONSTRAINTS

* **Standard Library Only:** The core logic must use only `tkinter`, `json`, and `os`.
* **Zero-Dependency:** No `pip install` or virtual environments required. 
* **Data Lifecycle:** `Input -> Validation -> JSON Storage -> Mathematical Analysis -> UI Output.`

---

## 4. MATHEMATICAL FRAMEWORK

The predictive engine is powered by the **Ordinary Least Squares (OLS)** method to calculate the **Line of Best Fit**:

$$y = mx + b$$

* **Slope (m):** Determines the trajectory (e.g., increasing wind speed or decreasing precipitation).
* **Intercept (b):** Establishes the historical starting point of the data series.
* **Forecasting (n+1):** Applies the derived coefficients to the next chronological index for a 24-hour prediction.

---

## 5. DATA INTEGRITY & SAFETY

* **Validation Layer:** Filters all inputs, preventing crashes from non-numeric entries.
* **Atomic Serialization:** Every entry is instantly saved to `weather_memory.json`, protecting data from power failures.

---

## 6. EXPECTED OUTCOME

The result is a reliable, lightweight utility (under 15KB) that proves functional AI does not require heavy frameworks. It provides a private, offline method to monitor **Temperature, Humidity, Wind, Rain, and Air Quality** with scientific accuracy.

---
