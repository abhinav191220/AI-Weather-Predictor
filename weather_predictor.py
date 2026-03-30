import tkinter as tk
from tkinter import messagebox, font

# --- DESIGN PALETTE ---
BG_MAIN = "#020617"      
BG_CARD = "#1e293b"      
ACCENT_CYAN = "#22d3ee"  
ACCENT_ROSE = "#f43f5e"  
TEXT_MAIN = "#ffffff"    # Pure White for Units/Values
TEXT_DIM = "#94a3b8"     
TERMINAL_GREEN = "#4ade80" 

class ProPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Weather Predictor")
        self.root.geometry("550x920")
        self.root.configure(bg=BG_MAIN)
        
        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg=BG_MAIN, pady=20)
        header.pack(fill="x")
        tk.Label(header, text="AI WEATHER PREDICTOR", font=("Impact", 28), fg=ACCENT_CYAN, bg=BG_MAIN).pack()
        tk.Label(header, text="WEATHER FORECASTING SYSTEM", font=("Verdana", 10), fg=TEXT_DIM, bg=BG_MAIN).pack()

        # City Input
        city_frame = tk.Frame(self.root, bg=BG_CARD, padx=15, pady=12, highlightbackground="#334155", highlightthickness=1)
        city_frame.pack(pady=10, padx=30, fill="x")
        tk.Label(city_frame, text="CITY NAME :", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10)).pack(side="left")
        self.city_input = tk.Entry(city_frame, bg=BG_CARD, fg=TEXT_MAIN, insertbackground="white", relief="flat", font=("Consolas", 12), width=20)
        self.city_input.pack(side="right")
        self.city_input.insert(0, "Bhopal")

        # Main Data Grid
        grid_container = tk.Frame(self.root, bg=BG_MAIN)
        grid_container.pack(pady=10, padx=30, fill="x")

        # Headers
        tk.Label(grid_container, text="ATMOSPHERIC DATA", fg=ACCENT_CYAN, bg=BG_MAIN, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        tk.Label(grid_container, text="YESTERDAY", fg=TEXT_DIM, bg=BG_MAIN, font=("Arial", 9)).grid(row=0, column=1)
        tk.Label(grid_container, text="TODAY", fg=TEXT_DIM, bg=BG_MAIN, font=("Arial", 9)).grid(row=0, column=2)

        self.inputs = {"yesterday": [], "today": []}
        
        metrics = [
            ("Temperature", "°C"),
            ("Humidity", "%"),
            ("Wind Speed", "km/h"),
            ("Precipitation", "mm"),
            ("Air Quality", "AQI")
        ]

        for i, (name, unit) in enumerate(metrics):
            tk.Label(grid_container, text=f"{name}", fg=TEXT_DIM, bg=BG_MAIN, font=("Arial", 10)).grid(row=i+1, column=0, sticky="w", pady=12)
            
            # Yesterday Input Group
            y_frame = tk.Frame(grid_container, bg=BG_CARD)
            y_frame.grid(row=i+1, column=1, padx=5)
            y_ent = tk.Entry(y_frame, width=7, justify='center', bg=BG_CARD, fg=TERMINAL_GREEN, relief="flat", font=("Consolas", 11))
            y_ent.pack(side="left", padx=2)
            tk.Label(y_frame, text=unit, fg=TEXT_MAIN, bg=BG_CARD, font=("Arial", 8, "bold")).pack(side="right", padx=5) # UNIT IS WHITE
            
            # Today Input Group
            t_frame = tk.Frame(grid_container, bg=BG_CARD)
            t_frame.grid(row=i+1, column=2, padx=5)
            t_ent = tk.Entry(t_frame, width=7, justify='center', bg=BG_CARD, fg=ACCENT_CYAN, relief="flat", font=("Consolas", 11))
            t_ent.pack(side="left", padx=2)
            tk.Label(t_frame, text=unit, fg=TEXT_MAIN, bg=BG_CARD, font=("Arial", 8, "bold")).pack(side="right", padx=5) # UNIT IS WHITE

            self.inputs["yesterday"].append(y_ent)
            self.inputs["today"].append(t_ent)

        # Buttons
        btn_frame = tk.Frame(self.root, bg=BG_MAIN)
        btn_frame.pack(pady=20, padx=30, fill="x")

        tk.Button(btn_frame, text="EXECUTE PREDICTION", command=self.calculate, 
                        bg=ACCENT_CYAN, fg=BG_MAIN, font=("Arial", 12, "bold"), 
                        activebackground=TERMINAL_GREEN, relief="flat", cursor="hand2").pack(fill="x", pady=5)
        
        tk.Button(btn_frame, text="SYSTEM RESET", command=self.reset_fields, 
                        bg="#334155", fg=TEXT_MAIN, font=("Arial", 10), 
                        activebackground=ACCENT_ROSE, relief="flat", cursor="hand2").pack(fill="x")

        # Terminal Output
        self.output_box = tk.Label(self.root, 
                                  text="[ SYSTEM IDLE ]\nAwaiting data stream...", 
                                  font=("Consolas", 11), fg=TERMINAL_GREEN, bg="#020617", 
                                  height=12, relief="flat", justify="left", anchor="nw", padx=25, pady=25)
        self.output_box.pack(pady=10, padx=30, fill="both")

    def reset_fields(self):
        for entry in self.inputs["yesterday"] + self.inputs["today"]:
            entry.delete(0, tk.END)
        self.output_box.config(text="[ SYSTEM RESET ]\nMemory cleared. Ready for new input.", fg=TERMINAL_GREEN)

    def calculate(self):
        try:
            city = self.city_input.get().upper()
            y_vals = [float(e.get()) for e in self.inputs["yesterday"]]
            t_vals = [float(e.get()) for e in self.inputs["today"]]
            
            preds = [t + (t - y) for y, t in zip(y_vals, t_vals)]
            
            m_names = ["TEMP", "HUMIDITY", "WIND", "PRECIP", "AIR QUALITY"]
            units = ["°C", "%", "km/h", "mm", "AQI"]
            
            res = f">> TARGET: {city}\n"
            res += "========================================\n"
            for i in range(5):
                res += f"{m_names[i]:<15} | {preds[i]:>8.2f} {units[i]}\n"
            res += "========================================\n"
            
            # Smart Insights
            res += "ANALYTICS:\n"
            if preds[3] > 5.0: res += "! WARNING: High Precipitation Expected.\n"
            if preds[4] > 100: res += "! ALERT: Poor Air Quality Forecasted.\n"
            if abs(preds[0] - t_vals[0]) > 5: res += "! NOTICE: Rapid Temp Shift Detected.\n"
            else: res += "√ Atmospheric Stability: STABLE\n"
            
            self.output_box.config(text=res, fg=TERMINAL_GREEN)
            
        except ValueError:
            self.output_box.config(text=">> ERROR: DATA STREAM CORRUPTED\nPlease check all metric inputs.", fg=ACCENT_ROSE)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProPredictorApp(root)
    root.mainloop()

