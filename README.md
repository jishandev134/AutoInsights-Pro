
# 📊 AutoInsights Pro - A Data Analysis Automation Tool

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-orange?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/YOUR_REPO?style=social)](https://github.com/YOUR_USERNAME/YOUR_REPO/stargazers)

A **Streamlit web application** that transforms raw Excel/CSV datasets into **clean, well-structured reports** with:
✅ Data Cleaning & Formatting
✅ Summary Statistics (Dynamic)
✅ Automated Charts & Graphs
✅ Downloadable Excel Report

Perfect for **quick data analysis**, automated reporting, and impressing managers or recruiters.

---

## 🚀 Features
- **Upload Any Dataset** (`.xlsx` / `.csv`)
- **Automatic Data Cleaning**
  - Removes duplicates
  - Fills missing numeric values with mean
  - Fills missing categorical values with mode
  - Trims whitespace in text columns
- **Dynamic Summary Statistics**
  - Count, Mean, Median, Min, Max, Standard Deviation
- **Interactive Charts**
  - Bar, Pie, Histogram, Line
- **Download Cleaned Report**
  - Cleaned dataset + summary + embedded charts

---

## 🖥️ Live Demo
[🌐 Try it here](https://autoinsights.streamlit.app/)

---

## 📂 Project Structure
```
excel_report_generator/
│── app.py                # Main Streamlit app
│── data_cleaning.py      # Data cleaning functions
│── report_generator.py   # Summary & chart generation
│── email_sender.py       # Sending Emails with SMTP
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/jishandev134/AutoInsights-Pro.git
cd AutoInsights-Pro
```

2. **Create a virtual environment**
```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack
- **Python** – Core logic
- **Streamlit** – Web interface
- **Pandas** – Data processing
- **OpenPyXL / XlsxWriter** – Excel report creation with embedded charts
- **Plotly / Matplotlib** – Interactive charts

---

## 👤 Author
**Jishan Khan**
💼 [LinkedIn](https://www.linkedin.com/in/jishan-khan-ba5880342) | 💻 [GitHub](https://github.com/jishandev134)

