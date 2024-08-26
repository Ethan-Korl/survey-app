from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("sa/", include("main.urls")),
    path("sp/", include("main.urls.sp_urls")),
]
