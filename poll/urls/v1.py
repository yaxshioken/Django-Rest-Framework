from rest_framework.routers import DefaultRouter

from poll.views import PollViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r"polls", PollViewSet, basename="polls")
router.register(r"users", UserCreateViewSet, basename="users")

urlpatterns = router.urls
