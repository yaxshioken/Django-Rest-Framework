from django.urls import path

from poll.views import VoteView, VoteDetailView

urlpatterns = [
    path('votes/',VoteView.as_view(),name='vote-list'),
    path('votes/<int:pk>/',VoteDetailView.as_view(),name='vote-detail'),

]