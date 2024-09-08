from django.urls import path

from poll.views import (PollDeleteView, PollDetailView, PollPatchView,
                        PollPutView, PollView, UserCreateView)

urlpatterns = [
    path("users/", UserCreateView.as_view(), name="users"),
    path("poll/", PollView.as_view(), name="poll-list"),
    path("put/<int:pk>/", PollPutView.as_view(), name="poll-put"),
    path("patch/<int:pk>/", PollPatchView.as_view(), name="poll-patch"),
    path("delete/<int:pk>/", PollDeleteView.as_view(), name="poll-delete"),
    path("detail/<int:pk>/", PollDetailView.as_view(), name="poll-detail"),
]
