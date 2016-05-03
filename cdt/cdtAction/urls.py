from rest_framework.routers import DefaultRouter
from cdtAction import views

router = DefaultRouter(trailing_slash=False)

router.register(r'user', views.UserViewSet, base_name='user')

urlpatterns = router.urls

urlpatterns += []
