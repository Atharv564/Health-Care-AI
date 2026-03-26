from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_csv, name="upload"),
    path("history/", views.history_view, name="history"),
    path("download/<int:report_id>/", views.download_dashboard_pdf, name="download_pdf"),

    # auth
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
]