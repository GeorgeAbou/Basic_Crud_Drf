from rest_framework import routers
from .api import ProjectViewSet

router=routers.DefaultRouter()# crea automaticamente las rutas basicas de crud

router.register('api/projects',ProjectViewSet,'projects')#nombre de la ruta=projects


urlpatterns = router.urls #guarda las urls crud
