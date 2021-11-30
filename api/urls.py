from rest_framework.routers import DefaultRouter
from .views import CarView

router = DefaultRouter()
router.register(r'cars', CarView, basename='user')
urlpatterns = router.urls
