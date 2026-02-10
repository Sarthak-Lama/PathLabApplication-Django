
from django.urls import path, include
from .routers import router
from .views import LoginAPI

urlpatterns = [
    path('',include(router.urls)),
    path('login/', LoginAPI.as_view(),name='login')
]


