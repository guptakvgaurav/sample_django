from django.urls import path
from .views import LoginViewSet, LogoutViewSet, SignupViewSet


urlpatterns = [
    path('signup/', SignupViewSet.as_view(actions={'post': 'post'})),
    path('login/', LoginViewSet.as_view(actions={'post': 'post'})),
    path('logout/', LogoutViewSet.as_view(actions={'post': 'post'}))
]
