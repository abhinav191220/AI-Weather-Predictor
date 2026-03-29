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
        self.root.geometry("400x650") # Increased height for new input
        self.root.configure(bg="#1a1a1a")

        self.history = self.load_data()

        # --- UI Layout ---
        tk.Label(root, text="Daily Weather Input", font=("Arial", 14, "bold"), fg="cyan", bg="#1a1a1a").pack(pady=10)

        # City Input
        self.city_input = self.create_input("City Name:")
        # Pre-fill with last saved city if exists
        if "city" in self.history and self.history["city"]:
            self.city_input.insert(0, self.history["city"])

        self.temp_input = self.create_input("Temperature (°C):")
        self.humid_input = self.create_input("Humidity (%):")
        self.aqi_input = self.create_input("AQI (1-500):")

        tk.Button(root, text="Save & Predict", command=self.process_data, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

        # Prediction Display
        self.prediction_box = tk.Label(root, text="Enter data to see predictions...", 
                                      font=("Arial", 10), fg="#bdc3c7", bg="#2c3e50", 
                                      width=45, height=12, relief="ridge", justify="left", anchor="nw", padx=10, pady=10)
        self.prediction_box.pack(pady=10)

        self.update_prediction_ui()

    def create_input(self, label_text):
        tk.Label(self.root, text=label_text, fg="white", bg="#1a1a1a").pack()
        entry = tk.Entry(self.root, justify='center')
        entry.pack(pady=5)
        return entry

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        # Added 'city' key to default dictionary
        return {"city": "", "temp": [], "humid": [], "aqi": []}

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.history, f)

    def predict_next(self, series):
        if len(series) < 2:
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
            a = float(self.aqi_input.get())

            if not c:
                messagebox.showwarning("Warning", "Please enter a city name.")
                return

            self.history["city"] = c
            self.history["temp"].append(t)
            self.history["humid"].append(h)
            self.history["aqi"].append(a)

            self.save_data()
            self.update_prediction_ui()
            
            # Clear inputs (except city, usually people track one city at a time)
            self.temp_input.delete(0, tk.END)
            self.humid_input.delete(0, tk.END)
            self.aqi_input.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Data for {c} saved!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Temp/Humid/AQI.")

    def update_prediction_ui(self):
        if len(self.history["temp"]) < 2:
            return

        p_temp = self.predict_next(self.history["temp"])
        p_humid = self.predict_next(self.history["humid"])
        p_aqi = self.predict_next(self.history["aqi"])
        city = self.history.get("city", "Unknown City")

        text = f"--- {city.upper()} WEATHER PREDICTION ---\n\n"
        text += f"Predicted Temp: {p_temp:.2f}°C\n"
        text += f"Predicted Humidity: {p_humid:.2f}%\n"
        text += f"Predicted AQI: {p_aqi:.2f}\n\n"
        
        trend = "Warming up" if p_temp > self.history["temp"][-1] else "Cooling down"
        text += f"Insight: The weather is {trend}."

        self.prediction_box.config(text=text)        

if __name__ == "__main__":
    root = tk.Tk()
    app = AIPredictorApp(root)
    root.mainloop()
