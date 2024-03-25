from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # this is django's built-in admin site to manage the database
    path('admin/', admin.site.urls),
    # whenever an empty string is requested, use the include function and redirect to base.urls
    path('', include("base.urls")),
    # whenever api is requested, use the include function and redirect to base.api.urls
    path('api/', include("base.api.urls"))
]
