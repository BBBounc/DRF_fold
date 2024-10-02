from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  
from rest_framework import routers
from storage.views import SupplyViewSet 

router = routers.DefaultRouter()
router.register(r'api/supply', SupplyViewSet)  

urlpatterns = [
    path('', views.index, name='index'),
    path('information/', views.information, name='information'),
    path('add_all/', views.add_all, name='add_all'),
    path('', include(router.urls)),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)