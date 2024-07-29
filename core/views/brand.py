from rest_framework.viewsets import ModelViewSet  
from rest_framework.permissions import IsAuthenticated

from core.models import Brand 
from core.serializers import BrandSerializer  

class BrandViewSet(ModelViewSet):     
    queryset = Brand.objects.all()     
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]