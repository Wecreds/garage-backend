from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Accessory
from core.serializers import AccessorySerializer

class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [IsAuthenticated]