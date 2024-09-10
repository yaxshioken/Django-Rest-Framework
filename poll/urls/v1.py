from django.urls import include, path
from rest_framework.routers import DefaultRouter

from poll.views import PollViewSet, UserCreateView

router = DefaultRouter()
router.register("polls", PollViewSet, basename="polls")
urlpatterns = [
    path("", include(router.urls)),
]
