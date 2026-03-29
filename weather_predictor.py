import tkinter as tk
from tkinter import messagebox
import json
import os

# JSON File to store data logs.
DATA_FILE = "weather_memory.json"

class AIPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily AI Weather Predictor")
        self.root.geometry("450x700") 
        self.root.configure(bg="#1a1a1a")

        self.history = self.load_data()

        # --- UI Layout ---
        tk.Label(root, text="Daily Weather Input", font=("Arial", 14, "bold"), fg="cyan", bg="#1a1a1a").pack(pady=10)

        # Inputs
        self.city_input = self.create_input("City Name:")
        if "city" in self.history and self.history["city"]:
            self.city_input.insert(0, self.history["city"])

        self.temp_input = self.create_input("Temperature (°C):")
        self.humid_input = self.create_input("Humidity (%):")
        self.wind_input = self.create_input("Wind Speed (km/h):")
        self.precip_input = self.create_input("Precipitation (mm):")
        self.aqi_input = self.create_input("AQI (1-500):")

        tk.Button(root, text="Save & Predict", command=self.process_data, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

        # Prediction Display
        self.prediction_box = tk.Label(root, text="Enter data to see predictions...", 
                                      font=("Arial", 10), fg="#bdc3c7", bg="#2c3e50", 
                                      width=50, height=12, relief="ridge", justify="left", anchor="nw", padx=10, pady=10)
        self.prediction_box.pack(pady=10)

        self.update_prediction_ui()

    def create_input(self, label_text):
        tk.Label(self.root, text=label_text, fg="white", bg="#1a1a1a").pack()
        entry = tk.Entry(self.root, justify='center')
        entry.pack(pady=3)
        return entry

    def load_data(self):
        default_data = {
            "city": "", "temp": [], "humid": [], "wind": [], 
            "precip": [], "aqi": []
        }
        
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
                    # Clean up data: ensure all keys exist and remove sunrise/sunset if they were there
                    for key in list(default_data.keys()):
                        if key not in data:
                            data[key] = default_data[key]
                    return data
            except (json.JSONDecodeError, IOError):
                return default_data
        return default_data

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.history, f, indent=4)

    def predict_next(self, series):
        if not series or len(series) < 2:
            return series[-1] if series else 0
        n = len(series)
        x = list(range(n))
        y = series
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xx = sum(i*i for i in x)
        sum_xy = sum(x[i]*y[i] for i in range(n))
        denominator = (n * sum_xx - sum_x**2)
        if denominator == 0: return series[-1]
        m = (n * sum_xy - sum_x * sum_y) / denominator
        b = (sum_y - m * sum_x) / n
        return m * n + b

    def process_data(self):
        try:
            c = self.city_input.get().strip()
            t = float(self.temp_input.get())
            h = float(self.humid_input.get())
            w = float(self.wind_input.get())
            p = float(self.precip_input.get())
            a = float(self.aqi_input.get())

            if not c:
                messagebox.showwarning("Warning", "Please enter a city name.")
                return

            self.history["city"] = c
            self.history["temp"].append(t)
            self.history["humid"].append(h)
            self.history["wind"].append(w)
            self.history["precip"].append(p)
            self.history["aqi"].append(a)

            self.save_data()
            self.update_prediction_ui()
            
            # Reset numerical fields
            for entry in [self.temp_input, self.humid_input, self.wind_input, self.precip_input, self.aqi_input]:
                entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Weather data for {c} saved!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields.")

    def update_prediction_ui(self):
        if len(self.history["temp"]) < 2:
            self.prediction_box.config(text="Log at least 2 days of data for predictions...")
            return

        p_temp = self.predict_next(self.history["temp"])
        p_humid = self.predict_next(self.history["humid"])
        p_wind = self.predict_next(self.history["wind"])
        p_precip = self.predict_next(self.history["precip"])
        p_aqi = self.predict_next(self.history["aqi"])
        
        city = self.history.get("city", "Unknown City")

        text = f"--- {city.upper()} WEATHER PREDICTION ---\n\n"
        text += f"Next Temp: {p_temp:.2f}°C\n"
        text += f"Next Humidity: {p_humid:.2f}%\n"
        text += f"Next Wind Speed: {p_wind:.2f} km/h\n"
        text += f"Next Precipitation: {p_precip:.2f} mm\n"
        text += f"Next AQI: {p_aqi:.2f}\n"
        text += f"---------------------------------\n\n"
        
        last_t = self.history["temp"][-1]
        trend = "Warming up" if p_temp > last_t else "Cooling down"
        text += f"Insight: The weather is {trend}."

        self.prediction_box.config(text=text)        

if __name__ == "__main__":
    root = tk.Tk()
    app = AIPredictorApp(root)
    root.mainloop()
