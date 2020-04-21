from django.urls import path
from .views import AuthorViewSet


single_view = AuthorViewSet.as_view(actions={
    'get': 'get_my_details',
    'post': 'create_author'
})


urlpatterns = [
    path('', single_view),
]
