from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.list import View


# Create your views here.
class StubView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = 'post_list'
    queryset = Post.objects.filter(published_date__exact=None)
    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
