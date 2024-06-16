from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('catalog/<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('catalog/create', ArticleCreateView.as_view(), name='articles_create'),
    path('catalog/<int:pk>/update/', ArticleUpdateView.as_view(), name='articles_update'),
    path('catalog/<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles_delete')
]
