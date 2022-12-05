from importlib.resources import path
from django.urls import path
from blog.views import detailView, list
urlpatterns = [
    path('', list.as_view(), name='home'),
    path('detail/slog:slog', detailView, name='detailView')
]