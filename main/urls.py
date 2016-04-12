from counter import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'counter', views.CounterViewSet)
router.register(r'word', views.WordViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    url(r'', views.IndexView.as_view()),
    url(r'^api/', include(router.urls))
]
