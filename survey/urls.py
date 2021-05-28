from django.urls import path
from .views import survey,review

urlpatterns = [
    path('', survey),
    path('review/',review)
]