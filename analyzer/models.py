from django.db import models
from django.contrib.auth.models import User

class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    
    summary = models.JSONField()
    top_diseases = models.JSONField()
    severity = models.JSONField()
    best_hospitals = models.JSONField()
    worst_hospitals = models.JSONField()
    
    insights = models.JSONField()
    ai_suggestions = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"