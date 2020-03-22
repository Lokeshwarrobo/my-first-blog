from django.views.generic import ListView,DetailView
from .models import Post
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ArticleListView(ListView):
    model = Post
    template_name = 'articles.html'
    paginate_by = 3
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'batman'


class ArticleCreateView(CreateView):
    model = Post
    template_name = 'new_article.html'
    fields = ['title','text']
    success_url = reverse_lazy('Articles')

class ArticleUpdateView(UpdateView):
    model = Post
    template_name = 'article_edit.html'
    fields = ['title','text']
    success_url = reverse_lazy('Articles')
class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    context_object_name = 'batman'
    success_url = reverse_lazy('Articles')

def home(request):
    return render(request,'home.html')

