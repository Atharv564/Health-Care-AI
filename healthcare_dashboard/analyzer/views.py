from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import CSVUploadForm
from .utils import process_healthcare_data, generate_insights
from .utils import generate_ai_suggestions
import os
from google import genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES["csv_file"]

            fs = FileSystemStorage(location="media/uploads")
            filename = fs.save(csv_file.name, csv_file)
            file_path = fs.path(filename)

            # ---------- PROCESS DATA ----------
            analytics = process_healthcare_data(file_path)
            df = analytics["df"]

            # ---------- CHART DATA ----------
            chart_data = {
                "disease_labels": list(analytics["top_diseases"].keys()),
                "disease_counts": list(analytics["top_diseases"].values()),

                "stay_days": df["stay_days"].tolist(),
                "costs": df["treatment_cost"].tolist(),

                "hospital_labels": list(analytics["best_hospitals"].keys()),
                "hospital_costs": list(analytics["best_hospitals"].values()),
            }

            # ---------- INSIGHTS ----------
            insights = generate_insights(df)

            ai_suggestions = generate_ai_suggestions(
                analytics["summary"],
                analytics["top_diseases"],
                analytics["best_hospitals"],
                analytics["worst_hospitals"],
            )


            context = {
                "summary": analytics["summary"],
                "top_diseases": analytics["top_diseases"],
                "severity": analytics["severity"],
                "best_hospitals": {"cost_per_day": analytics["best_hospitals"]},
                "worst_hospitals": {"cost_per_day": analytics["worst_hospitals"]},
                "chart_data": chart_data,
                "insights": insights,
                "ai_suggestions": ai_suggestions,
            }


            return render(request, "analyzer/dashboard.html", context)

    else:
        form = CSVUploadForm()

    return render(request, "analyzer/upload.html", {"form": form})
