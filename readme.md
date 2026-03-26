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

### 🔑 Admin Capabilities

- **View All Users**  
  Admins can see a complete list of registered users with basic info like username, email, and signup date.

- **Access User Reports**  
  Admins can download all reports uploaded by users, including metrics, charts, and AI insights.

- **Track User Activity**  
  Admins can monitor last login, number of uploaded datasets, and report history for each user.



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
|   |    |── analyzer/
|   |    |    ├── dashboard_report.html
|   |    |    ├── history.html 
|   |    |    ├── upload.html
|   |    |    └── dashboard.html
|   |    |── auth/
│   │         ├── upload.html
│   │         └── dashboard.html
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
git clone https://github.com/Atharv564/Health-Care-AI.git
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

## 🔄 System Workflow

1. User signs up / logs in  
2. Uploads healthcare dataset  
3. Data cleaned using Pandas  
4. Metrics computed  
5. Charts rendered  
6. Insights generated (rule-based + AI)  
7. Results stored in database  
8. User can:
   - View dashboard  
   - Access history  
   - Download PDF report  
---
## ⚠️ Design Principles

- All analytics are **data-driven** — no hardcoded or fake insights  
- Designed to handle **imperfect real-world datasets**  
- Safe error handling for AI and data failures  
- Focused on **correctness, not cosmetic outputs**  

---

## 🧠 Known Limitations

- Insight quality depends on dataset size  
- External AI (Gemini) availability may vary  
- SQLite is not suitable for production-scale workloads  

---

## 📌 Future Enhancements

- PostgreSQL integration with indexing  
- REST API (Django REST Framework)  
- Advanced filtering & search in history  
- Time-series disease trend analysis  
- Role-based access (admin vs user)  
- Docker deployment  

---

## 👨‍💻 Author

**Atharv**  
IT Engineer | Backend Developer  
Django • Data Analytics • AI Systems  

---

## 📜 License

For educational and demonstration purposes.
