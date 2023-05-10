from django.urls import path
from app import views
urlpatterns = [
    path('hackathon/',views.HackathonAPIView.as_view(),name="HackathonView"),
    path('my-hackathon/',views.MyHackathonListView.as_view(),name="ListMyHackathons"),
    path('hackathon/list/',views.HackathonList.as_view(),name="ListAllHackathons"),
    path('participate/',views.ParticipateView.as_view(),name="participateView"),
    path('submission/',views.HackathonSubmissionAPIView.as_view(),name='submission'),
    path('submission/<int:pk>/',views.HackathonSubmissionAPIView.as_view(),name='UpdateSubmission'),
    path('register/',views.UserRegisterView.as_view(),name="RegisterUser"),
]
