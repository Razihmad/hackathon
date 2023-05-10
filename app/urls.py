from django.urls import path
from app import views
urlpatterns = [
    path('hackathon/',views.HackathonAPIView.as_view(),name="HackathonView"),
    path('hackathon/list/',views.HackathonListView.as_view(),name="ListHackathons"),
    path('hackathon/list/<int:pk>/',views.HackathonListView.as_view(),name="ListHackathons"),
    path('participate/',views.ParticipateView.as_view(),name="participateView"),
    path('submission/',views.HackathonSubmissionAPIView.as_view(),name='submission'),
    path('submission/<int:pk>/',views.HackathonSubmissionAPIView.as_view(),name='UpdateSubmission'),
]
