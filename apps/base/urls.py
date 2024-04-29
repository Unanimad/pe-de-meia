from django.urls import path, include

from apps.base.routers import router
from apps.base.views import index

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
