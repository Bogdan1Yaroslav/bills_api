from rest_framework.routers import DefaultRouter
from .views import BillViewSet

router = DefaultRouter()
router.register(r'get_bills_list', BillViewSet, basename='bills_list')
router.register(r'upload_from_csv', BillViewSet, basename='upload_from_csv')
urlpatterns = router.urls
