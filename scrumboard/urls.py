from rest_framework.routers import DefaultRouter

from .api import ListViewSet, CardViewSet


router = DefaultRouter()
router.register(prefix=r'lists', viewset=ListViewSet)
router.register(prefix=r'cards', viewset=CardViewSet)

urlpatterns = router.urls
