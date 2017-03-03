from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Conectando nossa API usando rotas automaticas de URL.
# Além disso, nos incluimos URLs de login para a navegabilidade da API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
