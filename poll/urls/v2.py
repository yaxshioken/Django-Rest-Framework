from rest_framework import routers

from poll.views import ChoiceViewSet

router = routers.DefaultRouter()
router.register(r"choices", ChoiceViewSet)

urlpatterns = router.urls
