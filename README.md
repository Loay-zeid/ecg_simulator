# ❤️ ECG Heart Rate Simulation

## 📌 Overview

The **ECG Heart Rate Simulation** is a desktop application built using **Python**, **Tkinter**, and **Matplotlib**.
It allows users to simulate an ECG (electrocardiogram) signal based on a given heart rate (BPM) and visualize it in real time.

The application also classifies heart rate into different categories (low, normal, high), providing both visual and analytical feedback.

---

## 🚀 Key Features

- ❤️ Real-time ECG signal simulation
- 📊 Dynamic waveform visualization using Matplotlib
- 🔢 User input for heart rate (BPM)
- 🧠 Automatic heart rate classification
- ⚡ Smooth animated signal rendering
- 🛑 Start / Stop simulation controls

---

## 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| Tkinter | GUI framework |
| NumPy | Signal generation |
| Matplotlib | Waveform visualization |

---

## ⚙️ Getting Started

### 1️⃣ Install Dependencies

```bash
pip install numpy matplotlib
```

### 2️⃣ Run the Application

```bash
python main.py
```

---

## 🧭 How to Use the Application

### 1️⃣ Enter Heart Rate

- Input heart rate in BPM (between **30** and **200**)
- Click **Start Simulation**

<p align="center">
  <img src="input.png" width="600"/>
</p>

---

### 2️⃣ View ECG Signal

- Real-time ECG waveform will be displayed
- Signal updates dynamically with animation

<p align="center">
  <img src="ecg.png" width="800"/>
</p>

---

### 3️⃣ Heart Rate Classification

The system automatically classifies the heart rate:

| Category | BPM Range | Status |
|----------|-----------|--------|
| 🔵 Low | < 60 BPM | Bradycardia |
| 🟢 Normal | 60 – 100 BPM | Healthy |
| 🔴 High | > 100 BPM | Tachycardia |

<p align="center">
  <img src="result.png" width="600"/>
</p>

---

### 4️⃣ Stop Simulation

- Click **Stop** to pause the animation

---

## 📚 What I Learned

- Building GUI applications with **Tkinter**
- Generating and simulating signals using **NumPy**
- Creating real-time animations with **Matplotlib**
- Handling user input and validation
- Combining visualization with logical classification

---

## 📌 Future Improvements

- 🎨 Improve GUI design (modern UI)
- 📈 Add multiple ECG patterns
- 💾 Save generated signals to file
- 🧠 More advanced health analysis features
- 🌙 Dark mode support

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
