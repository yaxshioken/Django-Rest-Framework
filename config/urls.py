# config/urls.py
from django.contrib import admin
from django.urls import include, path

from config.swagger import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls.v1")),
    path("api/v1/", include("poll.urls.v1")),
    path("api/v2/", include("poll.urls.v2")),
    path("api/v3/", include("poll.urls.v3")),
]

urlpatterns += swagger_urlpatterns
