from django.urls import path, include

from apps.base.routers import router

app_name = 'base'

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
