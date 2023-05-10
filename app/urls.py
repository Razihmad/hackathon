from django.urls import path
from app import views
urlpatterns = [
    path('hackathons/',views.HackathonAPIView.as_view(),name="HackathonView"),
    path('owner/hackathon/',views.OwnersHackathonList.as_view(),name="ListMyHackathons"),
    path('users/enrolled_hackathons/',views.EnrolledHackathonsListView.as_view(),name="EnrolledHackathons"),
    path('hackathons/register/',views.ParticipateView.as_view(),name="participateView"),
    path('hackathons/submit/',views.HackathonSubmissionAPIView.as_view(),name='submission'),
    path('hackathons/submit/<int:pk>/',views.HackathonSubmissionAPIView.as_view(),name='UpdateSubmission'),
    path('users/submissions/',views.SubmissionList.as_view(),name="SubmissionsView"),
    path('user/register/',views.UserRegisterView.as_view(),name="RegisterUser"),
]
