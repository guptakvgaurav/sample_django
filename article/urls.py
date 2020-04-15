from django.urls import path
from .views import ArticleViewSet


single_view = ArticleViewSet.as_view(actions={
    'get': 'get_article',
})

urlpatterns = [
    path('', single_view),
]
