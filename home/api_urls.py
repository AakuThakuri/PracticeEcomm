from django.urls import path
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import ItemViewSet, ItemListView ,ItemCRUDView


router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('items', ItemListView.as_view(), name = 'items'),
    path('crud_items/<int:pk>/', ItemCRUDView.as_view(), name = 'crud_items'),
    
]