from rest_framework.routers import DefaultRouter

from poll.views import VoteViewSet

router = DefaultRouter()
router.register(r"votes", VoteViewSet, basename="votes")

urlpatterns = router.urls
