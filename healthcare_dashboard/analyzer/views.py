from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import CSVUploadForm
from .utils import process_healthcare_data, generate_insights
from .utils import generate_ai_suggestions
import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from google import genai
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Singup
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("upload")

    return render(request, "auth/signup.html")

# login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("upload")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "auth/login.html")

# logout
def logout_view(request):
    logout(request)
    return redirect("login")

from .models import HealthReport

# Upload csv
@login_required
def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES["csv_file"]

            fs = FileSystemStorage(location="media/uploads")
            filename = fs.save(csv_file.name, csv_file)
            file_path = fs.path(filename)

            # PROCESS DATA
            analytics = process_healthcare_data(file_path)

            if "error" in analytics:
                return render(request, "analyzer/upload.html", {
                    "form": form,
                    "error": analytics["error"]
                })

            df = analytics["df"]

            insights = generate_insights(df)

            ai_suggestions = generate_ai_suggestions(
                analytics["summary"],
                analytics["top_diseases"],
                analytics["best_hospitals"],
                analytics["worst_hospitals"],
            )

            # ✅ SAVE TO DATABASE (CORE FIX)
            report = HealthReport.objects.create(
                user=request.user,
                file=filename,
                summary=analytics["summary"],
                top_diseases=analytics["top_diseases"],
                severity=analytics["severity"],
                best_hospitals=analytics["best_hospitals"],
                worst_hospitals=analytics["worst_hospitals"],
                insights=insights,
                ai_suggestions=ai_suggestions,
            )

            # CHART DATA
            chart_data = {
                "disease_labels": list(analytics["top_diseases"].keys()),
                "disease_counts": list(analytics["top_diseases"].values()),
                "stay_days": df["stay_days"].tolist(),
                "costs": df["treatment_cost"].tolist(),
                "hospital_labels": list(analytics["best_hospitals"].keys()),
                "hospital_costs": list(analytics["best_hospitals"].values()),
            }

            context = {
                "report": report,
                "summary": analytics["summary"],
                "top_diseases": analytics["top_diseases"],
                "severity": analytics["severity"],
                "best_hospitals": analytics["best_hospitals"],
                "worst_hospitals": analytics["worst_hospitals"],
                "chart_data": chart_data,
                "insights": insights,
                "ai_suggestions": ai_suggestions,
            }

            return render(request, "analyzer/dashboard.html", context)

    else:
        form = CSVUploadForm()

    return render(request, "analyzer/upload.html", {"form": form})

# history
@login_required
def history_view(request):
    reports = HealthReport.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "analyzer/history.html", {"reports": reports})

# download pdf
@login_required
def download_dashboard_pdf(request, report_id):
    try:
        report = HealthReport.objects.get(id=report_id, user=request.user)
    except HealthReport.DoesNotExist:
        return HttpResponse("Unauthorized", status=403)

    context = {
        "summary": report.summary,
        "top_diseases": report.top_diseases,
        "severity": report.severity,
        "best_hospitals": report.best_hospitals,
        "worst_hospitals": report.worst_hospitals,
        "insights": report.insights,
        "ai_suggestions": report.ai_suggestions,
    }

    template = get_template("analyzer/dashboard_report.html")
    html = template.render(context)

    result = BytesIO()
    pdf = pisa.CreatePDF(html, dest=result)

    if pdf.err:
        return HttpResponse("Error generating PDF", status=500)

    response = HttpResponse(result.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Report.pdf"'
    return response