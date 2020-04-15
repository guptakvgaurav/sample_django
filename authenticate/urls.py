from django.urls import path
from .views import LoginViewSet, LogoutViewSet


urlpatterns = [
    path('login/', LoginViewSet.as_view(actions={'post': 'post'})),
    path('logout/', LogoutViewSet.as_view(actions={'post': 'post'}))
]
