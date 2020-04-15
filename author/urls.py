from django.urls import path
from .views import AuthorViewSet


single_view = AuthorViewSet.as_view(actions={
    'get': 'get_my_details',
    'post': 'create_author'
})

login_view = AuthorViewSet.as_view(actions={
    'post': 'login'
})


urlpatterns = [
    path('', single_view),
    path('login/', login_view)
]
