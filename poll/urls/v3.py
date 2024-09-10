from rest_framework.routers import DefaultRouter

from poll import views

router = DefaultRouter()
router.register("votes", views.VoteViewSet, basename="votes")
urlpatterns = router.urls
