# 🏥 Healthcare Analytics Dashboard with AI Insights

A Django-based data analytics dashboard that processes healthcare CSV data, generates statistical insights, visualizes trends using charts, and provides AI-powered recommendations using Google Gemini.

This project is designed to demonstrate **real-world data cleaning, analysis, visualization, and AI integration** — not toy examples.

---

## 🚀 Features

### 📂 Data Processing
- Upload healthcare CSV files
- Automatic column standardization
- Data cleaning & validation
- Invalid rows filtered safely (dates, costs, stay duration)

### 📊 Analytics Generated
- Total patients count
- Average hospital stay
- Average treatment cost
- Top 5 most common diseases
- Diseases with longest average hospital stay (severity)
- Most cost-efficient hospitals
- Least cost-efficient hospitals

### 📈 Visualizations
- Disease distribution (bar chart)
- Cost vs stay duration (scatter plot)
- Hospital cost comparison

### 🧠 Rule-Based Insights
- Disease concentration warnings
- Cost vs stay correlation detection
- Hospital efficiency gap analysis

### 🤖 AI-Powered Suggestions (Gemini)
- Cost optimization strategies
- Hospital efficiency improvements
- Disease prevention focus areas
- Actionable management recommendations

AI gracefully disables itself if API key is missing.

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Django 6.x |
| Data Analysis | Pandas, NumPy |
| Visualization | Chart.js |
| AI | Google Gemini API |
| Frontend | HTML, CSS, Bootstrap |
| Environment | Python 3.10+ |

---

## 📁 Project Structure

```
healthcare_dashboard/
│
├── analyzer/
│   ├── views.py          # Request handling
│   ├── utils.py          # Data processing & AI logic
│   ├── forms.py          # CSV upload form
│   ├── templates/
│   │   ├── upload.html
│   │   └── dashboard.html
│
├── static/
│   └── charts.js         # Chart rendering logic
│
├── media/
│   └── uploads/          # Uploaded CSV files
│
├── .env                  # Environment variables
├── manage.py
└── requirements.txt
```

---

## 📄 Expected CSV Format

The CSV **must** contain the following columns (case-insensitive):

```
hospital_name
patient_id
disease
admission_date
discharge_date
treatment_cost
```

Date format can be flexible — invalid rows are automatically removed.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <repo-url>
cd healthcare_dashboard
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

⚠️ If not set, AI features will auto-disable without crashing.

---

### 5️⃣ Run the Server
```bash
python manage.py migrate
python manage.py runserver
```

Visit:
```
http://127.0.0.1:8000/
```

---

## 🧪 How It Works (Pipeline)

1. User uploads CSV
2. Pandas cleans & validates data
3. Metrics and aggregations computed
4. Charts rendered on dashboard
5. Rule-based insights generated
6. AI suggestions requested from Gemini
7. Results displayed cleanly

---

## ⚠️ Important Design Notes

- Rankings are **data-dependent** — no fake insights
- Small datasets may show overlapping best/worst hospitals
- AI errors are handled safely
- No assumptions about perfect data

This project prioritizes **correctness over cosmetic results**.

---

## 🧠 Known Limitations

- Small datasets reduce insight quality
- Gemini API model availability may change
- Charts depend on cleaned data

---

## 📌 Future Enhancements

- PDF report export
- Database storage (PostgreSQL)
- User authentication
- Time-series disease trends
- Hospital performance scoring
- Docker deployment

---

## 👨‍💻 Author

**Atharv**  
Information Technology Engineer  
Python • Django • Data Analytics • AI Integration

---

## 📜 License

This project is for educational and demonstration purposes.

---

If you understand this README completely, you’re already above average.
If not — re-read it. That’s the level expected in real projects.

