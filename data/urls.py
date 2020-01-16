from rest_framework import routers
from .api import DataViewSet

router = routers.DefaultRouter()
router.register('api/numbers', DataViewSet, 'data')

urlpatterns = router.urls