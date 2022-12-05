from cgitb import reset
from django.shortcuts import render
from django.views.generic import ListView
from .models import createBlog, comments


class list(ListView):
    template_name = 'blog/index.html'
    queryset = createBlog.objects.all()
    paginate_by = 3
def detailView(request):
    article = createBlog.objects.get(slog= 'post-1') 
    content = {
        'article':article,
    }
    return render(request, 'blog/blog-details.html', content)