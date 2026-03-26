# 🏥 Healthcare Analytics Dashboard with AI Insights

A full-stack Django application that transforms raw healthcare CSV data into actionable insights using data analytics, visualization, and AI-driven recommendations.

Built to simulate a **real-world healthcare analytics pipeline** with authentication, persistent storage, and report generation.

---

## 🚀 Key Highlights

- 🔐 **User Authentication System** (Signup, Login, Logout)  
- 📊 **End-to-End Data Pipeline** (Upload → Clean → Analyze → Visualize)  
- 🧠 **AI-Powered Insights** using Google Gemini  
- 🗂️ **Persistent History Tracking** (Database-backed, per user)  
- 📄 **PDF Report Generation** for analytics export  
- ⚡ Designed for **real-world messy datasets**, not ideal inputs  

---

## 🧩 Core Features

### 🔐 Authentication & Security
- Django built-in authentication system  
- Login-required protected routes  
- Session-based user isolation  
- Secure logout flow  

---

### 📂 Data Processing Engine
- CSV upload with validation  
- Automatic column normalization  
- Robust data cleaning:
  - Invalid dates removed  
  - Negative/zero stay filtered  
  - Non-numeric costs handled  

- Derived metrics:
  - `stay_days`  
  - `cost_per_day`  

---

### 📊 Analytics & Metrics
- Total patients  
- Average stay duration  
- Average treatment cost  
- Top diseases (frequency-based)  
- High severity diseases (long stay)  
- Hospital efficiency ranking (cost/day)  

---

### 📈 Data Visualization
- Bar chart → Disease distribution  
- Scatter plot → Stay vs Cost correlation  
- Bar chart → Hospital efficiency  

---

### 🧠 Intelligent Insights

#### Rule-Based
- Disease concentration detection  
- Cost vs stay correlation analysis  
- Hospital efficiency gap identification  

#### AI-Based (Gemini API)
- Cost optimization strategies (₹)  
- Disease prevention insights  
- Hospital efficiency improvements  
- Actionable recommendations  

> Gracefully disables if API key is missing.

---

### 🗂️ History Management
- Each analysis stored in database  
- Linked to authenticated user  
- Enables:
  - Revisit past reports  
  - Real-world analytics tracking  

---

### 📄 Report Export
- Download dashboard report as PDF  
- Includes summary, hospital analysis, insights, and AI suggestions  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Django 6 |
| Data Processing | Pandas |
| Frontend | Tailwind CSS, Bootstrap |
| Visualization | Chart.js |
| AI Integration | Google Gemini API |
| Database | SQLite |

---

## 🧱 Project Architecture

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


