import pandas as pd
import os
from google import genai


def process_healthcare_data(csv_path):
    df = pd.read_csv(csv_path)

    # ---------------- CLEANING ----------------
    df.columns = df.columns.str.strip().str.lower()

    df['admission_date'] = pd.to_datetime(df['admission_date'], errors='coerce')
    df['discharge_date'] = pd.to_datetime(df['discharge_date'], errors='coerce')

    df = df.dropna(subset=['admission_date', 'discharge_date'])
    df = df[df['discharge_date'] >= df['admission_date']]

    df['stay_days'] = (df['discharge_date'] - df['admission_date']).dt.days
    df = df[df['stay_days'] > 0]

    df['treatment_cost'] = pd.to_numeric(df['treatment_cost'], errors='coerce')
    df = df.dropna(subset=['treatment_cost'])

    df['cost_per_day'] = df['treatment_cost'] / df['stay_days']

    # ---------------- DEBUG (VERY IMPORTANT) ----------------
    print("Unique stay days:", df['stay_days'].nunique())
    print("Stay distribution:\n", df['stay_days'].value_counts().head())

    # ---------------- BASIC ANALYTICS ----------------
    top_diseases = df['disease'].value_counts().head(5)

    severity = (
        df.groupby('disease')['stay_days']
        .mean()
        .sort_values(ascending=False)
        .head(3)
    )

    hospital_cost = (
        df.groupby('hospital_name')['cost_per_day']
        .mean()
        .sort_values()
    )

    # ---------------- SUMMARY ----------------
    summary = {
        "total_patients": int(len(df)),
        "avg_stay": round(df['stay_days'].mean(), 2),
        "avg_cost": round(df['treatment_cost'].mean(), 2),
    }

    # ---------------- CHART DATA ----------------

    # RAW scatter data
    stay_days = df['stay_days'].tolist()
    costs = df['treatment_cost'].tolist()

    # AGGREGATED (better visualization)
    grouped = (
        df.groupby('stay_days')['treatment_cost']
        .mean()
        .reset_index()
    )

    avg_stay_days = grouped['stay_days'].tolist()
    avg_costs = grouped['treatment_cost'].tolist()

    chart_data = {
        "disease_labels": list(top_diseases.keys()),
        "disease_counts": list(top_diseases.values),

        "stay_days": stay_days,
        "costs": costs,

        "avg_stay_days": avg_stay_days,
        "avg_costs": avg_costs,

        "hospital_labels": hospital_cost.index.tolist(),
        "hospital_costs": hospital_cost.values.tolist()
    }

    return {
        "df": df,
        "summary": summary,
        "top_diseases": top_diseases.to_dict(),
        "severity": severity.to_dict(),
        "best_hospitals": hospital_cost.head(3).to_dict(),
        "worst_hospitals": hospital_cost.tail(3).to_dict(),
        "chart_data": chart_data
    }


# ---------------- INSIGHTS ----------------
def generate_insights(df):
    insights = []

    if df['disease'].nunique() > 0:
        disease_share = df['disease'].value_counts(normalize=True).iloc[0] * 100
        if disease_share > 30:
            insights.append(
                f"One disease accounts for {disease_share:.1f}% of total admissions."
            )

    stay_std = df['stay_days'].std()
    cost_std = df['treatment_cost'].std()

    if stay_std > 0 and cost_std > 0:
        corr = df['stay_days'].corr(df['treatment_cost'])
        if corr > 0.6:
            insights.append(
                "Treatment cost strongly increases with hospital stay duration."
            )
    else:
        insights.append(
            "Not enough variation in stay duration or cost."
        )

    cost_per_day = df.groupby('hospital_name')['cost_per_day'].mean()

    if len(cost_per_day) > 1:
        gap = cost_per_day.max() - cost_per_day.min()
        if gap > 500:
            insights.append(
                f"Hospital efficiency gap is ₹{gap:.0f}/day."
            )

    return insights


# ---------------- AI ----------------
def generate_ai_suggestions(summary, top_diseases, best_hospitals, worst_hospitals):
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return ["GOOGLE_API_KEY missing"]

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Healthcare analytics summary:
{summary}

Diseases:
{top_diseases}

Best hospitals:
{best_hospitals}

Worst hospitals:
{worst_hospitals}

Give 4 short actionable suggestions.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return [line.strip() for line in response.text.split("\n") if line.strip()]

    except Exception as e:
        return [f"AI error: {str(e)}"]