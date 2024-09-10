from django.urls import include, path
from rest_framework import routers

from account import views

router = routers.DefaultRouter()
router.register("insterest", views.InterestViewSet, basename="insterest"),
router.register("", views.AccountViewSet, basename="accounts")

urlpatterns = [
    path("", include(router.urls)),
]
