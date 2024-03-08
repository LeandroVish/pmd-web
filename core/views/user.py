from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserSerializer
from core.views import CategoriaViewSet, EditoraViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
