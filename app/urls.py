from django.urls import path
from app import views
urlpatterns = [
    path('hackathon/',views.HackathonAPIView.as_view(),name="HackathonView"),
    path('hackathon/list/',views.HackathonListView.as_view(),name="ListHackathons"),
]
