from rest_framework import viewsets
from cdtAction.models import User
from cdtAction.serializers import UserSerializer
from cdt import mako_views
from cdt import settings


lookup = mako_views.TemplateRender(
    settings.TEMPLATE_DIRS[0].get('cdtAction'),
    ['from cdt import views'],
)


class UserViewSet(viewsets.ModelViewSet):
    user = User.objects.all()
    serializer_class = UserSerializer
