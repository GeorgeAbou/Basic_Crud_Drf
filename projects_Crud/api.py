from rest_framework import viewsets,permissions
from .models import Projects
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Projects.objects.all()
    permission_classes=[permissions.AllowAny]#cualquiera puede consultar al servidor
    serializer_class=ProjectSerializer
