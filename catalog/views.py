from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'slug', 'content', 'preview', 'published')
    success_url = reverse_lazy('catalog:articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'slug', 'content', 'preview', 'published')
    success_url = reverse_lazy('catalog:articles_list')

    def get_success_url(self):
        return reverse('catalog:articles_detail', args=[self.kwargs('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:articles_list')
