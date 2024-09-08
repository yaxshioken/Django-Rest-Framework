from django.urls import path

from poll.views import ChoiceView, ChoiceCRUDView

urlpatterns = [
    path('choices/',ChoiceView.as_view(),name='choices-list'),
    path('choices/<int:pk>/',ChoiceCRUDView.as_view(),name='choices-list'),
   ]