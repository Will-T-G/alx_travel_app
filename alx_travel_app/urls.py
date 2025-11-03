from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from rest_framework import permissions  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version='v1',
        description="API documentation for ALX Travel App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
