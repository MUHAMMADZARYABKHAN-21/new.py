"""
Battery Health Predictor — Desktop GUI (Tkinter)
==================================================
Trains your Ridge Regression pipeline on battery.csv, then opens a
real desktop window with sliders to predict Battery Health.

Run with:
    pip install pandas numpy scikit-learn matplotlib
    python battery_health_gui.py

Requires battery.csv in the same folder (or edit CSV_PATH below).
"""

import tkinter as tk
from tkinter import ttk, messagebox

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

CSV_PATH = "battery.csv"

NUMERICAL_FEATURES = [
    "Battery Age", "Daily Usage Hours", "Design Capacity", "Cycle Count",
    "CPU Usage", "GPU Usage", "Power Consumption", "Average Temperature",
    "Full Charge Capacity",
]
CATEGORICAL_FEATURES = ["Gaming User"]


# ============================================================
# TRAIN THE MODEL
# ============================================================

def train_model():
    df = pd.read_csv(CSV_PATH)
    X = df.drop("Battery Health", axis=1)
    Y = df["Battery Health"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessing = ColumnTransformer([
        ("numerical", numeric_pipeline, NUMERICAL_FEATURES),
        ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
    ])

    model = Pipeline([
        ("preprocessing", preprocessing),
        ("Model", Ridge(alpha=0.01)),
    ])
    model.fit(X_train, Y_train)

    preds = model.predict(X_test)
    metrics = {
        "MAE": mean_absolute_error(Y_test, preds),
        "MSE": mean_squared_error(Y_test, preds),
        "R2": r2_score(Y_test, preds),
    }
    return model, df, metrics


# ============================================================
# GUI
# ============================================================

BG = "#F4F6F8"
CARD = "#FFFFFF"
BORDER = "#E2E8F0"
TEXT = "#1F2937"
MUTED = "#6B7280"
BLUE = "#2563EB"
GREEN = "#16A34A"
ORANGE = "#D97706"
RED = "#DC2626"


class BatteryApp(tk.Tk):
    def __init__(self, model, df, metrics):
        super().__init__()
        self.model = model
        self.df = df
        self.metrics = metrics

        self.title("Battery Health Predictor")
        self.geometry("1000x680")
        self.minsize(880, 600)
        self.configure(bg=BG)

        self._build_style()
        self._build_layout()

    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=CARD)
        style.configure("TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 10))
        style.configure("Card.TLabel", background=CARD, foreground=TEXT, font=("Segoe UI", 10))
        style.configure("Heading.TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 16, "bold"))
        style.configure("Muted.TLabel", background=BG, foreground=MUTED, font=("Segoe UI", 9))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("Horizontal.TScale", background=CARD)

    def _build_layout(self):
        header = ttk.Frame(self, style="TFrame")
        header.pack(fill="x", padx=16, pady=(14, 4))
        ttk.Label(header, text="🔋 Battery Health Predictor", style="Heading.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text=f"Ridge Regression  |  R²={self.metrics['R2']:.3f}  MAE={self.metrics['MAE']:.2f}  MSE={self.metrics['MSE']:.2f}",
            style="Muted.TLabel",
        ).pack(anchor="w")

        body = ttk.Frame(self, style="TFrame")
        body.pack(fill="both", expand=True, padx=16, pady=10)
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        left = self._build_input_panel(body)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        right = self._build_result_panel(body)
        right.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

    # ------------------------------------------------------
    def _build_input_panel(self, parent):
        card = tk.Frame(parent, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        canvas = tk.Canvas(card, bg=CARD, highlightthickness=0)
        scrollbar = ttk.Scrollbar(card, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=CARD)

        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        tk.Label(inner, text="BATTERY INPUT", bg=CARD, fg=BLUE, font=("Segoe UI", 11, "bold")).pack(
            anchor="w", pady=(0, 10)
        )

        ranges = {
            "Battery Age": (0.0, float(self.df["Battery Age"].max()), "years"),
            "Daily Usage Hours": (0.0, float(self.df["Daily Usage Hours"].max()), "hrs"),
            "Design Capacity": (float(self.df["Design Capacity"].min()), float(self.df["Design Capacity"].max()), "mAh"),
            "Cycle Count": (0.0, float(self.df["Cycle Count"].max()), "cycles"),
            "CPU Usage": (0.0, 100.0, "%"),
            "GPU Usage": (0.0, 100.0, "%"),
            "Power Consumption": (0.0, float(self.df["Power Consumption"].max()), "W"),
            "Average Temperature": (float(self.df["Average Temperature"].min()), float(self.df["Average Temperature"].max()), "°C"),
            "Full Charge Capacity": (float(self.df["Full Charge Capacity"].min()), float(self.df["Full Charge Capacity"].max()), "mAh"),
        }

        self.sliders = {}
        self.value_labels = {}
        for feat, (lo, hi, unit) in ranges.items():
            row = tk.Frame(inner, bg=CARD)
            row.pack(fill="x", pady=6)

            top = tk.Frame(row, bg=CARD)
            top.pack(fill="x")
            tk.Label(top, text=feat, bg=CARD, fg=TEXT, font=("Segoe UI", 9, "bold")).pack(side="left")
            val_lbl = tk.Label(top, text="", bg=CARD, fg=MUTED, font=("Segoe UI", 9))
            val_lbl.pack(side="right")
            self.value_labels[feat] = (val_lbl, unit)

            default = float(self.df[feat].mean())
            var = tk.DoubleVar(value=round(default, 1))
            scale = tk.Scale(
                row, from_=lo, to=hi, orient="horizontal", variable=var,
                resolution=(hi - lo) / 200 or 1, showvalue=False,
                bg=CARD, fg=TEXT, troughcolor="#DBEAFE", highlightthickness=0,
                command=lambda v, f=feat: self._update_value_label(f),
            )
            scale.pack(fill="x")
            self.sliders[feat] = var
            self._update_value_label(feat)

        gaming_row = tk.Frame(inner, bg=CARD)
        gaming_row.pack(fill="x", pady=(14, 6))
        tk.Label(gaming_row, text="Gaming User", bg=CARD, fg=TEXT, font=("Segoe UI", 9, "bold")).pack(anchor="w")
        self.gaming_var = tk.StringVar(value="No")
        gaming_combo = ttk.Combobox(gaming_row, textvariable=self.gaming_var, values=["No", "Yes"], state="readonly")
        gaming_combo.pack(fill="x", pady=4)

        predict_btn = tk.Button(
            inner, text="Predict Battery Health", bg=BLUE, fg="white",
            font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=8,
            activebackground="#1D4ED8", activeforeground="white",
            command=self.predict,
        )
        predict_btn.pack(fill="x", pady=(16, 4))

        return card

    def _update_value_label(self, feat):
        lbl, unit = self.value_labels[feat]
        lbl.config(text=f"{self.sliders[feat].get():.1f} {unit}")

    # ------------------------------------------------------
    def _build_result_panel(self, parent):
        card = tk.Frame(parent, bg=CARD, highlightbackground=BORDER, highlightthickness=1)

        tk.Label(card, text="PREDICTION", bg=CARD, fg=BLUE, font=("Segoe UI", 11, "bold")).pack(
            anchor="w", padx=16, pady=(12, 6)
        )

        self.health_label = tk.Label(card, text="--", bg=CARD, fg=TEXT, font=("Segoe UI", 42, "bold"))
        self.health_label.pack(pady=(0, 0))

        self.status_label = tk.Label(card, text="Adjust sliders and click Predict", bg=CARD, fg=MUTED,
                                      font=("Segoe UI", 12, "bold"))
        self.status_label.pack(pady=(0, 10))

        fig = Figure(figsize=(4.2, 3.2), dpi=100, facecolor=CARD)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=card)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=16, pady=(0, 16))
        self._draw_gauge(0)

        return card

    def _draw_gauge(self, value):
        self.ax.clear()
        self.ax.barh(["Health"], [100], color="#E5E7EB", height=0.5)
        color = self._status_color(value)
        self.ax.barh(["Health"], [value], color=color, height=0.5)
        self.ax.set_xlim(0, 100)
        self.ax.set_yticks([])
        self.ax.set_xlabel("Battery Health (%)")
        for spine in ["top", "right", "left"]:
            self.ax.spines[spine].set_visible(False)
        self.canvas.draw_idle()

    @staticmethod
    def _status_color(value):
        if value >= 90:
            return GREEN
        elif value >= 75:
            return BLUE
        elif value >= 60:
            return ORANGE
        return RED

    @staticmethod
    def _status_text(value):
        if value >= 90:
            return "EXCELLENT"
        elif value >= 75:
            return "GOOD"
        elif value >= 60:
            return "MODERATE"
        return "POOR"

    # ------------------------------------------------------
    def predict(self):
        try:
            input_data = pd.DataFrame([{
                **{feat: var.get() for feat, var in self.sliders.items()},
                "Gaming User": self.gaming_var.get(),
            }])
            pred = float(self.model.predict(input_data)[0])
            pred = max(0.0, min(100.0, pred))

            color = self._status_color(pred)
            self.health_label.config(text=f"{pred:.1f}%", fg=color)
            self.status_label.config(text=self._status_text(pred), fg=color)
            self._draw_gauge(pred)
        except Exception as e:
            messagebox.showerror("Prediction Error", f"Could not generate a prediction:\n\n{e}")


# ============================================================
# ENTRY POINT
# ============================================================

def main():
    try:
        model, df, metrics = train_model()
    except Exception as e:
        print(f"Failed to train model: {e}")
        return
    app = BatteryApp(model, df, metrics)
    app.mainloop()


if __name__ == "__main__":
    main()
