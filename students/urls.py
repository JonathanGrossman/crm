from rest_framework import routers
from .api import StudentViewSet, SingleStudentViewSet

router = routers.DefaultRouter()
router.register('api/students', StudentViewSet, 'students')
router.register('api/students/:id', SingleStudentViewSet, 'students')

urlpatterns = router.urls