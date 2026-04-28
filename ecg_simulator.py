import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ================= ECG SIGNAL GENERATION =================
def generate_ecg(t, bpm):
    heart_rate = bpm / 60

    signal = 0.1 * np.sin(2 * np.pi * heart_rate * t)

    for beat in np.arange(0, t[-1], 1 / heart_rate):
        signal += np.exp(-((t - beat) ** 2) / 0.001)

    return signal


# ================= GUI APPLICATION =================
class ECGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Rate ECG Simulation")
        self.root.geometry("500x420")
        self.root.configure(bg="#f0f4f8")

        label_font  = ("Arial", 14)
        entry_font  = ("Arial", 14)
        button_font = ("Arial", 12, "bold")
        table_font  = ("Courier", 11)

        # ── Input ──────────────────────────────────────────────
        tk.Label(
            root, text="Enter Heart Rate (BPM):",
            font=label_font, bg="#f0f4f8"
        ).pack(pady=12)

        self.bpm_entry = tk.Entry(root, font=entry_font, justify="center")
        self.bpm_entry.pack(pady=4)

        btn_frame = tk.Frame(root, bg="#f0f4f8")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="▶  Start Simulation",
            font=button_font, bg="#4CAF50", fg="white",
            padx=10, command=self.start
        ).pack(side="left", padx=8)

        tk.Button(
            btn_frame, text="⏹  Stop",
            font=button_font, bg="#f44336", fg="white",
            padx=10, command=self.stop
        ).pack(side="left", padx=8)

        # ── Classification result label ────────────────────────
        self.status_label = tk.Label(
            root, text="", font=("Arial", 13, "bold"), bg="#f0f4f8"
        )
        self.status_label.pack(pady=6)

        # ── Classification table ───────────────────────────────
        table_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
        table_frame.pack(pady=8, padx=20, fill="x")

        headers = ["Category", "BPM Range", "Status"]
        col_widths = [12, 14, 14]

        # Header row
        header_frame = tk.Frame(table_frame, bg="#2c3e50")
        header_frame.pack(fill="x")
        for h, w in zip(headers, col_widths):
            tk.Label(
                header_frame, text=h, font=("Arial", 11, "bold"),
                fg="white", bg="#2c3e50", width=w, anchor="center",
                pady=5
            ).pack(side="left", padx=1)

        # Data rows  ─  stored so we can highlight the active one
        self.rows_data = [
            ("🔵 Low  ",    "< 60 BPM",      "Bradycardia",  "#d6eaf8"),
            ("  🟢  Normal", "60 – 100 BPM",  "Healthy",      "#d5f5e3"),
            ("🔴  High",   "> 100 BPM",     "Tachycardia",  "#fadbd8"),
        ]
        self.row_frames = []

        for category, bpm_range, status, color in self.rows_data:
            row = tk.Frame(table_frame, bg="#ffffff")
            row.pack(fill="x")
            for text, w in zip([category, bpm_range, status], col_widths):
                tk.Label(
                    row, text=text, font=table_font,
                    bg="#ffffff", width=w, anchor="center", pady=4
                ).pack(side="left", padx=1)
            self.row_frames.append((row, color))

        # ── Time axis ─────────────────────────────────────────
        self.t   = np.linspace(0, 5, 1000)
        self.ani = None
        self.fig = None


    # ================= HEART RATE CLASSIFICATION =================
    def classify_heart_rate(self, bpm):
        if bpm < 60:
            return 0, "🔵  Low Heart Rate  —  Bradycardia", "#2980b9"
        elif bpm <= 100:
            return 1, "🟢  Normal Heart Rate  —  Healthy",  "#27ae60"
        else:
            return 2, "🔴  High Heart Rate  —  Tachycardia", "#e74c3c"


    # ================= HIGHLIGHT ACTIVE ROW =================
    def highlight_row(self, active_index):
        for i, (row, color) in enumerate(self.row_frames):
            bg = color if i == active_index else "#ffffff"
            row.configure(bg=bg)
            for widget in row.winfo_children():
                widget.configure(bg=bg)


    # ================= START SIMULATION =================
    def start(self):
        try:
            bpm = int(self.bpm_entry.get())

            if bpm < 30 or bpm > 200:
                messagebox.showerror(
                    "Error",
                    "Please enter a value between 30 and 200 BPM"
                )
                return

            plt.close("all")

            # Classify & update UI
            row_index, label_text, label_color = self.classify_heart_rate(bpm)
            self.status_label.config(text=label_text, fg=label_color)
            self.highlight_row(row_index)

            # Generate ECG signal
            self.y = generate_ecg(self.t, bpm)

            self.fig, self.ax = plt.subplots()
            self.line, = self.ax.plot([], [], color="#e74c3c", linewidth=1.2)

            self.ax.set_xlim(0, 5)
            self.ax.set_ylim(-0.5, 2)
            self.ax.set_title(f"ECG Signal  —  {bpm} BPM  ({label_text.split('—')[-1].strip()})")
            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Amplitude")
            self.ax.grid(True, alpha=0.3)

            self.ani = FuncAnimation(
                self.fig, self.update,
                frames=len(self.t), interval=1, repeat=True
            )

            plt.show()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer number")


    # ================= UPDATE ANIMATION =================
    def update(self, frame):
        self.line.set_data(self.t[:frame], self.y[:frame])
        return self.line,


    # ================= STOP SIMULATION =================
    def stop(self):
        if self.ani:
            self.ani.event_source.stop()


# ================= RUN APP =================
root = tk.Tk()
app = ECGApp(root)
root.mainloop()